"""TC_F02: Trống tên đăng nhập, có mật khẩu -> 'Bạn chưa nhập tên đăng nhập'."""
import config as cfg


def test_TC_F02_empty_username(login_page):
    login_page.login("", "123456")
    assert login_page.wait_for_text(cfg.MSG_EMPTY_USERNAME)
    assert login_page.is_on_login_page()
