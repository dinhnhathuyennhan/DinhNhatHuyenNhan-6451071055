"""TC_F21: Thử sai nhiều lần -> hệ thống nên khóa tạm / CAPTCHA.

Không tự động chạy để tránh gây tải / khóa tài khoản trên hệ thống production.
Chỉ thực hiện thủ công khi được phép.
"""
import pytest


@pytest.mark.skip(reason="TC_F21: Brute-force gây tải lên hệ thống thật — chỉ chạy thủ công khi được phép")
def test_TC_F21_brute_force_lockout():
    pass
