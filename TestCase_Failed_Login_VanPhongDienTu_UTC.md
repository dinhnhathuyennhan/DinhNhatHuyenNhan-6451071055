# BỘ TEST CASE FAILED – TRANG ĐĂNG NHẬP VĂN PHÒNG ĐIỆN TỬ UTC

**URL kiểm thử:** https://vanphongdientu.utc.edu.vn/Login?r=https%3A%2F%2Fvanphongdientu.utc.edu.vn%2F
**Màn hình:** Đăng nhập hệ thống Văn phòng điện tử – Trường ĐH Giao thông Vận tải
**Loại test case:** Negative / Failed (các kịch bản mong đợi hệ thống **từ chối đăng nhập** hoặc **báo lỗi**)
**Ngày tạo:** 08/10/2026
**Người tạo:** QA Team

---

## 1. Mô tả các thành phần trên màn hình

| Thành phần | Thuộc tính kỹ thuật | Ghi chú |
|---|---|---|
| Ô Tên đăng nhập | `input[type=text][name=username]`, placeholder "Tên đăng nhập" | Không có `maxlength`, không `required`, không `autocomplete` |
| Ô Mật khẩu | `input[type=password][name=userpwd]`, placeholder "Mật khẩu" | Không có `maxlength`, không `required` |
| Checkbox "Giữ tôi luôn đăng nhập" | `input[type=checkbox][name=persistent][value=1]` | Mặc định không tích |
| Nút Đăng nhập | `input[type=submit].submit_login` | Submit form `POST /Login` |
| Trường ẩn redirect | `input[type=hidden][name=r]` | Chứa URL quay về sau đăng nhập |
| Link "Đăng nhập bằng e-mail UTC" | Google OAuth2 | `redirect_uri` đang dùng `http://` |
| Link "Bạn quên mật khẩu đăng nhập?" | `/Login/GetPass` | |
| Cookie phiên | `sso_utc_token_office` | Session SSO |

**Thông báo lỗi thực tế của hệ thống (đã xác minh):**
- Bỏ trống tên đăng nhập → `Bạn chưa nhập tên đăng nhập`
- Bỏ trống mật khẩu → `Bạn chưa nhập mật khẩu`
- Sai tài khoản/mật khẩu → `Tài khoản hoặc mật khẩu không đúng.`

---

## 2. Bộ Test Case Failed

> **Quy ước kết quả:** Mỗi test case ở trạng thái FAILED nghĩa là hệ thống **PHẢI** ngăn đăng nhập và/hoặc hiển thị thông báo lỗi phù hợp. Nếu hệ thống cho đăng nhập thành công hoặc không báo lỗi → test **FAIL thực sự (lỗi phần mềm)**.

### Nhóm A – Kiểm tra trường bắt buộc (Required / Empty)

| ID | Tiêu đề | Điều kiện tiên quyết | Dữ liệu nhập | Các bước thực hiện | Kết quả mong đợi |
|---|---|---|---|---|---|
| TC_F01 | Để trống cả hai trường | Đang ở trang Login | username = `""`, password = `""` | 1. Không nhập gì<br>2. Nhấn **Đăng nhập** | Hiển thị `Bạn chưa nhập tên đăng nhập`; không đăng nhập; vẫn ở trang Login |
| TC_F02 | Để trống tên đăng nhập | | username = `""`, password = `123456` | 1. Chỉ nhập mật khẩu<br>2. Nhấn **Đăng nhập** | Hiển thị `Bạn chưa nhập tên đăng nhập`; không đăng nhập |
| TC_F03 | Để trống mật khẩu | | username = `someuser`, password = `""` | 1. Chỉ nhập tên đăng nhập<br>2. Nhấn **Đăng nhập** | Hiển thị `Bạn chưa nhập mật khẩu`; không đăng nhập |
| TC_F04 | Nhập toàn khoảng trắng | | username = `"   "`, password = `"   "` | 1. Nhập toàn dấu cách<br>2. Nhấn **Đăng nhập** | Hệ thống trim và báo lỗi thiếu dữ liệu / sai thông tin; không đăng nhập |
| TC_F05 | Chỉ có khoảng trắng ở tên, mật khẩu hợp lệ | | username = `"  "`, password = `Abc@123` | 1. Nhập<br>2. Nhấn **Đăng nhập** | Báo lỗi tên đăng nhập không hợp lệ; không đăng nhập |

### Nhóm B – Sai thông tin xác thực (Authentication)

| ID | Tiêu đề | Dữ liệu nhập | Các bước thực hiện | Kết quả mong đợi |
|---|---|---|---|---|
| TC_F06 | Tài khoản không tồn tại | username = `user_khong_ton_tai_999`, password = `Any@123` | Nhập → Nhấn Đăng nhập | `Tài khoản hoặc mật khẩu không đúng.`; không đăng nhập |
| TC_F07 | Đúng tài khoản, sai mật khẩu | username = `<tài khoản hợp lệ>`, password = `sai_mat_khau` | Nhập → Nhấn Đăng nhập | `Tài khoản hoặc mật khẩu không đúng.`; không tiết lộ username có tồn tại hay không |
| TC_F08 | Sai cả tài khoản và mật khẩu | username = `aaaa`, password = `bbbb` | Nhập → Nhấn Đăng nhập | `Tài khoản hoặc mật khẩu không đúng.` |
| TC_F09 | Sai hoa/thường mật khẩu | username = `<hợp lệ>`, password = `<đúng nhưng đổi hoa-thường>` | Nhập → Nhấn Đăng nhập | Mật khẩu phân biệt hoa thường → báo sai; không đăng nhập |
| TC_F10 | Thừa khoảng trắng đầu/cuối mật khẩu | username = `<hợp lệ>`, password = `" matkhau "` | Nhập → Nhấn Đăng nhập | Báo sai thông tin (nếu không trim password); không đăng nhập |
| TC_F11 | Tài khoản đã bị khóa/vô hiệu hóa | username = `<tài khoản bị khóa>`, password = `<đúng>` | Nhập → Nhấn Đăng nhập | Thông báo tài khoản bị khóa/không hoạt động; không đăng nhập |
| TC_F12 | Đăng nhập lại bằng mật khẩu cũ sau khi đã đổi | username = `<hợp lệ>`, password = `<mật khẩu cũ>` | Nhập → Nhấn Đăng nhập | `Tài khoản hoặc mật khẩu không đúng.` |

### Nhóm C – Dữ liệu bất thường / Định dạng (Boundary & Format)

| ID | Tiêu đề | Dữ liệu nhập | Các bước thực hiện | Kết quả mong đợi |
|---|---|---|---|---|
| TC_F13 | Tên đăng nhập quá dài | username = chuỗi 1000 ký tự, password = `Abc@123` | Nhập → Nhấn Đăng nhập | Không crash; báo lỗi sai thông tin hoặc giới hạn độ dài; không đăng nhập |
| TC_F14 | Mật khẩu quá dài | username = `<hợp lệ>`, password = chuỗi 5000 ký tự | Nhập → Nhấn Đăng nhập | Không crash; báo sai thông tin; không đăng nhập |
| TC_F15 | Ký tự Unicode/emoji trong tên | username = `tên😀đăngnhập`, password = `Abc@123` | Nhập → Nhấn Đăng nhập | Báo sai thông tin; không crash; không đăng nhập |
| TC_F16 | Ký tự đặc biệt trong tên | username = `admin'--`, password = `x` | Nhập → Nhấn Đăng nhập | Báo sai thông tin; **không** thực thi (chống SQL Injection) |
| TC_F17 | Chuỗi SQL Injection cổ điển | username = `' OR '1'='1`, password = `' OR '1'='1` | Nhập → Nhấn Đăng nhập | **Không** đăng nhập được; báo sai thông tin; không lỗi 500 |
| TC_F18 | Chuỗi XSS trong trường nhập | username = `<script>alert(1)</script>`, password = `x` | Nhập → Nhấn Đăng nhập | Dữ liệu được escape; không chạy script; báo sai thông tin |
| TC_F19 | Khoảng trắng giữa chuỗi tên | username = `ab cd`, password = `Abc@123` | Nhập → Nhấn Đăng nhập | Báo sai thông tin (nếu username không chứa space); không đăng nhập |
| TC_F20 | Dán giá trị có ký tự xuống dòng | username = `user\nadmin`, password = `x` | Dán → Nhấn Đăng nhập | Xử lý an toàn; báo sai thông tin; không crash |

### Nhóm D – Bảo mật & Phiên làm việc (Security / Session)

| ID | Tiêu đề | Dữ liệu / Thao tác | Các bước thực hiện | Kết quả mong đợi |
|---|---|---|---|---|
| TC_F21 | Brute-force / thử sai nhiều lần | Sai mật khẩu liên tiếp ≥ 5–10 lần | Nhập sai lặp lại | Hệ thống nên khóa tạm / CAPTCHA / giới hạn; **không** cho thử vô hạn |
| TC_F22 | Thao túng trường redirect `r` | Sửa hidden `r` = `https://evil-site.com` | Sửa DOM → đăng nhập | Hệ thống **không** redirect ra domain ngoài (chống Open Redirect) |
| TC_F23 | Gửi POST thiếu trường `r` | Bỏ hidden `r` khỏi request | Gửi request thủ công | Xử lý mặc định an toàn; không lỗi 500 |
| TC_F24 | Mật khẩu bị gửi dạng rõ qua HTTP | | Bắt gói request | Form phải submit qua **HTTPS**; mật khẩu không lộ |
| TC_F25 | OAuth redirect_uri không an toàn | `redirect_uri` của Google dùng `http://` | Kiểm tra link OAuth | **FAIL bảo mật** nếu dùng `http://` thay vì `https://` |
| TC_F26 | Truy cập trang nội bộ khi chưa đăng nhập | | Mở trực tiếp URL nội bộ sau Login | Bị chuyển về trang Login; không truy cập được |
| TC_F27 | Dùng lại cookie phiên đã hết hạn | Cookie `sso_utc_token_office` cũ | Gửi request với cookie hết hạn | Yêu cầu đăng nhập lại; không nhận phiên cũ |
| TC_F28 | Nhấn Back sau khi đăng xuất | Đã logout | Nhấn Back trình duyệt | Không vào lại được hệ thống; quay về Login |
| TC_F29 | Thông báo lỗi lộ thông tin | Sai username vs sai password | So sánh 2 thông báo | Thông báo giống nhau (`Tài khoản hoặc mật khẩu không đúng.`), không phân biệt để tránh dò tài khoản |

### Nhóm E – Giao diện & Trải nghiệm (UI/UX khi lỗi)

| ID | Tiêu đề | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC_F30 | Thông báo lỗi hiển thị rõ ràng | Submit sai | Thông báo lỗi hiển thị tại vùng dễ thấy, tiếng Việt đúng chính tả |
| TC_F31 | Dữ liệu đã nhập sau khi lỗi | Submit sai | Vì lý do bảo mật, **mật khẩu phải bị xóa**; username có thể giữ lại |
| TC_F32 | Double-click nút Đăng nhập | Nhấn nhanh 2 lần | Không gửi 2 request / không lỗi phiên; chỉ xử lý 1 lần |
| TC_F33 | Nhấn Enter khi để trống | Focus ô password rỗng → Enter | Hiển thị lỗi thiếu dữ liệu (giống nhấn nút) |
| TC_F34 | Tắt JavaScript rồi submit rỗng | Disable JS → submit | Vẫn có validate phía server, báo lỗi; không đăng nhập |

---

## 3. Mẫu ghi nhận kết quả thực thi

| ID | Trạng thái (Pass/Fail) | Kết quả thực tế | Ảnh chụp | Ghi chú |
|---|---|---|---|---|
| TC_F01 | | | | |
| TC_F02 | | | | |
| ... | | | | |

---

## 4. Ghi chú quan sát & rủi ro tiềm ẩn (từ khảo sát trang)

1. **Thiếu thuộc tính HTML cơ bản:** các ô input không có `maxlength`, `required`, `autocomplete` → nên bổ sung validate và giới hạn độ dài phía client lẫn server (liên quan TC_F13, TC_F14).
2. **OAuth `redirect_uri` dùng `http://`** thay vì `https://` → rủi ro bảo mật (TC_F25).
3. **Trường redirect `r`** là hidden và nhận URL tuyệt đối → cần kiểm tra chống Open Redirect (TC_F22).
4. **Thông báo lỗi gộp chung** cho sai username/password là tốt (tránh user enumeration) → giữ nguyên (TC_F29).
5. **Cần kiểm tra cơ chế chống brute-force** (khóa tài khoản/CAPTCHA) vì hiện chưa quan sát thấy (TC_F21).

---

*Tài liệu phục vụ mục đích kiểm thử chất lượng (QA) trên hệ thống được phép truy cập.*
