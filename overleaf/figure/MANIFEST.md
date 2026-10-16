# Figure Manifest

## epsilon_subgradient

- `gen_epsilon_subgradient.js`: reproducible source script.
- `epsilon_subgradient.svg`: vector source figure.
- `epsilon_subgradient.png`: high-resolution raster preview.
- `epsilon_subgradient.pdf`: PDF export for LaTeX inclusion.
- `latex_include.tex`: LaTeX include snippet.

Purpose: illustrate that $\delta$ is a vertical relaxation of the supporting affine function in the definition of the $\delta$-subgradient.

## decomposition_dependence

- `gen_decomposition_dependence.py`: reproducible source script (run with a Python that has numpy + matplotlib; ~2.5 min).
- `decomposition_dependence.pdf`: PDF export for LaTeX inclusion.
- `decomposition_dependence.png`: high-resolution raster preview.

Purpose: contrast the decomposition dependence of the Frank--Wolfe DC gap of Maskan et al. (2025) with the near decomposition-invariance of the $(\delta_\phi,\delta_g,\varepsilon)$-mismatch, on $F=\sin(\pi x_1)\cos(\pi x_2)$ with decompositions $(Q,\,Q-F)$ and $(F+Q,\,Q)$. Panels a-b: the two gap landscapes (qualitatively different); panels c-d: the tightest mismatch $\varepsilon^*_\delta$ at $\delta=0.02$ (same structure, exact mirror identity); panel e: $\varepsilon^*_\delta(\bar x)$ versus the dial $\delta$ at three probe points. Printed diagnostics: mean relative deviation across decompositions 17% (mismatch) vs 27% (gap), correlation 0.93 vs 0.77, mirror identity exact to machine precision.
