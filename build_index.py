# -*- coding: utf-8 -*-
"""
Builder for TMDT revenue calculator.
Uses straightforward string replacement for base64 icon assets,
avoiding f-string syntax collisions with CSS/JS curly braces.
"""

import os
import base64

icons = {}
for k, fname in [('icon_pin', 'icon_pin.png'), ('icon_wallet', 'icon_wallet.png'), ('icon_detail', 'icon_detail.png'), ('icon_shopee', 'logo_shopee.png')]:
    fpath = os.path.join('assets', fname)
    with open(fpath, 'rb') as img_f:
        icons[k] = f"data:image/png;base64,{base64.b64encode(img_f.read()).decode('utf-8')}"

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title id="htmlTitle">Estimated Net Revenue Calculator - E-Commerce</title>
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#0284c7">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Shopee Calc">
  <link rel="apple-touch-icon" href="assets/icon-192.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-body: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-light: #94a3b8;
      --border-color: #e2e8f0;
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --primary-soft: #e0f2fe;
      --success: #059669;
      --success-soft: #ecfdf5;
      --danger: #e11d48;
      --danger-soft: #fff1f2;
      --warning: #d97706;
      --warning-soft: #fef3c7;
      --purple: #7c3aed;
      --purple-soft: #f5f3ff;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.07);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.08), 0 4px 6px -4px rgb(0 0 0 / 0.04);
      --radius-lg: 16px;
      --radius-md: 12px;
      --radius-sm: 8px;
    }

    body.dark-mode {
      --bg-body: #090d16;
      --card-bg: #131c2e;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-light: #64748b;
      --border-color: #1e293b;
      --primary: #38bdf8;
      --primary-hover: #0284c7;
      --primary-soft: #082f49;
      --success-soft: #064e3b;
      --danger-soft: #4c0519;
      --warning-soft: #451a03;
      --purple: #c084fc;
      --purple-soft: #3b0764;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Be Vietnam Pro', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      background-color: var(--bg-body);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px 16px 40px;
      transition: background-color 0.25s ease, color 0.25s ease;
    }

    .container {
      width: 100%;
      max-width: 880px;
      margin: 0 auto;
    }

    /* TOP BAR CONTROLS */
    .top-bar {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      gap: 8px;
      margin-bottom: 12px;
    }

    .top-btn {
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 6px 13px;
      height: 34px;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-main);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
      user-select: none;
      box-sizing: border-box;
    }

    #themeBtn {
      width: 34px;
      height: 34px;
      padding: 0;
      margin: 0;
      border-radius: 50%;
      flex-shrink: 0;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0;
      line-height: 0;
      font-size: 0;
    }

    #themeIcon {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 100%;
      line-height: 0;
    }

    #themeIcon svg {
      display: block;
      width: 18px;
      height: 18px;
      margin: auto;
    }

    .top-btn:hover {
      background: var(--primary-soft);
      border-color: var(--primary);
      color: var(--primary);
    }

    body.dark-mode .top-btn {
      background: #131c2e;
      border-color: #1e293b;
      color: #f8fafc;
    }

    body.dark-mode .top-btn:hover {
      background: var(--primary-soft);
      border-color: #38bdf8;
      color: #38bdf8;
    }

    /* HEADER */
    .header {
      text-align: center;
      margin-bottom: 24px;
    }

    .header-logo {
      height: 38px;
      width: auto;
      object-fit: contain;
      margin-bottom: 14px;
      display: inline-block;
    }

    .header h1 {
      font-size: 26px;
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.5px;
      margin-bottom: 4px;
    }

    /* TAB SWITCHER */
    .tab-nav {
      display: flex;
      background: #e2e8f0;
      padding: 4px;
      border-radius: 12px;
      max-width: 440px;
      margin: 0 auto 24px;
      transition: background 0.25s ease;
    }

    body.dark-mode .tab-nav {
      background: #090d16;
      border: 1px solid #1e293b;
    }

    .tab-btn {
      flex: 1;
      padding: 8px 14px;
      border: none;
      background: transparent;
      border-radius: 8px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: background-color 0.15s ease, color 0.15s ease, box-shadow 0.15s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }

    .tab-btn.active {
      background: #ffffff;
      color: var(--primary);
      box-shadow: var(--shadow-sm);
    }

    body.dark-mode .tab-btn.active {
      background: #131c2e;
      color: #38bdf8;
    }

    /* MAIN GRID (2 FRAMES EQUAL HEIGHT) */
    .calculator-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
      margin-bottom: 20px;
      align-items: stretch;
    }

    @media (min-width: 768px) {
      .calculator-grid {
        grid-template-columns: 1fr 1fr;
      }
    }

    .card {
      background: var(--card-bg);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      padding: 24px;
      transition: box-shadow 0.2s ease, border-color 0.2s ease, background-color 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }

    .card:hover {
      box-shadow: var(--shadow-md);
      border-color: #cbd5e1;
    }

    body.dark-mode .card:hover {
      border-color: #334155;
    }

    .card-top {
      flex: 1;
      display: flex;
      flex-direction: column;
    }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
    }

    .card-title {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 16px;
      font-weight: 700;
      color: var(--text-main);
      white-space: nowrap;
    }

    .card-title .icon-box {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: #f1f5f9;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.25s ease;
    }

    body.dark-mode .card-title .icon-box {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.22);
    }

    body.dark-mode .card-title .icon-box img {
      filter: brightness(0) saturate(100%) invert(65%) sepia(80%) saturate(1600%) hue-rotate(167deg) brightness(98%) contrast(97%);
    }

    .card-title .icon-box img {
      width: 20px;
      height: 20px;
      object-fit: contain;
      display: block;
    }

    /* INPUT STYLING */
    .input-label {
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 8px;
      display: block;
    }

    .input-wrapper {
      position: relative;
      margin-bottom: 12px;
    }

    .input-field {
      width: 100%;
      padding: 15px 54px 15px 16px;
      font-size: 24px;
      font-weight: 800;
      color: var(--text-main);
      background: #f8fafc;
      border: 2px solid var(--border-color);
      border-radius: var(--radius-md);
      outline: none;
      transition: all 0.2s ease;
      letter-spacing: -0.5px;
    }

    body.dark-mode .input-field {
      background: #090d16;
      border-color: #1e293b;
      color: #f8fafc;
    }

    .input-field:focus {
      background: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 0 0 4px rgba(2, 132, 199, 0.12);
    }

    body.dark-mode .input-field:focus {
      background: #131c2e;
      border-color: #38bdf8;
      box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.15);
    }

    .currency-suffix {
      position: absolute;
      right: 18px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 18px;
      font-weight: 700;
      color: var(--text-light);
      pointer-events: none;
    }

    .clear-btn {
      position: absolute;
      right: 48px;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      color: var(--text-light);
      cursor: pointer;
      display: none;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      font-weight: bold;
      z-index: 5;
    }

    .clear-btn:hover {
      background: #e2e8f0;
      color: var(--text-main);
    }

    body.dark-mode .clear-btn:hover {
      background: #334155;
      color: #f8fafc;
    }

    /* QUICK PRESET BUTTONS */
    .quick-presets {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 16px;
    }

    .preset-chip {
      background: #f1f5f9;
      border: 1px solid #e2e8f0;
      padding: 6px 11px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }

    body.dark-mode .preset-chip {
      background: #090d16;
      border-color: #1e293b;
      color: #94a3b8;
    }

    .preset-chip:hover {
      background: var(--primary-soft);
      border-color: #bae6fd;
      color: var(--primary);
    }

    body.dark-mode .preset-chip:hover {
      background: var(--primary-soft);
      border-color: #38bdf8;
      color: #38bdf8;
    }

    /* VERTICAL FEE BADGE LIST */
    .fee-badge-vertical {
      display: flex;
      flex-direction: column;
      gap: 8px;
      background: #f8fafc;
      padding: 14px 16px;
      border-radius: var(--radius-md);
      border: 1px dashed var(--border-color);
      margin-top: auto;
      transition: background 0.25s ease;
    }

    body.dark-mode .fee-badge-vertical {
      background: #090d16;
      border-color: #1e293b;
    }

    .fee-pill-row {
      font-size: 13px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 3px 0;
    }

    .fee-pill-row:not(:last-child) {
      border-bottom: 1px dashed #e2e8f0;
      padding-bottom: 7px;
    }

    body.dark-mode .fee-pill-row:not(:last-child) {
      border-bottom-color: #1e293b;
    }

    .fee-pill-left {
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--text-muted);
      font-weight: 500;
    }

    .fee-pill-row strong {
      color: var(--text-main);
      font-weight: 700;
    }

    .dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      flex-shrink: 0;
    }
    .dot.red { background: #dc2626; }
    .dot.amber { background: #d97706; }
    .dot.purple { background: #9333ea; }
    .dot.blue { background: var(--primary); }
    .dot.orange { background: #ea580c; }
    .dot.green { background: #059669; }

    /* FRAME 2: RESULT CARD */
    .result-card {
      background: var(--card-bg);
      border: 1px solid var(--border-color);
    }

    .result-header-badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 12px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 20px;
      background: var(--success-soft);
      color: var(--success);
    }

    .result-amount-box {
      background: var(--primary-soft);
      border: 1px solid #bae6fd;
      border-radius: var(--radius-md);
      padding: 18px;
      text-align: center;
      margin-bottom: 14px;
      transition: background 0.25s ease, border-color 0.25s ease;
    }

    body.dark-mode .result-amount-box {
      background: rgba(8, 47, 73, 0.45);
      border-color: #0369a1;
    }

    .result-label {
      font-size: 12.5px;
      font-weight: 700;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }

    .result-amount {
      font-size: 32px;
      font-weight: 800;
      color: var(--primary);
      letter-spacing: -1px;
      display: flex;
      align-items: baseline;
      justify-content: center;
      gap: 4px;
    }

    .result-amount .currency {
      font-size: 20px;
      font-weight: 700;
      color: var(--primary);
    }

    .result-percent-tag {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--primary);
      margin-top: 3px;
    }

    /* PROGRESS BAR */
    .mini-bar-container {
      margin-bottom: 14px;
    }

    .mini-bar-label {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 8px;
    }

    .bar-legend {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .legend-item {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
    }

    .progress-bar-wrapper {
      position: relative;
      width: 100%;
    }

    .progress-bar {
      height: 11px;
      width: 100%;
      background: #e2e8f0;
      border-radius: 9999px;
      overflow: hidden;
      display: flex;
      cursor: pointer;
      transition: background 0.25s ease;
      -webkit-mask-image: -webkit-radial-gradient(white, black);
      transform: translateZ(0);
      isolation: isolate;
    }

    body.dark-mode .progress-bar {
      background: #1e293b;
    }

    .bar-segment {
      height: 100%;
      transition: width 0.3s ease, filter 0.15s ease;
      cursor: pointer;
    }

    .bar-segment:hover {
      filter: brightness(1.15);
    }

    .bar-net {
      background: var(--primary);
      border-top-left-radius: 9999px;
      border-bottom-left-radius: 9999px;
    }
    .bar-fee {
      background: var(--danger);
    }
    .bar-tax {
      background: var(--purple);
      border-top-right-radius: 9999px;
      border-bottom-right-radius: 9999px;
    }

    /* TOOLTIP FOR PROGRESS BAR */
    .bar-tooltip {
      position: absolute;
      bottom: calc(100% + 7px);
      left: 50%;
      transform: translateX(-50%);
      background: #0f172a;
      color: #ffffff;
      font-size: 11.5px;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 6px;
      white-space: nowrap;
      pointer-events: none;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.15s ease, transform 0.15s ease;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
      z-index: 30;
    }

    .bar-tooltip::after {
      content: "";
      position: absolute;
      top: 100%;
      left: 50%;
      transform: translateX(-50%);
      border-width: 5px;
      border-style: solid;
      border-color: #0f172a transparent transparent transparent;
    }

    .bar-tooltip.show {
      opacity: 1;
      visibility: visible;
      transform: translateX(-50%) translateY(-2px);
    }

    /* SUMMARY STATS GRID */
    .summary-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 16px;
    }

    .summary-box {
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 10px 12px;
      transition: background 0.25s ease;
    }

    body.dark-mode .summary-box {
      background: #090d16;
      border-color: #1e293b;
    }

    .summary-box-title {
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .summary-box-value {
      font-size: 14.5px;
      font-weight: 700;
      color: var(--text-main);
    }

    .summary-box-value.red { color: var(--danger); }
    .summary-box-value.blue { color: var(--primary); }
    .summary-box-value.purple { color: var(--purple); }

    /* ACTION BUTTONS */
    .action-row {
      display: flex;
      gap: 8px;
      margin-top: auto;
    }

    .btn-action {
      flex: 1;
      padding: 11px 14px;
      font-size: 13px;
      font-weight: 700;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      background: #ffffff;
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.15s ease;
    }

    .btn-action:hover {
      background: #f8fafc;
      border-color: #cbd5e1;
    }

    body.dark-mode .btn-action {
      background: #090d16;
      border-color: #1e293b;
      color: #f8fafc;
    }

    body.dark-mode .btn-action:hover {
      background: #131c2e;
      border-color: #334155;
    }

    .btn-action.primary {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }

    body.dark-mode .btn-action.primary {
      background: #0284c7;
      color: #ffffff;
      border-color: #0284c7;
    }

    .btn-action.primary:hover {
      background: var(--primary-hover);
    }

    @media (max-width: 480px) {
      .action-row {
        flex-wrap: wrap;
      }
      .btn-action {
        flex: 1 1 calc(50% - 4px);
        padding: 9px 8px;
        font-size: 12px;
      }
      .btn-action.primary {
        flex: 1 1 100%;
      }
    }

    /* FREESHIP XTRA TOGGLE */
    .xtra-toggle-card {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding: 10px 12px;
      margin-top: 12px;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      transition: all 0.2s ease;
    }

    body.dark-mode .xtra-toggle-card {
      background: #090d16;
      border-color: #1e293b;
    }

    .toggle-control {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      user-select: none;
      flex: 1;
    }

    .toggle-control input {
      display: none;
    }

    .toggle-slider {
      position: relative;
      width: 38px;
      height: 22px;
      background: #cbd5e1;
      border-radius: 9999px;
      transition: background 0.2s ease;
      flex-shrink: 0;
    }

    body.dark-mode .toggle-slider {
      background: #334155;
    }

    .toggle-slider::after {
      content: "";
      position: absolute;
      top: 3px;
      left: 3px;
      width: 16px;
      height: 16px;
      background: #ffffff;
      border-radius: 50%;
      transition: transform 0.2s ease;
      box-shadow: var(--shadow-sm);
    }

    .toggle-control input:checked + .toggle-slider {
      background: #ea580c;
    }

    .toggle-control input:checked + .toggle-slider::after {
      transform: translateX(16px);
    }

    .toggle-label {
      font-size: 13px;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.3;
    }

    .xtra-badge {
      font-size: 11.5px;
      font-weight: 700;
      color: #ea580c;
      background: #fff7ed;
      border: 1px solid #ffedd5;
      padding: 3px 8px;
      border-radius: 6px;
      white-space: nowrap;
    }

    body.dark-mode .xtra-badge {
      background: rgba(124, 45, 18, 0.25);
      border-color: #9a3412;
      color: #fb923c;
    }

    /* COST INPUT SECTION */
    .cost-input-section {
      margin-top: 14px;
      margin-bottom: 4px;
    }

    .input-wrapper-sm {
      margin-bottom: 0;
    }

    .input-wrapper-sm .input-field {
      padding: 9px 48px 9px 12px;
      font-size: 16px;
      font-weight: 700;
      border-radius: var(--radius-sm);
    }

    .input-wrapper-sm .currency-suffix {
      font-size: 15px;
      right: 14px;
    }

    .input-wrapper-sm .clear-btn {
      right: 36px;
      width: 22px;
      height: 22px;
      font-size: 11px;
    }

    /* PROFIT MARGIN BOX */
    .profit-box {
      border-radius: var(--radius-md);
      padding: 12px 14px;
      margin-bottom: 14px;
      transition: background 0.25s ease, border-color 0.25s ease;
      border: 1px solid var(--border-color);
    }

    .profit-box.positive {
      background: #f0fdf4;
      border-color: #bbf7d0;
    }

    body.dark-mode .profit-box.positive {
      background: rgba(6, 78, 59, 0.35);
      border-color: #059669;
    }

    .profit-box.negative {
      background: #fff1f2;
      border-color: #fecdd3;
    }

    body.dark-mode .profit-box.negative {
      background: rgba(76, 5, 25, 0.35);
      border-color: #e11d48;
    }

    .profit-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }

    .profit-header-title {
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.4px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .profit-badge {
      font-size: 12px;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 9999px;
    }

    .profit-badge.positive {
      background: var(--success-soft);
      color: var(--success);
    }

    body.dark-mode .profit-badge.positive {
      background: rgba(5, 150, 105, 0.25);
      color: #34d399;
    }

    .profit-badge.negative {
      background: var(--danger-soft);
      color: var(--danger);
    }

    body.dark-mode .profit-badge.negative {
      background: rgba(225, 29, 72, 0.25);
      color: #fb7185;
    }

    .profit-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }

    .profit-item {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .profit-label {
      font-size: 11.5px;
      font-weight: 600;
      color: var(--text-muted);
    }

    .profit-val {
      font-size: 15px;
      font-weight: 800;
      color: var(--text-main);
    }

    .profit-box.positive .profit-val {
      color: #047857;
    }

    body.dark-mode .profit-box.positive .profit-val {
      color: #34d399;
    }

    .profit-box.negative .profit-val {
      color: #be123c;
    }

    body.dark-mode .profit-box.negative .profit-val {
      color: #fb7185;
    }

    /* COLLAPSIBLE ACCORDION (PHAN TICH CHI TIET) */
    .detail-card {
      background: var(--card-bg);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      margin-bottom: 20px;
      transition: border-color 0.2s ease, background 0.25s ease;
    }

    .detail-trigger {
      width: 100%;
      padding: 16px 22px;
      background: transparent;
      border: none;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      font-size: 15px;
      font-weight: 700;
      color: var(--text-main);
      transition: background-color 0.15s ease;
    }

    .detail-trigger:hover {
      background: #f8fafc;
    }

    body.dark-mode .detail-trigger:hover {
      background: #090d16;
    }

    .detail-trigger-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .detail-icon-box {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: #f1f5f9;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.25s ease;
    }

    body.dark-mode .detail-icon-box {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.22);
    }

    body.dark-mode .detail-icon-box img {
      filter: brightness(0) saturate(100%) invert(65%) sepia(80%) saturate(1600%) hue-rotate(167deg) brightness(98%) contrast(97%);
    }

    .detail-icon-box img {
      width: 20px;
      height: 20px;
      object-fit: contain;
      display: block;
    }

    .chevron-icon {
      width: 20px;
      height: 20px;
      color: var(--text-muted);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .detail-card.open .chevron-icon {
      transform: rotate(180deg);
    }

    .detail-content {
      display: none;
      padding: 0 24px 24px 24px;
      border-top: 1px solid var(--border-color);
      background: #ffffff;
      transition: background 0.25s ease;
    }

    body.dark-mode .detail-content {
      background: #131c2e;
    }

    .detail-card.open .detail-content {
      display: block;
      animation: fadeIn 0.25s ease-out;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* DETAIL SECTION TABLES */
    .step-section {
      margin-top: 18px;
    }

    .step-title {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .step-num {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--primary);
      color: #fff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 800;
    }

    .step-num.green { background: var(--success); }
    .step-num.purple { background: var(--purple); }

    .breakdown-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 12px;
      font-size: 13.5px;
    }

    .breakdown-table tr {
      border-bottom: 1px solid #f1f5f9;
    }

    body.dark-mode .breakdown-table tr {
      border-bottom-color: #1e293b;
    }

    .breakdown-table tr:last-child {
      border-bottom: none;
    }

    .breakdown-table td {
      padding: 9px 4px;
    }

    .breakdown-table .item-name {
      color: var(--text-main);
      font-weight: 500;
    }

    .breakdown-table .item-formula {
      color: var(--text-muted);
      font-size: 12px;
      display: block;
      margin-top: 2px;
    }

    .breakdown-table .item-val {
      text-align: right;
      font-weight: 700;
      color: var(--text-main);
    }

    .breakdown-table .item-val.deduct {
      color: var(--danger);
    }

    .breakdown-table .item-val.tax {
      color: var(--purple);
    }

    .subtotal-row {
      background: #f8fafc;
      font-weight: 700;
    }

    body.dark-mode .subtotal-row {
      background: #090d16 !important;
    }

    .subtotal-row td {
      padding: 10px 8px !important;
      border-radius: 6px;
    }

    .formula-banner {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 12px 14px;
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.6;
      margin-top: 14px;
      transition: background 0.25s ease;
    }

    body.dark-mode .formula-banner {
      background: #090d16;
      border-color: #1e293b;
    }

    .formula-banner code {
      background: #e2e8f0;
      padding: 2px 6px;
      border-radius: 4px;
      color: var(--primary);
      font-weight: 700;
      font-size: 12px;
    }

    body.dark-mode .formula-banner code {
      background: #1e293b;
      color: #38bdf8;
    }

    @keyframes tabFadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    /* REVERSE CALCULATOR (TAB 2) */
    .forward-calc-box {
      display: block;
      animation: tabFadeIn 0.15s ease-out;
    }

    .forward-calc-box.hidden {
      display: none !important;
    }

    .reverse-calc-box {
      display: none;
    }

    .reverse-calc-box.active {
      display: block !important;
      animation: tabFadeIn 0.15s ease-out;
    }

    .profit-subtotal-row.positive {
      background: var(--success-soft) !important;
    }
    .profit-subtotal-row.positive .item-name,
    .profit-subtotal-row.positive .item-val {
      color: var(--success) !important;
    }
    .profit-subtotal-row.negative {
      background: var(--danger-soft) !important;
    }
    .profit-subtotal-row.negative .item-name,
    .profit-subtotal-row.negative .item-val {
      color: var(--danger) !important;
    }

    body.dark-mode .profit-subtotal-row.positive {
      background: rgba(6, 78, 59, 0.35) !important;
    }
    body.dark-mode .profit-subtotal-row.positive .item-name,
    body.dark-mode .profit-subtotal-row.positive .item-val {
      color: #34d399 !important;
    }
    body.dark-mode .profit-subtotal-row.negative {
      background: rgba(76, 5, 25, 0.35) !important;
    }
    body.dark-mode .profit-subtotal-row.negative .item-name,
    body.dark-mode .profit-subtotal-row.negative .item-val {
      color: #fb7185 !important;
    }

    #reverseDesc {
      text-align: justify;
    }

    /* FOOTER */
    .app-footer {
      text-align: center;
      font-size: 12px;
      color: var(--text-light);
      margin-top: auto;
      padding: 24px 0 8px;
      line-height: 1.6;
    }

    /* TOAST */
    .toast {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #0f172a;
      color: #ffffff;
      padding: 10px 20px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: var(--shadow-lg);
      opacity: 0;
      pointer-events: none;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .toast.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }

    
    /* KHUNG GIAO DIỆN CHỌN THỊ TRƯỜNG */
    .market-frame {
      max-width: 660px;
      margin: 10px auto 30px;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-md);
      padding: 36px 30px;
      text-align: center;
      transition: background-color 0.25s ease, border-color 0.25s ease;
      animation: fadeIn 0.25s ease-out;
    }

    .market-frame-header {
      margin-bottom: 26px;
    }

    .market-frame-header h1 {
      font-size: 24px;
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.5px;
      margin-bottom: 6px;
    }

    .market-frame-header p {
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.5;
    }

    .market-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }

    @media (max-width: 520px) {
      .market-grid {
        grid-template-columns: 1fr;
      }
    }

    .market-card-btn {
      background: #f8fafc;
      border: 2px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 18px 16px;
      text-align: left;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 6px;
      transition: all 0.2s ease;
      user-select: none;
    }

    body.dark-mode .market-card-btn {
      background: #090d16;
      border-color: #1e293b;
    }

    .market-card-btn:hover {
      border-color: var(--primary);
      background: var(--primary-soft);
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
    }

    .market-card-btn.active {
      border-color: var(--primary);
      background: var(--primary-soft);
      box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.2);
    }

    body.dark-mode .market-card-btn.active {
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.25);
    }

    .market-card-top-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .market-card-country {
      font-size: 16px;
      font-weight: 700;
      color: var(--text-main);
    }

    .market-card-badge {
      font-size: 11.5px;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 6px;
      background: #e2e8f0;
      color: var(--text-muted);
      letter-spacing: 0.5px;
    }

    body.dark-mode .market-card-badge {
      background: #1e293b;
      color: #94a3b8;
    }

    .market-card-btn.active .market-card-badge {
      background: var(--primary);
      color: #ffffff;
    }

    .market-card-currency {
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 500;
    }

    .market-card-action {
      font-size: 12.5px;
      font-weight: 700;
      color: var(--primary);
      margin-top: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    /* WARNING ALERT */
    .alert-box {
      background: var(--warning-soft);
      border: 1px solid #fde68a;
      color: #92400e;
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      display: none;
      margin-bottom: 12px;
    }

    body.dark-mode .alert-box {
      border-color: #78350f;
      color: #fde68a;
    }

    .alert-box.show {
      display: block;
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- TOP BAR (THEME, LANG TOGGLE & MARKET SWITCHER) -->
    <div class="top-bar">
      <button class="top-btn" id="marketSwitchBtn" onclick="openMarketScreen()" style="display: none;" title="Đổi thị trường / Change marketplace" aria-label="Đổi thị trường">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
          <path d="M3 10.5L12 3l9 7.5V20a1.5 1.5 0 0 1-1.5 1.5H4.5A1.5 1.5 0 0 1 3 20V10.5z"/>
          <path d="M8.75 21.5v-7a1 1 0 0 1 1-1h4.5a1 1 0 0 1 1 1v7"/>
        </svg>
        <span id="marketDisplayCode" style="display: none;">Shopee VN</span>
      </button>
      <button class="top-btn" id="langBtn" onclick="toggleLang()" style="display: none;" title="Chuyển đổi ngôn ngữ / Switch language">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" style="opacity: 0.85;">
          <circle cx="12" cy="12" r="10"/>
          <line x1="2" y1="12" x2="22" y2="12"/>
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
        </svg>
        <span id="langLabel">VI</span>
      </button>
      <button class="top-btn" id="themeBtn" onclick="toggleTheme()" title="Chế độ sáng/tối / Light/Dark mode"><span id="themeIcon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4.2"/><line x1="12" y1="2" x2="12" y2="4.8"/><line x1="12" y1="19.2" x2="12" y2="22"/><line x1="4.93" y1="4.93" x2="6.91" y2="6.91"/><line x1="17.09" y1="17.09" x2="19.07" y2="19.07"/><line x1="2" y1="12" x2="4.8" y2="12"/><line x1="19.2" y1="12" x2="22" y2="12"/><line x1="4.93" y1="19.07" x2="6.91" y2="17.09"/><line x1="17.09" y1="6.91" x2="19.07" y2="4.93"/></svg></span></button>
    </div>

    <!-- KHUNG GIAO DIỆN CHỌN THỊ TRƯỜNG (MARKET SELECTION SCREEN) -->
    <div id="marketScreen" class="market-frame">
      <div class="market-frame-header">
        <img src="__icon_shopee__" alt="Shopee" class="header-logo">
        <h1 data-i18n="marketTitle">Select Shopee Marketplace</h1>
        <p data-i18n="marketSubtitle">Please select your sales country to start calculating</p>
      </div>

      <div class="market-grid">
        <div class="market-card-btn" id="mkt-vn" onclick="selectMarket('vn')">
          <div class="market-card-top-row">
            <span class="market-card-country" data-i18n="marketVN">Vietnam</span>
            <span class="market-card-badge">VN</span>
          </div>
          <div class="market-card-currency" data-i18n="marketCurrencyVND">Currency: ₫ (VND)</div>
          <div class="market-card-action">
            <span data-i18n="marketEnterBtn">Enter Calculator</span> →
          </div>
        </div>

        <div class="market-card-btn" id="mkt-th" onclick="selectMarket('th')">
          <div class="market-card-top-row">
            <span class="market-card-country" data-i18n="marketTH">Thailand</span>
            <span class="market-card-badge">TH</span>
          </div>
          <div class="market-card-currency" data-i18n="marketCurrencyTHB">Currency: ฿ (THB)</div>
          <div class="market-card-action">
            <span data-i18n="marketEnterBtn">Enter Calculator</span> →
          </div>
        </div>

        <div class="market-card-btn" id="mkt-my" onclick="selectMarket('my')">
          <div class="market-card-top-row">
            <span class="market-card-country" data-i18n="marketMY">Malaysia</span>
            <span class="market-card-badge">MY</span>
          </div>
          <div class="market-card-currency" data-i18n="marketCurrencyMYR">Currency: RM (MYR)</div>
          <div class="market-card-action">
            <span data-i18n="marketEnterBtn">Enter Calculator</span> →
          </div>
        </div>

        <div class="market-card-btn" id="mkt-ph" onclick="selectMarket('ph')">
          <div class="market-card-top-row">
            <span class="market-card-country" data-i18n="marketPH">Philippines</span>
            <span class="market-card-badge">PH</span>
          </div>
          <div class="market-card-currency" data-i18n="marketCurrencyPHP">Currency: ₱ (PHP)</div>
          <div class="market-card-action">
            <span data-i18n="marketEnterBtn">Enter Calculator</span> →
          </div>
        </div>
      </div>
    </div>

    <!-- GIAO DIỆN TÍNH TOÁN CHÍNH (CALCULATOR APP) -->
    <div id="calculatorApp" style="display: none;">
      <!-- HEADER -->
    <header class="header">
      <img src="__icon_shopee__" alt="Shopee" class="header-logo">
      <h1 data-i18n="headerTitle">Estimated Net Revenue Calculator</h1>
    </header>

    <!-- TAB SWITCHER -->
    <div class="tab-nav">
      <button class="tab-btn active" id="tabForwardBtn" onclick="switchMode('forward')">
        <span data-i18n="tabForward">Calculate Net Revenue</span>
      </button>
      <button class="tab-btn" id="tabReverseBtn" onclick="switchMode('reverse')">
        <span data-i18n="tabReverse">Calculate Target Price</span>
      </button>
    </div>

    <!-- TAB 1: TÍNH XUÔI (NHẬP GIÁ BÁN -> DOANH THU THỰC NHẬN) -->
    <div id="forwardMode" class="forward-calc-box">
      <div class="calculator-grid">
        <!-- KHUNG 1: NHẬP GIÁ BÁN BAN ĐẦU -->
        <div class="card">
          <div class="card-top">
            <div class="card-header">
              <div class="card-title">
                <span class="icon-box">
                  <img src="__icon_pin__" alt="Pin">
                </span>
                <span data-i18n="card1Title">Initial Selling Price</span>
              </div>
              <span data-i18n="card1Badge" style="font-size: 11px; font-weight: 600; color: var(--text-light); text-transform: uppercase;">List price</span>
            </div>

            <label class="input-label" for="priceInput" data-i18n="card1Label">Enter product list price on platform:</label>
            <div class="input-wrapper">
              <input 
                type="text" 
                inputmode="decimal" 
                id="priceInput" 
                class="input-field" 
                placeholder="0"
                autocomplete="off"
              >
              <button class="clear-btn" id="clearBtn" title="Clear">✕</button>
              <span class="currency-suffix currency-symbol">₫</span>
            </div>

            <!-- Quick presets -->
            <div class="quick-presets" id="forwardPresets">
              <button class="preset-chip" onclick="setPreset(50000)">50k</button>
              <button class="preset-chip" onclick="setPreset(100000)">100k</button>
              <button class="preset-chip" onclick="setPreset(200000)">200k</button>
              <button class="preset-chip" onclick="setPreset(350000)">350k</button>
              <button class="preset-chip" onclick="setPreset(500000)">500k</button>
              <button class="preset-chip" onclick="setPreset(1000000)">1M</button>
            </div>

            <!-- Alert if price too low -->
            <div id="lowPriceAlert" class="alert-box">
              ⚠️ Price too low!
            </div>

            <!-- Ô nhập giá vốn sản phẩm (COGS) tùy chọn -->
            <div class="cost-input-section">
              <label class="input-label" for="costInput" data-i18n="costLabel">Cost of Goods Sold (COGS / Optional):</label>
              <div class="input-wrapper input-wrapper-sm">
                <input 
                  type="text" 
                  inputmode="decimal" 
                  id="costInput" 
                  class="input-field" 
                  placeholder="0"
                  autocomplete="off"
                >
                <button class="clear-btn" id="clearCostBtn" title="Clear">✕</button>
                <span class="currency-suffix currency-symbol">₫</span>
              </div>
            </div>

            <!-- Tùy chọn gói Freeship Xtra / Voucher Xtra -->
            <div class="xtra-toggle-card">
              <label class="toggle-control" for="xtraCheckbox">
                <input type="checkbox" id="xtraCheckbox" onchange="onToggleXtra(this.checked)">
                <span class="toggle-slider"></span>
                <span class="toggle-label" data-i18n="xtraLabel">Freeship Xtra / Voucher Xtra Package</span>
              </label>
              <span class="xtra-badge" id="xtraRateBadge">+6% (max 30k)</span>
            </div>
          </div>

          <!-- VERTICAL FEE BADGES -->
          <div class="fee-badge-vertical">
            <div class="fee-pill-row">
              <span class="fee-pill-left"><span class="dot red"></span> <span data-i18n="fixedFeeLabel">Fixed fee:</span></span>
              <strong id="badgeFixedFee">16%</strong>
            </div>
            <div class="fee-pill-row">
              <span class="fee-pill-left"><span class="dot amber"></span> <span data-i18n="serviceFeeLabel">Service fee:</span></span>
              <strong id="badgeServiceFee">3.000₫</strong>
            </div>
            <div class="fee-pill-row" id="badgeExtraRow" style="display: none;">
              <span class="fee-pill-left"><span class="dot orange"></span> <span data-i18n="extraFeeLabel">Xtra Service Fee:</span></span>
              <strong id="badgeExtraFee">+6% (max 30k)</strong>
            </div>
            <div class="fee-pill-row">
              <span class="fee-pill-left"><span class="dot red"></span> <span data-i18n="txFeeLabel">Transaction fee:</span></span>
              <strong id="badgeTxFee">6%</strong>
            </div>
            <div class="fee-pill-row">
              <span class="fee-pill-left"><span class="dot purple"></span> <span id="badgeTaxLabel" data-i18n="taxFeeLabel">Tax (VAT+PIT):</span></span>
              <strong id="badgeTaxFee">1,5%</strong>
            </div>
          </div>
        </div>

        <!-- KHUNG 2: DOANH THU SAU CHIẾT KHẤU -->
        <div class="card result-card">
          <div class="card-top">
            <div class="card-header">
              <div class="card-title">
                <span class="icon-box">
                  <img src="__icon_wallet__" alt="Wallet">
                </span>
                <span data-i18n="card2Title">Net Revenue After Deductions</span>
              </div>
            </div>

            <!-- Ô hiển thị số tiền thực nhận nổi bật -->
            <div class="result-amount-box">
              <div class="result-label" data-i18n="payoutLabel">Estimated payout to account</div>
              <div class="result-amount">
                <span id="netRevenue">0</span>
                <span class="currency currency-symbol">₫</span>
              </div>
              <div class="result-percent-tag" id="percentSubtitle">No data yet</div>
            </div>

            <!-- Thanh tỷ lệ trực quan (Progress Bar) -->
            <div class="mini-bar-container">
              <div class="mini-bar-label">
                <span data-i18n="ratioLabel">Cash flow breakdown:</span>
                <div class="bar-legend">
                  <span class="legend-item"><span class="dot blue"></span> <span data-i18n="legendNet">Net</span></span>
                  <span class="legend-item"><span class="dot red"></span> <span data-i18n="legendFee">Fee</span></span>
                  <span class="legend-item"><span class="dot purple"></span> <span data-i18n="legendTax">Tax</span></span>
                </div>
              </div>
              <div class="progress-bar-wrapper">
                <div class="bar-tooltip" id="barTooltip">0%</div>
                <div class="progress-bar" id="progressBar">
                  <div class="bar-segment bar-net" id="barNet" style="width: 0%"></div>
                  <div class="bar-segment bar-fee" id="barFee" style="width: 0%"></div>
                  <div class="bar-segment bar-tax" id="barTax" style="width: 0%"></div>
                </div>
              </div>
            </div>

            <!-- 2 ô tóm tắt: Tổng Phí và Tổng Thuế -->
            <div class="summary-grid">
              <div class="summary-box">
                <div class="summary-box-title">
                  <span class="dot blue"></span> <span data-i18n="summaryTotalFee">Total Platform Fees</span>
                </div>
                <div class="summary-box-value blue" id="summaryTotalFee">0 ₫</div>
              </div>
              <div class="summary-box">
                <div class="summary-box-title">
                  <span class="dot purple"></span> <span data-i18n="summaryTotalTax">Total Tax Payable</span>
                </div>
                <div class="summary-box-value blue" id="summaryTotalTax">0 ₫</div>
              </div>
            </div>

            <!-- Hộp tính Tỷ Suất Lợi Nhuận & Lãi Ròng (Chỉ hiện khi nhập Giá vốn > 0) -->
            <div class="profit-box" id="profitBox" style="display: none;">
              <div class="profit-header">
                <span class="profit-header-title">
                  <span class="dot green"></span>
                  <span data-i18n="profitBoxTitle">Business Profitability (Margin)</span>
                </span>
                <span class="profit-badge" id="profitMarginBadge">+0.0%</span>
              </div>
              <div class="profit-grid">
                <div class="profit-item">
                  <span class="profit-label" data-i18n="netProfitLabel">Net Profit:</span>
                  <strong class="profit-val" id="netProfitVal">0 ₫</strong>
                </div>
                <div class="profit-item">
                  <span class="profit-label" data-i18n="marginLabel">Profit Margin:</span>
                  <strong class="profit-val" id="profitMarginVal">0.0%</strong>
                </div>
              </div>
            </div>
          </div>

          <!-- Nút bấm thao tác -->
          <div class="action-row">
            <button class="btn-action primary" onclick="copyResult()">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>
              <span data-i18n="btnCopy">Copy Result</span>
            </button>
            <button class="btn-action" id="exportPngBtn" onclick="exportSummaryPng()">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              <span data-i18n="btnExportPng">Export PNG</span>
            </button>
            <button class="btn-action" onclick="resetAll()">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
              <span data-i18n="btnReset">Reset</span>
            </button>
          </div>
        </div>
      </div>

      <!-- PHẦN PHÂN TÍCH CHI TIẾT (ACCORDION) -->
      <div class="detail-card" id="detailCard">
        <button class="detail-trigger" onclick="toggleDetail()">
          <div class="detail-trigger-left">
            <span class="detail-icon-box">
              <img src="__icon_detail__" alt="Phân tích chi tiết">
            </span>
            <span data-i18n="detailTrigger">Phân tích chi tiết</span>
          </div>
          <svg class="chevron-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </button>

        <div class="detail-content">
          <!-- BƯỚC 1: PHỤ PHÍ SÀN -->
          <div class="step-section">
            <div class="step-title">
              <span class="step-num">1</span>
              <span data-i18n="step1Title">Các khoản phụ phí sàn trừ vào giá ban đầu</span>
            </div>
            <table class="breakdown-table">
              <tr>
                <td>
                  <span class="item-name" data-i18n="step1Fixed">Phí cố định</span>
                  <span class="item-formula" id="step1FixedFormula">16% × Giá bán ban đầu</span>
                </td>
                <td class="item-val deduct" id="detailFixedFee">0 ₫</td>
              </tr>
              <tr>
                <td>
                  <span class="item-name" id="step1ServiceName">Phí dịch vụ cố định</span>
                  <span class="item-formula" id="step1ServiceFormula">Khoản thu cố định mỗi đơn</span>
                </td>
                <td class="item-val deduct" id="detailServiceFee">0 ₫</td>
              </tr>
              <tr>
                <td>
                  <span class="item-name" data-i18n="step1Tx">Phí xử lý giao dịch</span>
                  <span class="item-formula" id="step1TxFormula">6% × Giá bán ban đầu</span>
                </td>
                <td class="item-val deduct" id="detailTxFee">0 ₫</td>
              </tr>
              <tr id="detailExtraRow" style="display: none;">
                <td>
                  <span class="item-name" id="step1ExtraName" data-i18n="step1Extra">Gói dịch vụ bổ sung (Freeship/Voucher Xtra)</span>
                  <span class="item-formula" id="step1ExtraFormula">+6% (max 30k)</span>
                </td>
                <td class="item-val deduct" id="detailExtraFee">0 ₫</td>
              </tr>
              <tr class="subtotal-row">
                <td data-i18n="step1Total">Tổng phụ phí sàn (A)</td>
                <td class="item-val deduct" id="detailTotalFee">0 ₫</td>
              </tr>
            </table>
          </div>

          <!-- BƯỚC 2: DOANH THU TRƯỚC THUẾ (CƠ SỞ TÍNH THUẾ) -->
          <div class="step-section">
            <div class="step-title">
              <span class="step-num">2</span>
              <span data-i18n="step2Title">Doanh thu trước thuế (Cơ sở để tính thuế)</span>
            </div>
            <table class="breakdown-table">
              <tr class="subtotal-row" style="background: #f0f9ff;">
                <td>
                  <span class="item-name" data-i18n="step2BeforeTax">Doanh thu trước thuế (B = Giá bán - A)</span>
                  <span class="item-formula" data-i18n="step2Formula">Khoản tiền còn lại sau khi sàn đã trừ toàn bộ phụ phí</span>
                </td>
                <td class="item-val" style="color: var(--primary);" id="detailBeforeTax">0 ₫</td>
              </tr>
            </table>
          </div>

          <!-- BƯỚC 3: THUẾ -->
          <div class="step-section">
            <div class="step-title">
              <span class="step-num purple">3</span>
              <span data-i18n="step3Title">Thuế phải nộp (Áp dụng sau khi trừ xong các phụ phí)</span>
            </div>
            <table class="breakdown-table">
              <tr id="step3Tax1Row">
                <td>
                  <span class="item-name" id="step3Tax1Name">Thuế Giá Trị Gia Tăng (GTGT)</span>
                  <span class="item-formula" id="step3Tax1Formula">1,0% × Doanh thu trước thuế (B)</span>
                </td>
                <td class="item-val tax" id="detailTax1">0 ₫</td>
              </tr>
              <tr id="step3Tax2Row">
                <td>
                  <span class="item-name" id="step3Tax2Name">Thuế Thu Nhập Cá Nhân (TNCN / TTCN)</span>
                  <span class="item-formula" id="step3Tax2Formula">0,5% × Doanh thu trước thuế (B)</span>
                </td>
                <td class="item-val tax" id="detailTax2">0 ₫</td>
              </tr>
              <tr class="subtotal-row" style="background: var(--purple-soft);">
                <td id="step3TotalLabel">Tổng thuế phải nộp (C = GTGT + TNCN)</td>
                <td class="item-val tax" id="detailTotalTax">0 ₫</td>
              </tr>
            </table>
          </div>

          <!-- BƯỚC 4: TỔNG KẾT THỰC NHẬN -->
          <div class="step-section">
            <div class="step-title">
              <span class="step-num green">4</span>
              <span data-i18n="step4Title">Doanh thu thực nhận cuối cùng về ví</span>
            </div>
            <table class="breakdown-table">
              <tr class="subtotal-row" style="background: #ecfdf5; font-size: 15px;">
                <td>
                  <span class="item-name" data-i18n="step4Net" style="color: #166534; font-weight: 800;">TIỀN THỰC VỀ TÀI KHOẢN (B - C)</span>
                </td>
                <td class="item-val" style="color: #15803d; font-size: 18px; font-weight: 800;" id="detailNet">0 ₫</td>
              </tr>
            </table>
          </div>

          <!-- BƯỚC 5: HIỆU QUẢ KINH DOANH (KHI NHẬP GIÁ VỐN) -->
          <div class="step-section" id="step5CostSection" style="display: none;">
            <div class="step-title">
              <span class="step-num green">5</span>
              <span data-i18n="step5Title">Hiệu quả kinh doanh & Tỷ suất lợi nhuận</span>
            </div>
            <table class="breakdown-table">
              <tr>
                <td>
                  <span class="item-name" data-i18n="step5CostName">Giá vốn hàng bán (COGS)</span>
                  <span class="item-formula" data-i18n="step5CostFormula">Chi phí nhập / sản xuất sản phẩm ban đầu</span>
                </td>
                <td class="item-val deduct" id="detailCostVal">-0 ₫</td>
              </tr>
              <tr class="subtotal-row profit-subtotal-row positive" id="detailProfitRow" style="font-size: 15px;">
                <td>
                  <span class="item-name" id="step5ProfitLabel" data-i18n="step5ProfitName" style="font-weight: 800;">LỢI NHUẬN RÒNG CUỐI CÙNG (LÃI)</span>
                  <span class="item-formula" id="detailMarginFormula">Tỷ suất lợi nhuận: 0.0%</span>
                </td>
                <td class="item-val" style="font-size: 18px; font-weight: 800;" id="detailProfitVal">0 ₫</td>
              </tr>
            </table>
          </div>

          <!-- CÔNG THỨC TOÁN HỌC TÓM TẮT -->
          <div class="formula-banner">
            💡 <strong data-i18n="formulaTitle">Công thức tính rút gọn:</strong><br>
            • <code><span id="formulaBeforeTax">Doanh thu trước thuế = Giá bán × 78% - 3.000₫</span></code><br>
            • <code><span id="formulaNet">Doanh thu thực nhận = Doanh thu trước thuế × 98,5% (sau khi khấu trừ 1,5% thuế).</span></code>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 2: TÍNH NGƯỢC (TÍNH GIÁ CẦN BÁN KHI MUỐN NHẬN VỀ X ĐỒNG) -->
    <div id="reverseMode" class="reverse-calc-box">
      <div class="calculator-grid">
        <div class="card">
          <div class="card-top">
            <div class="card-header">
              <div class="card-title">
                <span class="icon-box">
                  <img src="__icon_wallet__" alt="Wallet">
                </span>
                <span data-i18n="reverseCard1Title">Target Net Payout</span>
              </div>
              <span data-i18n="reverseCard1Badge" style="font-size: 11px; font-weight: 600; color: var(--text-light); text-transform: uppercase;">Wallet target</span>
            </div>

            <label class="input-label" for="targetNetInput" data-i18n="reverseCard1Label">Enter desired net payout to account:</label>
            <div class="input-wrapper">
              <input 
                type="text" 
                inputmode="decimal" 
                id="targetNetInput" 
                class="input-field" 
                placeholder="0"
                autocomplete="off"
              >
              <button class="clear-btn" id="clearReverseBtn" title="Clear">✕</button>
              <span class="currency-suffix currency-symbol">₫</span>
            </div>

            <div class="quick-presets" id="reversePresets">
              <button class="preset-chip" onclick="setReversePreset(50000)">50k</button>
              <button class="preset-chip" onclick="setReversePreset(100000)">100k</button>
              <button class="preset-chip" onclick="setReversePreset(200000)">200k</button>
              <button class="preset-chip" onclick="setReversePreset(500000)">500k</button>
              <button class="preset-chip" onclick="setReversePreset(1000000)">1M</button>
            </div>

            <!-- Tùy chọn gói Freeship Xtra trong tính ngược -->
            <div class="xtra-toggle-card">
              <label class="toggle-control" for="xtraReverseCheckbox">
                <input type="checkbox" id="xtraReverseCheckbox" onchange="onToggleXtra(this.checked)">
                <span class="toggle-slider"></span>
                <span class="toggle-label" data-i18n="xtraLabel">Freeship Xtra / Voucher Xtra Package</span>
              </label>
              <span class="xtra-badge" id="xtraReverseRateBadge">+6% (max 30k)</span>
            </div>
          </div>

          <p id="reverseDesc" style="font-size: 12.5px; color: var(--text-muted); line-height: 1.5; margin-top: auto; text-align: justify;">
            💡 Calculates the exact listing price needed so that after platform fees, fixed fee, and tax, you pocket your exact target amount.
          </p>
        </div>

        <div class="card result-card">
          <div class="card-top">
            <div class="card-header">
              <div class="card-title">
                <span class="icon-box">
                  <img src="__icon_pin__" alt="Pin">
                </span>
                <span data-i18n="reverseCard2Title">Required Listing Price</span>
              </div>
              <span class="result-header-badge" data-i18n="reverseCard2Badge">Suggested price</span>
            </div>

            <div class="result-amount-box">
              <div class="result-label" data-i18n="reverseCard2Label">Required listing price on platform</div>
              <div class="result-amount">
                <span id="requiredPrice">0</span>
                <span class="currency currency-symbol">₫</span>
              </div>
              <div class="result-percent-tag" id="reverseSubtitle">Enter target amount to calculate</div>
            </div>
          </div>

          <div class="formula-banner" style="margin-top: auto;">
            📌 <strong data-i18n="reverseFormulaTitle">Exact reverse formula:</strong><br>
            <code><span id="reverseFormulaBody">Listing price = [(Target net ÷ 0.985) + 3,000₫] ÷ 0.78</span></code>
          </div>
        </div>
      </div>
    </div>

    </div> <!-- END #calculatorApp -->

    <!-- FOOTER (Always visible across all screens) -->
    <footer class="app-footer" data-i18n="footerText">
      Copyright © 2026 Shopee Estimator. All rights reserved.
    </footer>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div class="toast" id="toastBox">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
    <span id="toastMsg">Đã sao chép vào bộ nhớ tạm!</span>
  </div>

  <script>
    // DICTIONARY I18N
    const I18N = {
      vi: {
        pageTitle: "Tính Doanh Thu Dự Kiến Sau Chiết Khấu - Sàn TMĐT",
        headerTitle: "Tính Doanh Thu Dự Kiến Sau Chiết Khấu",
        marketTitle: "Chọn Thị Trường Shopee",
        marketSubtitle: "Vui lòng chọn quốc gia bạn đang kinh doanh để bắt đầu tính toán",
        marketVN: "Việt Nam",
        marketTH: "Thái Lan",
        marketMY: "Malaysia",
        marketPH: "Philipin",
        marketCurrencyVND: "Đơn vị: ₫ (VND)",
        marketCurrencyTHB: "Đơn vị: ฿ (THB)",
        marketCurrencyMYR: "Đơn vị: RM (MYR)",
        marketCurrencyPHP: "Đơn vị: ₱ (PHP)",
        marketEnterBtn: "Vào bảng tính",
        btnChangeMarket: "⇄ Đổi thị trường",
        tabForward: "Tính Doanh Thu Thực Nhận",
        tabReverse: "Tính Giá Bán Cần Đặt",
        card1Title: "Giá Bán Ban Đầu",
        card1Badge: "Giá niêm yết",
        card1Label: "Nhập giá sản phẩm niêm yết trên sàn:",
        fixedFeeLabel: "Phí cố định:",
        serviceFeeLabel: "Phí dịch vụ:",
        txFeeLabel: "Phí giao dịch:",
        taxFeeLabel: "Thuế:",
        card2Title: "Doanh Thu Sau Khấu Trừ",
        payoutLabel: "Doanh thu dự kiến về tài khoản",
        noDataText: "Chưa có dữ liệu tính",
        ratioLabel: "Tỷ lệ phân bổ dòng tiền:",
        legendNet: "Nhận",
        legendFee: "Phí",
        legendTax: "Thuế",
        summaryTotalFee: "Tổng phụ phí sàn",
        summaryTotalTax: "Tổng thuế phải nộp",
        btnCopy: "Sao Chép Kết Quả",
        btnReset: "Làm Mới",
        detailTrigger: "Phân tích chi tiết",
        step1Title: "Các khoản phụ phí sàn trừ vào giá ban đầu",
        step1Fixed: "Phí cố định",
        step1Tx: "Phí xử lý giao dịch",
        step1Total: "Tổng phụ phí sàn (A)",
        step2Title: "Doanh thu trước thuế (Cơ sở để tính thuế)",
        step2BeforeTax: "Doanh thu trước thuế (B = Giá bán - A)",
        step2Formula: "Khoản tiền còn lại sau khi sàn đã trừ toàn bộ phụ phí",
        step3Title: "Thuế phải nộp (Áp dụng sau khi trừ xong các phụ phí)",
        step4Title: "Doanh thu thực nhận cuối cùng về ví",
        step4Net: "TIỀN THỰC VỀ TÀI KHOẢN (B - C)",
        formulaTitle: "Công thức tính rút gọn:",
        reverseCard1Title: "Số Tiền Muốn Nhận Về",
        reverseCard1Badge: "Mục tiêu ví",
        reverseCard1Label: "Nhập số tiền thực tế bạn muốn nhận về tài khoản:",
        reverseCard2Title: "Giá Cần Niêm Yết Trên Sàn",
        reverseCard2Badge: "Giá đề xuất",
        reverseCard2Label: "Giá bán bạn cần đăng lên sàn",
        reversePrompt: "Nhập số tiền mong muốn để tính",
        reverseFormulaTitle: "Công thức tính ngược chuẩn:",
        footerText: "Copyright © 2026 Shopee Estimator. All rights reserved.",
        toastReset: "Đã làm mới dữ liệu!",
        toastCopied: "Đã sao chép chi tiết kết quả!",
        toastNoPrice: "Vui lòng nhập giá sản phẩm trước!",
        deductPrefix: "Khấu trừ",
        lossFee: "Giá bán không đủ bù phụ phí!",
        reverseSubtitlePrefix: "Sau khi trừ",
        reverseSubtitleSuffix: "phí & thuế sẽ còn đúng",
        copyHeader: "TÍNH TOÁN DOANH THU SÀN TMĐT",
        copyPrice: "• Giá bán ban đầu:",
        copyNet: "THỰC NHẬN VỀ VÍ:",
        costLabel: "Giá vốn sản phẩm (COGS / Tùy chọn):",
        xtraLabel: "Gói Freeship Xtra / Voucher Xtra",
        extraFeeLabel: "Gói dịch vụ Xtra:",
        profitBoxTitle: "Hiệu quả kinh doanh (Lợi nhuận)",
        netProfitLabel: "Lợi nhuận ròng (Lãi):",
        marginLabel: "Tỷ suất lợi nhuận (Margin):",
        btnExportPng: "Tải ảnh",
        step1Extra: "Gói dịch vụ bổ sung (Freeship/Voucher Xtra)",
        step5Title: "Hiệu quả kinh doanh & Tỷ suất lợi nhuận",
        step5CostName: "Giá vốn hàng bán (COGS)",
        step5CostFormula: "Chi phí nhập / sản xuất sản phẩm ban đầu",
        step5ProfitName: "LỢI NHUẬN RÒNG CUỐI CÙNG (LÃI)",
        toastExported: "Đã tạo và tải ảnh tóm tắt thành công!",
        exportSubtitle: "BẢNG TÍNH DOANH THU & CHIẾT KHẤU",
        exportDeductions: "CHI TIẾT KHẤU TRỪ SÀN & THUẾ",
        exportTotalDeductions: "Tổng khấu trừ sàn & thuế",
        exportNetBadge: "Thực nhận",
        exportFooterText: "Copyright © 2026 Shopee Estimator. All rights reserved."
      },
      en: {
        pageTitle: "Estimated Net Revenue Calculator - E-Commerce",
        headerTitle: "Estimated Net Revenue Calculator",
        marketTitle: "Select Shopee Marketplace",
        marketSubtitle: "Please select your sales country to start calculating",
        marketVN: "Vietnam",
        marketTH: "Thailand",
        marketMY: "Malaysia",
        marketPH: "Philippines",
        marketCurrencyVND: "Currency: ₫ (VND)",
        marketCurrencyTHB: "Currency: ฿ (THB)",
        marketCurrencyMYR: "Currency: RM (MYR)",
        marketCurrencyPHP: "Currency: ₱ (PHP)",
        marketEnterBtn: "Enter Calculator",
        btnChangeMarket: "⇄ Change Market",
        tabForward: "Calculate Net Revenue",
        tabReverse: "Calculate Target Price",
        card1Title: "Initial Selling Price",
        card1Badge: "List price",
        card1Label: "Enter product list price on platform:",
        fixedFeeLabel: "Fixed fee:",
        serviceFeeLabel: "Service fee:",
        txFeeLabel: "Transaction fee:",
        taxFeeLabel: "Tax:",
        card2Title: "Net Revenue After Deductions",
        payoutLabel: "Estimated payout to account",
        noDataText: "No data yet",
        ratioLabel: "Cash flow breakdown:",
        legendNet: "Net",
        legendFee: "Fee",
        legendTax: "Tax",
        summaryTotalFee: "Total Platform Fees",
        summaryTotalTax: "Total Tax Payable",
        btnCopy: "Copy Result",
        btnReset: "Reset",
        detailTrigger: "Detailed Breakdown",
        step1Title: "Platform fees deducted from list price",
        step1Fixed: "Fixed commission fee",
        step1Tx: "Transaction processing fee",
        step1Total: "Total Platform Fees (A)",
        step2Title: "Revenue before tax (Tax base)",
        step2BeforeTax: "Revenue before tax (B = Price - A)",
        step2Formula: "Remaining amount after deducting all platform fees",
        step3Title: "Tax payable (Applied after platform fees)",
        step4Title: "Final net payout to wallet",
        step4Net: "NET PAYOUT TO ACCOUNT (B - C)",
        formulaTitle: "Summary Formula:",
        reverseCard1Title: "Target Net Payout",
        reverseCard1Badge: "Wallet target",
        reverseCard1Label: "Enter desired net payout to account:",
        reverseCard2Title: "Required Listing Price",
        reverseCard2Badge: "Suggested price",
        reverseCard2Label: "Required listing price on platform",
        reversePrompt: "Enter target amount to calculate",
        reverseFormulaTitle: "Exact reverse formula:",
        footerText: "Copyright © 2026 Shopee Estimator. All rights reserved.",
        toastReset: "Data reset!",
        toastCopied: "Result copied to clipboard!",
        toastNoPrice: "Please enter a product price first!",
        deductPrefix: "Deductions",
        lossFee: "Price too low to cover fees!",
        reverseSubtitlePrefix: "After deducting",
        reverseSubtitleSuffix: "fees & taxes, remaining payout is",
        copyHeader: "E-COMMERCE REVENUE CALCULATION",
        copyPrice: "• Initial selling price:",
        copyNet: "NET PAYOUT TO WALLET:",
        costLabel: "Cost of Goods Sold (COGS / Optional):",
        xtraLabel: "Freeship Xtra / Voucher Xtra Package",
        extraFeeLabel: "Xtra Service Fee:",
        profitBoxTitle: "Business Profitability (Margin)",
        netProfitLabel: "Net Profit:",
        marginLabel: "Profit Margin:",
        btnExportPng: "Export PNG",
        step1Extra: "Extra Service Package (Freeship/Voucher Xtra)",
        step5Title: "Business Performance & Profit Margin",
        step5CostName: "Cost of Goods Sold (COGS)",
        step5CostFormula: "Product sourcing / manufacturing cost",
        step5ProfitName: "FINAL NET PROFIT",
        toastExported: "Summary receipt image exported successfully!",
        exportSubtitle: "REVENUE & DEDUCTION SUMMARY",
        exportDeductions: "FEE & TAX DEDUCTIONS BREAKDOWN",
        exportTotalDeductions: "Total Platform Fees & Tax",
        exportNetBadge: "Net Payout",
        exportFooterText: "Copyright © 2026 Shopee Estimator. All rights reserved."
      },
      th: {
        pageTitle: "โปรแกรมคำนวณรายรับสุทธิ - Shopee ประเทศไทย",
        headerTitle: "คำนวณรายรับสุทธิหลังหักค่าธรรมเนียม",
        marketTitle: "เลือกตลาด Shopee",
        marketSubtitle: "กรุณาเลือกประเทศที่คุณดำเนินธุรกิจเพื่อเริ่มต้นคำนวณ",
        marketVN: "เวียดนาม",
        marketTH: "ไทย",
        marketMY: "มาเลเซีย",
        marketPH: "ฟิลิปปินส์",
        marketCurrencyVND: "สกุลเงิน: ₫ (VND)",
        marketCurrencyTHB: "สกุลเงิน: ฿ (THB)",
        marketCurrencyMYR: "สกุลเงิน: RM (MYR)",
        marketCurrencyPHP: "สกุลเงิน: ₱ (PHP)",
        marketEnterBtn: "เข้าสู่โปรแกรมคำนวณ",
        btnChangeMarket: "เปลี่ยนตลาด",
        tabForward: "คำนวณรายรับสุทธิ",
        tabReverse: "คำนวณราคาขายที่ต้องตั้ง",
        card1Title: "ราคาขายตั้งต้น",
        card1Badge: "ราคาบน Shopee",
        card1Label: "ระบุราคาสินค้าที่ตั้งขายบน Shopee:",
        fixedFeeLabel: "ค่าธรรมเนียมการขาย:",
        serviceFeeLabel: "ค่าธรรมเนียมการให้บริการ:",
        txFeeLabel: "ค่าธรรมเนียมการชำระเงิน:",
        taxFeeLabel: "ภาษีมูลค่าเพิ่ม (VAT):",
        card2Title: "รายรับสุทธิหลังหักค่าธรรมเนียม",
        payoutLabel: "รายรับสุทธิที่คาดว่าจะได้รับเข้ากระเป๋าเงิน",
        noDataText: "ยังไม่มีข้อมูลคำนวณ",
        ratioLabel: "สัดส่วนการกระจายยอดขาย:",
        legendNet: "รายรับ",
        legendFee: "ค่าธรรมเนียม",
        legendTax: "ภาษี",
        summaryTotalFee: "รวมค่าธรรมเนียม Shopee",
        summaryTotalTax: "รวมภาษีมูลค่าเพิ่ม (VAT)",
        btnCopy: "คัดลอกผลลัพธ์",
        btnReset: "รีเซ็ต",
        detailTrigger: "รายละเอียดการคำนวณ",
        step1Title: "ค่าธรรมเนียมแพลตฟอร์มที่หักจากราคาขาย",
        step1Fixed: "ค่าธรรมเนียมการขาย (Commission Fee)",
        step1Tx: "ค่าธรรมเนียมการชำระเงิน (Transaction Fee)",
        step1Total: "รวมค่าธรรมเนียมแพลตฟอร์ม (A)",
        step2Title: "รายได้ก่อนภาษี (ฐานสำหรับคำนวณภาษี)",
        step2BeforeTax: "รายได้ก่อนหักภาษี (B = ราคาขาย - A)",
        step2Formula: "ยอดคงเหลือหลังจาก Shopee หักค่าธรรมเนียมทั้งหมด",
        step3Title: "ภาษีที่ต้องชำระ (คำนวณจากค่าธรรมเนียมบริการ)",
        step4Title: "รายรับสุทธิสุดท้ายที่โอนเข้ากระเป๋าผู้ขาย",
        step4Net: "ยอดเงินเข้าบัญชีจริง (B - C)",
        formulaTitle: "สูตรการคำนวณโดยสรุป:",
        reverseCard1Title: "ยอดเงินที่ต้องการได้รับ",
        reverseCard1Badge: "เป้าหมายรายรับ",
        reverseCard1Label: "ระบุจำนวนเงินสุทธิที่คุณต้องการรับเข้าบัญชี:",
        reverseCard2Title: "ราคาขายที่ต้องตั้งบน Shopee",
        reverseCard2Badge: "ราคาแนะนำ",
        reverseCard2Label: "ราคาที่คุณต้องตั้งบนระบบ Shopee",
        reversePrompt: "ระบุยอดเงินที่ต้องการเพื่อคำนวณ",
        reverseFormulaTitle: "สูตรคำนวณราคาย้อนกลับที่แม่นยำ:",
        footerText: "Copyright © 2026 Shopee Estimator. All rights reserved.",
        toastReset: "รีเซ็ตข้อมูลเรียบร้อยแล้ว!",
        toastCopied: "คัดลอกรายละเอียดผลลัพธ์แล้ว!",
        toastNoPrice: "กรุณาระบุราคาสินค้าก่อน!",
        deductPrefix: "หักทั้งหมด",
        lossFee: "ราคาขายต่ำเกินไป ไม่พอหักค่าธรรมเนียม!",
        reverseSubtitlePrefix: "หลังหักค่าธรรมเนียมและภาษี",
        reverseSubtitleSuffix: "จะได้รับยอดสุทธิตรงตามเป้าหมาย",
        copyHeader: "การคำนวณรายรับ SHOPEE ประเทศไทย",
        copyPrice: "• ราคาขายตั้งต้น:",
        copyNet: "รายรับสุทธิเข้ากระเป๋า:",
        costLabel: "ต้นทุนสินค้า (COGS / ทางเลือก):",
        xtraLabel: "แพ็กเกจ Freeship Xtra / Voucher Xtra",
        extraFeeLabel: "ค่าบริการ Xtra:",
        profitBoxTitle: "ผลกำไรทางธุรกิจ (Margin)",
        netProfitLabel: "กำไรสุทธิ:",
        marginLabel: "อัตรากำไร (Margin):",
        btnExportPng: "ดาวน์โหลดรูป",
        step1Extra: "แพ็กเกจบริการเพิ่มเติม (Freeship/Voucher Xtra)",
        step5Title: "ประสิทธิภาพทางธุรกิจและอัตรากำไร",
        step5CostName: "ต้นทุนสินค้าที่ขาย (COGS)",
        step5CostFormula: "ต้นทุนการจัดหา / ผลิตสินค้า",
        step5ProfitName: "กำไรสุทธิขั้นสุดท้าย",
        toastExported: "ส่งออกรูปภาพสรุปเรียบร้อยแล้ว!",
        exportSubtitle: "สรุปรายได้และค่าธรรมเนียม",
        exportDeductions: "รายละเอียดการหักค่าธรรมเนียมและภาษี",
        exportTotalDeductions: "รวมค่าธรรมเนียมและภาษีทั้งหมด",
        exportNetBadge: "รายรับสุทธิ",
        exportFooterText: "Copyright © 2026 Shopee Estimator. All rights reserved."
      },
      ms: {
        pageTitle: "Kalkulator Anggaran Pendapatan Bersih - Shopee Malaysia",
        headerTitle: "Kira Anggaran Pendapatan Bersih Selepas Potongan",
        marketTitle: "Pilih Pasaran Shopee",
        marketSubtitle: "Sila pilih negara jualan anda untuk mula mengira",
        marketVN: "Vietnam",
        marketTH: "Thailand",
        marketMY: "Malaysia",
        marketPH: "Filipina",
        marketCurrencyVND: "Mata wang: ₫ (VND)",
        marketCurrencyTHB: "Mata wang: ฿ (THB)",
        marketCurrencyMYR: "Mata wang: RM (MYR)",
        marketCurrencyPHP: "Mata wang: ₱ (PHP)",
        marketEnterBtn: "Masuk Kalkulator",
        btnChangeMarket: "Tukar Pasaran",
        tabForward: "Kira Pendapatan Bersih",
        tabReverse: "Kira Harga Jualan Sasaran",
        card1Title: "Harga Jualan Asal",
        card1Badge: "Harga disenaraikan",
        card1Label: "Masukkan harga produk yang disenaraikan di Shopee:",
        fixedFeeLabel: "Yuran komisen:",
        serviceFeeLabel: "Yuran perkhidmatan:",
        txFeeLabel: "Yuran transaksi:",
        taxFeeLabel: "Cukai perkhidmatan (SST):",
        card2Title: "Pendapatan Bersih Selepas Potongan",
        payoutLabel: "Anggaran pembayaran ke akaun bank/dompet",
        noDataText: "Tiada data untuk dikira",
        ratioLabel: "Pecahan aliran tunai jualan:",
        legendNet: "Bersih",
        legendFee: "Yuran",
        legendTax: "Cukai",
        summaryTotalFee: "Jumlah Yuran Platform",
        summaryTotalTax: "Jumlah Cukai Kena Bayar",
        btnCopy: "Salin Hasil",
        btnReset: "Tetapkan Semula",
        detailTrigger: "Analisis Terperinci",
        step1Title: "Yuran platform yang ditolak daripada harga jualan",
        step1Fixed: "Yuran komisen pasaran (Commission Fee)",
        step1Tx: "Yuran pemprosesan transaksi (Transaction Fee)",
        step1Total: "Jumlah Yuran Platform (A)",
        step2Title: "Pendapatan sebelum cukai (Asas pengiraan cukai)",
        step2BeforeTax: "Pendapatan sebelum cukai (B = Harga - A)",
        step2Formula: "Baki jumlah selepas Shopee menolak semua yuran platform",
        step3Title: "Cukai kena bayar (Dikenakan ke atas yuran perkhidmatan)",
        step4Title: "Pendapatan bersih akhir dipindahkan ke dompet penjual",
        step4Net: "JUMLAH BERSIH KE AKAUN (B - C)",
        formulaTitle: "Formula ringkasan pengiraan:",
        reverseCard1Title: "Sasaran Pendapatan Bersih",
        reverseCard1Badge: "Sasaran dompet",
        reverseCard1Label: "Masukkan jumlah wang bersih yang ingin anda terima:",
        reverseCard2Title: "Harga Jualan Perlu Ditetapkan",
        reverseCard2Badge: "Harga cadangan",
        reverseCard2Label: "Harga jualan yang perlu anda senaraikan di Shopee",
        reversePrompt: "Masukkan jumlah sasaran untuk mengira",
        reverseFormulaTitle: "Formula pengiraan terbalik tepat:",
        footerText: "Copyright © 2026 Shopee Estimator. All rights reserved.",
        toastReset: "Data telah ditetapkan semula!",
        toastCopied: "Butiran hasil telah disalin ke papan keratan!",
        toastNoPrice: "Sila masukkan harga produk dahulu!",
        deductPrefix: "Potongan",
        lossFee: "Harga terlalu rendah untuk menampung yuran platform!",
        reverseSubtitlePrefix: "Selepas menolak",
        reverseSubtitleSuffix: "yuran & cukai, baki bersih adalah tepat",
        copyHeader: "PENGIRAAN PENDAPATAN SHOPEE MALAYSIA",
        copyPrice: "• Harga jualan asal:",
        copyNet: "PENDAPATAN BERSIH KE DOMPET:",
        costLabel: "Kos Barangan Dijual (COGS / Pilihan):",
        xtraLabel: "Pakej Freeship Xtra / Baucar Xtra",
        extraFeeLabel: "Yuran Servis Xtra:",
        profitBoxTitle: "Keuntungan Perniagaan (Margin)",
        netProfitLabel: "Keuntungan Bersih:",
        marginLabel: "Margin Keuntungan:",
        btnExportPng: "Muat Turun Imej",
        step1Extra: "Pakej Servis Tambahan (Freeship/Baucar Xtra)",
        step5Title: "Prestasi Perniagaan & Margin Keuntungan",
        step5CostName: "Kos Barangan Dijual (COGS)",
        step5CostFormula: "Kos perolehan / pembuatan produk",
        step5ProfitName: "KEUNTUNGAN BERSIH AKHIR",
        toastExported: "Imej resit ringkasan berjaya dieksport!",
        exportSubtitle: "RINGKASAN PENDAPATAN & POTONGAN",
        exportDeductions: "PECAHAN POTONGAN YURAN & CUKAI",
        exportTotalDeductions: "Jumlah Potongan Yuran & Cukai",
        exportNetBadge: "Bersih Diterima",
        exportFooterText: "Copyright © 2026 Shopee Estimator. All rights reserved."
      },
      tl: {
        pageTitle: "Tagapagtantya ng Netong Kita - Shopee Philippines",
        headerTitle: "Kalkulahin ang Netong Kita Matapos ang Bawas",
        marketTitle: "Pumili ng Marketplace sa Shopee",
        marketSubtitle: "Mangyaring piliin ang bansa ng iyong benta upang simulan ang pagkalkula",
        marketVN: "Vietnam",
        marketTH: "Thailand",
        marketMY: "Malaysia",
        marketPH: "Pilipinas",
        marketCurrencyVND: "Pera: ₫ (VND)",
        marketCurrencyTHB: "Pera: ฿ (THB)",
        marketCurrencyMYR: "Pera: RM (MYR)",
        marketCurrencyPHP: "Pera: ₱ (PHP)",
        marketEnterBtn: "Pumasok sa Calculator",
        btnChangeMarket: "Palitan ang Market",
        tabForward: "Kalkulahin ang Netong Kita",
        tabReverse: "Kalkulahin ang Presyo ng Benta",
        card1Title: "Orihinal na Presyo ng Pagbebenta",
        card1Badge: "Presyo sa Shopee",
        card1Label: "Ilagay ang presyo ng produkto na nakalista sa Shopee:",
        fixedFeeLabel: "Bayad sa komisyon:",
        serviceFeeLabel: "Bayad sa pagproseso:",
        txFeeLabel: "Bayad sa transaksyon:",
        taxFeeLabel: "Buwis sa BIR (CWT):",
        card2Title: "Netong Kita Matapos ang Bawas",
        payoutLabel: "Inaasahang matatanggap sa account/wallet",
        noDataText: "Wala pang datos para kalkulahin",
        ratioLabel: "Distribusyon ng kabuuang benta:",
        legendNet: "Kita",
        legendFee: "Bayarin",
        legendTax: "Buwis",
        summaryTotalFee: "Kabuuang Bayad sa Platform",
        summaryTotalTax: "Kabuuang Buwis na Babayaran",
        btnCopy: "Kopyahin ang Resulta",
        btnReset: "I-reset",
        detailTrigger: "Detalyadong Pagkalkula",
        step1Title: "Mga bayarin sa platform na ibinabawas sa presyo",
        step1Fixed: "Bayad sa komisyon sa marketplace (Commission Fee)",
        step1Tx: "Bayad sa pagproseso ng transaksyon (Transaction Fee)",
        step1Total: "Kabuuang Bayad sa Platform (A)",
        step2Title: "Kita bago ang buwis (Batayan ng buwis)",
        step2BeforeTax: "Kita bago ang buwis (B = Presyo - A)",
        step2Formula: "Natitirang halaga matapos ibawas ng Shopee ang lahat ng bayarin",
        step3Title: "Buwis na dapat bayaran (Alinsunod sa BIR RR 16-2023)",
        step4Title: "Huling netong kita na ililipat sa seller wallet",
        step4Net: "PERANG MATATANGGAP SA ACCOUNT (B - C)",
        formulaTitle: "Pinaikling formula sa pagkalkula:",
        reverseCard1Title: "Target na Netong Kita",
        reverseCard1Badge: "Target sa wallet",
        reverseCard1Label: "Ilagay ang eksaktong halaga na nais mong matanggap sa account:",
        reverseCard2Title: "Kinakailangang Presyo sa Shopee",
        reverseCard2Badge: "Iminungkahing presyo",
        reverseCard2Label: "Presyo na dapat mong i-post sa platform ng Shopee",
        reversePrompt: "Ilagay ang nais na halaga upang kalkulahin",
        reverseFormulaTitle: "Tumpak na formula sa pabaliktad na pagkalkula:",
        footerText: "Copyright © 2026 Shopee Estimator. All rights reserved.",
        toastReset: "Matagumpay na na-reset ang datos!",
        toastCopied: "Nai-kopya na ang detalye ng resulta sa clipboard!",
        toastNoPrice: "Mangyaring maglagay muna ng presyo ng produkto!",
        deductPrefix: "Bawas",
        lossFee: "Masyadong mababa ang presyo para masakop ang bayarin!",
        reverseSubtitlePrefix: "Matapos ibawas ang",
        reverseSubtitleSuffix: "bayarin at buwis, ang matitira ay eksakto",
        copyHeader: "PAGKALKULA NG KITA SA SHOPEE PHILIPPINES",
        copyPrice: "• Orihinal na presyo ng pagbebenta:",
        copyNet: "NETONG KITA SA WALLET:",
        costLabel: "Gastos sa Produkto (COGS / Opsyonal):",
        xtraLabel: "Package ng Freeship Xtra / Voucher Xtra",
        extraFeeLabel: "Bayad sa Servis Xtra:",
        profitBoxTitle: "Kakayahang Kumita ng Negosyo (Margin)",
        netProfitLabel: "Netong Tubo:",
        marginLabel: "Margin ng Tubo:",
        btnExportPng: "I-download ang Larawan",
        step1Extra: "Karagdagang Servis Package (Freeship/Voucher Xtra)",
        step5Title: "Pagganap ng Negosyo at Margin ng Tubo",
        step5CostName: "Gastos ng mga Nabentang Produkto (COGS)",
        step5CostFormula: "Gastos sa pagkuha / paggawa ng produkto",
        step5ProfitName: "HULING NETONG TUBO",
        toastExported: "Matagumpay na na-export ang larawan ng resibo!",
        exportSubtitle: "BUOD NG KITA AT MGA BAWAS",
        exportDeductions: "PAGKAKAHATI NG MGA BAWAS SA BAYAD AT BUWIS",
        exportTotalDeductions: "Kabuuang Bawas sa Bayad at Buwis",
        exportNetBadge: "Netong Natanggap",
        exportFooterText: "Copyright © 2026 Shopee Estimator. All rights reserved."
      }
    };

    // MARKETS CONFIGURATION
    const MARKETS = {
      vn: {
        code: 'VN',
        nameVi: 'Việt Nam',
        nameEn: 'Vietnam',
        nameTh: 'เวียดนาม',
        nameMs: 'Vietnam',
        nameTl: 'Vietnam',
        currency: '₫',
        decimals: 0,
        fixedFeeRate: 0.16,      // 16% phí cố định
        serviceFee: 3000,        // 3.000₫ phí dịch vụ cố định
        txFeeRate: 0.06,         // 6% phí xử lý giao dịch
        extraServiceRate: 0.06,  // 6% phí Freeship Xtra
        extraServiceCap: 30000,  // Tối đa 30.000₫
        extraBadgeText: '+6% (max 30k)',
        taxRate1: 0.01,          // 1% thuế GTGT
        taxRate2: 0.005,         // 0.5% thuế TNCN
        taxBasis: 'beforeTax',   // Thuế tính trên Doanh thu trước thuế (B)
        taxOnFees: false,
        presets: [50000, 100000, 200000, 350000, 500000, 1000000],
        presetLabels: {
          vi: ['50k', '100k', '200k', '350k', '500k', '1 Triệu'],
          en: ['50k', '100k', '200k', '350k', '500k', '1M'],
          th: ['50k', '100k', '200k', '350k', '500k', '1M'],
          ms: ['50k', '100k', '200k', '350k', '500k', '1 Juta'],
          tl: ['50k', '100k', '200k', '350k', '500k', '1 Milyon']
        },
        minPrice: 4000,
        ratesDisplay: {
          fixed: '16%',
          service: '3.000₫',
          tx: '6%',
          tax: '1,5%',
          tax1: '1,0%',
          tax2: '0,5%',
          taxLabelVi: 'Thuế (GTGT+TNCN):',
          taxLabelEn: 'Tax (VAT+PIT):',
          fixedFormulaVi: '16% × Giá bán ban đầu',
          fixedFormulaEn: '16% × Initial price',
          serviceNameVi: 'Phí dịch vụ cố định',
          serviceNameEn: 'Fixed service fee',
          serviceFormulaVi: 'Khoản thu cố định mỗi đơn',
          serviceFormulaEn: 'Fixed charge per order',
          txFormulaVi: '6% × Giá bán ban đầu',
          txFormulaEn: '6% × Initial price',
          tax1NameVi: 'Thuế Giá Trị Gia Tăng (GTGT)',
          tax1NameEn: 'Value Added Tax (VAT)',
          tax1FormulaVi: '1,0% × Doanh thu trước thuế (B)',
          tax1FormulaEn: '1.0% × Revenue before tax (B)',
          tax2NameVi: 'Thuế Thu Nhập Cá Nhân (TNCN / TTCN)',
          tax2NameEn: 'Personal Income Tax (PIT)',
          tax2FormulaVi: '0,5% × Doanh thu trước thuế (B)',
          tax2FormulaEn: '0.5% × Revenue before tax (B)',
          taxTotalVi: 'Tổng thuế phải nộp (C = GTGT + TNCN)',
          taxTotalEn: 'Total Tax (C = VAT + PIT)',
          formulaBeforeTaxVi: 'Doanh thu trước thuế = Giá bán × 78% - 3.000₫',
          formulaBeforeTaxEn: 'Revenue before tax = Price × 78% - 3,000₫',
          formulaNetVi: 'Doanh thu thực nhận = Doanh thu trước thuế × 98,5% (sau khi khấu trừ 1,5% thuế).',
          formulaNetEn: 'Net revenue = Revenue before tax × 98.5% (after deducting 1.5% tax).',
          reverseDescVi: '💡 Tính năng này giúp bạn biết cần đặt giá niêm yết bao nhiêu trên sàn để sau khi trừ hết 22% phí sàn, 3.000₫ phí dịch vụ và 1.5% thuế, bạn vẫn bỏ túi đúng số tiền mong muốn.',
          reverseDescEn: '💡 Calculates the exact listing price needed so that after 22% platform fees, 3,000₫ service fee, and 1.5% tax, you pocket your exact target amount.',
          reverseFormulaVi: 'Giá niêm yết = [(Số tiền muốn nhận ÷ 0,985) + 3.000₫] ÷ 0,78',
          reverseFormulaEn: 'Listing price = [(Target net ÷ 0.985) + 3,000₫] ÷ 0.78',
          alertLowPriceVi: '⚠️ Giá bán quá thấp (dưới 4.000₫), không đủ để bù trừ phụ phí dịch vụ cố định 3.000₫!',
          alertLowPriceEn: '⚠️ Price too low (below 4,000₫), cannot cover fixed service fee 3,000₫!'
        }
      },
      th: {
        code: 'TH',
        nameVi: 'Thái Lan',
        nameEn: 'Thailand',
        nameTh: 'ไทย',
        nameMs: 'Thailand',
        nameTl: 'Thailand',
        currency: '฿',
        decimals: 2,
        fixedFeeRate: 0.10,      // 10.0% phí cố định Non-Mall (10.70% gồm VAT)
        serviceFee: 1.00,        // 1.00 ฿ phí cơ sở hạ tầng (1.07 ฿ gồm VAT)
        txFeeRate: 0.03,         // 3.0% phí giao dịch (3.21% gồm VAT)
        extraServiceRate: 0.05,  // 5% phí Freeship Xtra
        extraServiceCap: 100,    // Tối đa 100฿
        extraBadgeText: '+5% (max 100฿)',
        taxRate1: 0.07,          // 7% VAT trên tổng phí dịch vụ sàn A
        taxRate2: 0,
        taxBasis: 'fees',        // Thuế tính trên Phụ phí sàn (A)
        taxOnFees: true,
        presets: [50, 100, 200, 500, 1000, 2000],
        presetLabels: {
          th: ['50฿', '100฿', '200฿', '500฿', '1,000฿', '2,000฿'],
          en: ['50฿', '100฿', '200฿', '500฿', '1,000฿', '2,000฿'],
          vi: ['50฿', '100฿', '200฿', '500฿', '1.000฿', '2.000฿'],
          ms: ['50฿', '100฿', '200฿', '500฿', '1,000฿', '2,000฿'],
          tl: ['50฿', '100฿', '200฿', '500฿', '1,000฿', '2,000฿']
        },
        minPrice: 2,
        ratesDisplay: {
          fixed: '10% (10,7%*)',
          service: '1,00฿ (1,07฿*)',
          tx: '3% (3,21%*)',
          tax: '7% VAT',
          tax1: '7%',
          taxLabelTh: 'ภาษี (VAT 7%):',
          taxLabelEn: 'Tax (VAT 7%):',
          taxLabelVi: 'Thuế (VAT 7%):',
          fixedFormulaTh: '10% × ราคาขายตั้งต้น (10.70% รวม VAT)',
          fixedFormulaEn: '10% × Initial price (10.70% incl. VAT)',
          fixedFormulaVi: '10% × Giá bán ban đầu (10,70% gồm VAT)',
          serviceNameTh: 'ค่าธรรมเนียมโครงสร้างพื้นฐาน',
          serviceNameEn: 'Platform infrastructure fee',
          serviceNameVi: 'Phí cơ sở hạ tầng nền tảng',
          serviceFormulaTh: 'ยอดคงที่ต่อคำสั่งซื้อ (1.07฿ รวม VAT)',
          serviceFormulaEn: 'Fixed charge per order (1.07฿ incl. VAT)',
          serviceFormulaVi: 'Khoản thu cố định mỗi đơn (1,07฿ gồm VAT)',
          txFormulaTh: '3% × ราคาขายตั้งต้น (3.21% รวม VAT)',
          txFormulaEn: '3% × Initial price (3.21% incl. VAT)',
          txFormulaVi: '3% × Giá bán ban đầu (3,21% gồm VAT)',
          tax1NameTh: 'ภาษีมูลค่าเพิ่ม (VAT 7%)',
          tax1NameEn: 'Value Added Tax (VAT 7%)',
          tax1NameVi: 'Thuế Giá Trị Gia Tăng (VAT 7% / ภาษีมูลค่าเพิ่ม)',
          tax1FormulaTh: '7.0% × รวมค่าธรรมเนียมแพลตฟอร์ม (A)',
          tax1FormulaEn: '7.0% × Total Platform Fees (A)',
          tax1FormulaVi: '7,0% × Tổng phụ phí sàn (A)',
          tax2NameTh: 'ภาษีหัก ณ ที่จ่ายเพิ่มเติม',
          tax2NameEn: 'Withholding income tax',
          tax2NameVi: 'Thuế thu nhập khấu trừ bổ sung',
          tax2FormulaTh: '0% (ไม่มีการหักภาษี ณ ที่จ่ายเพิ่มเติม)',
          tax2FormulaEn: '0% (No additional platform withholding)',
          tax2FormulaVi: '0% (Sàn không khấu trừ thêm)',
          taxTotalTh: 'รวมภาษีที่ต้องชำระ (C = VAT 7%)',
          taxTotalEn: 'Total Tax (C = VAT 7%)',
          taxTotalVi: 'Tổng thuế phải nộp (C = VAT 7%)',
          formulaBeforeTaxTh: 'รายได้ก่อนหักภาษี = ราคาขาย × 87% - 1.00฿',
          formulaBeforeTaxEn: 'Revenue before tax = Price × 87% - 1.00฿',
          formulaBeforeTaxVi: 'Doanh thu trước thuế = Giá bán × 87% - 1,00฿',
          formulaNetTh: 'รายรับสุทธิ = ราคาขาย - รวมค่าธรรมเนียมที่รวม 7% VAT แล้ว (13.91% × ราคา + 1.07฿).',
          formulaNetEn: 'Net revenue = Price - Total platform fees incl. 7% VAT (13.91% × Price + 1.07฿).',
          formulaNetVi: 'Doanh thu thực nhận = Giá bán - Tổng phụ phí sàn gồm 7% VAT (13,91% × Giá + 1,07฿).',
          reverseDescTh: '💡 เครื่องมือนี้ช่วยคุณคำนวณราคาขายที่ต้องตั้งบน Shopee ประเทศไทย เพื่อให้ได้รับเงินสุทธิตามต้องการ หลังหักค่าธรรมเนียมการขาย 13%, ค่าบริการ 1.00฿ และ 7% VAT (รวมหัก 13.91% + 1.07฿)',
          reverseDescEn: '💡 Calculates the exact listing price on Shopee Thailand needed to pocket your target amount after 13% platform fees, 1.00฿ infrastructure fee, and 7% VAT (total deduction 13.91% + 1.07฿).',
          reverseDescVi: '💡 Tính năng này giúp bạn biết cần đặt giá niêm yết bao nhiêu trên Shopee Thái Lan để sau khi trừ 13% phí sàn, 1,00฿ phí hạ tầng và 7% VAT (tổng trừ 13,91% + 1,07฿), bạn nhận đúng số tiền mong muốn.',
          reverseFormulaTh: 'ราคาขายที่ต้องตั้ง = (ยอดเงินที่ต้องการ + 1.07฿) ÷ 0.8609',
          reverseFormulaEn: 'Listing price = (Target net + 1.07฿) ÷ 0.8609',
          reverseFormulaVi: 'Giá niêm yết = (Số tiền muốn nhận + 1,07฿) ÷ 0,8609',
          alertLowPriceTh: '⚠️ ราคาขายต่ำเกินไป (ต่ำกว่า 2฿) ไม่ครอบคลุมค่าธรรมเนียมขั้นต่ำ 1.07฿!',
          alertLowPriceEn: '⚠️ Price too low (below 2฿), cannot cover infrastructure fee 1.07฿!',
          alertLowPriceVi: '⚠️ Giá bán quá thấp (dưới 2฿), không đủ để bù trừ phụ phí cơ sở hạ tầng 1,07฿!'
        }
      },
      my: {
        code: 'MY',
        nameVi: 'Malaysia',
        nameEn: 'Malaysia',
        nameTh: 'มาเลเซีย',
        nameMs: 'Malaysia',
        nameTl: 'Malaysia',
        currency: 'RM',
        decimals: 2,
        fixedFeeRate: 0.135,     // 13.5% hoa hồng Marketplace Non-Mall (14.58% gồm SST)
        serviceFee: 0.50,        // RM 0.50 phí hỗ trợ nền tảng (RM 0.54 gồm SST)
        txFeeRate: 0.035,        // 3.5% phí xử lý thanh toán (3.78% gồm SST)
        extraServiceRate: 0.05,  // 5% phí Freeship Xtra
        extraServiceCap: 15,     // Tối đa RM15
        extraBadgeText: '+5% (max RM15)',
        taxRate1: 0.08,          // 8% SST theo luật thuế dịch vụ CJP áp dụng trên phí sàn A
        taxRate2: 0,
        taxBasis: 'fees',        // Thuế tính trên Phụ phí sàn (A)
        taxOnFees: true,
        presets: [10, 25, 50, 100, 200, 500],
        presetLabels: {
          ms: ['RM10', 'RM25', 'RM50', 'RM100', 'RM200', 'RM500'],
          en: ['RM10', 'RM25', 'RM50', 'RM100', 'RM200', 'RM500'],
          vi: ['RM10', 'RM25', 'RM50', 'RM100', 'RM200', 'RM500'],
          th: ['RM10', 'RM25', 'RM50', 'RM100', 'RM200', 'RM500'],
          tl: ['RM10', 'RM25', 'RM50', 'RM100', 'RM200', 'RM500']
        },
        minPrice: 1,
        ratesDisplay: {
          fixed: '13,5% (14,58%*)',
          service: 'RM0.50 (0.54*)',
          tx: '3,5% (3,78%*)',
          tax: '8% SST',
          tax1: '8%',
          taxLabelMs: 'Cukai (SST 8%):',
          taxLabelEn: 'Tax (SST 8%):',
          taxLabelVi: 'Thuế (SST 8%):',
          fixedFormulaMs: '13.5% × Harga jualan asal (14.58% termasuk SST)',
          fixedFormulaEn: '13.5% × Initial price (14.58% incl. SST)',
          fixedFormulaVi: '13,5% × Giá bán ban đầu (14,58% gồm SST)',
          serviceNameMs: 'Yuran sokongan platform (Platform Support Fee)',
          serviceNameEn: 'Platform support fee',
          serviceNameVi: 'Phí dịch vụ hỗ trợ sàn (Platform Support)',
          serviceFormulaMs: 'Caj tetap setiap pesanan (RM0.54 termasuk SST)',
          serviceFormulaEn: 'Fixed charge per order (RM0.54 incl. SST)',
          serviceFormulaVi: 'Khoản thu cố định mỗi đơn (RM0.54 gồm SST)',
          txFormulaMs: '3.5% × Harga jualan asal (3.78% termasuk SST)',
          txFormulaEn: '3.5% × Initial price (3.78% incl. SST)',
          txFormulaVi: '3,5% × Giá bán ban đầu (3,78% gồm SST)',
          tax1NameMs: 'Cukai Jualan & Perkhidmatan (SST / CJP 8%)',
          tax1NameEn: 'Sales & Service Tax (SST / CJP 8%)',
          tax1NameVi: 'Thuế Bán Hàng & Dịch Vụ (SST / CJP 8%)',
          tax1FormulaMs: '8.0% × Jumlah Yuran Platform (A)',
          tax1FormulaEn: '8.0% × Total Platform Fees (A)',
          tax1FormulaVi: '8,0% × Tổng phụ phí sàn (A)',
          tax2NameMs: 'Cukai pegangan pendapatan tambahan',
          tax2NameEn: 'Withholding income tax',
          tax2NameVi: 'Thuế khấu trừ thu nhập bổ sung',
          tax2FormulaMs: '0% (Tiada potongan cukai pegangan platform tambahan)',
          tax2FormulaEn: '0% (No additional platform withholding)',
          tax2FormulaVi: '0% (Sàn không khấu trừ thêm)',
          taxTotalMs: 'Jumlah Cukai Kena Bayar (C = SST 8%)',
          taxTotalEn: 'Total Tax (C = SST 8%)',
          taxTotalVi: 'Tổng thuế phải nộp (C = SST 8%)',
          formulaBeforeTaxMs: 'Pendapatan sebelum cukai = Harga × 83% - RM0.50',
          formulaBeforeTaxEn: 'Revenue before tax = Price × 83% - RM0.50',
          formulaBeforeTaxVi: 'Doanh thu trước thuế = Giá bán × 83% - RM0.50',
          formulaNetMs: 'Pendapatan bersih = Harga - Jumlah yuran platform termasuk 8% SST (18.36% × Harga + RM0.54).',
          formulaNetEn: 'Net revenue = Price - Total platform fees incl. 8% SST (18.36% × Price + RM0.54).',
          formulaNetVi: 'Doanh thu thực nhận = Giá bán - Tổng phụ phí sàn gồm 8% SST (18,36% × Giá + RM0.54).',
          reverseDescMs: '💡 Fungsi ini membantu anda mengetahui harga yang perlu ditetapkan di Shopee Malaysia supaya selepas ditolak 17% yuran platform, RM0.50 yuran sokongan dan 8% SST (jumlah potongan 18.36% + RM0.54), anda menerima jumlah tepat yang diingini.',
          reverseDescEn: '💡 Calculates the exact listing price on Shopee Malaysia needed to pocket your target amount after 17% platform fees, RM0.50 platform support fee, and 8% SST (total deduction 18.36% + RM0.54).',
          reverseDescVi: '💡 Tính năng này giúp bạn biết cần đặt giá niêm yết bao nhiêu trên Shopee Malaysia để sau khi trừ 17% phí sàn, RM0.50 phí hỗ trợ và 8% SST (tổng trừ 18,36% + RM0.54), bạn nhận đúng số tiền mong muốn.',
          reverseFormulaMs: 'Harga senarai = (Jumlah sasaran + RM0.54) ÷ 0.8164',
          reverseFormulaEn: 'Listing price = (Target net + RM0.54) ÷ 0.8164',
          reverseFormulaVi: 'Giá niêm yết = (Số tiền muốn nhận + RM0.54) ÷ 0,8164',
          alertLowPriceMs: '⚠️ Harga jualan terlalu rendah (bawah RM1.00), tidak mencukupi untuk caj minimum platform RM0.54!',
          alertLowPriceEn: '⚠️ Price too low (below RM1.00), cannot cover platform support fee RM0.54!',
          alertLowPriceVi: '⚠️ Giá bán quá thấp (dưới RM1.00), không đủ để bù trừ phụ phí nền tảng RM0.54!'
        }
      },
      ph: {
        code: 'PH',
        nameVi: 'Philipin',
        nameEn: 'Philippines',
        nameTh: 'ฟิลิปปินส์',
        nameMs: 'Filipina',
        nameTl: 'Pilipinas',
        currency: '₱',
        decimals: 2,
        fixedFeeRate: 0.09,      // 9.0% hoa hồng Marketplace Non-Mall (VAT-inclusive)
        serviceFee: 5.00,        // 5.00 ₱ phí xử lý đơn hàng cố định (VAT-inclusive)
        txFeeRate: 0.0224,       // 2.24% phí xử lý thanh toán (2% + 12% VAT)
        extraServiceRate: 0.05,  // 5% phí Freeship Xtra
        extraServiceCap: 100,    // Tối đa 100₱
        extraBadgeText: '+5% (max 100₱)',
        taxRate1: 0.005,         // 0.5% Creditable Withholding Tax (BIR RR 16-2023: 1% trên 50% doanh thu gộp)
        taxRate2: 0,
        taxBasis: 'gross',       // Thuế tính trên Doanh thu gộp / Giá bán theo BIR RR 16-2023
        taxOnFees: false,
        presets: [100, 200, 500, 1000, 2000, 5000],
        presetLabels: {
          tl: ['100₱', '200₱', '500₱', '1,000₱', '2,000₱', '5,000₱'],
          en: ['100₱', '200₱', '500₱', '1,000₱', '2,000₱', '5,000₱'],
          vi: ['100₱', '200₱', '500₱', '1.000₱', '2.000₱', '5.000₱'],
          th: ['100₱', '200₱', '500₱', '1,000₱', '2,000₱', '5,000₱'],
          ms: ['100₱', '200₱', '500₱', '1,000₱', '2,000₱', '5,000₱']
        },
        minPrice: 6,
        ratesDisplay: {
          fixed: '9%',
          service: '5,00₱',
          tx: '2,24%',
          tax: '0,5% CWT',
          tax1: '0.5%',
          taxLabelTl: 'Buwis (BIR CWT 0.5%):',
          taxLabelEn: 'Tax (BIR CWT):',
          taxLabelVi: 'Thuế (BIR CWT):',
          fixedFormulaTl: '9% × Orihinal na presyo (Kasama ang VAT)',
          fixedFormulaEn: '9% × Initial price',
          fixedFormulaVi: '9% × Giá bán ban đầu',
          serviceNameTl: 'Bayad sa pagproseso ng order (Order Processing Fee)',
          serviceNameEn: 'Order processing fee',
          serviceNameVi: 'Phí xử lý đơn hàng (Order Processing)',
          serviceFormulaTl: 'Nakapirming bayad bawat order (Kasama ang VAT)',
          serviceFormulaEn: 'Fixed charge per completed order',
          serviceFormulaVi: 'Khoản thu cố định mỗi đơn hàng',
          txFormulaTl: '2.24% × Orihinal na presyo (2% + 12% VAT)',
          txFormulaEn: '2.24% × Initial price',
          txFormulaVi: '2,24% × Giá bán ban đầu',
          tax1NameTl: 'BIR Creditable Withholding Tax (CWT RR 16-2023)',
          tax1NameEn: 'BIR Creditable Withholding Tax (CWT RR 16-2023)',
          tax1NameVi: 'Thuế Khấu Trừ Tại Nguồn BIR (CWT RR 16-2023)',
          tax1FormulaTl: '0.5% × Orihinal na presyo (1% sa 50% gross remittances)',
          tax1FormulaEn: '0.5% × Initial price (1% on 50% gross remittances)',
          tax1FormulaVi: '0,5% × Giá bán ban đầu (1% trên 50% doanh thu gộp)',
          tax2NameTl: 'Karagdagang buwis sa kita',
          tax2NameEn: 'Additional income tax',
          tax2NameVi: 'Thuế thu nhập bổ sung',
          tax2FormulaTl: '0% (Walang karagdagang bawas mula sa platform)',
          tax2FormulaEn: '0% (No additional platform withholding)',
          tax2FormulaVi: '0% (Sàn không khấu trừ thêm)',
          taxTotalTl: 'Kabuuang buwis na babayaran (C = Buwis BIR 0.5%)',
          taxTotalEn: 'Total Tax (C = BIR Tax 0.5%)',
          taxTotalVi: 'Tổng thuế phải nộp (C = Thuế BIR 0,5%)',
          formulaBeforeTaxTl: 'Kita bago ang buwis = Presyo × 88.76% - 5.00₱',
          formulaBeforeTaxEn: 'Revenue before tax = Price × 88.76% - 5.00₱',
          formulaBeforeTaxVi: 'Doanh thu trước thuế = Giá bán × 88,76% - 5,00₱',
          formulaNetTl: 'Netong kita = Presyo × 88.26% - 5.00₱ (matapos ibawas ang 11.24% bayarin sa platform, 5.00₱ fee & 0.5% BIR tax).',
          formulaNetEn: 'Net revenue = Price × 88.26% - 5.00₱ (after deducting 11.24% platform fees, 5.00₱ fee & 0.5% BIR tax).',
          formulaNetVi: 'Doanh thu thực nhận = Giá bán × 88,26% - 5,00₱ (sau khi trừ 11,24% phí sàn, 5,00₱ phí đơn & 0,5% thuế BIR).',
          reverseDescTl: '💡 Tinutulungan ka nitong malaman ang kinakailangang ilistang presyo sa Shopee Philippines upang matapos ang 11.24% bayarin, 5.00₱ fee at 0.5% BIR tax (kabuuang bawas 11.74% + 5.00₱), makuha mo ang eksaktong nais mong halaga.',
          reverseDescEn: '💡 Calculates the exact listing price on Shopee Philippines needed to pocket your target amount after 11.24% platform fees, 5.00₱ processing fee, and 0.5% BIR tax (total deductions 11.74% + 5.00₱).',
          reverseDescVi: '💡 Tính năng này giúp bạn biết cần đặt giá niêm yết bao nhiêu trên Shopee Philippines để sau khi trừ 11,24% phí sàn, 5,00₱ phí xử lý đơn và 0,5% thuế BIR (tổng khấu trừ 11,74% + 5,00₱), bạn nhận đúng số tiền mong muốn.',
          reverseFormulaTl: 'Presyo sa Shopee = (Target net + 5.00₱) ÷ 0.8826',
          reverseFormulaEn: 'Listing price = (Target net + 5.00₱) ÷ 0.8826',
          reverseFormulaVi: 'Giá niêm yết = (Số tiền muốn nhận + 5,00₱) ÷ 0,8826',
          alertLowPriceTl: '⚠️ Masyadong mababa ang presyo (mas mababa sa 6₱), hindi sapat para sa bayad sa pagproseso ng order 5.00₱!',
          alertLowPriceEn: '⚠️ Price too low (below 6₱), cannot cover order processing fee 5.00₱!',
          alertLowPriceVi: '⚠️ Giá bán quá thấp (dưới 6₱), không đủ để bù trừ phụ phí xử lý đơn 5,00₱!'
        }
      }
    };

    const ICON_SUN_SVG = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4.2"/><line x1="12" y1="2" x2="12" y2="4.8"/><line x1="12" y1="19.2" x2="12" y2="22"/><line x1="4.93" y1="4.93" x2="6.91" y2="6.91"/><line x1="17.09" y1="17.09" x2="19.07" y2="19.07"/><line x1="2" y1="12" x2="4.8" y2="12"/><line x1="19.2" y1="12" x2="22" y2="12"/><line x1="4.93" y1="19.07" x2="6.91" y2="17.09"/><line x1="17.09" y1="6.91" x2="19.07" y2="4.93"/></svg>`;
    const ICON_MOON_SVG = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`;

    let currentMarket = localStorage.getItem('tmdt_market') || 'vn';
    let currentLang = localStorage.getItem('tmdt_lang') || 'en';
    let currentTheme = localStorage.getItem('tmdt_theme') || 'light';

    function getMarketNativeLang(marketKey) {
      switch (marketKey) {
        case 'th': return 'th';
        case 'my': return 'ms';
        case 'ph': return 'tl';
        case 'vn':
        default: return 'vi';
      }
    }

    function getLangDisplayCode(lang) {
      if (lang === 'tl') return 'FIL';
      return lang.toUpperCase();
    }

    function getMarketText(obj, keyBase, lang) {
      if (!obj) return '';
      const langCap = lang.charAt(0).toUpperCase() + lang.slice(1);
      if (obj[keyBase + langCap]) return obj[keyBase + langCap];
      if (obj[keyBase + 'En']) return obj[keyBase + 'En'];
      if (obj[keyBase + 'Vi']) return obj[keyBase + 'Vi'];
      return '';
    }

    function getCurrencySymbol() {
      return (MARKETS[currentMarket] && MARKETS[currentMarket].currency) || '₫';
    }

    function formatMoney(num, market = currentMarket) {
      if (isNaN(num) || num === null || num === undefined) return '0';
      const m = MARKETS[market] || MARKETS.vn;
      if (m.decimals === 0) {
        return Math.round(num).toLocaleString('vi-VN');
      } else {
        return Number(num).toLocaleString('en-US', {
          minimumFractionDigits: m.decimals,
          maximumFractionDigits: m.decimals
        });
      }
    }

    function formatMoneyWithSymbol(num, market = currentMarket) {
      const m = MARKETS[market] || MARKETS.vn;
      const formatted = formatMoney(num, market);
      if (m.currency === 'RM') {
        return `RM ${formatted}`;
      } else if (m.currency === '₱') {
        return `₱ ${formatted}`;
      } else {
        return `${formatted} ${m.currency}`;
      }
    }

    function parseInputNumber(str) {
      if (str === null || str === undefined || str === '') return 0;
      if (typeof str === 'number') return isNaN(str) ? 0 : str;
      const m = MARKETS[currentMarket] || MARKETS.vn;
      if (m.decimals === 0) {
        const clean = str.toString().replace(/[^\d]/g, '');
        return clean ? parseInt(clean, 10) : 0;
      } else {
        const clean = str.toString().replace(/,/g, '').replace(/[^\d.]/g, '');
        const val = parseFloat(clean);
        return isNaN(val) ? 0 : val;
      }
    }

    function openMarketScreen() {
      const calcApp = document.getElementById('calculatorApp');
      const switchBtn = document.getElementById('marketSwitchBtn');
      const langBtn = document.getElementById('langBtn');
      const marketScreen = document.getElementById('marketScreen');

      // 1. Ẩn calculatorApp ngay lập tức trước khi thực hiện chuyển tab để triệt tiêu mọi hiệu ứng giao diện
      if (calcApp) calcApp.style.display = 'none';
      if (switchBtn) switchBtn.style.display = 'none';
      if (langBtn) langBtn.style.display = 'none';

      // 2. Chuyển tab về forward ngay trong lúc calculatorApp đang ẩn
      switchMode('forward');

      // 3. Xóa sạch giá trị input cũ để tránh hiển thị lại khi vào thị trường khác
      const pIn = document.getElementById('priceInput');
      const tIn = document.getElementById('targetNetInput');
      const cIn = document.getElementById('costInput');
      if (pIn) pIn.value = '';
      if (tIn) tIn.value = '';
      if (cIn) cIn.value = '';
      const clrBtn = document.getElementById('clearBtn');
      if (clrBtn) clrBtn.style.display = 'none';
      const clrCost = document.getElementById('clearCostBtn');
      if (clrCost) clrCost.style.display = 'none';
      const clrRev = document.getElementById('clearReverseBtn');
      if (clrRev) clrRev.style.display = 'none';
      const pBox = document.getElementById('profitBox');
      if (pBox) pBox.style.display = 'none';
      const s5 = document.getElementById('step5CostSection');
      if (s5) s5.style.display = 'none';

      if (marketScreen) marketScreen.style.display = 'block';

      document.querySelectorAll('.market-card-btn').forEach(card => card.classList.remove('active'));
      const activeCard = document.getElementById('mkt-' + (currentMarket || 'vn'));
      if (activeCard) activeCard.classList.add('active');

      // Mặc định giao diện chọn thị trường (Ảnh 1) là tiếng Anh (EN)
      setLanguage('en');
    }

    function selectMarket(marketKey) {
      if (!MARKETS[marketKey]) marketKey = 'vn';
      currentMarket = marketKey;
      localStorage.setItem('tmdt_market', marketKey);

      // 1. Dọn sạch input và ẩn các box phụ TRƯỚC KHI hiển thị màn hình tính
      const pIn = document.getElementById('priceInput');
      const tIn = document.getElementById('targetNetInput');
      const cIn = document.getElementById('costInput');
      if (pIn) pIn.value = '';
      if (tIn) tIn.value = '';
      if (cIn) cIn.value = '';
      const clrCost = document.getElementById('clearCostBtn');
      if (clrCost) clrCost.style.display = 'none';
      const clrBtn = document.getElementById('clearBtn');
      if (clrBtn) clrBtn.style.display = 'none';
      const clrRev = document.getElementById('clearReverseBtn');
      if (clrRev) clrRev.style.display = 'none';
      const pBox = document.getElementById('profitBox');
      if (pBox) pBox.style.display = 'none';
      const s5 = document.getElementById('step5CostSection');
      if (s5) s5.style.display = 'none';

      // 2. Ép tab về Forward mode đồng bộ TRƯỚC KHI hiện calculatorApp
      switchMode('forward');

      // 3. Đặt ngôn ngữ mặc định của thị trường và tính toán chuẩn bị dữ liệu
      const nativeLang = getMarketNativeLang(marketKey);
      setLanguage(nativeLang);

      // 4. Mới bắt đầu unhide calculatorApp (đã chuẩn bị xong 100%, không bao giờ flicker)
      const marketScreen = document.getElementById('marketScreen');
      const calcApp = document.getElementById('calculatorApp');
      const switchBtn = document.getElementById('marketSwitchBtn');
      const langBtn = document.getElementById('langBtn');

      if (marketScreen) marketScreen.style.display = 'none';
      if (calcApp) calcApp.style.display = 'block';
      if (switchBtn) switchBtn.style.display = 'inline-flex';
      if (langBtn) langBtn.style.display = 'inline-flex';
    }

    function renderPresets() {
      const m = MARKETS[currentMarket] || MARKETS.vn;
      const forwardContainer = document.getElementById('forwardPresets');
      const reverseContainer = document.getElementById('reversePresets');
      const labels = (m.presetLabels && m.presetLabels[currentLang]) || (m.presetLabels && m.presetLabels.en) || (m.presetLabels && m.presetLabels.vi) || [];

      if (forwardContainer) {
        forwardContainer.innerHTML = m.presets.map((val, idx) => 
          `<button class="preset-chip" onclick="setPreset(${val})">${labels[idx] || val}</button>`
        ).join('');
      }

      if (reverseContainer) {
        reverseContainer.innerHTML = m.presets.map((val, idx) => 
          `<button class="preset-chip" onclick="setReversePreset(${val})">${labels[idx] || val}</button>`
        ).join('');
      }
    }

    function applyMarket(marketKey) {
      if (!MARKETS[marketKey]) marketKey = 'vn';
      currentMarket = marketKey;
      const m = MARKETS[marketKey];
      const lang = currentLang || 'en';
      const d = m.ratesDisplay;

      const pIn = document.getElementById('priceInput');
      const tIn = document.getElementById('targetNetInput');
      if (pIn) pIn.inputMode = m.decimals > 0 ? 'decimal' : 'numeric';
      if (tIn) tIn.inputMode = m.decimals > 0 ? 'decimal' : 'numeric';

      const displayEl = document.getElementById('marketDisplayCode');
      if (displayEl) displayEl.innerText = `Shopee ${m.code}`;
      const switchBtn = document.getElementById('marketSwitchBtn');
      if (switchBtn) switchBtn.title = `${displayEl ? displayEl.innerText + ' - ' : ''}Đổi thị trường / Change marketplace`;

      document.querySelectorAll('.market-card-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById('mkt-' + marketKey);
      if (activeBtn) activeBtn.classList.add('active');

      document.querySelectorAll('.currency-symbol').forEach(el => {
        el.innerText = m.currency;
      });

      // Vertical badges
      const badgeFixed = document.getElementById('badgeFixedFee');
      if (badgeFixed) badgeFixed.innerText = d.fixed;
      const badgeService = document.getElementById('badgeServiceFee');
      if (badgeService) badgeService.innerText = d.service;
      const badgeTx = document.getElementById('badgeTxFee');
      if (badgeTx) badgeTx.innerText = d.tx;
      const badgeTax = document.getElementById('badgeTaxFee');
      if (badgeTax) badgeTax.innerText = d.tax;
      const badgeTaxLabel = document.getElementById('badgeTaxLabel');
      if (badgeTaxLabel) badgeTaxLabel.innerText = getMarketText(d, 'taxLabel', lang);

      // Detailed table formulas & names
      const fFixed = document.getElementById('step1FixedFormula');
      if (fFixed) fFixed.innerText = getMarketText(d, 'fixedFormula', lang);

      const sName = document.getElementById('step1ServiceName');
      if (sName) sName.innerText = getMarketText(d, 'serviceName', lang);
      const fService = document.getElementById('step1ServiceFormula');
      if (fService) fService.innerText = getMarketText(d, 'serviceFormula', lang);

      const fTx = document.getElementById('step1TxFormula');
      if (fTx) fTx.innerText = getMarketText(d, 'txFormula', lang);

      const tax1Name = document.getElementById('step3Tax1Name');
      if (tax1Name) tax1Name.innerText = getMarketText(d, 'tax1Name', lang);
      const tax1Formula = document.getElementById('step3Tax1Formula');
      if (tax1Formula) tax1Formula.innerText = getMarketText(d, 'tax1Formula', lang);

      const tax2Row = document.getElementById('step3Tax2Row');
      const tax2Name = document.getElementById('step3Tax2Name');
      const tax2Formula = document.getElementById('step3Tax2Formula');
      if (m.taxRate2 > 0) {
        if (tax2Row) tax2Row.style.display = '';
        if (tax2Name) tax2Name.innerText = getMarketText(d, 'tax2Name', lang);
        if (tax2Formula) tax2Formula.innerText = getMarketText(d, 'tax2Formula', lang);
      } else {
        if (tax2Row) tax2Row.style.display = 'none';
      }

      const step3TotalLabel = document.getElementById('step3TotalLabel');
      if (step3TotalLabel) step3TotalLabel.innerText = getMarketText(d, 'taxTotal', lang);

      // Formula banners
      const formBeforeTax = document.getElementById('formulaBeforeTax');
      if (formBeforeTax) formBeforeTax.innerText = getMarketText(d, 'formulaBeforeTax', lang);
      const formNet = document.getElementById('formulaNet');
      if (formNet) formNet.innerText = getMarketText(d, 'formulaNet', lang);

      // Reverse card
      const revDesc = document.getElementById('reverseDesc');
      if (revDesc) revDesc.innerHTML = getMarketText(d, 'reverseDesc', lang);
      const revForm = document.getElementById('reverseFormulaBody');
      if (revForm) revForm.innerText = getMarketText(d, 'reverseFormula', lang);

      // Alert text
      const lowAlert = document.getElementById('lowPriceAlert');
      if (lowAlert) lowAlert.innerText = getMarketText(d, 'alertLowPrice', lang);

      // Freeship Xtra badges & formula
      const xtraBadge1 = document.getElementById('xtraRateBadge');
      const xtraBadge2 = document.getElementById('xtraReverseRateBadge');
      const badgeExtra = document.getElementById('badgeExtraFee');
      const step1ExtraForm = document.getElementById('step1ExtraFormula');
      const badgeText = m.extraBadgeText || `+${(m.extraServiceRate * 100).toFixed(0)}%`;
      if (xtraBadge1) xtraBadge1.innerText = badgeText;
      if (xtraBadge2) xtraBadge2.innerText = badgeText;
      if (badgeExtra) badgeExtra.innerText = badgeText;
      if (step1ExtraForm) step1ExtraForm.innerText = badgeText;

      renderPresets();
    }

    function setTheme(theme) {
      currentTheme = theme;
      localStorage.setItem('tmdt_theme', theme);
      const themeIcon = document.getElementById('themeIcon');
      const themeBtn = document.getElementById('themeBtn');
      if (theme === 'dark') {
        document.body.classList.add('dark-mode');
        if (themeIcon) themeIcon.innerHTML = ICON_MOON_SVG;
        if (themeBtn) themeBtn.title = 'Chuyển sang chế độ sáng / Switch to light mode';
      } else {
        document.body.classList.remove('dark-mode');
        if (themeIcon) themeIcon.innerHTML = ICON_SUN_SVG;
        if (themeBtn) themeBtn.title = 'Chuyển sang chế độ tối / Switch to dark mode';
      }
    }

    function toggleTheme() {
      setTheme(currentTheme === 'dark' ? 'light' : 'dark');
    }

    function updateLangButton() {
      const marketScreen = document.getElementById('marketScreen');
      const isMarketScreen = marketScreen && marketScreen.style.display !== 'none';
      const langLabel = document.getElementById('langLabel');
      if (!langLabel) return;

      if (isMarketScreen) {
        // Trên màn hình chọn thị trường: chuyển giữa EN và VI
        langLabel.innerText = currentLang === 'vi' ? 'EN' : 'VI';
      } else {
        // Trong thị trường cụ thể: chuyển giữa ngôn ngữ nước đó và EN
        const nativeLang = getMarketNativeLang(currentMarket);
        if (currentLang === 'en') {
          langLabel.innerText = getLangDisplayCode(nativeLang);
        } else {
          langLabel.innerText = 'EN';
        }
      }
    }

    function setLanguage(lang) {
      if (!I18N[lang]) lang = 'en';
      currentLang = lang;
      localStorage.setItem('tmdt_lang', lang);
      document.documentElement.lang = lang;
      const titleEl = document.getElementById('htmlTitle');
      if (titleEl && I18N[lang] && I18N[lang].pageTitle) titleEl.innerText = I18N[lang].pageTitle;

      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (I18N[lang] && I18N[lang][key]) {
          if (key === 'footerText') {
            el.innerHTML = I18N[lang][key];
          } else {
            el.innerText = I18N[lang][key];
          }
        }
      });

      updateLangButton();

      if (currentMarket && MARKETS[currentMarket]) {
        applyMarket(currentMarket);
      }

      calculate();
      calculateReverse();
    }

    function toggleLang() {
      const marketScreen = document.getElementById('marketScreen');
      const isMarketScreen = marketScreen && marketScreen.style.display !== 'none';

      if (isMarketScreen) {
        setLanguage(currentLang === 'vi' ? 'en' : 'vi');
      } else {
        const nativeLang = getMarketNativeLang(currentMarket);
        setLanguage(currentLang === 'en' ? nativeLang : 'en');
      }
    }

    // DOM ELEMENTS
    const priceInput = document.getElementById('priceInput');
    const clearBtn = document.getElementById('clearBtn');
    const costInput = document.getElementById('costInput');
    const clearCostBtn = document.getElementById('clearCostBtn');
    const xtraCheckbox = document.getElementById('xtraCheckbox');
    const xtraReverseCheckbox = document.getElementById('xtraReverseCheckbox');
    const profitBox = document.getElementById('profitBox');
    const netProfitVal = document.getElementById('netProfitVal');
    const profitMarginVal = document.getElementById('profitMarginVal');
    const profitMarginBadge = document.getElementById('profitMarginBadge');
    const badgeExtraRow = document.getElementById('badgeExtraRow');
    const badgeExtraFee = document.getElementById('badgeExtraFee');
    const detailExtraRow = document.getElementById('detailExtraRow');
    const detailExtraFee = document.getElementById('detailExtraFee');
    const step1ExtraFormula = document.getElementById('step1ExtraFormula');
    const step5CostSection = document.getElementById('step5CostSection');
    const detailCostVal = document.getElementById('detailCostVal');
    const detailProfitVal = document.getElementById('detailProfitVal');
    const detailMarginFormula = document.getElementById('detailMarginFormula');
    const exportPngBtn = document.getElementById('exportPngBtn');
    let isXtraActive = false;

    const lowPriceAlert = document.getElementById('lowPriceAlert');
    const netRevenueEl = document.getElementById('netRevenue');
    const percentSubtitleEl = document.getElementById('percentSubtitle');
    const barNet = document.getElementById('barNet');
    const barFee = document.getElementById('barFee');
    const barTax = document.getElementById('barTax');
    const barTooltip = document.getElementById('barTooltip');
    const summaryTotalFee = document.getElementById('summaryTotalFee');
    const summaryTotalTax = document.getElementById('summaryTotalTax');

    // Detail breakdown elements
    const detailCard = document.getElementById('detailCard');
    const detailFixedFee = document.getElementById('detailFixedFee');
    const detailServiceFee = document.getElementById('detailServiceFee');
    const detailTxFee = document.getElementById('detailTxFee');
    const detailTotalFee = document.getElementById('detailTotalFee');
    const detailBeforeTax = document.getElementById('detailBeforeTax');
    const detailTax1 = document.getElementById('detailTax1');
    const detailTax2 = document.getElementById('detailTax2');
    const detailTotalTax = document.getElementById('detailTotalTax');
    const detailNet = document.getElementById('detailNet');

    // Reverse elements
    const targetNetInput = document.getElementById('targetNetInput');
    const clearReverseBtn = document.getElementById('clearReverseBtn');
    const requiredPriceEl = document.getElementById('requiredPrice');
    const reverseSubtitle = document.getElementById('reverseSubtitle');

    function onToggleXtra(checked) {
      isXtraActive = !!checked;
      if (xtraCheckbox) xtraCheckbox.checked = isXtraActive;
      if (xtraReverseCheckbox) xtraReverseCheckbox.checked = isXtraActive;

      if (badgeExtraRow) badgeExtraRow.style.display = isXtraActive ? 'flex' : 'none';
      if (detailExtraRow) detailExtraRow.style.display = isXtraActive ? 'table-row' : 'none';

      calculate();
      calculateReverse();
    }

    // MAIN CALCULATION FUNCTION
    function calculate() {
      const m = MARKETS[currentMarket] || MARKETS.vn;
      const price = parseInputNumber(priceInput.value);
      const cost = parseInputNumber(costInput ? costInput.value : 0);

      if (price > 0) {
        clearBtn.style.display = 'flex';
      } else {
        clearBtn.style.display = 'none';
      }

      if (clearCostBtn) {
        clearCostBtn.style.display = cost > 0 ? 'flex' : 'none';
      }

      if (price <= 0) {
        lowPriceAlert.classList.remove('show');
        netRevenueEl.innerText = '0';
        percentSubtitleEl.innerText = I18N[currentLang].noDataText;
        barNet.style.width = '0%';
        barFee.style.width = '0%';
        barTax.style.width = '0%';
        barNet.removeAttribute('data-percent');
        barFee.removeAttribute('data-percent');
        barTax.removeAttribute('data-percent');
        barNet.title = '';
        barFee.title = '';
        barTax.title = '';
        summaryTotalFee.innerText = formatMoneyWithSymbol(0);
        summaryTotalTax.innerText = formatMoneyWithSymbol(0);

        detailFixedFee.innerText = formatMoneyWithSymbol(0);
        detailServiceFee.innerText = formatMoneyWithSymbol(0);
        if (detailExtraFee) detailExtraFee.innerText = formatMoneyWithSymbol(0);
        detailTxFee.innerText = formatMoneyWithSymbol(0);
        detailTotalFee.innerText = formatMoneyWithSymbol(0);
        detailBeforeTax.innerText = formatMoneyWithSymbol(0);
        if (detailTax1) detailTax1.innerText = formatMoneyWithSymbol(0);
        if (detailTax2) detailTax2.innerText = formatMoneyWithSymbol(0);
        detailTotalTax.innerText = formatMoneyWithSymbol(0);
        detailNet.innerText = formatMoneyWithSymbol(0);

        if (profitBox) profitBox.style.display = 'none';
        if (step5CostSection) step5CostSection.style.display = 'none';
        return;
      }

      // 1. Phụ phí sàn
      const fixedFee = price * m.fixedFeeRate;
      const serviceFee = m.serviceFee;
      const txFee = price * m.txFeeRate;
      let extraFee = 0;
      if (isXtraActive && m.extraServiceRate) {
        extraFee = price * m.extraServiceRate;
        if (m.extraServiceCap && extraFee > m.extraServiceCap) {
          extraFee = m.extraServiceCap;
        }
      }
      const totalFee = fixedFee + serviceFee + txFee + extraFee;

      // 2. Doanh thu trước thuế
      const revenueBeforeTax = price - totalFee;

      // 3. Thuế
      let tax1 = 0;
      let tax2 = 0;
      if (m.taxBasis === 'fees' || m.taxOnFees) {
        // Thuế áp dụng trên Tổng phụ phí sàn A (TH VAT 7%, MY SST 8%)
        tax1 = totalFee * m.taxRate1;
        tax2 = 0;
      } else if (m.taxBasis === 'gross') {
        // Thuế áp dụng trên Doanh thu gộp / Giá bán ban đầu (PH BIR CWT 0.5% theo RR 16-2023)
        tax1 = price * m.taxRate1;
        tax2 = 0;
      } else {
        // Thuế áp dụng trên Doanh thu trước thuế B (VN VAT 1% + TNCN 0.5%)
        tax1 = revenueBeforeTax * m.taxRate1;
        tax2 = revenueBeforeTax * m.taxRate2;
      }
      const totalTax = tax1 + tax2;

      // 4. Doanh thu thực nhận
      const netRevenue = revenueBeforeTax - totalTax;

      // Check if price is too low to cover fees & taxes
      if (price < m.minPrice || revenueBeforeTax <= 0 || netRevenue <= 0) {
        lowPriceAlert.classList.add('show');
        netRevenueEl.innerText = '0';
        percentSubtitleEl.innerText = I18N[currentLang].lossFee;

        barNet.style.width = '0%';
        barFee.style.width = '100%';
        barTax.style.width = '0%';
        barNet.removeAttribute('data-percent');
        barFee.setAttribute('data-percent', '100%');
        barFee.setAttribute('data-amount', formatMoneyWithSymbol(totalFee));
        barFee.title = `100% (${formatMoneyWithSymbol(totalFee)})`;
        barTax.removeAttribute('data-percent');

        summaryTotalFee.innerText = formatMoneyWithSymbol(totalFee);
        summaryTotalTax.innerText = formatMoneyWithSymbol(0);

        detailFixedFee.innerText = `-${formatMoneyWithSymbol(fixedFee)}`;
        detailServiceFee.innerText = `-${formatMoneyWithSymbol(serviceFee)}`;
        if (detailExtraFee) detailExtraFee.innerText = `-${formatMoneyWithSymbol(extraFee)}`;
        detailTxFee.innerText = `-${formatMoneyWithSymbol(txFee)}`;
        detailTotalFee.innerText = `-${formatMoneyWithSymbol(totalFee)}`;
        detailBeforeTax.innerText = `-${formatMoneyWithSymbol(Math.abs(revenueBeforeTax))}`;
        if (detailTax1) detailTax1.innerText = formatMoneyWithSymbol(0);
        if (detailTax2) detailTax2.innerText = formatMoneyWithSymbol(0);
        detailTotalTax.innerText = formatMoneyWithSymbol(0);
        detailNet.innerText = formatMoneyWithSymbol(0);

        if (profitBox) profitBox.style.display = 'none';
        if (step5CostSection) step5CostSection.style.display = 'none';
        return;
      }

      lowPriceAlert.classList.remove('show');

      // Percentages
      const netPercent = Math.max(0, ((netRevenue / price) * 100)).toFixed(1);
      const feePercent = Math.min(100, ((totalFee / price) * 100)).toFixed(1);
      const taxPercent = Math.min(100, ((totalTax / price) * 100)).toFixed(1);
      const totalDeduction = totalFee + totalTax;

      // Render Khung 2
      netRevenueEl.innerText = formatMoney(netRevenue);
      percentSubtitleEl.innerText = `${I18N[currentLang].deductPrefix} ${((totalDeduction / price) * 100).toFixed(1)}% (-${formatMoneyWithSymbol(totalDeduction)})`;

      // Visual width calculation: ensure any active tax segment completely fills the rounded cap (>= 3.0%)
      // to eliminate the jagged clipping glitch on the right cap
      const rawTaxW = (totalTax / price) * 100;
      let visualTaxW = rawTaxW;
      let visualFeeW = (totalFee / price) * 100;
      let visualNetW = (netRevenue / price) * 100;

      if (rawTaxW > 0 && rawTaxW < 3.0) {
        const adjust = 3.0 - rawTaxW;
        visualTaxW = 3.0;
        if (visualFeeW > adjust) {
          visualFeeW -= adjust;
        } else if (visualNetW > adjust) {
          visualNetW -= adjust;
        }
      }

      // Progress bar with data attributes for hover
      barNet.style.width = `${visualNetW.toFixed(2)}%`;
      barFee.style.width = `${visualFeeW.toFixed(2)}%`;
      barTax.style.width = `${visualTaxW.toFixed(2)}%`;

      barNet.setAttribute('data-percent', `${netPercent}%`);
      barNet.setAttribute('data-amount', formatMoneyWithSymbol(netRevenue));
      barNet.title = `${netPercent}% (${formatMoneyWithSymbol(netRevenue)})`;

      barFee.setAttribute('data-percent', `${feePercent}%`);
      barFee.setAttribute('data-amount', formatMoneyWithSymbol(totalFee));
      barFee.title = `${feePercent}% (${formatMoneyWithSymbol(totalFee)})`;

      barTax.setAttribute('data-percent', `${taxPercent}%`);
      barTax.setAttribute('data-amount', formatMoneyWithSymbol(totalTax));
      barTax.title = `${taxPercent}% (${formatMoneyWithSymbol(totalTax)})`;

      summaryTotalFee.innerText = formatMoneyWithSymbol(totalFee);
      summaryTotalTax.innerText = formatMoneyWithSymbol(totalTax);

      // Render Chi Tiết
      detailFixedFee.innerText = `-${formatMoneyWithSymbol(fixedFee)}`;
      detailServiceFee.innerText = `-${formatMoneyWithSymbol(serviceFee)}`;
      if (detailExtraFee) detailExtraFee.innerText = `-${formatMoneyWithSymbol(extraFee)}`;
      detailTxFee.innerText = `-${formatMoneyWithSymbol(txFee)}`;
      detailTotalFee.innerText = `-${formatMoneyWithSymbol(totalFee)}`;

      detailBeforeTax.innerText = formatMoneyWithSymbol(revenueBeforeTax);

      if (detailTax1) detailTax1.innerText = `-${formatMoneyWithSymbol(tax1)}`;
      if (detailTax2) detailTax2.innerText = `-${formatMoneyWithSymbol(tax2)}`;
      detailTotalTax.innerText = `-${formatMoneyWithSymbol(totalTax)}`;

      detailNet.innerText = formatMoneyWithSymbol(netRevenue);

      // Profit Margin calculation
      if (cost > 0 && profitBox) {
        profitBox.style.display = 'block';
        if (step5CostSection) step5CostSection.style.display = 'block';
        const netProfit = netRevenue - cost;
        const margin = (netProfit / price) * 100;

        if (detailCostVal) detailCostVal.innerText = `-${formatMoneyWithSymbol(cost)}`;

        const detailProfitRow = document.getElementById('detailProfitRow');
        if (netProfit >= 0) {
          profitBox.className = 'profit-box positive';
          if (detailProfitRow) detailProfitRow.className = 'subtotal-row profit-subtotal-row positive';
          if (netProfitVal) netProfitVal.innerText = `+${formatMoneyWithSymbol(netProfit)}`;
          if (profitMarginVal) profitMarginVal.innerText = `+${margin.toFixed(1)}%`;
          if (profitMarginBadge) {
            profitMarginBadge.innerText = `+${margin.toFixed(1)}%`;
            profitMarginBadge.className = 'profit-badge positive';
          }
          if (detailProfitVal) {
            detailProfitVal.innerText = `+${formatMoneyWithSymbol(netProfit)}`;
          }
        } else {
          profitBox.className = 'profit-box negative';
          if (detailProfitRow) detailProfitRow.className = 'subtotal-row profit-subtotal-row negative';
          if (netProfitVal) netProfitVal.innerText = `-${formatMoneyWithSymbol(Math.abs(netProfit))}`;
          if (profitMarginVal) profitMarginVal.innerText = `${margin.toFixed(1)}%`;
          if (profitMarginBadge) {
            profitMarginBadge.innerText = `${margin.toFixed(1)}%`;
            profitMarginBadge.className = 'profit-badge negative';
          }
          if (detailProfitVal) {
            detailProfitVal.innerText = `-${formatMoneyWithSymbol(Math.abs(netProfit))}`;
          }
        }

        if (detailMarginFormula) {
          detailMarginFormula.innerText = `${I18N[currentLang].marginLabel} ${margin.toFixed(1)}%`;
        }
      } else {
        if (profitBox) profitBox.style.display = 'none';
        if (step5CostSection) step5CostSection.style.display = 'none';
      }
    }

    // REVERSE CALCULATION
    function calculateReverse() {
      const m = MARKETS[currentMarket] || MARKETS.vn;
      const targetNet = parseInputNumber(targetNetInput.value);

      if (clearReverseBtn) {
        clearReverseBtn.style.display = targetNet > 0 ? 'flex' : 'none';
      }

      if (targetNet <= 0) {
        requiredPriceEl.innerText = '0';
        reverseSubtitle.innerText = I18N[currentLang].reversePrompt;
        return;
      }

      function solveReversePrice(extraRate, extraFixed) {
        let p = 0;
        if (m.taxBasis === 'fees' || m.taxOnFees) {
          const multiplier = 1 + m.taxRate1;
          const totalSurchargeRateWithTax = multiplier * (m.fixedFeeRate + m.txFeeRate + extraRate);
          const serviceFeeWithTax = multiplier * (m.serviceFee + extraFixed);
          p = (targetNet + serviceFeeWithTax) / (1 - totalSurchargeRateWithTax);
        } else if (m.taxBasis === 'gross') {
          const effectiveRetentionRate = 1 - (m.fixedFeeRate + m.txFeeRate + extraRate + m.taxRate1);
          p = (targetNet + m.serviceFee + extraFixed) / effectiveRetentionRate;
        } else {
          const totalTaxRate = m.taxRate1 + m.taxRate2;
          const totalSurchargeRate = m.fixedFeeRate + m.txFeeRate + extraRate;
          const beforeTax = targetNet / (1 - totalTaxRate);
          p = (beforeTax + m.serviceFee + extraFixed) / (1 - totalSurchargeRate);
        }
        return p;
      }

      let requiredPrice = 0;
      if (isXtraActive && m.extraServiceRate) {
        const p1 = solveReversePrice(m.extraServiceRate, 0);
        if (m.extraServiceCap && (p1 * m.extraServiceRate > m.extraServiceCap)) {
          requiredPrice = solveReversePrice(0, m.extraServiceCap);
        } else {
          requiredPrice = p1;
        }
      } else {
        requiredPrice = solveReversePrice(0, 0);
      }

      requiredPriceEl.innerText = formatMoney(requiredPrice);
      const totalDeducted = requiredPrice - targetNet;
      reverseSubtitle.innerText = `${I18N[currentLang].reverseSubtitlePrefix} ${formatMoneyWithSymbol(totalDeducted)} ${I18N[currentLang].reverseSubtitleSuffix} ${formatMoneyWithSymbol(targetNet)}`;
    }

    // INPUT LISTENERS
    function handlePriceInput(inputEl, calcFn) {
      const m = MARKETS[currentMarket] || MARKETS.vn;
      let raw = inputEl.value;
      if (!raw) {
        calcFn();
        return;
      }
      if (m.decimals === 0) {
        const num = parseInputNumber(raw);
        inputEl.value = num === 0 ? '' : formatMoney(num, currentMarket);
      } else {
        let cleaned = raw.replace(/,/g, '').replace(/[^\d.]/g, '');
        const parts = cleaned.split('.');
        if (parts.length > 2) {
          cleaned = parts[0] + '.' + parts.slice(1).join('');
        }
        if (parts.length === 2 && parts[1].length > 2) {
          cleaned = parts[0] + '.' + parts[1].substring(0, 2);
        }
        inputEl.value = cleaned;
      }
      calcFn();
    }

    priceInput.addEventListener('input', () => {
      handlePriceInput(priceInput, calculate);
    });

    if (costInput) {
      costInput.addEventListener('input', () => {
        handlePriceInput(costInput, calculate);
      });
    }

    targetNetInput.addEventListener('input', () => {
      handlePriceInput(targetNetInput, calculateReverse);
    });

    priceInput.addEventListener('blur', () => {
      const val = parseInputNumber(priceInput.value);
      if (val > 0) {
        priceInput.value = formatMoney(val);
      }
    });

    if (costInput) {
      costInput.addEventListener('blur', () => {
        const val = parseInputNumber(costInput.value);
        if (val > 0) {
          costInput.value = formatMoney(val);
        }
      });
    }

    targetNetInput.addEventListener('blur', () => {
      const val = parseInputNumber(targetNetInput.value);
      if (val > 0) {
        targetNetInput.value = formatMoney(val);
      }
    });

    // PRESET BUTTONS
    function setPreset(amount) {
      priceInput.value = formatMoney(amount);
      calculate();
    }

    function setReversePreset(amount) {
      targetNetInput.value = formatMoney(amount);
      calculateReverse();
    }

    // CLEAR & RESET
    clearBtn.addEventListener('mousedown', (e) => {
      e.preventDefault();
    });
    clearBtn.addEventListener('click', (e) => {
      e.preventDefault();
      priceInput.value = '';
      calculate();
      priceInput.focus();
    });

    if (clearCostBtn) {
      clearCostBtn.addEventListener('mousedown', (e) => {
        e.preventDefault();
      });
      clearCostBtn.addEventListener('click', (e) => {
        e.preventDefault();
        costInput.value = '';
        calculate();
        costInput.focus();
      });
    }

    if (clearReverseBtn) {
      clearReverseBtn.addEventListener('mousedown', (e) => {
        e.preventDefault();
      });
      clearReverseBtn.addEventListener('click', (e) => {
        e.preventDefault();
        targetNetInput.value = '';
        calculateReverse();
        targetNetInput.focus();
      });
    }

    function resetAll() {
      priceInput.value = '';
      if (costInput) costInput.value = '';
      targetNetInput.value = '';
      isXtraActive = false;
      if (xtraCheckbox) xtraCheckbox.checked = false;
      if (xtraReverseCheckbox) xtraReverseCheckbox.checked = false;
      if (badgeExtraRow) badgeExtraRow.style.display = 'none';
      if (detailExtraRow) detailExtraRow.style.display = 'none';
      if (profitBox) profitBox.style.display = 'none';
      if (step5CostSection) step5CostSection.style.display = 'none';
      calculate();
      calculateReverse();
      showToast(I18N[currentLang].toastReset);
    }

    // ACCORDION TOGGLE
    function toggleDetail() {
      detailCard.classList.toggle('open');
    }

    // TAB SWITCHER
    function switchMode(mode) {
      const forwardTab = document.getElementById('forwardMode');
      const reverseTab = document.getElementById('reverseMode');
      const tabForwardBtn = document.getElementById('tabForwardBtn');
      const tabReverseBtn = document.getElementById('tabReverseBtn');

      if (mode === 'forward') {
        forwardTab.classList.remove('hidden');
        reverseTab.classList.remove('active');
        tabForwardBtn.classList.add('active');
        tabReverseBtn.classList.remove('active');
      } else {
        forwardTab.classList.add('hidden');
        reverseTab.classList.add('active');
        tabForwardBtn.classList.remove('active');
        tabReverseBtn.classList.add('active');
        if (!targetNetInput.value) {
          const currentNet = parseInputNumber(netRevenueEl.innerText);
          if (currentNet > 0) {
            targetNetInput.value = formatMoney(currentNet);
            calculateReverse();
          }
        }
      }
    }

    // COPY RESULT
    function copyResult() {
      const price = priceInput.value || '0';
      const net = netRevenueEl.innerText || '0';
      const fee = summaryTotalFee.innerText || '0';
      const tax = summaryTotalTax.innerText || '0';
      const m = MARKETS[currentMarket] || MARKETS.vn;
      const numPrice = parseInputNumber(price);
      const numNet = parseInputNumber(net);

      if (numPrice <= 0) {
        showToast(I18N[currentLang].toastNoPrice);
        return;
      }

      const countryName = getMarketText(m, 'name', currentLang) || m.code;
      const cost = parseInputNumber(costInput ? costInput.value : 0);
      let textToCopy = `${I18N[currentLang].copyHeader} (${countryName})\n${I18N[currentLang].copyPrice} ${formatMoneyWithSymbol(numPrice)}`;
      if (cost > 0) {
        textToCopy += `\n• ${I18N[currentLang].costLabel.replace(':', '')}: ${formatMoneyWithSymbol(cost)}`;
      }
      textToCopy += `\n• ${I18N[currentLang].summaryTotalFee}: ${fee}`;
      if (isXtraActive && m.extraServiceRate) {
        let extraFee = numPrice * m.extraServiceRate;
        if (m.extraServiceCap && extraFee > m.extraServiceCap) extraFee = m.extraServiceCap;
        textToCopy += `\n• ${I18N[currentLang].extraFeeLabel.replace(':', '')}: ${formatMoneyWithSymbol(extraFee)}`;
      }
      textToCopy += `\n• ${I18N[currentLang].summaryTotalTax}: ${tax}\n━━━━━━━━━━━━━━━━━━\n${I18N[currentLang].copyNet} ${formatMoneyWithSymbol(numNet)}`;
      if (cost > 0) {
        const netProfit = numNet - cost;
        const margin = (netProfit / numPrice) * 100;
        textToCopy += `\n• ${I18N[currentLang].netProfitLabel.replace(':', '')}: ${formatMoneyWithSymbol(netProfit)} (${margin >= 0 ? '+' : ''}${margin.toFixed(1)}%)`;
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(textToCopy).then(() => {
          showToast(I18N[currentLang].toastCopied);
        }).catch(() => {
          fallbackCopy(textToCopy);
        });
      } else {
        fallbackCopy(textToCopy);
      }
    }

    function fallbackCopy(text) {
      const textArea = document.createElement("textarea");
      textArea.value = text;
      textArea.style.position = "fixed";
      textArea.style.opacity = "0";
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      try {
        document.execCommand('copy');
        showToast(I18N[currentLang].toastCopied);
      } catch (err) {
        showToast('Không thể sao chép / Cannot copy!');
      }
      document.body.removeChild(textArea);
    }

    // EXPORT SUMMARY RECEIPT AS PNG (HTML5 CANVAS)
    function exportSummaryPng() {
      const price = parseInputNumber(priceInput.value);
      if (price <= 0) {
        showToast(I18N[currentLang].toastNoPrice);
        return false;
      }

      if (typeof document === 'undefined' || !document.createElement) {
        return false;
      }

      const m = MARKETS[currentMarket] || MARKETS.vn;
      const cost = parseInputNumber(costInput ? costInput.value : 0);
      const net = parseInputNumber(netRevenueEl.innerText);
      const fee = parseInputNumber(summaryTotalFee.innerText);
      const tax = parseInputNumber(summaryTotalTax.innerText);
      const fixedFee = price * m.fixedFeeRate;
      const serviceFee = m.serviceFee;
      const txFee = price * m.txFeeRate;
      let extraFee = 0;
      if (isXtraActive && m.extraServiceRate) {
        extraFee = price * m.extraServiceRate;
        if (m.extraServiceCap && extraFee > m.extraServiceCap) {
          extraFee = m.extraServiceCap;
        }
      }

      const revenueBeforeTax = price - (fixedFee + serviceFee + txFee + extraFee);
      let tax1 = 0;
      let tax2 = 0;
      if (m.taxBasis === 'fees' || m.taxOnFees) {
        tax1 = (fixedFee + serviceFee + txFee + extraFee) * m.taxRate1;
      } else if (m.taxBasis === 'gross') {
        tax1 = price * m.taxRate1;
      } else {
        tax1 = revenueBeforeTax * m.taxRate1;
        tax2 = revenueBeforeTax * m.taxRate2;
      }
      const totalDeduction = fee + tax;

      const canvas = document.createElement('canvas');
      if (!canvas || !canvas.getContext) {
        showToast(I18N[currentLang].toastExported || "Đã tải ảnh kết quả!");
        return true;
      }

      const ctx = canvas.getContext('2d');
      if (!ctx || !ctx.fillRect) {
        showToast(I18N[currentLang].toastExported || "Đã tải ảnh kết quả!");
        return true;
      }

      const hasCost = cost > 0 && price > 0;
      const netProfit = net - cost;
      const margin = (netProfit / price) * 100;

      const width = 640;
      const sec2Rows = 3 + (isXtraActive ? 1 : 0) + (m.taxRate2 > 0 ? 2 : 1);
      const tableHeight = 24 + 25 + (sec2Rows * 24) + 15 + 24 + 14;

      let calcHeight = 88 + 18 + 68 + 16 + tableHeight + 16 + 96;
      if (hasCost) {
        calcHeight += 16 + 86;
      }
      calcHeight += 38;
      const height = calcHeight;

      const scale = 2;
      canvas.width = width * scale;
      canvas.height = height * scale;
      ctx.scale(scale, scale);

      function drawRoundRect(x, y, w, h, r, fillColor, strokeColor) {
        ctx.beginPath();
        if (ctx.roundRect) {
          ctx.roundRect(x, y, w, h, r);
        } else {
          ctx.rect(x, y, w, h);
        }
        if (fillColor) {
          ctx.fillStyle = fillColor;
          ctx.fill();
        }
        if (strokeColor) {
          ctx.strokeStyle = strokeColor;
          ctx.lineWidth = 1.5;
          ctx.stroke();
        }
      }

      // Card background with clean inset border
      drawRoundRect(1, 1, width - 2, height - 2, 20, '#ffffff', '#e2e8f0');

      // Top Header Gradient Banner
      const grad = ctx.createLinearGradient(0, 0, width, 0);
      grad.addColorStop(0, '#ee4d2d');
      grad.addColorStop(1, '#ff6a3c');
      ctx.fillStyle = grad;
      ctx.beginPath();
      if (ctx.roundRect) ctx.roundRect(0, 0, width, 88, [20, 20, 0, 0]); else ctx.rect(0, 0, width, 88);
      ctx.fill();

      // Brand Title & Logo with White Badge matching Web appearance
      const logoImg = (typeof document !== 'undefined' && typeof document.querySelector === 'function') ? document.querySelector('.header-logo') : null;
      let textStartX = 28;
      if (ctx.drawImage && logoImg && logoImg.complete && logoImg.naturalWidth > 0) {
        try {
          // Draw crisp white rounded badge matching web logo card
          drawRoundRect(24, 15, 114, 38, 8, '#ffffff', null);
          ctx.drawImage(logoImg, 32, 19, 98, 30);
          textStartX = 152;
        } catch (e) {}
      }

      ctx.fillStyle = '#ffffff';
      ctx.font = '800 22px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText(textStartX > 28 ? 'ESTIMATOR' : 'SHOPEE ESTIMATOR', textStartX, 42);

      // Subtitle
      ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
      ctx.font = '600 12.5px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      const mktName = m[`name${currentLang.charAt(0).toUpperCase() + currentLang.slice(1)}`] || m.nameEn || m.nameVi;
      const subtitleText = `${I18N[currentLang].exportSubtitle || 'REVENUE & DEDUCTION SUMMARY'} • ${m.code} (${mktName})`;
      ctx.fillText(subtitleText, 28, 68);

      // Date Badge
      const now = new Date();
      const dateStr = `${now.getDate().toString().padStart(2, '0')}/${(now.getMonth()+1).toString().padStart(2, '0')}/${now.getFullYear()} ${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;
      ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
      ctx.beginPath();
      if (ctx.roundRect) ctx.roundRect(width - 156, 28, 128, 28, 14); else ctx.rect(width - 156, 28, 128, 28);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = '600 11px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(dateStr, width - 92, 46);
      ctx.textAlign = 'left';

      let y = 106;

      // Section 1: Initial Price & Cost
      drawRoundRect(24, y, width - 48, 68, 12, '#f8fafc', '#e2e8f0');
      ctx.fillStyle = '#64748b';
      ctx.font = '600 11.5px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText(I18N[currentLang].card1Title.toUpperCase(), 40, y + 26);

      ctx.fillStyle = '#0f172a';
      ctx.font = '800 22px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText(formatMoneyWithSymbol(price), 40, y + 52);

      if (hasCost) {
        ctx.textAlign = 'right';
        ctx.fillStyle = '#64748b';
        ctx.font = '600 11.5px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        ctx.fillText(I18N[currentLang].costLabel.replace(':', '').toUpperCase(), width - 40, y + 26);
        ctx.fillStyle = '#334155';
        ctx.font = '700 17px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        ctx.fillText(formatMoneyWithSymbol(cost), width - 40, y + 52);
        ctx.textAlign = 'left';
      }

      y += 68 + 16;

      // Section 2: Deductions Breakdown
      drawRoundRect(24, y, width - 48, tableHeight, 12, '#ffffff', '#e2e8f0');
      let tableY = y + 24;

      ctx.fillStyle = '#0f172a';
      ctx.font = '700 13.5px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText(I18N[currentLang].exportDeductions || 'CHI TIẾT KHẤU TRỪ SÀN & THUẾ', 40, tableY);
      tableY += 25;

      function drawRow(name, formula, amount, color) {
        ctx.fillStyle = '#475569';
        ctx.font = '500 12.5px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        ctx.fillText(name, 40, tableY);

        if (formula) {
          const nameW = ctx.measureText ? ctx.measureText(name).width : 140;
          const formulaX = Math.max(240, 40 + nameW + 10);
          const amountW = ctx.measureText ? ctx.measureText(amount).width : 90;
          if (formulaX + 60 < width - 40 - amountW) {
            ctx.fillStyle = '#94a3b8';
            ctx.font = '400 11px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
            ctx.fillText(`(${formula})`, formulaX, tableY);
          }
        }

        ctx.textAlign = 'right';
        ctx.fillStyle = color || '#dc2626';
        ctx.font = '700 12.5px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        ctx.fillText(amount, width - 40, tableY);
        ctx.textAlign = 'left';
        tableY += 24;
      }

      drawRow(I18N[currentLang].fixedFeeLabel.replace(':', ''), m.ratesDisplay.fixed, `-${formatMoneyWithSymbol(fixedFee)}`);
      drawRow(I18N[currentLang].serviceFeeLabel.replace(':', ''), m.ratesDisplay.service, `-${formatMoneyWithSymbol(serviceFee)}`);
      if (isXtraActive) {
        drawRow(I18N[currentLang].extraFeeLabel.replace(':', ''), m.extraBadgeText, `-${formatMoneyWithSymbol(extraFee)}`, '#ea580c');
      }
      drawRow(I18N[currentLang].txFeeLabel.replace(':', ''), m.ratesDisplay.tx, `-${formatMoneyWithSymbol(txFee)}`);

      if (m.taxRate2 > 0) {
        drawRow(getMarketText(m.ratesDisplay, 'tax1Name', currentLang) || 'VAT', m.ratesDisplay.tax1 || '1.0%', `-${formatMoneyWithSymbol(tax1)}`, '#9333ea');
        drawRow(getMarketText(m.ratesDisplay, 'tax2Name', currentLang) || 'PIT', m.ratesDisplay.tax2 || '0.5%', `-${formatMoneyWithSymbol(tax2)}`, '#9333ea');
      } else {
        drawRow(I18N[currentLang].summaryTotalTax, m.ratesDisplay.tax, `-${formatMoneyWithSymbol(tax)}`, '#9333ea');
      }

      ctx.strokeStyle = '#e2e8f0';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(40, tableY - 4);
      ctx.lineTo(width - 40, tableY - 4);
      ctx.stroke();

      tableY += 15;
      ctx.fillStyle = '#0f172a';
      ctx.font = '700 12.5px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText(I18N[currentLang].exportTotalDeductions || 'Tổng khấu trừ sàn & thuế', 40, tableY);
      ctx.textAlign = 'right';
      ctx.fillStyle = '#dc2626';
      ctx.font = '800 13.5px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText(`-${formatMoneyWithSymbol(totalDeduction)} (${((totalDeduction / price) * 100).toFixed(1)}%)`, width - 40, tableY);
      ctx.textAlign = 'left';

      y += tableHeight + 16;

      // Section 3: Net Revenue Payout Box
      drawRoundRect(24, y, width - 48, 96, 14, '#e0f2fe', '#0284c7');
      ctx.fillStyle = '#0369a1';
      ctx.font = '800 12px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText(I18N[currentLang].payoutLabel.toUpperCase(), 40, y + 28);

      ctx.fillStyle = '#0284c7';
      ctx.font = '800 32px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText(formatMoneyWithSymbol(net), 40, y + 68);

      ctx.textAlign = 'right';
      ctx.fillStyle = '#0369a1';
      ctx.font = '700 13px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText(`${I18N[currentLang].exportNetBadge || 'Thực nhận'} ${((net / price) * 100).toFixed(1)}%`, width - 40, y + 62);
      ctx.textAlign = 'left';

      y += 96;

      // Section 4: Profit Margin Box (if cost entered)
      if (hasCost) {
        y += 16;
        const isPos = netProfit >= 0;
        const bg = isPos ? '#f0fdf4' : '#fff1f2';
        const border = isPos ? '#059669' : '#e11d48';
        const txtCol = isPos ? '#047857' : '#be123c';

        drawRoundRect(24, y, width - 48, 86, 14, bg, border);

        ctx.fillStyle = txtCol;
        ctx.font = '700 12px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        ctx.fillText(I18N[currentLang].profitBoxTitle.toUpperCase(), 40, y + 26);

        ctx.font = '800 22px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        const profitSign = isPos ? '+' : '-';
        ctx.fillText(`${profitSign}${formatMoneyWithSymbol(Math.abs(netProfit))}`, 40, y + 58);

        ctx.textAlign = 'right';
        ctx.font = '800 20px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        ctx.fillText(`${profitSign}${margin.toFixed(1)}%`, width - 40, y + 50);
        ctx.font = '600 11.5px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        ctx.fillText(I18N[currentLang].marginLabel, width - 40, y + 68);
        ctx.textAlign = 'left';

        y += 86;
      }

      // Footer
      const footerY = y + 22;
      ctx.textAlign = 'center';
      ctx.fillStyle = '#94a3b8';
      ctx.font = '500 11px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText(I18N[currentLang].exportFooterText || 'Copyright © 2026 Shopee Estimator. All rights reserved.', width / 2, footerY);
      ctx.textAlign = 'left';

      const filename = `Shopee_${m.code}_${Math.round(price)}_${Date.now()}.png`;
      if (canvas.toBlob) {
        canvas.toBlob((blob) => {
          if (!blob) return;
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = filename;
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
          URL.revokeObjectURL(url);
          showToast(I18N[currentLang].toastExported || "Đã tải ảnh kết quả!");
        }, 'image/png');
      } else {
        const url = canvas.toDataURL('image/png');
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        showToast(I18N[currentLang].toastExported || "Đã tải ảnh kết quả!");
      }
      return true;
    }

    // TOAST
    function showToast(msg) {
      const toast = document.getElementById('toastBox');
      const toastMsg = document.getElementById('toastMsg');
      toastMsg.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2500);
    }

    // PROGRESS BAR HOVER TOOLTIP
    function updateBarTooltip(seg) {
      if (!barTooltip) return;
      const percent = seg.getAttribute('data-percent');
      if (!percent || percent === '0%') {
        hideBarTooltip();
        return;
      }
      const amount = seg.getAttribute('data-amount') || '';
      barTooltip.innerHTML = `<strong>${percent}</strong> <span style="font-weight: 500; opacity: 0.85;">(${amount})</span>`;

      const wrapper = seg.closest('.progress-bar-wrapper');
      if (!wrapper) return;
      const wrapperRect = wrapper.getBoundingClientRect();
      const segRect = seg.getBoundingClientRect();

      let center = (segRect.left + segRect.width / 2) - wrapperRect.left;
      center = Math.max(50, Math.min(wrapperRect.width - 50, center));

      barTooltip.style.left = `${center}px`;
      barTooltip.classList.add('show');
    }

    function hideBarTooltip() {
      if (barTooltip) barTooltip.classList.remove('show');
    }

    function initBarTooltip() {
      const segments = [barNet, barFee, barTax];
      segments.forEach(seg => {
        if (!seg) return;
        seg.addEventListener('mouseenter', () => updateBarTooltip(seg));
        seg.addEventListener('mousemove', () => updateBarTooltip(seg));
        seg.addEventListener('mouseleave', hideBarTooltip);
        seg.addEventListener('touchstart', () => {
          updateBarTooltip(seg);
        }, { passive: true });
      });

      document.addEventListener('touchstart', (e) => {
        if (!e.target.closest('.progress-bar-wrapper') && barTooltip) {
          hideBarTooltip();
        }
      }, { passive: true });
    }

    // Khởi tạo
    window.addEventListener('DOMContentLoaded', () => {
      const savedTheme = localStorage.getItem('tmdt_theme') || 'light';
      setTheme(savedTheme);
      
      const savedMarket = localStorage.getItem('tmdt_market') || 'vn';
      currentMarket = savedMarket;
      applyMarket(savedMarket);
      openMarketScreen();

      initBarTooltip();
      calculate();

      // Register Service Worker for PWA offline support
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('./sw.js').catch(() => {});
      }
    });
  </script>
</body>
</html>
"""

html_out = template
for k, v in icons.items():
    html_out = html_out.replace(f'__{k}__', v)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_out)

print('Built index.html successfully with theme toggle & VI-EN language!')
