# B1: THIẾT KẾ TEST CASE – XÂY DỰNG CÁC CA KIỂM THỬ

**Trang kiểm thử:** vanphongdientu.utc.edu.vn/Login
**Màn hình:** Đăng nhập hệ thống Văn phòng điện tử – Trường ĐH Giao thông Vận tải
**Loại:** Test case failed (ca kiểm thử mong đợi hệ thống **từ chối đăng nhập** / **báo lỗi**)
**Ngày tạo:** 08/10/2026

---

## Bảng các ca kiểm thử

| STT | ID | Description | Steps | Expected Output |
|:---:|:---|:---|:---|:---|
| 1 | TC_F01 | Để trống cả username và password | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Không nhập username<br>3. Không nhập password<br>4. Click vào nút Đăng nhập | Bạn chưa nhập tên đăng nhập |
| 2 | TC_F02 | Để trống username, có nhập password | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào ô password<br>3. Nhập password là "123456"<br>4. Click vào nút Đăng nhập | Bạn chưa nhập tên đăng nhập |
| 3 | TC_F03 | Có username, để trống password | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào ô username<br>3. Nhập username là "someuser"<br>4. Click vào nút Đăng nhập | Bạn chưa nhập mật khẩu |
| 4 | TC_F04 | Nhập toàn khoảng trắng ở cả hai ô | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập username là "   " (dấu cách)<br>3. Nhập password là "   " (dấu cách)<br>4. Click vào nút Đăng nhập | Không đăng nhập; vẫn ở trang Login (báo thiếu/sai thông tin) |
| 5 | TC_F06 | Đăng nhập với tài khoản không tồn tại | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào ô username<br>3. Nhập username là "user_khong_ton_tai_999"<br>4. Nhập password là "Any@123"<br>5. Click vào nút Đăng nhập | Tài khoản hoặc mật khẩu không đúng. |
| 6 | TC_F07 | Đúng tên đăng nhập, sai mật khẩu | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập username là \<tài khoản hợp lệ><br>3. Nhập password sai<br>4. Click vào nút Đăng nhập | Tài khoản hoặc mật khẩu không đúng. |
| 7 | TC_F08 | Sai cả tài khoản lẫn mật khẩu | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập username là "aaaa"<br>3. Nhập password là "bbbb"<br>4. Click vào nút Đăng nhập | Tài khoản hoặc mật khẩu không đúng. |
| 8 | TC_F13 | Tên đăng nhập quá dài (1000 ký tự) | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập username là chuỗi 1000 ký tự "a"<br>3. Nhập password là "Abc@123"<br>4. Click vào nút Đăng nhập | Không crash; không đăng nhập; vẫn ở trang Login |
| 9 | TC_F15 | Tên đăng nhập chứa Unicode/emoji | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập username là "tên😀đăngnhập"<br>3. Nhập password là "Abc@123"<br>4. Click vào nút Đăng nhập | Không crash; không đăng nhập |
| 10 | TC_F17 | Chuỗi SQL Injection | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập username là `' OR '1'='1`<br>3. Nhập password là `' OR '1'='1`<br>4. Click vào nút Đăng nhập | Không đăng nhập được; không lộ lỗi SQL ra giao diện |
| 11 | TC_F18 | Chuỗi XSS trong trường nhập | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập username là `<script>alert(1)</script>`<br>3. Nhập password là "x"<br>4. Click vào nút Đăng nhập | Dữ liệu được escape; không chạy script; không đăng nhập |
| 12 | TC_F24 | Trang Login phải phục vụ qua HTTPS | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Quan sát URL trên thanh địa chỉ | URL bắt đầu bằng https:// |
| 13 | TC_F25 | Kiểm tra redirect_uri của nút "Đăng nhập bằng e-mail UTC" | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Kiểm tra thuộc tính href của nút OAuth | redirect_uri dùng https:// (hiện đang http:// → lỗi bảo mật) |
| 14 | TC_F29 | Thông báo lỗi không tiết lộ tài khoản tồn tại (chống dò tài khoản) | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập username không tồn tại<br>3. Nhập password bất kỳ<br>4. Click vào nút Đăng nhập | Tài khoản hoặc mật khẩu không đúng. (thông điệp chung) |
| 15 | TC_F31 | Mật khẩu bị xóa sau khi đăng nhập lỗi | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập username là "aaaa"<br>3. Nhập password là "secret_pw_123"<br>4. Click vào nút Đăng nhập<br>5. Quan sát ô password sau khi báo lỗi | Báo "Tài khoản hoặc mật khẩu không đúng." và ô mật khẩu trống |
| 16 | TC_F33 | Nhấn Enter khi để trống username | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Để trống username<br>3. Đặt con trỏ vào ô password, nhấn Enter | Bạn chưa nhập tên đăng nhập |
| 17 | TC_F21 | Thử sai nhiều lần liên tiếp (brute-force) | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập sai mật khẩu liên tiếp ≥ 5–10 lần<br>3. Click vào nút Đăng nhập mỗi lần | Hệ thống khóa tạm / hiện CAPTCHA (kiểm tra thủ công) |
| 18 | TC_F22 | Thao túng tham số redirect `r` (open redirect) | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Sửa trường ẩn `r` thành domain ngoài (vd https://evil.com)<br>3. Đăng nhập | Hệ thống không redirect ra domain ngoài |

---

## Ghi chú & rủi ro tiềm ẩn (quan sát từ trang thực tế)

1. Các ô input thiếu `maxlength`, `required`, `autocomplete` → nên bổ sung validate và giới hạn độ dài (liên quan TC_F13).
2. **OAuth `redirect_uri` đang dùng `http://`** thay vì `https://` → rủi ro bảo mật (TC_F25).
3. Trường ẩn `r` nhận URL tuyệt đối → cần kiểm tra chống Open Redirect (TC_F22).
4. Thông báo lỗi gộp chung cho sai username/password là tốt (tránh dò tài khoản – TC_F29).
5. Chưa quan sát thấy cơ chế chống brute-force → cần kiểm tra (TC_F21).

> Các thông báo lỗi trong cột Expected Output là **thông điệp thực tế đã xác minh** trên hệ thống:
> `Bạn chưa nhập tên đăng nhập` · `Bạn chưa nhập mật khẩu` · `Tài khoản hoặc mật khẩu không đúng.`
>
> Bộ test case này được tự động hóa bằng Selenium Python trong thư mục `selenium_tests/`
> (mỗi ID `TC_Fxx` tương ứng một file `test_TC_Fxx.py`).
