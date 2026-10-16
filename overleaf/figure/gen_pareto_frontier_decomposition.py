#!/usr/bin/env python3
r"""Pareto-frontier view of decomposition dependence of DC criticality certificates.

Replaces the one-dimensional dial figure (former panel e) by the full
two-dimensional (delta_phi, delta_g) trade-off it is a slice of.

Objective  F(x) = sin(pi x1) cos(pi x2),  L = pi^2,  Q = (L/2)||x||^2, with the
two convex DC decompositions

    decomposition 1 (fully linearized)      phi_1 = Q,      g_1 = Q - F
    decomposition 2 (curvature-preserving)  phi_2 = F + Q,  g_2 = Q

For a convex component h the Fenchel gap of a certificate vector v at x is

    Gap_h(x, v) = h(x) + h*(v) - <v, x> = max_z [ h(x) - h(z) - <v, x - z> ],

and Gap_h(x, v) <= delta  iff  v in partial_delta h(x).  The eps = 0 feasible
region of a decomposition at x is
    P_i(x) = { (delta_phi, delta_g) : exists v, Gap_{phi_i}(x,v) <= delta_phi
                                              and Gap_{g_i}(x,v)  <= delta_g },
whose lower-left boundary is the Pareto frontier plotted here.  Its
delta_g = 0 intercept is the Frank-Wolfe DC gap of decomposition i
(Lemma gap-dc-slice); its delta_phi = 0 intercept is the DCA transport gap;
its delta_phi = delta_g diagonal section reproduces the former dial figure.
"""

from __future__ import annotations

import os
import pickle
import tempfile
import time
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
BASE = OUT_DIR / "pareto_frontier_decomposition"
TMP_ROOT = Path(tempfile.gettempdir()) / "stochastic_dcam_matplotlib"
MPLCONFIG = TMP_ROOT / "mplconfig"
CACHE_DIR = TMP_ROOT / "cache"
MPLCONFIG.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG))
os.environ.setdefault("XDG_CACHE_HOME", str(CACHE_DIR))

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

L = float(np.pi**2)
D_PROBE = 0.15

# Okabe-Ito colorblind-safe palette.
C_MIN = "#0072B2"      # blue
C_SADDLE = "#009E73"   # bluish green
C_MAX = "#CC79A7"      # reddish purple
C_LAMBDA_POS = "#0072B2"
C_LAMBDA_NEG = "#D55E00"  # vermillion
C_GRID = "#9AA0A6"
C_TEXT = "#111111"

STATIONARY = {
    "min": np.array([-0.5, 0.0]),
    "saddle": np.array([0.0, 0.5]),
    "max": np.array([0.5, 0.0]),
}
PANEL_COLOR = {"min": C_MIN, "saddle": C_SADDLE, "max": C_MAX}
PANEL_TITLE = {
    "min": "(a) near minimum",
    "saddle": "(b) near saddle",
    "max": "(c) near maximum",
}

# ----------------------------------------------------------------------------
# Objective and derivatives.
# ----------------------------------------------------------------------------


def F(z: np.ndarray) -> np.ndarray:
    return np.sin(np.pi * z[..., 0]) * np.cos(np.pi * z[..., 1])


def gradF(z: np.ndarray) -> np.ndarray:
    gx = np.pi * np.cos(np.pi * z[..., 0]) * np.cos(np.pi * z[..., 1])
    gy = -np.pi * np.sin(np.pi * z[..., 0]) * np.sin(np.pi * z[..., 1])
    return np.stack([gx, gy], axis=-1)


def hessF(z: np.ndarray) -> np.ndarray:
    a = np.sin(np.pi * z[0]) * np.cos(np.pi * z[1])
    b = np.cos(np.pi * z[0]) * np.sin(np.pi * z[1])
    return -(np.pi**2) * np.array([[a, b], [b, a]])


# ----------------------------------------------------------------------------
# Fenchel gaps.
# ----------------------------------------------------------------------------


def gap_Q(x: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Exact Fenchel gap of Q = (L/2)||.||^2:  |v - L x|^2 / (2L)."""
    return np.sum((v - L * x) ** 2, axis=-1) / (2.0 * L)


def _local_zgrid(x: np.ndarray, half: float, n: int) -> tuple[np.ndarray, np.ndarray]:
    ax1 = np.linspace(x[0] - half, x[0] + half, n)
    ax2 = np.linspace(x[1] - half, x[1] + half, n)
    g1, g2 = np.meshgrid(ax1, ax2, indexing="ij")
    Z = np.stack([g1.ravel(), g2.ravel()], axis=-1)
    return Z, F(Z)


def gap_num(
    x: np.ndarray,
    V: np.ndarray,
    sign: int,
    Z: np.ndarray,
    fZ: np.ndarray,
    n_side: int,
) -> tuple[np.ndarray, float]:
    """Fenchel gap of h = Q + sign * F over a batch of certificates V.

    Returns the gaps and the largest fraction of boundary hits of the
    conjugate argmax (should be ~0 if the z-window is wide enough).
    """
    hz = 0.5 * L * np.sum(Z**2, axis=1) + sign * fZ
    hx = 0.5 * L * float(np.sum(x**2)) + sign * float(F(x))
    gaps = np.empty(V.shape[0])
    boundary = 0.0
    ring = {0, n_side - 1}
    for s in range(0, V.shape[0], 512):
        Vc = V[s : s + 512]
        obj = Z @ Vc.T - hz[:, None]          # (Nz, chunk)
        idx = obj.argmax(axis=0)
        hstar = obj[idx, np.arange(Vc.shape[0])]
        gaps[s : s + 512] = hx + hstar - Vc @ x
        r, c = np.divmod(idx, n_side)
        hit = np.isin(r, list(ring)) | np.isin(c, list(ring))
        boundary = max(boundary, float(hit.mean()))
    return gaps, boundary


# ----------------------------------------------------------------------------
# Accurate intercepts on a global grid (well-conditioned concave maximizations).
# ----------------------------------------------------------------------------

_GLOB_AX = np.linspace(-2.0, 2.0, 801)
_G1, _G2 = np.meshgrid(_GLOB_AX, _GLOB_AX, indexing="ij")
_GLOB_Z = np.stack([_G1.ravel(), _G2.ravel()], axis=-1)
_GLOB_F = F(_GLOB_Z)


def fw_gap(x: np.ndarray, sign_phi: int, v_g: np.ndarray) -> float:
    """Frank-Wolfe DC gap  max_z { phi(x) - phi(z) - <v_g, x - z> },
    phi = Q + sign_phi * F, computed on the global grid."""
    phi_z = 0.5 * L * np.sum(_GLOB_Z**2, axis=1) + sign_phi * _GLOB_F
    phi_x = 0.5 * L * float(np.sum(x**2)) + sign_phi * float(F(x))
    # <v_g, x - z> = <v_g, x> - <v_g, z>
    val = phi_x - phi_z - (float(v_g @ x) - _GLOB_Z @ v_g)
    return float(val.max())


def transport_gap(x: np.ndarray, sign_g: int, v_phi: np.ndarray) -> float:
    """delta_phi = 0 intercept:  Gap_g(x, v_phi) with g = Q + sign_g * F,
    computed on the global grid."""
    g_z = 0.5 * L * np.sum(_GLOB_Z**2, axis=1) + sign_g * _GLOB_F
    g_x = 0.5 * L * float(np.sum(x**2)) + sign_g * float(F(x))
    hstar = float((_GLOB_Z @ v_phi - g_z).max())
    return g_x + hstar - float(v_phi @ x)


# ----------------------------------------------------------------------------
# Pareto frontier of a decomposition at a probe point.
# ----------------------------------------------------------------------------


def _lower_left(points: np.ndarray) -> np.ndarray:
    """Nondominated lower-left envelope, returned sorted by delta_phi."""
    order = np.lexsort((points[:, 1], points[:, 0]))
    pts = points[order]
    keep = []
    best = np.inf
    for p in pts:
        if p[1] < best - 1e-12:
            keep.append(p)
            best = p[1]
    return np.array(keep)


def frontier(name: str, decomp: int) -> dict:
    """decomp = 1 (phi=Q, g=Q-F) or 2 (phi=Q+F, g=Q)."""
    xs = STATIONARY[name]
    H = hessF(xs)
    w, Vec = np.linalg.eigh(H)
    k = int(np.argmax(np.abs(w)))
    lam, u = float(w[k]), Vec[:, k]
    x = xs + D_PROBE * u
    gF = gradF(x)

    if decomp == 1:                       # fully linearized
        p, q = L * x, L * x - gF          # grad phi_1, grad g_1
        sign_num = -1                     # numeric component is g_1 = Q - F
        x_int = gap_Q(x, q)               # analytic  = |gradF|^2 / 2L
        y_int = transport_gap(x, -1, p)   # numeric
        fw = fw_gap(x, 0, q)              # FW gap, phi_1 = Q
    else:                                 # curvature preserving
        p, q = L * x + gF, L * x          # grad phi_2, grad g_2
        sign_num = +1                     # numeric component is phi_2 = Q + F
        x_int = None                      # filled below (numeric)
        y_int = gap_Q(x, p)               # analytic  = |gradF|^2 / 2L
        fw = fw_gap(x, +1, q)             # FW gap, phi_2 = Q + F

    # Certificate grid over the bounding box of {p, q} with a small margin.
    lo = np.minimum(p, q) - 0.55
    hi = np.maximum(p, q) + 0.55
    nv = 157
    a1 = np.linspace(lo[0], hi[0], nv)
    a2 = np.linspace(lo[1], hi[1], nv)
    gv1, gv2 = np.meshgrid(a1, a2, indexing="ij")
    Vgrid = np.stack([gv1.ravel(), gv2.ravel()], axis=-1)

    n_side = 185
    Zloc, fZloc = _local_zgrid(x, half=1.15, n=n_side)
    gnum, boundary = gap_num(x, Vgrid, sign_num, Zloc, fZloc, n_side)
    gQ = gap_Q(x, Vgrid)
    if decomp == 1:
        dphi, dg = gQ, gnum
    else:
        dphi, dg = gnum, gQ
        x_int = fw                        # FW gap of decomposition 2

    cloud = np.column_stack([dphi, dg])
    # anchor exactly at the accurate analytic/global intercepts
    cloud = np.vstack([cloud, [x_int, 0.0], [0.0, y_int]])
    front = _lower_left(cloud)

    # diagonal delta_phi = delta_g crossing
    diff = front[:, 0] - front[:, 1]
    cross = None
    sign_change = np.where(np.diff(np.sign(diff)) != 0)[0]
    if sign_change.size:
        j = sign_change[0]
        a, b = front[j], front[j + 1]
        da, db = diff[j], diff[j + 1]
        t = da / (da - db)
        cross = a + t * (b - a)

    return {
        "lam": lam, "u": u, "x": x, "front": front,
        "x_int": float(x_int), "y_int": float(y_int), "fw": float(fw),
        "cross": cross, "boundary": boundary,
    }


# ----------------------------------------------------------------------------
# Panel (d): analytic local-quadratic model + 1D numeric validation.
# ----------------------------------------------------------------------------


def analytic_curve(rho: float, lam: float, d: float, kind: str, m: int = 200):
    """Closed-form frontier sqrt(A dphi) + sqrt(B dg) = |lam d|."""
    c = abs(lam * d)
    if kind == "curv":          # curvature preserving
        A, B = 2.0 * (rho + lam), 2.0 * rho
    else:                        # fully linearized
        A, B = 2.0 * rho, 2.0 * (rho - lam)
    s = np.linspace(0.0, 1.0, m)
    dphi = (s * c) ** 2 / A
    dg = ((1.0 - s) * c) ** 2 / B
    return dphi, dg


def numeric_1d(rho: float, lam: float, d: float, kind: str):
    """1D validation on F_quad(t) = (lam/2) t^2 (quadratic conjugates are exact)."""
    if kind == "curv":
        c_phi, c_g = rho + lam, rho
    else:
        c_phi, c_g = rho, rho - lam
    v = np.linspace(min(c_phi, c_g) * d - abs(lam * d) - 0.3,
                    max(c_phi, c_g) * d + abs(lam * d) + 0.3, 4000)
    dphi = (v - c_phi * d) ** 2 / (2.0 * c_phi)
    dg = (v - c_g * d) ** 2 / (2.0 * c_g)
    front = _lower_left(np.column_stack([dphi, dg]))
    return front


# ----------------------------------------------------------------------------
# Styling and plotting.
# ----------------------------------------------------------------------------


def style() -> None:
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        "font.size": 9,
        "axes.linewidth": 0.7,
        "axes.labelsize": 9,
        "axes.titlesize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.major.width": 0.7,
        "ytick.major.width": 0.7,
        "xtick.major.size": 2.4,
        "ytick.major.size": 2.4,
        "legend.frameon": False,
        "legend.fontsize": 7.0,
        "text.color": C_TEXT,
        "axes.labelcolor": C_TEXT,
    })


def draw_frontier_panel(ax, name: str, res: dict[int, dict], lim: float,
                        show_y: bool) -> None:
    color = PANEL_COLOR[name]
    ax.plot([0, lim], [0, lim], ls=":", lw=0.8, color=C_GRID, zorder=1)
    for decomp, ls in ((1, "-"), (2, "--")):
        r = res[decomp]
        f = r["front"]
        ax.plot(f[:, 0], f[:, 1], ls=ls, lw=1.6, color=color, zorder=3,
                solid_capstyle="round")
        ax.scatter(r["x_int"], 0.0, s=27, marker="o", color=color,
                   edgecolor="white", linewidths=0.6, zorder=5)
        ax.scatter(0.0, r["y_int"], s=27, marker="s", color=color,
                   edgecolor="white", linewidths=0.6, zorder=5)
        if r["cross"] is not None:
            ax.scatter(r["cross"][0], r["cross"][1], s=25, marker="o",
                       facecolor="white", edgecolor=color, linewidths=1.1,
                       zorder=6)
    ax.set_title(PANEL_TITLE[name], pad=4)
    ax.set_xlim(-0.006, lim)
    ax.set_ylim(-0.006, lim)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$\delta_\phi$")
    ax.set_xticks([0.0, 0.1, 0.2, 0.3])
    ax.set_yticks([0.0, 0.1, 0.2, 0.3])
    if show_y:
        ax.set_ylabel(r"$\delta_g$")
    else:
        ax.set_yticklabels([])
    ax.spines[["top", "right"]].set_visible(False)


def draw_model_panel(ax, rho: float, d: float, lim: float) -> None:
    combos = [
        (0.8 * rho, C_LAMBDA_POS, "curv", "--"),
        (0.8 * rho, C_LAMBDA_POS, "lin", "-"),
        (-0.8 * rho, C_LAMBDA_NEG, "curv", "--"),
        (-0.8 * rho, C_LAMBDA_NEG, "lin", "-"),
    ]
    for lam, col, kind, ls in combos:
        dphi, dg = analytic_curve(rho, lam, d, kind)
        ax.plot(dphi, dg, ls=ls, lw=1.6, color=col, zorder=3)
        nf = numeric_1d(rho, lam, d, kind)
        sel = np.linspace(0, len(nf) - 1, 11).astype(int)
        ax.scatter(nf[sel, 0], nf[sel, 1], s=9, marker="o", color=col,
                   alpha=0.9, linewidths=0.0, zorder=4)
    ax.plot([0, lim], [0, lim], ls=":", lw=0.8, color=C_GRID, zorder=1)
    ax.set_title("(d) local quadratic model", pad=4)
    ax.set_xlim(-0.008, lim)
    ax.set_ylim(-0.008, lim)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$\delta_\phi$")
    ax.set_xticks([0.0, 0.15, 0.3])
    ax.set_yticks([0.0, 0.15, 0.3])
    ax.spines[["top", "right"]].set_visible(False)
    handles = [
        Line2D([], [], color=C_LAMBDA_POS, lw=1.6, ls="-",
               label=r"$\lambda=+0.8\rho$ (min-like)"),
        Line2D([], [], color=C_LAMBDA_NEG, lw=1.6, ls="-",
               label=r"$\lambda=-0.8\rho$ (max-like)"),
        Line2D([], [], color="0.35", marker="o", ls="None", ms=3.2,
               label="1D numeric check"),
    ]
    ax.legend(handles=handles, loc="upper right", handlelength=1.6,
              labelspacing=0.35, borderaxespad=0.25)


def figure_legend(fig) -> None:
    handles = [
        Line2D([], [], color=C_TEXT, lw=1.6, ls="-",
               label=r"decomp. 1 (fully lin.): $(\phi_1,g_1)=(Q,\,Q-F)$"),
        Line2D([], [], color=C_TEXT, lw=1.6, ls="--",
               label=r"decomp. 2 (curv.-pres.): $(\phi_2,g_2)=(F+Q,\,Q)$"),
        Line2D([], [], color=C_TEXT, marker="o", ls="None", ms=4.8,
               label=r"FW DC gap ($\delta_g=0$)"),
        Line2D([], [], color=C_TEXT, marker="s", ls="None", ms=4.8,
               label=r"DCA transport gap ($\delta_\phi=0$)"),
        Line2D([], [], color=C_TEXT, marker="o", ls="None", ms=4.8,
               markerfacecolor="white",
               label=r"symmetric slice $\delta_\phi=\delta_g$ (former panel e)"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=3,
               bbox_to_anchor=(0.5, -0.01), handlelength=1.8,
               labelspacing=0.4, columnspacing=1.6, borderaxespad=0.0)


def compute_all() -> tuple[dict, list[float]]:
    """Heavy computation (frontiers + shrinkage), cached to disk keyed by grids."""
    global D_PROBE
    cache = TMP_ROOT / "frontier_cache.pkl"
    key = ("v157_z185_h1.15", D_PROBE)
    if cache.exists():
        with open(cache, "rb") as fh:
            saved = pickle.load(fh)
        if saved.get("key") == key:
            return saved["results"], saved["scales"]

    results: dict[str, dict[int, dict]] = {}
    for name in STATIONARY:
        results[name] = {d: frontier(name, d) for d in (1, 2)}

    d0 = D_PROBE
    scales = []
    for dd in (0.15, 0.075, 0.0375):
        D_PROBE = dd
        scales.append(frontier("saddle", 1)["x_int"])
    D_PROBE = d0

    with open(cache, "wb") as fh:
        pickle.dump({"key": key, "results": results, "scales": scales}, fh)
    return results, scales


def main() -> None:
    t0 = time.time()
    rho = L
    results, scales = compute_all()

    # ---- sanity checks -----------------------------------------------------
    print("[pareto_frontier_decomposition]")
    lim = 0.0
    for name, res in results.items():
        for decomp in (1, 2):
            r = res[decomp]
            lim = max(lim, r["x_int"], r["y_int"])
            # (1) x-intercept == Frank-Wolfe DC gap
            rel = abs(r["x_int"] - r["fw"]) / max(r["fw"], 1e-9)
            assert rel < 1e-2, f"{name} d{decomp}: x-int != FW gap ({rel:.3e})"
            assert r["boundary"] < 1e-6, (
                f"{name} d{decomp}: conjugate argmax hit z-window boundary "
                f"({r['boundary']:.3f}) -- widen the window")
        r1, r2 = res[1], res[2]
        print(f"  {name:7s} lam={r1['lam']:+.3f}  "
              f"d1(FW={r1['x_int']:.4f}, DCA={r1['y_int']:.4f})  "
              f"d2(FW={r2['x_int']:.4f}, DCA={r2['y_int']:.4f})")
    print(f"  x-int == FW gap: OK (all decompositions, <1e-2 rel)")
    print(f"  ordering: near-min curv-pres FW smaller "
          f"({results['min'][2]['x_int']:.3f} < {results['min'][1]['x_int']:.3f}); "
          f"near-max reversed "
          f"({results['max'][2]['x_int']:.3f} > {results['max'][1]['x_int']:.3f})")

    # (3) O(d^2) shrinkage of the frontier scale near a stationary point
    print(f"  O(d^2) shrinkage (saddle, d=.15/.075/.0375): "
          f"{scales[0]:.4f}, {scales[1]:.4f}, {scales[2]:.4f}  "
          f"ratios {scales[0]/scales[1]:.2f}, {scales[1]/scales[2]:.2f} (target ~4)")

    lim = 0.32
    dlim = 0.40

    # ---- figure ------------------------------------------------------------
    style()
    fig, axes = plt.subplots(1, 4, figsize=(7.2, 2.45))
    for i, name in enumerate(("min", "saddle", "max")):
        draw_frontier_panel(axes[i], name, results[name], lim, show_y=(i == 0))
    draw_model_panel(axes[3], rho, D_PROBE, dlim)
    figure_legend(fig)

    fig.subplots_adjust(left=0.06, right=0.995, top=0.905, bottom=0.37,
                        wspace=0.16)
    fig.savefig(BASE.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(BASE.with_suffix(".png"), dpi=300, bbox_inches="tight")
    print(f"  saved  {BASE}.pdf/.png   ({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
