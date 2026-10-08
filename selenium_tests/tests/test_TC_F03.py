"""TC_F03: Có tên đăng nhập, trống mật khẩu -> 'Bạn chưa nhập mật khẩu'."""
import config as cfg


def test_TC_F03_empty_password(login_page):
    login_page.login("someuser", "")
    assert login_page.wait_for_text(cfg.MSG_EMPTY_PASSWORD)
    assert login_page.is_on_login_page()
