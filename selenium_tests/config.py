"""Cấu hình chung cho bộ test đăng nhập Văn phòng điện tử UTC.

Tài khoản hợp lệ (nếu có) được lấy từ biến môi trường để không hard-code:
    export UTC_VALID_USERNAME="tai_khoan"
    export UTC_VALID_PASSWORD="mat_khau"
Các test cần tài khoản hợp lệ sẽ tự bị skip nếu biến môi trường chưa đặt.
"""
import os

BASE_URL = "https://vanphongdientu.utc.edu.vn"
LOGIN_URL = f"{BASE_URL}/Login?r=https%3A%2F%2Fvanphongdientu.utc.edu.vn%2F"

# Tài khoản thật (tùy chọn) phục vụ một số test cần đăng nhập đúng/ sai mật khẩu
VALID_USERNAME = os.getenv("UTC_VALID_USERNAME")
VALID_PASSWORD = os.getenv("UTC_VALID_PASSWORD")

# Thông báo lỗi thực tế của hệ thống (đã xác minh khi khảo sát trang)
MSG_EMPTY_USERNAME = "Bạn chưa nhập tên đăng nhập"
MSG_EMPTY_PASSWORD = "Bạn chưa nhập mật khẩu"
MSG_WRONG_CREDENTIAL = "Tài khoản hoặc mật khẩu không đúng."

# Timeout mặc định (giây)
TIMEOUT = 15

# Chạy ẩn (headless) hay hiện cửa sổ: HEADLESS=0 để xem trình duyệt
HEADLESS = os.getenv("HEADLESS", "1") != "0"
