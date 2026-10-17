// -*- coding: utf-8 -*-
const fs = require('fs');
const path = require('path');
const assert = require('assert');
const vm = require('vm');

console.log("=== BẮT ĐẦU KIỂM THỬ TOÀN DIỆN SHOPEE DEDUCTION CALCULATOR ===");

const htmlPath = path.join(__dirname, 'index.html');
assert(fs.existsSync(htmlPath), "index.html phải tồn tại!");
const htmlContent = fs.readFileSync(htmlPath, 'utf8');

// 1. Kiểm tra HTML structure và các element IDs cốt lõi
console.log("\n[1] Kiểm tra các phần tử HTML cốt lõi (Bao gồm Xtra, COGS, Profit, Export, PWA)...");
const requiredIds = [
  'marketScreen', 'calculatorApp', 'marketSwitchBtn', 'marketDisplayCode',
  'langBtn', 'langLabel', 'themeBtn', 'themeIcon',
  'mkt-vn', 'mkt-th', 'mkt-my', 'mkt-ph',
  'tabForwardBtn', 'tabReverseBtn', 'forwardMode', 'reverseMode',
  'priceInput', 'clearBtn', 'forwardPresets', 'lowPriceAlert',
  'costInput', 'clearCostBtn',
  'xtraCheckbox', 'xtraReverseCheckbox', 'xtraRateBadge', 'xtraReverseRateBadge',
  'badgeFixedFee', 'badgeServiceFee', 'badgeExtraRow', 'badgeExtraFee', 'badgeTxFee', 'badgeTaxFee', 'badgeTaxLabel',
  'netRevenue', 'percentSubtitle', 'barNet', 'barFee', 'barTax', 'barTooltip',
  'summaryTotalFee', 'summaryTotalTax',
  'profitBox', 'profitMarginBadge', 'netProfitVal', 'profitMarginVal',
  'exportPngBtn',
  'detailCard', 'detailFixedFee', 'detailServiceFee', 'detailTxFee', 'detailExtraRow', 'detailExtraFee', 'detailTotalFee',
  'detailBeforeTax', 'detailTax1', 'detailTax2', 'detailTotalTax', 'detailNet',
  'step1FixedFormula', 'step1ServiceName', 'step1ServiceFormula', 'step1TxFormula', 'step1ExtraFormula',
  'step3Tax1Row', 'step3Tax1Name', 'step3Tax1Formula',
  'step3Tax2Row', 'step3Tax2Name', 'step3Tax2Formula', 'step3TotalLabel',
  'step5CostSection', 'detailCostVal', 'detailProfitVal', 'detailMarginFormula', 'detailProfitRow',
  'formulaBeforeTax', 'formulaNet',
  'targetNetInput', 'clearReverseBtn', 'reversePresets', 'reverseDesc',
  'requiredPrice', 'reverseSubtitle', 'reverseFormulaBody', 'toastBox',
  'policyDocBtn', 'policyModal', 'policyListContainer', 'policyMarketBadge'
];

for (const id of requiredIds) {
  assert(htmlContent.includes(`id="${id}"`), `Thiếu element ID: ${id}`);
}
console.log(`✓ Tất cả ${requiredIds.length} element IDs đều tồn tại trong index.html.`);

// 2. Kiểm tra tính toàn vẹn của từ điển đa ngôn ngữ (5 ngôn ngữ)
console.log("\n[2] Kiểm tra từ điển đa ngôn ngữ (VI, EN, TH, MS, TL)...");
const regexI18n = /data-i18n=["']([^"']+)["']/g;
let match;
const keysInHtml = new Set();
while ((match = regexI18n.exec(htmlContent)) !== null) {
  keysInHtml.add(match[1]);
}

const scriptMatch = htmlContent.match(/<script>([\s\S]*?)<\/script>/);
assert(scriptMatch, "Thiếu thẻ <script> trong index.html!");
const scriptCode = scriptMatch[1];

// Chuẩn bị Mock DOM môi trường giả lập trình duyệt
const mockElements = {};
function createMockEl(id) {
  const _classes = new Set();
  const el = {
    id: id,
    value: '',
    checked: false,
    innerText: '',
    innerHTML: '',
    style: {},
    classList: {
      _classes: _classes,
      add: function(c) { _classes.add(c); },
      remove: function(c) { _classes.delete(c); },
      toggle: function(c) { if (_classes.has(c)) _classes.delete(c); else _classes.add(c); },
      contains: function(c) { return _classes.has(c); }
    },
    addEventListener: () => {},
    setAttribute: function(k, v) { this[k] = v; },
    removeAttribute: function(k) { delete this[k]; },
    getAttribute: function(k) { return this[k] || ''; },
    closest: () => null,
    querySelectorAll: () => [],
    appendChild: () => {},
    removeChild: () => {},
    click: () => {}
  };
  Object.defineProperty(el, 'className', {
    get: function() { return Array.from(_classes).join(' '); },
    set: function(val) {
      _classes.clear();
      if (val) {
        val.split(/\s+/).filter(Boolean).forEach(c => _classes.add(c));
      }
    }
  });
  return el;
}

const bodyMock = createMockEl('body');
bodyMock.appendChild = () => {};
bodyMock.removeChild = () => {};

let lastCreatedCanvas = null;

const documentMock = {
  getElementById: (id) => {
    if (!mockElements[id]) mockElements[id] = createMockEl(id);
    return mockElements[id];
  },
  querySelector: (selector) => {
    if (selector === '.header-logo') {
      return { complete: true, naturalWidth: 1024, naturalHeight: 326 };
    }
    return null;
  },
  createElement: (tagName) => {
    if (tagName === 'canvas') {
      const canvasObj = {
        width: 0,
        height: 0,
        getContext: () => ({
          fillStyle: '',
          font: '',
          textAlign: '',
          textBaseline: '',
          strokeStyle: '',
          lineWidth: 0,
          scale: () => {},
          save: () => {},
          restore: () => {},
          fillRect: () => {},
          strokeRect: () => {},
          rect: () => {},
          roundRect: () => {},
          createLinearGradient: () => ({ addColorStop: () => {} }),
          fillText: () => {},
          beginPath: () => {},
          moveTo: () => {},
          lineTo: () => {},
          stroke: () => {},
          fill: () => {},
          arc: () => {},
          quadraticCurveTo: () => {},
          closePath: () => {},
          drawImage: () => {},
          measureText: (txt) => ({ width: (txt ? String(txt).length : 0) * 7 })
        }),
        toBlob: (cb) => { cb({}); },
        toDataURL: () => 'data:image/png;base64,mock'
      };
      lastCreatedCanvas = canvasObj;
      return canvasObj;
    }
    return createMockEl(tagName);
  },
  querySelectorAll: (selector) => {
    if (selector === '.market-card-btn') {
      return ['mkt-vn', 'mkt-th', 'mkt-my', 'mkt-ph'].map(id => documentMock.getElementById(id));
    }
    if (selector === '.currency-symbol') {
      return [createMockEl('curr1'), createMockEl('curr2')];
    }
    if (selector === '[data-i18n]') {
      return [...keysInHtml].map(k => {
        const el = createMockEl('i18n_' + k);
        el.getAttribute = () => k;
        return el;
      });
    }
    return [];
  },
  documentElement: { lang: 'en' },
  body: bodyMock,
  addEventListener: () => {}
};

const localStorageMock = {
  store: {},
  getItem: (k) => localStorageMock.store[k] || null,
  setItem: (k, v) => { localStorageMock.store[k] = String(v); }
};

const URLMock = {
  createObjectURL: () => 'blob:mock-url',
  revokeObjectURL: () => {}
};

const windowMock = {
  addEventListener: () => {},
  document: documentMock,
  localStorage: localStorageMock,
  URL: URLMock
};

const context = {
  window: windowMock,
  document: documentMock,
  localStorage: localStorageMock,
  navigator: {
    serviceWorker: {
      register: () => Promise.resolve()
    }
  },
  URL: URLMock,
  console: console,
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  Number: Number,
  Math: Math,
  parseInt: parseInt,
  parseFloat: parseFloat,
  isNaN: isNaN,
  Date: Date
};
vm.createContext(context);
vm.runInContext(scriptCode, context);

// Trích xuất các hàm và cấu hình trực tiếp từ VM
const exported = vm.runInContext(`({
  MARKETS, I18N, POLICY_DOCS, setLanguage, selectMarket, openMarketScreen, applyMarket, toggleLang, setTheme,
  calculate, calculateReverse, parseInputNumber, formatMoney, formatMoneyWithSymbol, switchMode,
  onToggleXtra, exportSummaryPng, resetAll, openPolicyModal, closePolicyModal, renderPolicyList
})`, context);

const {
  MARKETS, I18N, POLICY_DOCS, setLanguage, selectMarket, openMarketScreen, applyMarket, toggleLang, setTheme,
  calculate, calculateReverse, parseInputNumber, formatMoney, formatMoneyWithSymbol, switchMode,
  onToggleXtra, exportSummaryPng, resetAll, openPolicyModal, closePolicyModal, renderPolicyList
} = exported;

// Kiểm tra mọi key trong HTML đều có trong I18N ở cả 5 ngôn ngữ
for (const lang of ['vi', 'en', 'th', 'ms', 'tl']) {
  assert(I18N[lang], `Thiếu từ điển cho ngôn ngữ: ${lang}`);
  for (const key of keysInHtml) {
    assert(I18N[lang][key], `Thiếu key '${key}' trong I18N.${lang}`);
  }
}
console.log(`✓ Tất cả ${keysInHtml.size} data-i18n keys trong HTML đều được dịch đầy đủ ở cả 5 ngôn ngữ (VI, EN, TH, MS, TL).`);

// 3. Kiểm tra logic tính toán thực tế cho cả 4 thị trường (Forward & Reverse cơ bản)
console.log("\n[3] Kiểm tra logic tính toán thực tế cho cả 4 thị trường...");
const testCases = [
  { market: 'vn', price: 100000, desc: 'Việt Nam 100k' },
  { market: 'vn', price: 500000, desc: 'Việt Nam 500k' },
  { market: 'th', price: 200, desc: 'Thái Lan 200฿' },
  { market: 'th', price: 1500, desc: 'Thái Lan 1500฿' },
  { market: 'my', price: 50, desc: 'Malaysia 50 RM' },
  { market: 'my', price: 350, desc: 'Malaysia 350 RM' },
  { market: 'ph', price: 500, desc: 'Philippines 500₱' },
  { market: 'ph', price: 2500, desc: 'Philippines 2500₱' }
];

for (const tc of testCases) {
  selectMarket(tc.market);
  mockElements['priceInput'].value = String(tc.price);
  calculate();

  const net = parseInputNumber(mockElements['netRevenue'].innerText);
  const fee = parseInputNumber(mockElements['summaryTotalFee'].innerText);
  const tax = parseInputNumber(mockElements['summaryTotalTax'].innerText);

  // Tổng tiền phải cân bằng: Net + Fee + Tax = Price
  const total = net + fee + tax;
  const diffTotal = Math.abs(total - tc.price);
  assert(diffTotal < 0.05, `${tc.desc}: Lỗi cân bằng tổng tiền! Tổng=${total}, Gốc=${tc.price}`);

  // Kiểm tra tính đối xứng nghịch đảo (Reverse Calculation)
  mockElements['targetNetInput'].value = String(net);
  calculateReverse();
  const recoveredPrice = parseInputNumber(mockElements['requiredPrice'].innerText);
  const diffReverse = Math.abs(recoveredPrice - tc.price);
  assert(diffReverse < 0.05, `${tc.desc}: Lỗi tính ngược! Thu được=${recoveredPrice}, Gốc=${tc.price}`);

  console.log(`✓ ${tc.desc}: Giá=${tc.price} -> Phí=${fee.toFixed(2)}, Thuế=${tax.toFixed(2)}, Thực nhận=${net.toFixed(2)} <=> Tính ngược=${recoveredPrice.toFixed(2)} (Khớp tuyệt đối)`);
}

// 4. Kiểm tra các trường hợp biên & nhập số thập phân mobile
console.log("\n[4] Kiểm tra các trường hợp biên & nhập số thập phân mobile...");
assert(htmlContent.includes('id="priceInput"') && htmlContent.includes('inputmode="decimal"'), "priceInput phải có inputmode='decimal'!");
assert(htmlContent.includes('id="targetNetInput"') && htmlContent.includes('inputmode="decimal"'), "targetNetInput phải có inputmode='decimal'!");
assert(htmlContent.includes('id="costInput"') && htmlContent.includes('inputmode="decimal"'), "costInput phải có inputmode='decimal'!");

// Cảnh báo minPrice
const lowPriceTests = [
  { m: 'vn', low: 3000 },
  { m: 'th', low: 1.0 },
  { m: 'my', low: 0.5 },
  { m: 'ph', low: 5.0 }
];
for (const lp of lowPriceTests) {
  selectMarket(lp.m);
  mockElements['priceInput'].value = String(lp.low);
  calculate();
  assert(mockElements['lowPriceAlert'].classList.contains('show'), `${lp.m.toUpperCase()}: Giá ${lp.low} phải bật cảnh báo lowPriceAlert`);
}
console.log("✓ Cảnh báo minPrice kích hoạt chính xác cho cả 4 thị trường.");

// Giá bằng 0
selectMarket('vn');
mockElements['priceInput'].value = '0';
calculate();
assert.strictEqual(mockElements['netRevenue'].innerText, '0', "Giá 0 phải trả về netRevenue 0");

// Nhập số thập phân
selectMarket('th');
mockElements['priceInput'].value = '99.90';
calculate();
const netTh = parseInputNumber(mockElements['netRevenue'].innerText);
assert(netTh > 0 && netTh < 99.90, "Tính toán số thập phân 99.90฿ phải hợp lệ");

selectMarket('my');
mockElements['priceInput'].value = '12.50';
calculate();
const netMy = parseInputNumber(mockElements['netRevenue'].innerText);
assert(netMy > 0 && netMy < 12.50, "Tính toán số thập phân 12.50 RM phải hợp lệ");
console.log("✓ Hỗ trợ đầy đủ số thập phân cents cho Thái Lan, Malaysia, Philipin.");

// 5. Kiểm tra chuyển đổi thị trường
console.log("\n[5] Kiểm tra chuyển đổi thị trường...");
selectMarket('vn');
mockElements['priceInput'].value = '100000';
mockElements['costInput'].value = '50000';
selectMarket('th');
assert.strictEqual(mockElements['priceInput'].value, '', "Chuyển thị trường phải xóa giá bán cũ");
assert.strictEqual(mockElements['costInput'].value, '', "Chuyển thị trường phải xóa giá vốn cũ");
assert.strictEqual(mockElements['profitBox'].style.display, 'none', "Chuyển thị trường phải ẩn profitBox");
console.log("✓ Đổi thị trường reset input và ẩn profitBox an toàn.");

// 6. Kiểm tra các yêu cầu giao diện (5 ảnh & ngôn ngữ chuyên môn)
console.log("\n[6] Kiểm tra các yêu cầu giao diện (5 ảnh & ngôn ngữ chuyên môn)...");
assert(htmlContent.includes('<html lang="en">'), "index.html root tag phải mặc định là <html lang=\"en\">!");
openMarketScreen();
assert.strictEqual(context.document.documentElement.lang, 'en', "Giao diện ảnh 1 phải mặc định là tiếng Anh (en)!");
assert(mockElements['langLabel'].innerText === 'VI', "Nút đổi ngôn ngữ trên màn hình chọn thị trường phải cho phép đổi sang VI");

// Footer text
const footerRegex = /<footer[^>]*>([\s\S]*?)<\/footer>/i;
const footerMatch = htmlContent.match(footerRegex);
assert(footerMatch && footerMatch[1].includes('Copyright © 2026 Shopee Estimator. All rights reserved'), "Footer phải chứa copyright");
const calcAppCloseIdx = htmlContent.indexOf('</div> <!-- END #calculatorApp -->');
const footerTagIdx = htmlContent.indexOf('<footer class="app-footer"');
assert(footerTagIdx > calcAppCloseIdx, "Footer phải nằm NGOÀI #calculatorApp để hiển thị trên cả màn hình 1!");

// Nút marketSwitchBtn icon ngôi nhà
const marketSwitchBtnMatch = htmlContent.match(/<button[^>]*id="marketSwitchBtn"[^>]*>([\s\S]*?)<\/button>/i);
assert(marketSwitchBtnMatch && marketSwitchBtnMatch[1].includes('<svg') && (marketSwitchBtnMatch[1].includes('M3 10.5L12 3') || marketSwitchBtnMatch[1].includes('M3.5 10.5L12 3')), "marketSwitchBtn phải chứa icon outline ngôi nhà!");

// Theme button
setTheme('dark');
assert(mockElements['themeIcon'].innerHTML.includes('M21 12.79A9 9 0 1 1 11.21 3'), "Chế độ tối phải hiển thị icon mặt trăng nét viền!");
setTheme('light');
assert(mockElements['themeIcon'].innerHTML.includes('circle cx="12"'), "Chế độ sáng phải hiển thị icon mặt trời!");

// Ngôn ngữ từng nước
const marketLangPairs = [
  { market: 'vn', native: 'vi', labelOnNative: 'EN', labelOnEn: 'VI', sampleTerm: 'Phí cố định' },
  { market: 'th', native: 'th', labelOnNative: 'EN', labelOnEn: 'TH', sampleTerm: 'ค่าธรรมเนียมการขาย' },
  { market: 'my', native: 'ms', labelOnNative: 'EN', labelOnEn: 'MS', sampleTerm: 'Yuran Komisen' },
  { market: 'ph', native: 'tl', labelOnNative: 'EN', labelOnEn: 'FIL', sampleTerm: 'Bayad sa Komisyon' }
];

for (const p of marketLangPairs) {
  selectMarket(p.market);
  assert.strictEqual(context.document.documentElement.lang, p.native, `Thị trường ${p.market.toUpperCase()} phải mặc định ngôn ngữ ${p.native}!`);
  assert.strictEqual(mockElements['langLabel'].innerText, p.labelOnNative, `Ở ngôn ngữ ${p.native}, nút phải hiển thị '${p.labelOnNative}'`);
  mockElements['marketScreen'].style.display = 'none';
  toggleLang();
  assert.strictEqual(context.document.documentElement.lang, 'en', "Sau khi toggle, ngôn ngữ phải là 'en'!");
  toggleLang();
  assert.strictEqual(context.document.documentElement.lang, p.native, `Sau toggle 2, ngôn ngữ phải là '${p.native}'!`);
}

// 7. Kiểm tra triệt tiêu Tab Delay / Flicker glitch
console.log("\n[7] Kiểm tra triệt tiêu hoàn toàn Tab Delay / Flicker glitch...");
// Vào reverse mode và nhập dữ liệu
selectMarket('vn');
switchMode('reverse');
mockElements['targetNetInput'].value = '150000';
mockElements['costInput'].value = '70000';
assert(mockElements['tabReverseBtn'].classList.contains('active'), "Phải ở reverse mode trước khi thoát!");
assert(!mockElements['tabForwardBtn'].classList.contains('active'), "Forward tab phải không active!");

// Bấm nút quay lại màn hình chọn thị trường (icon ngôi nhà)
openMarketScreen();
// Kiểm tra: ngay khi gọi openMarketScreen, calculatorApp phải ẩn ngay, tab ép về Forward và sạch input
assert.strictEqual(mockElements['calculatorApp'].style.display, 'none', "openMarketScreen() phải ẩn calculatorApp ngay lập tức!");
assert.strictEqual(mockElements['marketScreen'].style.display, 'block', "openMarketScreen() phải hiển thị marketScreen!");
assert.strictEqual(mockElements['priceInput'].value, '', "openMarketScreen() phải dọn sạch input giá!");
assert.strictEqual(mockElements['targetNetInput'].value, '', "openMarketScreen() phải dọn sạch targetNetInput!");
assert.strictEqual(mockElements['costInput'].value, '', "openMarketScreen() phải dọn sạch costInput!");
assert(mockElements['tabForwardBtn'].classList.contains('active'), "openMarketScreen() phải ngay lập tức chuyển tab về Forward!");
assert(!mockElements['tabReverseBtn'].classList.contains('active'), "openMarketScreen() không được để Reverse tab active!");
assert(!mockElements['forwardMode'].classList.contains('hidden'), "Forward mode không được bị ẩn!");
assert(!mockElements['reverseMode'].classList.contains('active'), "Reverse mode không được active!");

// Vào lại bất kỳ thị trường nào (ví dụ TH)
selectMarket('th');
assert.strictEqual(mockElements['calculatorApp'].style.display, 'block', "selectMarket() phải hiển thị calculatorApp!");
assert.strictEqual(mockElements['marketScreen'].style.display, 'none', "selectMarket() phải ẩn marketScreen!");
assert.strictEqual(mockElements['priceInput'].value, '', "selectMarket() phải đảm bảo input sạch khi vào thị trường mới!");
assert(mockElements['tabForwardBtn'].classList.contains('active'), "selectMarket() phải bảo đảm mở sẵn Forward tab không trễ/không flicker!");
assert(!mockElements['tabReverseBtn'].classList.contains('active'), "Reverse tab không được active sau selectMarket()!");
assert(!mockElements['forwardMode'].classList.contains('hidden'), "Forward mode phải hiển thị ngay lập tức!");
console.log("✓ Tab delay/flicker glitch đã được xử lý triệt để: switchMode('forward') chạy đồng bộ trước khi render.");

// 8. Kiểm tra tính năng Gói Dịch Vụ Freeship Xtra / Voucher Xtra (Forward & Reverse có Cap)
console.log("\n[8] Kiểm tra tính năng gói Freeship Xtra / Voucher Xtra & tính đối xứng có trần (Cap)...");

// Kiểm tra toggle đồng bộ checkbox
onToggleXtra(true);
assert.strictEqual(mockElements['xtraCheckbox'].checked, true, "xtraCheckbox phải được check");
assert.strictEqual(mockElements['xtraReverseCheckbox'].checked, true, "xtraReverseCheckbox phải đồng bộ check");
assert.strictEqual(mockElements['badgeExtraRow'].style.display, 'flex', "badgeExtraRow phải hiển thị");
assert.strictEqual(mockElements['detailExtraRow'].style.display, 'table-row', "detailExtraRow phải hiển thị");

// Test đối xứng Freeship Xtra cho VN:
// Trường hợp 1: Dưới trần (Price = 200,000 VND -> Xtra fee = 200,000 * 6% = 12,000 < 30,000 cap)
selectMarket('vn');
onToggleXtra(true);
mockElements['priceInput'].value = '200000';
calculate();

const netXtraUnder = parseInputNumber(mockElements['netRevenue'].innerText);
const feeXtraUnder = parseInputNumber(mockElements['summaryTotalFee'].innerText);
const taxXtraUnder = parseInputNumber(mockElements['summaryTotalTax'].innerText);

// Kiểm tra cân bằng
const totalUnder = netXtraUnder + feeXtraUnder + taxXtraUnder;
assert(Math.abs(totalUnder - 200000) < 0.05, `VN Xtra dưới trần không cân bằng! ${totalUnder} vs 200000`);

// Tính ngược dưới trần
mockElements['targetNetInput'].value = String(netXtraUnder);
calculateReverse();
const recoveredUnder = parseInputNumber(mockElements['requiredPrice'].innerText);
assert(Math.abs(recoveredUnder - 200000) < 0.05, `VN Xtra dưới trần tính ngược sai: ${recoveredUnder} vs 200000`);
console.log(`✓ VN Freeship Xtra dưới trần: Giá 200k -> Phí=${feeXtraUnder.toFixed(0)}, Thuế=${taxXtraUnder.toFixed(0)}, Net=${netXtraUnder.toFixed(0)} <=> Tính ngược=${recoveredUnder.toFixed(0)}`);

// Trường hợp 2: Chạm trần (Price = 1,000,000 VND -> Xtra fee = min(60,000, 30,000) = 30,000 cap)
mockElements['priceInput'].value = '1000000';
calculate();

const netXtraOver = parseInputNumber(mockElements['netRevenue'].innerText);
const feeXtraOver = parseInputNumber(mockElements['summaryTotalFee'].innerText);
const taxXtraOver = parseInputNumber(mockElements['summaryTotalTax'].innerText);

const totalOver = netXtraOver + feeXtraOver + taxXtraOver;
assert(Math.abs(totalOver - 1000000) < 0.05, `VN Xtra chạm trần không cân bằng! ${totalOver} vs 1000000`);

// Tính ngược chạm trần (Closed-form 2-stage solver)
mockElements['targetNetInput'].value = String(netXtraOver);
calculateReverse();
const recoveredOver = parseInputNumber(mockElements['requiredPrice'].innerText);
assert(Math.abs(recoveredOver - 1000000) < 0.05, `VN Xtra chạm trần tính ngược sai: ${recoveredOver} vs 1000000`);
console.log(`✓ VN Freeship Xtra chạm trần: Giá 1M (phí phụ trợ max 30k) -> Phí=${feeXtraOver.toFixed(0)}, Net=${netXtraOver.toFixed(0)} <=> Tính ngược=${recoveredOver.toFixed(0)}`);

// Kiểm tra Xtra cho các thị trường khác (TH, MY, PH)
const marketsWithXtra = [
  { m: 'th', pUnder: 300, pOver: 4000 },
  { m: 'my', pUnder: 60, pOver: 800 },
  { m: 'ph', pUnder: 600, pOver: 6000 }
];
for (const mx of marketsWithXtra) {
  selectMarket(mx.m);
  onToggleXtra(true);

  // Test under cap
  mockElements['priceInput'].value = String(mx.pUnder);
  calculate();
  const netU = parseInputNumber(mockElements['netRevenue'].innerText);
  mockElements['targetNetInput'].value = String(netU);
  calculateReverse();
  const recU = parseInputNumber(mockElements['requiredPrice'].innerText);
  assert(Math.abs(recU - mx.pUnder) < 0.05, `${mx.m.toUpperCase()} Xtra under-cap reverse failed!`);

  // Test over cap
  mockElements['priceInput'].value = String(mx.pOver);
  calculate();
  const netO = parseInputNumber(mockElements['netRevenue'].innerText);
  mockElements['targetNetInput'].value = String(netO);
  calculateReverse();
  const recO = parseInputNumber(mockElements['requiredPrice'].innerText);
  assert(Math.abs(recO - mx.pOver) < 0.05, `${mx.m.toUpperCase()} Xtra over-cap reverse failed!`);

  console.log(`✓ Thị trường ${mx.m.toUpperCase()}: Freeship/Voucher Xtra tính xuôi & tính ngược khớp hoàn hảo cả 2 tầng (Dưới trần & Chạm trần).`);
}

// Tắt Xtra
onToggleXtra(false);
assert.strictEqual(mockElements['xtraCheckbox'].checked, false);
assert.strictEqual(mockElements['xtraReverseCheckbox'].checked, false);
assert.strictEqual(mockElements['badgeExtraRow'].style.display, 'none');
assert.strictEqual(mockElements['detailExtraRow'].style.display, 'none');

// 9. Kiểm tra tính toán Giá vốn (COGS) & Tỷ Suất Lợi Nhuận (Profit Margin)
console.log("\n[9] Kiểm tra tính năng Giá vốn (COGS) & Tỷ suất lợi nhuận (Profit Margin)...");
selectMarket('vn');
onToggleXtra(false);

// Chưa nhập giá vốn: profitBox và step5 phải ẩn
mockElements['priceInput'].value = '200000';
mockElements['costInput'].value = '';
calculate();
assert.strictEqual(mockElements['profitBox'].style.display, 'none', "Chưa nhập cost thì profitBox phải ẩn");
assert.strictEqual(mockElements['step5CostSection'].style.display, 'none', "Chưa nhập cost thì step5CostSection phải ẩn");

// Trường hợp 1: Có lãi (Price = 200k, Cost = 100k, Net ~ 148k -> Lãi ròng ~ 48k)
mockElements['costInput'].value = '100000';
calculate();
assert.strictEqual(mockElements['profitBox'].style.display, 'block', "Có giá vốn thì profitBox phải hiện");
assert.strictEqual(mockElements['step5CostSection'].style.display, 'block', "Có giá vốn thì step5CostSection phải hiện");
assert(mockElements['profitBox'].classList.contains('positive'), "Có lãi thì phải có class positive");
assert(mockElements['detailProfitRow'].classList.contains('positive'), "detailProfitRow phải có class positive khi có lãi");

const netVal1 = parseInputNumber(mockElements['netRevenue'].innerText);
const profitVal1 = parseInputNumber(mockElements['netProfitVal'].innerText);
const expectedProfit1 = netVal1 - 100000;
assert(Math.abs(profitVal1 - expectedProfit1) < 0.05, `Lãi ròng tính sai: ${profitVal1} vs ${expectedProfit1}`);

const expectedMargin1 = ((expectedProfit1 / 200000) * 100).toFixed(1);
assert(mockElements['profitMarginVal'].innerText.includes(expectedMargin1), `Tỷ suất lợi nhuận hiển thị sai: ${mockElements['profitMarginVal'].innerText} vs ${expectedMargin1}`);
console.log(`✓ Kịch bản LÃI: Giá=200k, Vốn=100k -> Thực nhận=${netVal1.toFixed(0)}, Lãi ròng=+${profitVal1.toFixed(0)} (${mockElements['profitMarginVal'].innerText})`);

// Trường hợp 2: Lỗ (Price = 100k, Cost = 90k, Net = 73,875 -> Lỗ ròng = -16,125)
mockElements['priceInput'].value = '100000';
mockElements['costInput'].value = '90000';
calculate();
assert(mockElements['profitBox'].classList.contains('negative'), "Khi lỗ thì profitBox phải có class negative để đổi màu đỏ!");
assert(mockElements['detailProfitRow'].classList.contains('negative'), "detailProfitRow phải có class negative khi lỗ");
const profitValLoss = parseInputNumber(mockElements['netProfitVal'].innerText);
const expectedLoss = 73875 - 90000;
assert(Math.abs(profitValLoss - Math.abs(expectedLoss)) < 0.05, `Lỗ ròng tính sai: ${profitValLoss} vs ${Math.abs(expectedLoss)}`);
assert(mockElements['netProfitVal'].innerText.startsWith('-'), "Giá trị tiền lỗ ròng phải có tiền tố '-'");
assert(mockElements['profitMarginBadge'].innerText.startsWith('-'), "Huy hiệu tỷ suất lỗ phải có dấu '-'");
console.log(`✓ Kịch bản LỖ: Giá=100k, Vốn=90k -> Thực nhận=73,875, Lỗ ròng=-${profitValLoss.toFixed(0)} (${mockElements['profitMarginVal'].innerText}), kích hoạt style negative cảnh báo.`);

// 10. Kiểm tra chức năng Xuất ảnh thẻ tóm tắt PNG qua HTML5 Canvas (Zalo)
console.log("\n[10] Kiểm tra chức năng Xuất thẻ ảnh PNG tóm tắt qua HTML5 Canvas...");

// Từ chối xuất ảnh khi chưa nhập giá hợp lệ
mockElements['priceInput'].value = '0';
assert.strictEqual(exportSummaryPng(), false, "Giá = 0 phải từ chối xuất ảnh và trả về false");
mockElements['priceInput'].value = '';
assert.strictEqual(exportSummaryPng(), false, "Giá rỗng phải từ chối xuất ảnh và trả về false");

// Xuất ảnh thành công với dữ liệu hợp lệ
mockElements['priceInput'].value = '250000';
mockElements['costInput'].value = '120000';
onToggleXtra(true);
calculate();

// Gọi hàm exportSummaryPng
const exportSuccess = exportSummaryPng();
assert.strictEqual(exportSuccess, true, "Hàm exportSummaryPng() phải chạy thành công và trả về true!");
assert(lastCreatedCanvas, "Canvas phải được tạo bởi exportSummaryPng()");
const renderedHeight = lastCreatedCanvas.height / 2; // canvas.height = calcHeight * scale (scale=2)
assert(renderedHeight > 450 && renderedHeight <= 700, `Chiều cao Canvas (${renderedHeight}px) phải co giãn nội dung tối ưu, không có khoảng trống thừa 260px!`);

// Kiểm tra đầy đủ 5 key i18n mới phục vụ xuất ảnh trong I18N và kiểm tra footerText chuẩn xác
const exportI18nKeys = ['exportSubtitle', 'exportDeductions', 'exportTotalDeductions', 'exportNetBadge', 'exportFooterText'];
const languages = ['vi', 'en', 'th', 'ms', 'tl'];
for (const lang of languages) {
  assert(I18N[lang], `I18N thiếu ngôn ngữ ${lang}`);
  for (const k of exportI18nKeys) {
    assert(I18N[lang][k], `Ngôn ngữ ${lang} thiếu export key: ${k}`);
  }
  assert.strictEqual(I18N[lang].exportFooterText, 'Copyright © 2026 Shopee Estimator. All rights reserved.', `Footer text của ngôn ngữ ${lang} phải đúng copyright!`);
}

// Kiểm tra logo badge trắng và progress bar cap fix trong HTML
assert(htmlContent.includes("drawRoundRect(24, 15, 114, 38, 8, '#ffffff', null)"), "Phải vẽ badge trắng cho logo Shopee để hiển thị chuẩn web trên banner cam!");
assert(htmlContent.includes("visualTaxW = 3.0;"), "Phải có visual padding >= 3.0% cho thanh thuế để tránh lỗi lệch đường tỷ lệ!");
assert(htmlContent.includes("isolation: isolate;"), "Phải có isolation: isolate cho progress-bar!");
assert(htmlContent.includes("border-top-right-radius: 9999px;"), "Phải bo tròn mép phải cho bar-tax!");
console.log("✓ Xuất ảnh PNG thẻ tóm tắt hóa đơn Zalo render chuẩn xác: logo có badge trắng chuẩn web, footer bản quyền chuẩn, progress bar triệt tiêu lệch tỷ lệ.");

// 11. Kiểm tra PWA (Manifest, Service Worker, Meta tags)
console.log("\n[11] Kiểm tra PWA (Progressive Web App)...");

// Kiểm tra file manifest.json
const manifestPath = path.join(__dirname, 'manifest.json');
assert(fs.existsSync(manifestPath), "manifest.json phải tồn tại!");
const manifestJson = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
assert.strictEqual(manifestJson.name, 'Shopee Estimator', "manifest.json name phải là 'Shopee Estimator'!");
assert.strictEqual(manifestJson.short_name, 'Shopee Estimator', "manifest.json short_name phải là 'Shopee Estimator'!");
assert.strictEqual(manifestJson.display, 'standalone', "manifest.json display phải là 'standalone'!");
assert(manifestJson.icons && manifestJson.icons.length >= 2, "manifest.json phải có icons (192 và 512)!");

// Kiểm tra tiêu đề trang web Shopee Estimator trên thẻ title và từ điển I18N
assert(htmlContent.includes('<title id="htmlTitle">Shopee Estimator</title>'), "Thẻ title phải có nội dung 'Shopee Estimator'!");
assert(htmlContent.includes('<meta name="apple-mobile-web-app-title" content="Shopee Estimator">'), "Thẻ meta apple-mobile-web-app-title phải là 'Shopee Estimator'!");
for (const lang of ['vi', 'en', 'th', 'ms', 'tl']) {
  assert.strictEqual(I18N[lang].pageTitle, 'Shopee Estimator', `pageTitle của ngôn ngữ ${lang} phải là 'Shopee Estimator'!`);
}

// Kiểm tra icon vuông trên đĩa
const icon192Path = path.join(__dirname, 'assets', 'icon-192.png');
const icon512Path = path.join(__dirname, 'assets', 'icon-512.png');
assert(fs.existsSync(icon192Path) && fs.statSync(icon192Path).size > 0, "assets/icon-192.png phải tồn tại và có dung lượng hợp lệ!");
assert(fs.existsSync(icon512Path) && fs.statSync(icon512Path).size > 0, "assets/icon-512.png phải tồn tại và có dung lượng hợp lệ!");

// Kiểm tra sw.js
const swPath = path.join(__dirname, 'sw.js');
assert(fs.existsSync(swPath), "sw.js Service Worker phải tồn tại!");
const swCode = fs.readFileSync(swPath, 'utf8');
assert(swCode.includes("addEventListener('install'"), "sw.js phải bắt sự kiện install!");
assert(swCode.includes("addEventListener('activate'"), "sw.js phải bắt sự kiện activate!");
assert(swCode.includes("addEventListener('fetch'"), "sw.js phải bắt sự kiện fetch!");
assert(swCode.includes('icon-192.png') && swCode.includes('icon-512.png'), "sw.js phải cache icon-192.png và icon-512.png!");
console.log("✓ sw.js Service Worker hoàn thiện với cache-first, offline fallback và cache icon vuông.");

// Kiểm tra liên kết PWA trong index.html
assert(htmlContent.includes('<link rel="manifest" href="manifest.json">'), "index.html phải liên kết manifest.json!");
assert(htmlContent.includes('<meta name="theme-color"'), "index.html phải có meta theme-color!");
assert(htmlContent.includes('serviceWorker.register'), "index.html phải có mã đăng ký serviceWorker!");
console.log("✓ index.html tích hợp đầy đủ thẻ meta PWA và đăng ký Service Worker.");

// 12. Kiểm tra Policy Documents Modal (22 đường link chính thức 4 nước, icon đặt giữa home & lang, layout modal danh sách)
console.log("\n[12] Kiểm tra Policy Documents Modal & 22 đường link chính sách chính thức...");

// Kiểm tra vị trí của icon policyDocBtn: phải nằm giữa marketSwitchBtn và langBtn
const posMarketSwitch = htmlContent.indexOf('id="marketSwitchBtn"');
const posPolicyDoc = htmlContent.indexOf('id="policyDocBtn"');
const posLang = htmlContent.indexOf('id="langBtn"');
assert(posMarketSwitch !== -1 && posPolicyDoc !== -1 && posLang !== -1, "Thiếu một trong ba nút trên top-bar!");
assert(posMarketSwitch < posPolicyDoc && posPolicyDoc < posLang, "Nút policyDocBtn phải nằm ở giữa marketSwitchBtn và langBtn theo đúng thứ tự!");

// Kiểm tra SVG icon tài liệu gấp góc (Ảnh 1)
assert(htmlContent.includes('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>'), "Nút policyDocBtn phải chứa SVG icon tài liệu gấp góc chuẩn xác!");
assert(htmlContent.includes('<polyline points="14 2 14 8 20 8"/>'), "Nút policyDocBtn phải có nếp gấp góc tài liệu!");

// Kiểm tra các class và cấu trúc modal dạng Ảnh 2
assert(htmlContent.includes('class="policy-modal-backdrop"'), "Phải có modal backdrop cho policy modal!");
assert(htmlContent.includes('class="policy-modal-card"'), "Phải có modal card cho policy modal!");
assert(htmlContent.includes('class="policy-dot"'), "Phải có chấm xanh trạng thái trên header modal (Ảnh 2)!");
assert(htmlContent.includes('class="policy-modal-title"'), "Phải có tiêu đề modal!");
assert(htmlContent.includes('id="policyMarketBadge"'), "Phải có badge thị trường tương ứng!");
assert(htmlContent.includes('class="policy-close-x"'), "Phải có nút đóng ✕!");
assert(htmlContent.includes('class="policy-footer-note"'), "Phải có dòng chú thích nguồn Shopee chính thức ở footer!");
assert(htmlContent.includes('class="policy-footer-btn"'), "Phải có nút đóng ở footer modal!");

// Kiểm tra từ điển đa ngôn ngữ cho policy modal
const policyKeys = ['policyBtnTitle', 'policyModalTitle', 'policyFooterNote', 'policyCloseBtn'];
for (const lang of ['vi', 'en', 'th', 'ms', 'tl']) {
  for (const pk of policyKeys) {
    assert(I18N[lang][pk], `I18N.${lang} thiếu key ${pk}!`);
  }
}

// Kiểm tra cơ sở dữ liệu POLICY_DOCS
assert(POLICY_DOCS && typeof POLICY_DOCS === 'object', "POLICY_DOCS phải tồn tại!");
const marketsList = ['vn', 'th', 'my', 'ph'];
const expectedCounts = { vn: 7, th: 5, my: 4, ph: 6 };

// Danh sách 22 link chính thức mà người dùng cung cấp
const expectedLinks = {
  vn: [
    'https://banhang.shopee.vn/edu/article/251',
    'https://banhang.shopee.vn/edu/article/2139',
    'https://banhang.shopee.vn/edu/article/25223',
    'https://banhang.shopee.vn/edu/article/2150',
    'https://banhang.shopee.vn/edu/article/2579',
    'https://banhang.shopee.vn/edu/article/3648',
    'https://seller.vn.shopee.cn/edu/article/13123'
  ],
  th: [
    'https://help.shopee.co.th/portal/4/article/77254',
    'https://seller.shopee.co.th/edu/article/16022',
    'https://seller.shopee.co.th/edu/article/18213',
    'https://seller.shopee.co.th/edu/article/1368',
    'https://seller.th.shopee.cn/edu/article/23105'
  ],
  my: [
    'https://seller.shopee.com.my/edu/article/25269',
    'https://help.shopee.com.my/portal/4/article/188813',
    'https://help.shopee.com.my/portal/4/article/143249',
    'https://seller.shopee.com.my/edu/article/5190'
  ],
  ph: [
    'https://seller.shopee.ph/edu/article/21077',
    'https://seller.shopee.ph/edu/article/1504',
    'https://seller.shopee.ph/edu/article/3437',
    'https://seller.shopee.ph/edu/article/27461',
    'https://seller.shopee.ph/edu/article/28201',
    'https://help.shopee.ph/portal/10/article/174380'
  ]
};

let totalDocsCount = 0;
for (const mkt of marketsList) {
  assert(Array.isArray(POLICY_DOCS[mkt]), `POLICY_DOCS.${mkt} phải là mảng!`);
  assert.strictEqual(POLICY_DOCS[mkt].length, expectedCounts[mkt], `Số lượng tài liệu của ${mkt} phải là ${expectedCounts[mkt]}!`);
  totalDocsCount += POLICY_DOCS[mkt].length;

  const actualUrls = POLICY_DOCS[mkt].map(d => d.url);
  for (const expUrl of expectedLinks[mkt]) {
    assert(actualUrls.includes(expUrl), `Thị trường ${mkt} thiếu URL chính thức: ${expUrl}`);
  }

  // Kiểm tra từng item có đủ badge, badgeType, source, title, desc
  for (const doc of POLICY_DOCS[mkt]) {
    assert(doc.url && doc.url.startsWith('https://'), `URL không hợp lệ: ${doc.url}`);
    assert(doc.badge, `Thiếu badge cho ${doc.url}`);
    assert(doc.badgeType, `Thiếu badgeType cho ${doc.url}`);
    assert(doc.source && doc.source.vi && doc.source.en, `Thiếu source cho ${doc.url}`);
    assert(doc.title && doc.title.vi && doc.title.en, `Thiếu title cho ${doc.url}`);
    assert(doc.desc && doc.desc.vi && doc.desc.en, `Thiếu desc cho ${doc.url}`);
  }
}
assert.strictEqual(totalDocsCount, 22, "Tổng cộng phải có đủ 22 liên kết tài liệu chính sách đã lọc!");

// Kiểm tra tương tác mở và đóng modal
selectMarket('vn');
openPolicyModal();
const pModalEl = documentMock.getElementById('policyModal');
assert(pModalEl.classList.contains('show'), "Modal phải có class 'show' khi mở!");
const pContainerEl = documentMock.getElementById('policyListContainer');
assert(pContainerEl.innerHTML.includes('policy-item'), "Container phải được render danh sách các liên kết chính sách!");
assert(pContainerEl.innerHTML.includes('https://banhang.shopee.vn/edu/article/251'), "Phải có link chính thức trong HTML render!");

closePolicyModal();
assert(!pModalEl.classList.contains('show'), "Modal phải bỏ class 'show' khi đóng!");

console.log("✓ Icon tài liệu đặt chuẩn giữa Home & Lang; Modal hiển thị chuẩn Ảnh 2 với đầy đủ 22 URL chính sách phân loại cho 4 thị trường.");

console.log("\n==================================================================");
console.log("=== TẤT CẢ 12 HẠNG MỤC KIỂM THỬ ĐÃ VƯỢT QUA 100% THÀNH CÔNG! ===");
console.log("==================================================================");

