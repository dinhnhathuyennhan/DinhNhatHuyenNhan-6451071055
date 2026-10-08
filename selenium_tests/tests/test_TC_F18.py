"""TC_F18: Chuỗi XSS -> dữ liệu phải được escape, không chạy script."""


def test_TC_F18_xss_input(login_page):
    login_page.login("<script>alert(1)</script>", "x")
    # Không có alert nào bật ra (nếu có, driver sẽ treo / UnexpectedAlert)
    assert login_page.is_on_login_page()
