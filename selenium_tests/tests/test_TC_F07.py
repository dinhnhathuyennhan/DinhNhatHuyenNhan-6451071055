"""TC_F07: Đúng tài khoản, sai mật khẩu -> sai thông tin.

Cần tài khoản hợp lệ qua biến môi trường UTC_VALID_USERNAME / UTC_VALID_PASSWORD,
nếu chưa có sẽ tự động skip.
"""
import pytest

import config as cfg

needs_valid_account = pytest.mark.skipif(
    not (cfg.VALID_USERNAME and cfg.VALID_PASSWORD),
    reason="Cần đặt UTC_VALID_USERNAME / UTC_VALID_PASSWORD để chạy test này",
)


@needs_valid_account
def test_TC_F07_valid_user_wrong_password(login_page):
    login_page.login(cfg.VALID_USERNAME, "mat_khau_chac_chan_sai_123!@#")
    assert login_page.wait_for_text(cfg.MSG_WRONG_CREDENTIAL)
    assert login_page.is_on_login_page()
