---
title: Screaming Firehawk
description: 
published: true
date: 2026-06-04T01:09:19.964Z
tags: 
editor: markdown
dateCreated: 2024-11-11T20:47:57.922Z
---

# Screaming Firehawk
Future VTOL aircraft. Flip & Burn.
Powered by diesel-electric engine.
![gl10_test013_8-19-14.jpg](/gl10_test013_8-19-14.jpg)

Instead of ptototype gobilda motors, we will use some brushless ones. Comparison from Claude AI:

<div>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BLDC vs Brushed DC — Power Draw Comparison</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

  :root {
    --bg-primary: #0c0e12;
    --bg-secondary: #13161c;
    --bg-card: #181c24;
    --bg-card-hover: #1e2330;
    --border: rgba(255,255,255,0.06);
    --border-accent: rgba(255,255,255,0.1);
    --text-primary: #e8eaed;
    --text-secondary: #8b919e;
    --text-tertiary: #565c6a;
    --accent-red: #e85c5c;
    --accent-red-soft: rgba(232,92,92,0.12);
    --accent-red-glow: rgba(232,92,92,0.25);
    --accent-green: #34c88a;
    --accent-green-soft: rgba(52,200,138,0.12);
    --accent-green-glow: rgba(52,200,138,0.25);
    --accent-amber: #e8a84c;
    --accent-blue: #5b8def;
    --font-body: 'DM Sans', -apple-system, sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;
    --radius-xl: 18px;
  }

  body {
    font-family: var(--font-body);
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.6;
    min-height: 100vh;
    -webkit-font-smoothing: antialiased;
  }

  .container {
    max-width: 960px;
    margin: 0 auto;
    padding: 2.5rem 1.5rem 4rem;
  }

  .header {
    margin-bottom: 2.5rem;
  }

  .header h1 {
    font-size: 1.6rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 0.35rem;
    background: linear-gradient(135deg, var(--text-primary) 0%, var(--text-secondary) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .header p {
    font-size: 0.85rem;
    color: var(--text-tertiary);
    max-width: 600px;
  }

  .motor-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 2rem;
  }

  .motor-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.1rem 1.25rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
  }

  .motor-card:hover {
    border-color: var(--border-accent);
  }

  .motor-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
  }

  .motor-card.red::before { background: var(--accent-red); }
  .motor-card.green::before { background: var(--accent-green); }

  .motor-card .tag {
    display: inline-block;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 3px 8px;
    border-radius: var(--radius-sm);
    margin-bottom: 0.6rem;
  }

  .motor-card.red .tag {
    background: var(--accent-red-soft);
    color: var(--accent-red);
  }

  .motor-card.green .tag {
    background: var(--accent-green-soft);
    color: var(--accent-green);
  }

  .motor-card .name {
    font-size: 1.05rem;
    font-weight: 600;
    margin-bottom: 0.15rem;
    letter-spacing: -0.01em;
  }

  .motor-card .type {
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-bottom: 0.6rem;
  }

  .motor-card .specs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem 1.2rem;
    font-size: 0.72rem;
    font-family: var(--font-mono);
    color: var(--text-tertiary);
  }

  .motor-card .specs span {
    white-space: nowrap;
  }

  .control-section {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.25rem 1.5rem;
    margin-bottom: 2rem;
  }

  .control-section label {
    display: block;
    font-size: 0.82rem;
    font-weight: 500;
    color: var(--text-secondary);
    margin-bottom: 0.6rem;
  }

  .slider-row {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  input[type="range"] {
    -webkit-appearance: none;
    appearance: none;
    flex: 1;
    height: 4px;
    border-radius: 2px;
    background: var(--border-accent);
    outline: none;
    cursor: pointer;
  }

  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: var(--accent-green);
    border: 3px solid var(--bg-primary);
    box-shadow: 0 0 10px var(--accent-green-glow);
    cursor: pointer;
    transition: transform 0.15s;
  }

  input[type="range"]::-webkit-slider-thumb:hover {
    transform: scale(1.15);
  }

  input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: var(--accent-green);
    border: 3px solid var(--bg-primary);
    box-shadow: 0 0 10px var(--accent-green-glow);
    cursor: pointer;
  }

  .slider-value {
    font-family: var(--font-mono);
    font-size: 1.1rem;
    font-weight: 600;
    min-width: 52px;
    text-align: right;
    color: var(--accent-green);
  }

  .control-hint {
    font-size: 0.72rem;
    color: var(--text-tertiary);
    margin-top: 0.5rem;
    line-height: 1.5;
  }

  .chart-section {
    margin-bottom: 2.5rem;
  }

  .chart-title {
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-secondary);
    margin-bottom: 0.3rem;
    letter-spacing: 0.02em;
  }

  .chart-subtitle {
    font-size: 0.7rem;
    color: var(--text-tertiary);
    margin-bottom: 1rem;
  }

  .chart-wrap {
    position: relative;
    width: 100%;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.25rem;
  }

  .chart-canvas-wrap {
    position: relative;
    width: 100%;
    height: 300px;
  }

  .chart-canvas-wrap.short {
    height: 220px;
  }

  .legend {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-top: 1rem;
    padding-top: 0.75rem;
    border-top: 1px solid var(--border);
  }

  .legend-item {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.72rem;
    color: var(--text-secondary);
  }

  .legend-dot {
    width: 8px;
    height: 8px;
    border-radius: 2px;
    flex-shrink: 0;
  }

  .legend-line {
    width: 18px;
    height: 0;
    flex-shrink: 0;
  }

  .summary-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-bottom: 2rem;
  }

  .summary-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 0.9rem 1rem;
    text-align: center;
  }

  .summary-card .label {
    font-size: 0.68rem;
    color: var(--text-tertiary);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 0.25rem;
  }

  .summary-card .value {
    font-family: var(--font-mono);
    font-size: 1.3rem;
    font-weight: 700;
  }

  .summary-card .value.green { color: var(--accent-green); }
  .summary-card .value.amber { color: var(--accent-amber); }
  .summary-card .value.blue { color: var(--accent-blue); }

  .summary-card .unit {
    font-size: 0.7rem;
    color: var(--text-tertiary);
    margin-top: 2px;
  }

  .data-table-wrap {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    overflow: hidden;
  }

  .data-table-title {
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-secondary);
    padding: 1rem 1.25rem 0.6rem;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.75rem;
  }

  thead th {
    text-align: right;
    padding: 0.5rem 0.6rem;
    font-weight: 500;
    color: var(--text-tertiary);
    font-size: 0.68rem;
    letter-spacing: 0.03em;
    text-transform: uppercase;
    border-bottom: 1px solid var(--border-accent);
    white-space: nowrap;
  }

  thead th:first-child { text-align: left; padding-left: 1.25rem; }

  tbody td {
    text-align: right;
    padding: 0.55rem 0.6rem;
    font-family: var(--font-mono);
    font-size: 0.73rem;
    border-bottom: 1px solid var(--border);
    color: var(--text-secondary);
  }

  tbody td:first-child {
    text-align: left;
    padding-left: 1.25rem;
    color: var(--text-primary);
    font-weight: 500;
  }

  tbody tr:last-child td { border-bottom: none; }

  tbody tr:hover td { background: var(--bg-card-hover); }

  .td-red { color: var(--accent-red) !important; }
  .td-green { color: var(--accent-green) !important; }
  .td-saving { color: var(--accent-green) !important; font-weight: 600 !important; }

  @media (max-width: 640px) {
    .motor-cards { grid-template-columns: 1fr; }
    .summary-cards { grid-template-columns: 1fr; }
    .container { padding: 1.5rem 1rem 3rem; }
    table { font-size: 0.68rem; }
  }
</style>
</head>
<body>

<div class="container">

  <div class="header">
    <h1>BLDC vs brushed DC — power draw comparison</h1>
    <p>Matched operating points: at each RPM, both motors produce the same torque. The BLDC model includes FOC controller overhead; the goBILDA model includes brush friction and iron losses.</p>
  </div>

  <div class="motor-cards">
    <div class="motor-card red">
      <div class="tag">Baseline</div>
      <div class="name">goBILDA 5203</div>
      <div class="type">Brushed DC, 12V nominal</div>
      <div class="specs">
        <span>R = 1.30 Ω</span>
        <span>Kt = 0.0191 N·m/A</span>
        <span>Stall = 1.47 kg·cm</span>
        <span>I₀ = 0.25 A</span>
      </div>
    </div>
    <div class="motor-card green">
      <div class="tag">Replacement</div>
      <div class="name">Surpass C2838 V2 800KV</div>
      <div class="type">BLDC + FOC, 12V supply</div>
      <div class="specs">
        <span>R = 0.115 Ω</span>
        <span>Kt = 0.0119 N·m/A</span>
        <span>Max = 23 A / 380 W</span>
        <span>I₀ = 0.50 A</span>
      </div>
    </div>
  </div>

  <div class="control-section">
    <label>Load factor — percentage of goBILDA's max torque at each RPM</label>
    <div class="slider-row">
      <input type="range" min="5" max="100" value="50" step="5" id="load-slider" />
      <span class="slider-value" id="load-out">50%</span>
    </div>
    <div class="control-hint">100% = goBILDA at full 12 V (maximum torque-speed curve). 50% = half that torque at each speed. Adjust to match your typical operating load.</div>
  </div>

  <div class="summary-cards" id="summary-cards">
    <div class="summary-card"><div class="label">Avg. power saving</div><div class="value green" id="s-avg">—</div><div class="unit">across all speeds</div></div>
    <div class="summary-card"><div class="label">Peak saving</div><div class="value amber" id="s-peak">—</div><div class="unit" id="s-peak-rpm">—</div></div>
    <div class="summary-card"><div class="label">Avg. heat reduction</div><div class="value blue" id="s-heat">—</div><div class="unit">less thermal waste</div></div>
  </div>

  <div class="chart-section">
    <div class="chart-title">PSU power draw at matched torque</div>
    <div class="chart-subtitle">Solid = total PSU input — dashed = wasted as heat</div>
    <div class="chart-wrap">
      <div class="chart-canvas-wrap"><canvas id="powerChart"></canvas></div>
      <div class="legend" id="legend1"></div>
    </div>
  </div>

  <div class="chart-section">
    <div class="chart-title">Power saving — C2838 vs goBILDA</div>
    <div class="chart-subtitle">Percentage reduction in PSU draw at each speed, same mechanical output</div>
    <div class="chart-wrap">
      <div class="chart-canvas-wrap short"><canvas id="savingsChart"></canvas></div>
      <div class="legend" id="legend2"></div>
    </div>
  </div>

  <div class="data-table-wrap">
    <div class="data-table-title">Detailed operating points</div>
    <div id="table-container"></div>
  </div>

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script>
const V = 12;
const gob_noload_rpm = 6000;
const gob_noload_I = 0.25;
const gob_stall_I = 9.2;
const gob_stall_T_kgcm = 1.47;
const gob_stall_T = gob_stall_T_kgcm * 0.0981;
const gob_R = 1.30;
const gob_Kt = gob_stall_T / gob_stall_I;
const gob_Ke = V / gob_noload_rpm;
const gob_noload_power = V * gob_noload_I;

const bldc_R = 0.115;
const bldc_KV = 800;
const bldc_Kt = 60 / (2 * Math.PI * bldc_KV);
const bldc_noload_I = 0.5;
const bldc_eff_foc = 0.95;

const rpms = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500];

function compute(loadFrac) {
  const gob_psu = [], bldc_psu = [], savings_pct = [], bldc_heat = [], gob_heat = [];
  const rows = [];

  for (const rpm of rpms) {
    const max_T = gob_stall_T * (1 - rpm / gob_noload_rpm);
    if (max_T <= 0) {
      gob_psu.push(null); bldc_psu.push(null); savings_pct.push(null);
      gob_heat.push(null); bldc_heat.push(null);
      rows.push({ rpm, T_kgcm: null, gob_pw: null, bldc_pw: null, gob_h: null, bldc_h: null, P_mech: null, save: null });
      continue;
    }
    const T = max_T * loadFrac;
    const T_kgcm = T / 0.0981;
    const P_mech = T * (rpm * 2 * Math.PI / 60);

    // goBILDA model with corrected fixed overhead
    const gob_I_load = gob_noload_I + (gob_stall_I - gob_noload_I) * (T / gob_stall_T);
    const gob_V_needed = rpm * gob_Ke + gob_I_load * gob_R;
    // Electrical input at the operating point
    let gob_pw = gob_V_needed * gob_I_load;
    // Add fixed mechanical overhead: brush friction + windage, proportional to speed
    // The no-load power (V * I_noload = 3W at full speed) represents these fixed losses
    const gob_friction_loss = gob_noload_power * (rpm / gob_noload_rpm);
    gob_pw += gob_friction_loss;
    const gob_h = gob_pw - P_mech;

    // BLDC model
    const bldc_I_torque = T / bldc_Kt;
    const bldc_I_total = bldc_I_torque + bldc_noload_I;
    const bldc_back_emf = rpm / bldc_KV;
    const copper_loss = bldc_I_total * bldc_I_total * bldc_R;
    const iron_loss = bldc_noload_I * bldc_back_emf;
    let bldc_pw = (P_mech + copper_loss + iron_loss) / bldc_eff_foc;
    const bldc_h_val = bldc_pw - P_mech;

    const save = Math.round((1 - bldc_pw / gob_pw) * 100);

    gob_psu.push(+gob_pw.toFixed(2));
    bldc_psu.push(+bldc_pw.toFixed(2));
    gob_heat.push(+gob_h.toFixed(2));
    bldc_heat.push(+bldc_h_val.toFixed(2));
    savings_pct.push(save);

    rows.push({
      rpm,
      T_kgcm: +T_kgcm.toFixed(3),
      gob_pw: +gob_pw.toFixed(2),
      bldc_pw: +bldc_pw.toFixed(2),
      gob_h: +gob_h.toFixed(2),
      bldc_h: +bldc_h_val.toFixed(2),
      P_mech: +P_mech.toFixed(2),
      save
    });
  }
  return { gob_psu, bldc_psu, savings_pct, gob_heat, bldc_heat, rows };
}

// Chart theming
const gridColor = 'rgba(255,255,255,0.05)';
const textColor = 'rgba(255,255,255,0.45)';
const RED = '#e85c5c';
const GREEN = '#34c88a';
const RED_SOFT = 'rgba(232,92,92,0.10)';
const GREEN_SOFT = 'rgba(52,200,138,0.10)';
const RED_DASH = 'rgba(232,92,92,0.35)';
const GREEN_DASH = 'rgba(52,200,138,0.35)';

Chart.defaults.font.family = "'DM Sans', sans-serif";

const init = compute(0.5);

// Power chart
const chart1 = new Chart(document.getElementById('powerChart'), {
  type: 'line',
  data: {
    labels: rpms.map(s => s.toLocaleString()),
    datasets: [
      { label: 'goBILDA PSU', data: init.gob_psu, borderColor: RED, backgroundColor: RED_SOFT, fill: true, tension: 0.35, pointRadius: 4, pointBackgroundColor: RED, pointBorderColor: 'transparent', borderWidth: 2 },
      { label: 'C2838 PSU', data: init.bldc_psu, borderColor: GREEN, backgroundColor: GREEN_SOFT, fill: true, tension: 0.35, pointRadius: 4, pointBackgroundColor: GREEN, pointBorderColor: 'transparent', borderWidth: 2 },
      { label: 'goBILDA heat', data: init.gob_heat, borderColor: RED_DASH, backgroundColor: 'transparent', borderDash: [5, 4], tension: 0.35, pointRadius: 0, borderWidth: 1.5 },
      { label: 'C2838 heat', data: init.bldc_heat, borderColor: GREEN_DASH, backgroundColor: 'transparent', borderDash: [5, 4], tension: 0.35, pointRadius: 0, borderWidth: 1.5 }
    ]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: '#1e2330', titleColor: '#e8eaed', bodyColor: '#8b919e', borderColor: 'rgba(255,255,255,0.08)', borderWidth: 1, cornerRadius: 8, padding: 10,
        callbacks: { label: c => c.dataset.label + ': ' + (c.raw !== null ? c.raw.toFixed(1) + ' W' : 'N/A') }
      }
    },
    scales: {
      x: { title: { display: true, text: 'Motor shaft speed (RPM)', color: textColor, font: { size: 11 } }, ticks: { color: textColor, font: { size: 10 }, autoSkip: false, maxRotation: 0 }, grid: { display: false }, border: { color: 'rgba(255,255,255,0.06)' } },
      y: { title: { display: true, text: 'Power (W)', color: textColor, font: { size: 11 } }, ticks: { color: textColor, font: { size: 10 } }, grid: { color: gridColor }, border: { display: false }, beginAtZero: true }
    }
  }
});

document.getElementById('legend1').innerHTML =
  '<span class="legend-item"><span class="legend-dot" style="background:'+RED+';"></span>goBILDA PSU input</span>' +
  '<span class="legend-item"><span class="legend-dot" style="background:'+GREEN+';"></span>C2838 PSU input</span>' +
  '<span class="legend-item"><span class="legend-line" style="border-top:2px dashed '+RED_DASH+';"></span>goBILDA heat</span>' +
  '<span class="legend-item"><span class="legend-line" style="border-top:2px dashed '+GREEN_DASH+';"></span>C2838 heat</span>';

// Savings chart
const chart2 = new Chart(document.getElementById('savingsChart'), {
  type: 'bar',
  data: {
    labels: rpms.map(s => s.toLocaleString()),
    datasets: [{
      label: 'Power savings',
      data: init.savings_pct,
      backgroundColor: GREEN,
      borderRadius: 4, barPercentage: 0.6
    }]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: '#1e2330', titleColor: '#e8eaed', bodyColor: '#8b919e', borderColor: 'rgba(255,255,255,0.08)', borderWidth: 1, cornerRadius: 8, padding: 10,
        callbacks: { label: c => 'Saving: ' + (c.raw !== null ? c.raw + '%' : 'N/A') }
      }
    },
    scales: {
      x: { title: { display: true, text: 'Motor shaft speed (RPM)', color: textColor, font: { size: 11 } }, ticks: { color: textColor, font: { size: 10 }, autoSkip: false, maxRotation: 0 }, grid: { display: false }, border: { color: 'rgba(255,255,255,0.06)' } },
      y: { title: { display: true, text: 'Power saving (%)', color: textColor, font: { size: 11 } }, ticks: { color: textColor, font: { size: 10 }, callback: v => v + '%' }, grid: { color: gridColor }, border: { display: false }, min: 0, max: 100 }
    }
  }
});

document.getElementById('legend2').innerHTML =
  '<span class="legend-item"><span class="legend-dot" style="background:'+GREEN+';"></span>C2838 power saving vs goBILDA at same torque and speed</span>';

function updateSummary(rows) {
  const valid = rows.filter(r => r.save !== null);
  if (!valid.length) return;
  const avg = Math.round(valid.reduce((s, r) => s + r.save, 0) / valid.length);
  const peak = valid.reduce((best, r) => r.save > best.save ? r : best, valid[0]);
  const avgHeatRed = Math.round((1 - valid.reduce((s, r) => s + r.bldc_h, 0) / valid.reduce((s, r) => s + r.gob_h, 0)) * 100);
  document.getElementById('s-avg').textContent = avg + '%';
  document.getElementById('s-peak').textContent = peak.save + '%';
  document.getElementById('s-peak-rpm').textContent = 'at ' + peak.rpm.toLocaleString() + ' RPM';
  document.getElementById('s-heat').textContent = avgHeatRed + '%';
}

function renderTable(rows) {
  let html = '<table><thead><tr>';
  ['RPM','Torque','Mech. out','goBILDA in','C2838 in','goBILDA heat','C2838 heat','Saving'].forEach(h => {
    html += '<th>' + h + '</th>';
  });
  html += '</tr></thead><tbody>';
  for (const r of rows) {
    if (r.gob_pw === null) continue;
    html += '<tr>';
    html += '<td>' + r.rpm.toLocaleString() + '</td>';
    html += '<td>' + r.T_kgcm.toFixed(2) + ' kg·cm</td>';
    html += '<td>' + r.P_mech.toFixed(1) + ' W</td>';
    html += '<td class="td-red">' + r.gob_pw.toFixed(1) + ' W</td>';
    html += '<td class="td-green">' + r.bldc_pw.toFixed(1) + ' W</td>';
    html += '<td class="td-red">' + r.gob_h.toFixed(1) + ' W</td>';
    html += '<td class="td-green">' + r.bldc_h.toFixed(1) + ' W</td>';
    html += '<td class="td-saving">' + r.save + '%</td>';
    html += '</tr>';
  }
  html += '</tbody></table>';
  document.getElementById('table-container').innerHTML = html;
}

updateSummary(init.rows);
renderTable(init.rows);

document.getElementById('load-slider').addEventListener('input', function() {
  const frac = parseInt(this.value) / 100;
  document.getElementById('load-out').textContent = this.value + '%';
  const d = compute(frac);
  chart1.data.datasets[0].data = d.gob_psu;
  chart1.data.datasets[1].data = d.bldc_psu;
  chart1.data.datasets[2].data = d.gob_heat;
  chart1.data.datasets[3].data = d.bldc_heat;
  chart1.update('none');
  chart2.data.datasets[0].data = d.savings_pct;
  chart2.update('none');
  updateSummary(d.rows);
  renderTable(d.rows);
});
</script>

</body>
</html>
  </div>
