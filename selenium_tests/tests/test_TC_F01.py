"""TC_F01: Để trống cả hai trường -> 'Bạn chưa nhập tên đăng nhập'."""
import config as cfg


def test_TC_F01_empty_both_fields(login_page):
    login_page.login("", "")
    assert login_page.wait_for_text(cfg.MSG_EMPTY_USERNAME), (
        "Mong đợi thông báo thiếu tên đăng nhập"
    )
    assert login_page.is_on_login_page(), "Không được đăng nhập khi để trống"
