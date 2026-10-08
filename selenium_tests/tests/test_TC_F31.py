"""TC_F31: Sau khi submit lỗi, ô mật khẩu PHẢI bị xóa (bảo mật)."""
import config as cfg


def test_TC_F31_password_cleared_after_error(login_page):
    login_page.login("aaaa", "secret_pw_123")
    login_page.wait_for_text(cfg.MSG_WRONG_CREDENTIAL)
    assert login_page.password_value() == "", "Mật khẩu không được giữ lại sau lỗi"
