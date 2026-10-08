"""TC_F33: Nhấn Enter khi để trống -> hiển thị lỗi thiếu dữ liệu."""
from selenium.webdriver.common.keys import Keys

import config as cfg
from pages.login_page import LoginPage


def test_TC_F33_enter_key_empty_shows_error(driver):
    page = LoginPage(driver).open()
    page.set_username("")
    pwd = driver.find_element(*LoginPage.PASSWORD)
    pwd.send_keys(Keys.ENTER)
    assert page.wait_for_text(cfg.MSG_EMPTY_USERNAME) or page.is_on_login_page()
