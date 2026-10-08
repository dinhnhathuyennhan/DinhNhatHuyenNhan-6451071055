"""TC_F13: Tên đăng nhập 1000 ký tự -> không crash, không đăng nhập."""


def test_TC_F13_very_long_username(login_page):
    login_page.login("a" * 1000, "Abc@123")
    assert login_page.is_on_login_page()
