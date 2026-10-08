"""TC_F25: redirect_uri của OAuth nên dùng https:// (hiện quan sát thấy http://).

LỖI THẬT đã xác nhận -> đánh dấu xfail đến khi hệ thống khắc phục sang https://.
"""
import pytest


@pytest.mark.xfail(
    reason="TC_F25: LỖI THẬT đã xác nhận — redirect_uri OAuth đang dùng http://. "
           "Đánh dấu xfail đến khi hệ thống khắc phục sang https://.",
    strict=False,
)
def test_TC_F25_oauth_redirect_uri_scheme(login_page):
    url = login_page.oauth_url()
    assert "redirect_uri=http%3A%2F%2F" not in url, (
        "redirect_uri đang dùng http:// — rủi ro bảo mật, cần chuyển sang https://"
    )
