# Selenium Test – Trang đăng nhập Văn phòng điện tử UTC

Bộ test tự động (negative/failed) cho trang đăng nhập, xây dựng từ tài liệu
[`../TestCase_Failed_Login_VanPhongDienTu_UTC.md`](../TestCase_Failed_Login_VanPhongDienTu_UTC.md).

## Cấu trúc
```
selenium_tests/
├── config.py                 # URL, thông báo lỗi, timeout, tài khoản (env)
├── conftest.py               # fixtures: driver (Chrome), login_page
├── pages/login_page.py       # Page Object màn hình Login
├── tests/                    # MỖI test case 1 file riêng (1 commit = 1 test case)
│   ├── test_TC_F01.py ... test_TC_F33.py
├── pytest.ini
└── requirements.txt
```

## Cài đặt
```bash
python3 -m venv .venv
.venv/bin/pip install -r selenium_tests/requirements.txt
```
> Cần Google Chrome đã cài. Selenium Manager (Selenium ≥ 4.6) tự tải chromedriver.

## Chạy
```bash
# Chạy ẩn (mặc định)
.venv/bin/python -m pytest selenium_tests

# Xem trình duyệt chạy
HEADLESS=0 .venv/bin/python -m pytest selenium_tests -v

# Chạy 1 test cụ thể
.venv/bin/python -m pytest selenium_tests -k TC_F17
```

## Tài khoản hợp lệ (tùy chọn)
Một số test (vd TC_F07 – đúng tài khoản/sai mật khẩu) cần tài khoản thật,
sẽ tự **skip** nếu chưa cấu hình:
```bash
export UTC_VALID_USERNAME="ten_dang_nhap"
export UTC_VALID_PASSWORD="mat_khau"
```

## Ánh xạ test ↔ tài liệu
| Test | Tài liệu | Nội dung |
|---|---|---|
| TC_F01–F04 | Nhóm A | Trường bắt buộc / khoảng trắng |
| TC_F06–F08 | Nhóm B | Sai xác thực |
| TC_F13–F18 | Nhóm C | Dữ liệu dài, Unicode, SQLi, XSS |
| TC_F24,F25,F29 | Nhóm D | HTTPS, OAuth redirect_uri, chống dò tài khoản |
| TC_F31,F33 | Nhóm E | Xóa mật khẩu sau lỗi, phím Enter |
| TC_F21,F22 | Nhóm D | **skip** – brute-force / open-redirect: chạy thủ công khi được phép |

## Kết quả mẫu
```
14 passed, 3 skipped, 1 xfailed
```
- **xfailed – TC_F25**: lỗi thật đã xác nhận — `redirect_uri` của OAuth dùng `http://`
  thay vì `https://`. Giữ `xfail` đến khi hệ thống khắc phục.
- **skipped – TC_F21, TC_F22**: không tự động chạy để tránh gây tải/khóa tài khoản
  trên hệ thống production; chỉ thực hiện thủ công khi có sự cho phép.

> Lưu ý: bộ test chạy trực tiếp lên hệ thống thật, chỉ dùng cho mục đích kiểm thử
> được phép. Các test không brute-force và chỉ gửi vài request.
