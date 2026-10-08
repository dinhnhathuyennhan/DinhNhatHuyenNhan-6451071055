"""TC_F08: Sai cả tài khoản lẫn mật khẩu."""
import config as cfg


def test_TC_F08_wrong_both(login_page):
    login_page.login("aaaa", "bbbb")
    assert login_page.wait_for_text(cfg.MSG_WRONG_CREDENTIAL)
    assert login_page.is_on_login_page()
