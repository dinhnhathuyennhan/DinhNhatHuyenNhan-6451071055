"""TC_F04: Nhập toàn khoảng trắng -> không đăng nhập."""


def test_TC_F04_whitespace_only(login_page):
    login_page.login("   ", "   ")
    assert login_page.is_on_login_page(), "Khoảng trắng không được coi là hợp lệ"
