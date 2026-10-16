const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const sharp = require("/Users/liluxuan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp");

const outDir = __dirname;
const svgPath = path.join(outDir, "epsilon_subgradient.svg");
const pngPath = path.join(outDir, "epsilon_subgradient.png");
const pdfPath = path.join(outDir, "epsilon_subgradient.pdf");
const htmlPath = path.join(outDir, "epsilon_subgradient_print.html");
const latexPath = path.join(outDir, "latex_include.tex");
const manifestPath = path.join(outDir, "MANIFEST.md");

const W = 1680;
const H = 900;

const colors = {
  blue: "#0072B2",
  orange: "#D55E00",
  green: "#009E73",
  grid: "#e5e7eb",
  axis: "#222222",
  text: "#111111",
  softText: "#4b5563",
};

function f(y) {
  return 0.45 * (y - 0.25) ** 2 + 0.45;
}

function gradF(y) {
  return 0.9 * (y - 0.25);
}

function linePath(points) {
  return points
    .map((p, i) => `${i === 0 ? "M" : "L"} ${p[0].toFixed(2)} ${p[1].toFixed(2)}`)
    .join(" ");
}

function makeScale(domainMin, domainMax, rangeMin, rangeMax) {
  return (value) => rangeMin + ((value - domainMin) / (domainMax - domainMin)) * (rangeMax - rangeMin);
}

function drawPanel({
  id,
  x,
  y,
  width,
  height,
  xMin,
  xMax,
  yMin,
  yMax,
  showTicks,
  panelLabel,
}) {
  const sx = makeScale(xMin, xMax, x, x + width);
  const sy = makeScale(yMin, yMax, y + height, y);

  const x0 = 0.85;
  const fx0 = f(x0);
  const v = gradF(x0);
  const delta = 0.85;
  const yArrow = 2.35;
  const topArrow = fx0 + v * (yArrow - x0);

  const n = 360;
  const ys = Array.from({ length: n }, (_, i) => xMin + (i / (n - 1)) * (xMax - xMin));
  const fPoints = ys.map((yy) => [sx(yy), sy(f(yy))]);
  const supportPoints = ys.map((yy) => [sx(yy), sy(fx0 + v * (yy - x0))]);
  const relaxedPoints = ys.map((yy) => [sx(yy), sy(fx0 + v * (yy - x0) - delta)]);
  const bandPath =
    linePath(supportPoints) +
    " " +
    relaxedPoints
      .slice()
      .reverse()
      .map((p) => `L ${p[0].toFixed(2)} ${p[1].toFixed(2)}`)
      .join(" ") +
    " Z";

  const xTicks = showTicks ? [-2, -1, 0, 1, 2, 3].filter((t) => t >= xMin && t <= xMax) : [];
  const yTicks = showTicks ? [0, 1, 2, 3, 4].filter((t) => t >= yMin && t <= yMax) : [];

  let s = "";
  s += `<g>`;
  s += `<defs><clipPath id="clip-${id}"><rect x="${x}" y="${y}" width="${width}" height="${height}"/></clipPath></defs>`;
  s += `<rect x="${x}" y="${y}" width="${width}" height="${height}" fill="white"/>`;

  for (const tick of xTicks) {
    s += `<line x1="${sx(tick).toFixed(2)}" y1="${y}" x2="${sx(tick).toFixed(2)}" y2="${y + height}" stroke="${colors.grid}" stroke-width="1"/>`;
  }
  for (const tick of yTicks) {
    s += `<line x1="${x}" y1="${sy(tick).toFixed(2)}" x2="${x + width}" y2="${sy(tick).toFixed(2)}" stroke="${colors.grid}" stroke-width="1"/>`;
  }

  s += `<g clip-path="url(#clip-${id})">`;
  s += `<path d="${bandPath}" fill="${colors.green}" opacity="0.14"/>`;
  s += `<path d="${linePath(fPoints)}" fill="none" stroke="${colors.blue}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>`;
  s += `<path d="${linePath(supportPoints)}" fill="none" stroke="${colors.orange}" stroke-width="4" stroke-dasharray="16 8" stroke-linejoin="round" stroke-linecap="round"/>`;
  s += `<path d="${linePath(relaxedPoints)}" fill="none" stroke="${colors.green}" stroke-width="4" stroke-dasharray="18 7 4 7" stroke-linejoin="round" stroke-linecap="round"/>`;
  s += `</g>`;

  if (showTicks) {
    s += `<line x1="${x}" y1="${y + height}" x2="${x + width}" y2="${y + height}" stroke="${colors.axis}" stroke-width="2"/>`;
    s += `<line x1="${x}" y1="${y}" x2="${x}" y2="${y + height}" stroke="${colors.axis}" stroke-width="2"/>`;
    for (const tick of xTicks) {
      s += `<line x1="${sx(tick).toFixed(2)}" y1="${y + height}" x2="${sx(tick).toFixed(2)}" y2="${y + height + 8}" stroke="${colors.axis}" stroke-width="1.5"/>`;
      s += `<text x="${sx(tick).toFixed(2)}" y="${y + height + 33}" text-anchor="middle" font-size="25" fill="${colors.softText}">${tick}</text>`;
    }
    for (const tick of yTicks) {
      s += `<line x1="${x - 8}" y1="${sy(tick).toFixed(2)}" x2="${x}" y2="${sy(tick).toFixed(2)}" stroke="${colors.axis}" stroke-width="1.5"/>`;
      s += `<text x="${x - 19}" y="${sy(tick).toFixed(2) + 8}" text-anchor="end" font-size="25" fill="${colors.softText}">${tick}</text>`;
    }
    s += `<text x="${x + width / 2}" y="${y + height + 74}" text-anchor="middle" font-size="31" fill="${colors.text}" font-style="italic">y</text>`;
    s += `<text transform="translate(${x - 76},${y + height / 2}) rotate(-90)" text-anchor="middle" font-size="29" fill="${colors.text}">value</text>`;
  } else {
    s += `<rect x="${x}" y="${y}" width="${width}" height="${height}" fill="none" stroke="#6b7280" stroke-width="2"/>`;
  }

  const pointVisible = x0 >= xMin && x0 <= xMax && fx0 >= yMin && fx0 <= yMax;
  if (pointVisible) {
    s += `<line x1="${sx(x0).toFixed(2)}" y1="${sy(yMin).toFixed(2)}" x2="${sx(x0).toFixed(2)}" y2="${sy(fx0).toFixed(2)}" stroke="#737373" stroke-width="2" stroke-dasharray="4 7"/>`;
    s += `<circle cx="${sx(x0).toFixed(2)}" cy="${sy(fx0).toFixed(2)}" r="${showTicks ? 8 : 6}" fill="${colors.text}"/>`;

    if (showTicks) {
      s += `<text x="${sx(x0) + 16}" y="${sy(fx0) - 20}" font-size="27" fill="${colors.text}">(x, f(x))</text>`;
    }
  }

  s += `<line x1="${sx(yArrow).toFixed(2)}" y1="${sy(topArrow).toFixed(2)}" x2="${sx(yArrow).toFixed(2)}" y2="${sy(topArrow - delta).toFixed(2)}" stroke="${colors.text}" stroke-width="${showTicks ? 4 : 3}" marker-start="url(#arrow)" marker-end="url(#arrow)"/>`;
  s += `<text x="${sx(yArrow) + (showTicks ? 17 : 14)}" y="${sy(topArrow - delta / 2) + 10}" font-size="${showTicks ? 38 : 34}" fill="${colors.text}" font-style="italic">&#948;</text>`;

  if (!showTicks) {
    s += `<text x="${x + width / 2}" y="${y + height + 45}" text-anchor="middle" font-size="27" fill="${colors.softText}">local vertical gap</text>`;
  }

  s += `<text x="${x}" y="${y - 24}" font-size="29" font-weight="600" fill="${colors.text}">${panelLabel}</text>`;
  s += `</g>`;
  return s;
}

function legendItem(x, y, color, dash, text) {
  const dashAttr = dash ? ` stroke-dasharray="${dash}"` : "";
  return [
    `<line x1="${x}" y1="${y}" x2="${x + 82}" y2="${y}" stroke="${color}" stroke-width="5" stroke-linecap="round"${dashAttr}/>`,
    `<text x="${x + 100}" y="${y + 9}" font-size="28" fill="${colors.text}">${text}</text>`,
  ].join("");
}

function makeSvg() {
  const main = drawPanel({
    id: "main",
    x: 130,
    y: 160,
    width: 900,
    height: 580,
    xMin: -2.25,
    xMax: 3.15,
    yMin: -0.85,
    yMax: 4.25,
    showTicks: true,
    panelLabel: "Global view",
  });

  const zoom = drawPanel({
    id: "zoom",
    x: 1130,
    y: 230,
    width: 440,
    height: 350,
    xMin: 1.85,
    xMax: 2.72,
    yMin: 0.24,
    yMax: 2.75,
    showTicks: false,
    panelLabel: "Zoomed error",
  });

  const legend = [
    legendItem(150, 72, colors.blue, "", "<tspan font-style=\"italic\">f</tspan>(<tspan font-style=\"italic\">y</tspan>)"),
    legendItem(430, 72, colors.orange, "16 8", "<tspan font-style=\"italic\">f</tspan>(<tspan font-style=\"italic\">x</tspan>) + <tspan font-style=\"italic\">v</tspan><tspan baseline-shift=\"super\" font-size=\"18\">T</tspan>(<tspan font-style=\"italic\">y</tspan> - <tspan font-style=\"italic\">x</tspan>)"),
    legendItem(920, 72, colors.green, "18 7 4 7", "<tspan font-style=\"italic\">f</tspan>(<tspan font-style=\"italic\">x</tspan>) + <tspan font-style=\"italic\">v</tspan><tspan baseline-shift=\"super\" font-size=\"18\">T</tspan>(<tspan font-style=\"italic\">y</tspan> - <tspan font-style=\"italic\">x</tspan>) - &#948;"),
  ].join("");

  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto-start-reverse">
      <path d="M 0 0 L 8 4 L 0 8 z" fill="${colors.text}"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="white"/>
  <g font-family="Times New Roman, Times, DejaVu Serif, serif">
    ${legend}
    ${main}
    ${zoom}
  </g>
</svg>`;
}

function writeLatexInclude(pdfWritten) {
  const ext = pdfWritten ? "pdf" : "svg";
  const content = `% Delta-subgradient illustration
\\begin{figure}[t]
    \\centering
    \\includegraphics[width=0.86\\textwidth]{figure/epsilon_subgradient.${ext}}
    \\caption{Geometric interpretation of the $\\delta$-subgradient. The green affine function is the ordinary supporting affine function shifted downward by a vertical distance $\\delta$.}
    \\label{fig:epsilon_subgradient}
\\end{figure}
`;
  fs.writeFileSync(latexPath, content);
}

function writeManifest(pdfWritten) {
  const pdfLine = pdfWritten
    ? "- `epsilon_subgradient.pdf`: PDF export for LaTeX inclusion.\n"
    : "- `epsilon_subgradient.pdf`: not generated because headless Chrome export failed.\n";
  const content = `# Figure Manifest

## epsilon_subgradient

- ` + "`gen_epsilon_subgradient.js`" + `: reproducible source script.
- ` + "`epsilon_subgradient.svg`" + `: vector source figure.
- ` + "`epsilon_subgradient.png`" + `: high-resolution raster preview.
${pdfLine}- ` + "`latex_include.tex`" + `: LaTeX include snippet.

Purpose: illustrate that $\\delta$ is a vertical relaxation of the supporting affine function in the definition of the $\\delta$-subgradient.
`;
  fs.writeFileSync(manifestPath, content);
}

async function main() {
  const svg = makeSvg();
  fs.writeFileSync(svgPath, svg);

  await sharp(Buffer.from(svg)).resize({ width: 3360 }).png().toFile(pngPath);

  fs.writeFileSync(
    htmlPath,
    `<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
@page { size: 8.4in 4.5in; margin: 0; }
html, body { margin: 0; padding: 0; width: 8.4in; height: 4.5in; background: white; }
svg { width: 8.4in; height: 4.5in; display: block; }
</style>
</head>
<body>
${svg}
</body>
</html>`
  );

  let pdfWritten = false;
  try {
    execFileSync("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", [
      "--headless",
      "--disable-gpu",
      "--no-pdf-header-footer",
      `--print-to-pdf=${pdfPath}`,
      `file://${htmlPath}`,
    ]);
    pdfWritten = fs.existsSync(pdfPath) && fs.statSync(pdfPath).size > 0;
  } catch (error) {
    pdfWritten = false;
  }

  writeLatexInclude(pdfWritten);
  writeManifest(pdfWritten);

  console.log(`Wrote ${svgPath}`);
  console.log(`Wrote ${pngPath}`);
  if (pdfWritten) {
    console.log(`Wrote ${pdfPath}`);
  } else {
    console.log("Skipped PDF export; SVG and PNG are available.");
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
