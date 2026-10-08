"""TC_F06: Tài khoản không tồn tại -> 'Tài khoản hoặc mật khẩu không đúng.'."""
import config as cfg


def test_TC_F06_nonexistent_account(login_page):
    login_page.login("user_khong_ton_tai_999", "Any@123")
    assert login_page.wait_for_text(cfg.MSG_WRONG_CREDENTIAL)
    assert login_page.is_on_login_page()
