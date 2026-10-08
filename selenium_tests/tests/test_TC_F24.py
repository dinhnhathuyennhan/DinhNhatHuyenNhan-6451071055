"""TC_F24: Trang đăng nhập phải phục vụ qua HTTPS."""


def test_TC_F24_form_submits_over_https(login_page):
    assert login_page.driver.current_url.startswith("https://"), (
        "Trang Login phải dùng HTTPS"
    )
