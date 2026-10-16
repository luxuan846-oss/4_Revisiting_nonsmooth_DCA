#!/usr/bin/env python3
"""Decomposition dependence of the Frank-Wolfe DC gap vs the (delta,eps) measure.

Reproduces the experiment of Maskan et al. (2025), Figure 1, on
F(x) = sin(pi x1) cos(pi x2) with L = pi^2, for the two DC decompositions

    decomposition 1:  phi_1 = Q,          g_1 = Q - F      (gap linearizes F)
    decomposition 2:  phi_2 = F + Q,      g_2 = Q          (gap keeps F exact)

where Q = (L/2)||x||^2, and compares (top row) the decomposition-dependent
DC gap with (bottom row) the mismatch measure

    eps*_delta(x) = dist( partial_delta phi_i(x), partial_delta g_i(x) )

induced by our (delta_phi, delta_g, eps)-criticality.  The quadratic side has
the exact delta-subdifferential ball B(Lx, sqrt(2 L delta)); the nonquadratic
side is inner-approximated by transported subgradients: grad h(y) is a
delta-subgradient at x whenever the Bregman gap B_h(x, y) <= delta.
"""

from __future__ import annotations

import os
import tempfile
import time
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
BASE = OUT_DIR / "decomposition_dependence"
TMP_ROOT = Path(tempfile.gettempdir()) / "stochastic_dcam_matplotlib"
MPLCONFIG = TMP_ROOT / "mplconfig"
CACHE_DIR = TMP_ROOT / "cache"
MPLCONFIG.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG))
os.environ.setdefault("XDG_CACHE_HOME", str(CACHE_DIR))

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D

L = np.pi**2
DELTA_HEAT = 0.02
STEP = 0.02
VIEW = 1.0
PAD = 0.76

COLORS = {
    "min": "#2a78d6",
    "saddle": "#008300",
    "max": "#e87ba4",
    "text": "#111111",
    "soft_text": "#4B5563",
}
PROBES = {
    "min": (-0.40, 0.06),
    "saddle": (0.14, 0.58),
    "max": (0.68, 0.16),
}
STATIONARY = {
    "min": ([(-0.5, 0.0)], "o"),
    "saddle": ([(0.0, 0.5), (0.0, -0.5)], "D"),
    "max": ([(0.5, 0.0)], "^"),
}


def F(x1: np.ndarray, x2: np.ndarray) -> np.ndarray:
    return np.sin(np.pi * x1) * np.cos(np.pi * x2)


def gradF(x1: np.ndarray, x2: np.ndarray) -> np.ndarray:
    gx = np.pi * np.cos(np.pi * x1) * np.cos(np.pi * x2)
    gy = -np.pi * np.sin(np.pi * x1) * np.sin(np.pi * x2)
    return np.stack([gx, gy], axis=-1)


def make_grid(lo: float, hi: float, step: float = STEP) -> tuple[np.ndarray, np.ndarray]:
    n = int(round((hi - lo) / step)) + 1
    ax = np.linspace(lo, hi, n)
    g1, g2 = np.meshgrid(ax, ax)
    return ax, np.stack([g1.ravel(), g2.ravel()], axis=-1)


def field_chunk(
    x_pts: np.ndarray,
    y_pts: np.ndarray,
    f_y: np.ndarray,
    g_y: np.ndarray,
    delta: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return (gap2, eps1, eps2) on a chunk of evaluation points."""
    f_x = F(x_pts[:, 0], x_pts[:, 1])
    diff = x_pts[:, None, :] - y_pts[None, :, :]
    sq = np.einsum("mnk,mnk->mn", diff, diff)
    d_f = f_x[:, None] - f_y[None, :] - np.einsum("nk,mnk->mn", g_y, diff)
    breg1 = 0.5 * L * sq - d_f
    breg2 = 0.5 * L * sq + d_f
    gap2 = (f_x[:, None] - f_y[None, :] - 0.5 * L * sq).max(axis=1)

    radius = np.sqrt(2.0 * L * delta)
    target = L * x_pts
    cand1 = L * y_pts - g_y
    cand2 = L * y_pts + g_y
    tol = 1e-12
    eps = []
    for breg, cand in ((breg1, cand1), (breg2, cand2)):
        dist = np.linalg.norm(cand[None, :, :] - target[:, None, :], axis=-1)
        dist = np.where(breg <= delta + tol, dist, np.inf).min(axis=1)
        eps.append(np.maximum(0.0, dist - radius))
    return gap2, eps[0], eps[1]


def compute_fields(delta: float) -> dict[str, np.ndarray]:
    ax_e, x_all = make_grid(-VIEW, VIEW)
    _, y_all = make_grid(-VIEW - PAD, VIEW + PAD, step=0.0125)
    f_y = F(y_all[:, 0], y_all[:, 1])
    g_y = gradF(y_all[:, 0], y_all[:, 1])

    n = ax_e.size
    grad_e = gradF(x_all[:, 0], x_all[:, 1])
    gap1 = (np.linalg.norm(grad_e, axis=-1) ** 2 / (2.0 * L)).reshape(n, n)

    gap2 = np.empty(x_all.shape[0])
    eps1 = np.empty_like(gap2)
    eps2 = np.empty_like(gap2)
    chunk = 128
    for i in range(0, x_all.shape[0], chunk):
        s = slice(i, i + chunk)
        gap2[s], eps1[s], eps2[s] = field_chunk(x_all[s], y_all, f_y, g_y, delta)
    return {
        "axis": ax_e,
        "gap1": gap1,
        "gap2": gap2.reshape(n, n),
        "eps1": eps1.reshape(n, n),
        "eps2": eps2.reshape(n, n),
    }


def dial_curves(deltas: np.ndarray) -> dict[str, np.ndarray]:
    """Fine local transport grid per probe keeps the curves smooth."""
    out: dict[str, np.ndarray] = {}
    tol = 1e-12
    win, fine = 0.7, 0.004
    for name, probe in PROBES.items():
        x = np.array([probe])
        n_nodes = 2 * int(round(win / fine)) + 1
        ax1 = np.linspace(probe[0] - win, probe[0] + win, n_nodes)
        ax2 = np.linspace(probe[1] - win, probe[1] + win, n_nodes)
        g1, g2 = np.meshgrid(ax1, ax2)
        y_all = np.stack([g1.ravel(), g2.ravel()], axis=-1)
        f_y = F(y_all[:, 0], y_all[:, 1])
        g_y = gradF(y_all[:, 0], y_all[:, 1])
        f_x = F(x[:, 0], x[:, 1])
        diff = x[:, None, :] - y_all[None, :, :]
        sq = np.einsum("mnk,mnk->mn", diff, diff)[0]
        d_f = (f_x[:, None] - f_y[None, :] - np.einsum("nk,mnk->mn", g_y, diff))[0]
        target = L * x[0]
        for idx, (breg, cand) in enumerate(
            (
                (0.5 * L * sq - d_f, L * y_all - g_y),
                (0.5 * L * sq + d_f, L * y_all + g_y),
            ),
            start=1,
        ):
            dist = np.linalg.norm(cand - target[None, :], axis=-1)
            curve = np.empty_like(deltas)
            for k, dl in enumerate(deltas):
                dmin = np.where(breg <= dl + tol, dist, np.inf).min()
                curve[k] = max(0.0, dmin - np.sqrt(2.0 * L * dl))
            if not np.isfinite(curve).all():
                raise ValueError(
                    f"probe {name} off-grid: empty candidate set at small delta"
                )
            out[f"{name}{idx}"] = curve
    return out


def report(fields: dict[str, np.ndarray]) -> dict[str, float]:
    gap1, gap2 = fields["gap1"], fields["gap2"]
    eps1, eps2 = fields["eps1"], fields["eps2"]
    mirror = np.abs(eps2 - eps1[:, ::-1]).max()
    stats = {
        "gap_rel_mean": np.abs(gap1 - gap2).mean() / max(gap1.mean(), gap2.mean()),
        "gap_rel_max": np.abs(gap1 - gap2).max() / max(gap1.max(), gap2.max()),
        "gap_corr": np.corrcoef(gap1.ravel(), gap2.ravel())[0, 1],
        "eps_rel_mean": np.abs(eps1 - eps2).mean() / max(eps1.mean(), eps2.mean()),
        "eps_rel_max": np.abs(eps1 - eps2).max() / max(eps1.max(), eps2.max()),
        "eps_corr": np.corrcoef(eps1.ravel(), eps2.ravel())[0, 1],
        "mirror_check": mirror,
    }
    for key, val in stats.items():
        print(f"  {key:14s} = {val:.4f}")
    return stats


def style() -> None:
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
            "font.size": 7,
            "axes.linewidth": 0.6,
            "axes.labelsize": 7,
            "axes.titlesize": 7,
            "xtick.labelsize": 6.5,
            "ytick.labelsize": 6.5,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.major.width": 0.6,
            "ytick.major.width": 0.6,
            "xtick.major.size": 2.2,
            "ytick.major.size": 2.2,
            "legend.frameon": False,
            "legend.fontsize": 6.2,
            "text.color": COLORS["text"],
            "axes.labelcolor": COLORS["text"],
        }
    )


def draw_heatmap(ax: plt.Axes, field: np.ndarray, vmax: float, title: str) -> object:
    im = ax.imshow(
        field,
        origin="lower",
        extent=(-VIEW, VIEW, -VIEW, VIEW),
        cmap="viridis",
        vmin=0.0,
        vmax=vmax,
        interpolation="bilinear",
        rasterized=True,
    )
    for pts, marker in STATIONARY.values():
        for px, py in pts:
            ax.scatter(
                px, py, s=16, marker=marker, facecolor="white",
                edgecolor="black", linewidths=0.5, zorder=3,
            )
    ax.set_title(title, pad=3)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    return im


def main() -> None:
    t0 = time.time()
    print(f"[decomposition_dependence] delta = {DELTA_HEAT}")
    fields = compute_fields(DELTA_HEAT)
    stats = report(fields)
    deltas = np.linspace(0.0, 0.08, 161)
    dials = dial_curves(deltas)
    print(f"  compute time   = {time.time() - t0:.1f}s")

    style()
    fig = plt.figure(figsize=(7.2, 3.35))
    gs = GridSpec(
        2, 3, figure=fig, width_ratios=[1, 1, 1.42],
        wspace=0.18, hspace=0.42, left=0.055, right=0.985, top=0.90, bottom=0.13,
    )
    axes = [fig.add_subplot(gs[r, c]) for r in (0, 1) for c in (0, 1)]
    ax_dial = fig.add_subplot(gs[:, 2])

    gap_max = max(fields["gap1"].max(), fields["gap2"].max())
    eps_max = max(fields["eps1"].max(), fields["eps2"].max())
    ims = [
        draw_heatmap(axes[0], fields["gap1"], gap_max,
                     r"$\mathrm{gap}_{\mathrm{DC}}$ under $(\phi_1,g_1)$"),
        draw_heatmap(axes[1], fields["gap2"], gap_max,
                     r"$\mathrm{gap}_{\mathrm{DC}}$ under $(\phi_2,g_2)$"),
        draw_heatmap(axes[2], fields["eps1"], eps_max,
                     r"$\varepsilon^{*}_{\delta}$ under $(\phi_1,g_1)$"),
        draw_heatmap(axes[3], fields["eps2"], eps_max,
                     r"$\varepsilon^{*}_{\delta}$ under $(\phi_2,g_2)$"),
    ]
    for ax in (axes[0], axes[1]):
        ax.set_xticklabels([])
    for ax in (axes[1], axes[3]):
        ax.set_yticklabels([])
    axes[2].set_xlabel(r"$x_1$")
    axes[3].set_xlabel(r"$x_1$")
    axes[0].set_ylabel(r"$x_2$")
    axes[2].set_ylabel(r"$x_2$")
    for im, pair in zip((ims[1], ims[3]), ((axes[0], axes[1]), (axes[2], axes[3]))):
        cbar = fig.colorbar(im, ax=list(pair), fraction=0.05, pad=0.025)
        cbar.ax.tick_params(labelsize=6, width=0.6, length=2.0)
        cbar.outline.set_linewidth(0.6)

    for name in PROBES:
        ax_dial.plot(deltas, dials[f"{name}1"], color=COLORS[name], lw=1.15, ls="-")
        ax_dial.plot(deltas, dials[f"{name}2"], color=COLORS[name], lw=1.15, ls="--")
    ax_dial.axvline(DELTA_HEAT, color=COLORS["soft_text"], lw=0.7, ls=":")
    ax_dial.annotate(
        r"$\delta$ used in c, d", xy=(DELTA_HEAT, 0.985),
        xycoords=("data", "axes fraction"), xytext=(4, 0),
        textcoords="offset points", fontsize=6.2, color=COLORS["soft_text"],
    )
    ax_dial.set_xlabel(r"$\delta$")
    ax_dial.set_ylabel(r"$\varepsilon^{*}_{\delta}(\bar{x})$")
    ax_dial.set_xlim(0.0, 0.08)
    ax_dial.spines[["top", "right"]].set_visible(False)
    handles = [
        Line2D([], [], color=COLORS[name], lw=1.15, ls="-", label=f"near {name}")
        for name in PROBES
    ] + [
        Line2D([], [], color=COLORS["text"], lw=1.15, ls="-",
               label=r"decomp. $(\phi_1,g_1)$"),
        Line2D([], [], color=COLORS["text"], lw=1.15, ls="--",
               label=r"decomp. $(\phi_2,g_2)$"),
    ]
    ax_dial.legend(handles=handles, loc="upper right", handlelength=1.9,
                   labelspacing=0.4, borderaxespad=0.2)

    for label, ax in zip("abcd", axes):
        ax.text(-0.16, 1.07, label, transform=ax.transAxes,
                fontsize=8, fontweight="bold", va="bottom")
    ax_dial.text(-0.14, 1.028, "e", transform=ax_dial.transAxes,
                 fontsize=8, fontweight="bold", va="bottom")

    fig.savefig(BASE.with_suffix(".pdf"), dpi=600)
    fig.savefig(BASE.with_suffix(".png"), dpi=600)
    print(f"  saved          = {BASE}.pdf/.png")
    print(f"  caption stats: eps rel-max {stats['eps_rel_max']:.3f}, "
          f"gap rel-max {stats['gap_rel_max']:.3f}")


if __name__ == "__main__":
    main()
