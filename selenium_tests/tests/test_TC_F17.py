"""TC_F17: Chuỗi SQL Injection -> KHÔNG được bypass đăng nhập."""


def test_TC_F17_sql_injection(login_page):
    login_page.login("' OR '1'='1", "' OR '1'='1")
    assert login_page.is_on_login_page(), "SQLi không được phép đăng nhập thành công"
    txt = login_page.page_text().lower()
    assert "sql" not in txt and "syntax" not in txt, "Không được lộ lỗi SQL ra giao diện"
