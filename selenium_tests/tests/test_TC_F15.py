"""TC_F15: Unicode/emoji trong tên -> không crash, không đăng nhập."""


def test_TC_F15_unicode_emoji_username(login_page):
    login_page.login("tên😀đăngnhập", "Abc@123")
    assert login_page.is_on_login_page()
