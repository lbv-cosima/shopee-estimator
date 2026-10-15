# Tính Doanh Thu Dự Kiến Sau Chiết Khấu (Shopee)

Công cụ web đơn giản giúp người bán trên Shopee **ước tính số tiền thực nhận về ví** sau khi trừ phụ phí sàn và thuế, đồng thời **tính ngược giá niêm yết** cần đặt để nhận về đúng số tiền mong muốn.

> **Lưu ý quan trọng:** Kết quả của công cụ **chỉ mang tính chất tham khảo, không đảm bảo chính xác 100%**. Các mức phí và thuế trong công cụ là **giá trị cố định đã được cài đặt sẵn**, trong khi thực tế phí của Shopee có thể thay đổi theo ngành hàng, chương trình tham gia và chính sách từng thời kỳ. Vui lòng đối chiếu với **báo cáo doanh thu / số dư trong Kênh Người Bán** để có con số chính xác nhất.

---

## Tính năng

**Tab 1 – Tính Doanh Thu Thực Nhận**
- Nhập giá bán niêm yết, xem ngay số tiền dự kiến về tài khoản.
- Các nút chọn nhanh mức giá: 50k, 100k, 200k, 350k, 500k, 1 triệu.
- Thanh tỷ lệ phân bổ dòng tiền (Nhận / Phí / Thuế), di chuột hoặc chạm để xem phần trăm và số tiền từng phần.
- Hai ô tóm tắt: tổng phụ phí sàn và tổng thuế phải nộp.
- Mục **Phân tích chi tiết** (bấm để mở rộng) trình bày từng bước tính.
- Cảnh báo khi giá bán quá thấp, không đủ bù phụ phí.
- Nút **Sao Chép Kết Quả** và **Làm Mới**.

**Tab 2 – Tính Giá Bán Cần Đặt**
- Nhập số tiền muốn nhận về ví, công cụ tính ra giá cần niêm yết trên sàn.
- Tự điền sẵn số tiền thực nhận từ Tab 1 khi chuyển tab (nếu có).

Giao diện responsive, dùng tốt trên cả máy tính và điện thoại.

---

## 🧮 Cách tính

Công cụ đang áp dụng các mức sau (khai báo ở đầu phần `<script>` trong `index.html`):

| Khoản | Mức áp dụng | Cơ sở tính |
|---|---|---|
| Phí cố định | 16% | Giá bán ban đầu |
| Phí dịch vụ | 3.000₫ / đơn | Cố định |
| Phí giao dịch | 6% | Giá bán ban đầu |
| Thuế GTGT | 1% | Doanh thu trước thuế |
| Thuế TNCN | 0,5% | Doanh thu trước thuế |

**Tính xuôi (giá bán → tiền thực nhận):**

```
Tổng phụ phí sàn (A) = 16% × Giá bán + 3.000₫ + 6% × Giá bán
Doanh thu trước thuế (B) = Giá bán − A          (= Giá bán × 78% − 3.000₫)
Tổng thuế (C) = (1% + 0,5%) × B
Tiền thực nhận = B − C                          (= B × 98,5%)
```

**Tính ngược (tiền muốn nhận → giá niêm yết):**

```
Giá niêm yết = [(Số tiền muốn nhận ÷ 0,985) + 3.000₫] ÷ 0,78
```

---

## Ví dụ minh họa

Giá bán niêm yết **200.000₫**:

| Hạng mục | Giá trị |
|---|---|
| Phí cố định (16%) | −32.000₫ |
| Phí dịch vụ | −3.000₫ |
| Phí giao dịch (6%) | −12.000₫ |
| **Tổng phụ phí sàn (A)** | **−47.000₫** |
| **Doanh thu trước thuế (B)** | **153.000₫** |
| Thuế GTGT (1%) | −1.530₫ |
| Thuế TNCN (0,5%) | −765₫ |
| **Tổng thuế (C)** | **−2.295₫** |
| **Tiền thực nhận về ví** | **150.705₫** |

Tổng khấu trừ: 49.295₫ (khoảng 24,6% giá bán).

Muốn nhận về **100.000₫**? Giá cần niêm yết xấp xỉ **134.004₫**.

---

## Cách sử dụng

1. Mở file `index.html` bằng trình duyệt (không cần cài đặt hay kết nối máy chủ).
2. **Tính doanh thu:** nhập giá sản phẩm ở khung "Giá Bán Ban Đầu" và xem kết quả ở khung "Doanh Thu Sau Khấu Trừ".
3. **Tính giá cần đặt:** chuyển sang tab "Tính Giá Bán Cần Đặt", nhập số tiền muốn nhận về.
4. Bấm "Phân tích chi tiết" để xem từng bước tính, hoặc "Sao Chép Kết Quả" để gửi cho người khác.

> Lần đầu mở cần có kết nối Internet để tải font **Be Vietnam Pro** từ Google Fonts. Nếu không có mạng, công cụ vẫn hoạt động bình thường với font hệ thống.

---

## Cấu trúc dự án

```
.
├── index.html        # Trang công cụ (HTML + CSS + JS trong một file)
├── build_index.py    # Script tạo index.html, nhúng các icon dạng base64
├── assets/           # Icon và logo dùng khi build
│   ├── icon_pin.png
│   ├── icon_wallet.png
│   ├── icon_detail.png
│   └── logo_shopee.png
└── README.md
```

**Tạo lại `index.html`** sau khi chỉnh sửa giao diện trong `build_index.py`:

```bash
python build_index.py
```

---

## Tùy chỉnh mức phí

Khi Shopee thay đổi chính sách, bạn có thể chỉnh các hằng số ở đầu phần script:

```js
const FIXED_FEE_RATE = 0.16;   // Phí cố định
const SERVICE_FEE    = 3000;   // Phí dịch vụ cố định mỗi đơn
const TX_FEE_RATE    = 0.06;   // Phí giao dịch
const VAT_RATE       = 0.01;   // Thuế GTGT
const PIT_RATE       = 0.005;  // Thuế TNCN
```

Nếu tạo lại file bằng `build_index.py`, hãy sửa các hằng số này trong script tương ứng. Các dòng chữ hiển thị mức phí (ví dụ "16%", "3.000₫", công thức rút gọn) cũng cần cập nhật theo.

---

## Hạn chế

- Mức phí là **một bộ cố định**, chưa phân biệt theo ngành hàng hay chương trình (Freeship Xtra, Voucher Xtra…).
- Chưa tính voucher do shop chịu, phí quảng cáo, phí vận chuyển, giá vốn, hoàn hàng hoặc các khoản phạt.
- Thuế được tính trên doanh thu sau khi trừ phụ phí sàn. Cách xác định cơ sở tính thuế thực tế có thể khác tùy hình thức kinh doanh và quy định hiện hành.
- Số liệu được làm tròn đến đơn vị đồng nên có thể lệch nhẹ so với thực tế.

---

## Tuyên bố miễn trừ trách nhiệm

Công cụ này là sản phẩm độc lập, **không liên kết hay được bảo trợ bởi Shopee**. Mọi kết quả chỉ nhằm mục đích **tham khảo**. Tác giả không chịu trách nhiệm về các quyết định kinh doanh được đưa ra dựa trên kết quả ước tính từ công cụ này.
