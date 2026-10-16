#!/usr/bin/env python3
"""Generate a paper-style comparison of Goldstein and approximate subgradients."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path


OUT_DIR = Path(__file__).resolve().parent
BASE = OUT_DIR / "goldstein_vs_approximate_subdifferential"
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


COLORS = {
    "blue": "#0072B2",
    "orange": "#D55E00",
    "green": "#009E73",
    "grid": "#E5E7EB",
    "axis": "#222222",
    "text": "#111111",
    "soft_text": "#4B5563",
    "violet": "#5B4BC4",
}


def B(y: np.ndarray | float) -> np.ndarray | float:
    return 0.45 * (y - 0.25) ** 2 + 0.45


def grad_B(y: float) -> float:
    return 0.9 * (y - 0.25)


def affine_at(point: float, slope: float, y: np.ndarray) -> np.ndarray:
    return B(point) + slope * (y - point)


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
            "font.size": 8.5,
            "axes.labelsize": 9,
            "axes.titlesize": 9.5,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8.2,
            "mathtext.fontset": "stix",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.edgecolor": COLORS["axis"],
            "axes.linewidth": 0.8,
            "xtick.color": COLORS["soft_text"],
            "ytick.color": COLORS["soft_text"],
        }
    )


def decorate_axis(ax: plt.Axes, show_ylabel: bool) -> None:
    ax.set_xlim(-1.15, 2.15)
    ax.set_ylim(0.05, 2.35)
    ax.set_xlabel(r"$y$")
    if show_ylabel:
        ax.set_ylabel("value")
    else:
        ax.tick_params(labelleft=False)

    ax.grid(True, color=COLORS["grid"], linewidth=0.6, alpha=0.85)
    ax.set_axisbelow(True)
    ax.tick_params(length=3, width=0.7)


def draw_goldstein_panel(ax: plt.Axes, y_grid: np.ndarray) -> None:
    x = 0.45
    delta = 0.62
    y1 = -0.02
    y2 = 0.92

    ax.plot(y_grid, B(y_grid), color=COLORS["blue"], lw=2.1, solid_capstyle="round")
    ax.axvspan(x - delta, x + delta, color=COLORS["green"], alpha=0.055, lw=0)
    ax.axvline(x - delta, color=COLORS["green"], lw=1.0, ls=(0, (4, 4)), alpha=0.8)
    ax.axvline(x + delta, color=COLORS["green"], lw=1.0, ls=(0, (4, 4)), alpha=0.8)

    for point, label, x_shift in [
        (y1, r"$\partial B(y_1)$", -0.72),
        (y2, r"$\partial B(y_2)$", 0.08),
    ]:
        local = np.linspace(point - 0.46, point + 0.46, 60)
        ax.plot(
            local,
            affine_at(point, grad_B(point), local),
            color=COLORS["orange"],
            lw=1.7,
            ls=(0, (5, 3)),
            solid_capstyle="round",
        )
        ax.scatter([point], [B(point)], s=28, color=COLORS["orange"], zorder=5)
        ax.text(
            point + x_shift,
            B(point) + 0.13,
            label,
            color=COLORS["orange"],
            fontsize=8,
        )

    ax.scatter([x], [B(x)], s=36, color=COLORS["violet"], zorder=6)
    ax.text(x + 0.05, B(x) + 0.12, r"$x$", color=COLORS["violet"], fontsize=9)
    ax.text(y1 - 0.02, B(y1) - 0.18, r"$y_1$", color=COLORS["soft_text"], fontsize=8)
    ax.text(y2 + 0.02, B(y2) - 0.20, r"$y_2$", color=COLORS["soft_text"], fontsize=8)

    bracket_y = 0.31
    ax.annotate(
        "",
        xy=(x - delta, bracket_y),
        xytext=(x + delta, bracket_y),
        arrowprops={
            "arrowstyle": "|-|",
            "lw": 1.1,
            "color": COLORS["green"],
            "shrinkA": 0,
            "shrinkB": 0,
        },
    )
    ax.text(
        x,
        bracket_y - 0.13,
        r"$\|y-x\|\leq\delta$",
        ha="center",
        va="top",
        color=COLORS["green"],
        fontsize=8.4,
    )
    ax.set_title(r"(a) Goldstein relaxation", fontweight="bold")


def draw_approximate_panel(ax: plt.Axes, y_grid: np.ndarray) -> None:
    x = 0.45
    delta = 0.30
    exact_slope = grad_B(x)
    approximate_slope = exact_slope + 0.52
    exact_line = affine_at(x, exact_slope, y_grid)
    approximate_line = affine_at(x, approximate_slope, y_grid) - delta

    ax.plot(y_grid, B(y_grid), color=COLORS["blue"], lw=2.1, solid_capstyle="round")
    ax.plot(
        y_grid,
        exact_line,
        color=COLORS["orange"],
        lw=1.8,
        ls=(0, (5, 3)),
        solid_capstyle="round",
    )
    ax.plot(
        y_grid,
        approximate_line,
        color=COLORS["green"],
        lw=1.9,
        ls=(0, (6, 2, 1.5, 2)),
        solid_capstyle="round",
    )

    visible = (y_grid >= -0.15) & (y_grid <= 1.85)
    ax.fill_between(
        y_grid[visible],
        exact_line[visible],
        approximate_line[visible],
        color=COLORS["green"],
        alpha=0.12,
        linewidth=0,
    )

    ax.scatter([x], [B(x)], s=36, color=COLORS["violet"], zorder=6)
    ax.text(x + 0.05, B(x) + 0.09, r"$x$", color=COLORS["violet"], fontsize=9)

    exact_at_x = B(x)
    approx_at_x = B(x) - delta
    ax.annotate(
        "",
        xy=(x, exact_at_x),
        xytext=(x, approx_at_x),
        arrowprops={
            "arrowstyle": "<|-|>",
            "lw": 1.0,
            "color": COLORS["axis"],
            "shrinkA": 1,
            "shrinkB": 1,
        },
    )
    ax.text(x + 0.08, (exact_at_x + approx_at_x) / 2, r"$\Delta$", fontsize=10)
    ax.text(
        1.02,
        B(x) + approximate_slope * (1.02 - x) - delta + 0.08,
        r"$b\in\partial_{\Delta}B(x)$",
        color=COLORS["green"],
        fontsize=8.4,
    )
    ax.set_title(r"(b) Approximate subdifferential", fontweight="bold")


def make_figure() -> plt.Figure:
    setup_style()
    y_grid = np.linspace(-1.15, 2.15, 500)

    fig, axes = plt.subplots(1, 2, figsize=(7.05, 3.05), sharey=True)
    fig.subplots_adjust(left=0.07, right=0.995, bottom=0.19, top=0.75, wspace=0.12)

    for i, ax in enumerate(axes):
        decorate_axis(ax, show_ylabel=i == 0)

    draw_goldstein_panel(axes[0], y_grid)
    draw_approximate_panel(axes[1], y_grid)

    handles = [
        Line2D([0], [0], color=COLORS["blue"], lw=2.1, label=r"$B(y)$"),
        Line2D(
            [0],
            [0],
            color=COLORS["orange"],
            lw=1.8,
            ls=(0, (5, 3)),
            label="exact support",
        ),
        Line2D(
            [0],
            [0],
            color=COLORS["green"],
            lw=1.9,
            ls=(0, (6, 2, 1.5, 2)),
            label="relaxed support",
        ),
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.985),
        ncol=3,
        frameon=False,
        handlelength=2.8,
        columnspacing=2.8,
    )
    return fig


def main() -> None:
    fig = make_figure()
    fig.savefig(BASE.with_suffix(".pdf"), bbox_inches="tight", pad_inches=0.02)
    fig.savefig(BASE.with_suffix(".svg"), bbox_inches="tight", pad_inches=0.02)
    fig.savefig(BASE.with_suffix(".png"), dpi=320, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print(f"Wrote {BASE.with_suffix('.pdf')}")
    print(f"Wrote {BASE.with_suffix('.svg')}")
    print(f"Wrote {BASE.with_suffix('.png')}")


if __name__ == "__main__":
    main()
