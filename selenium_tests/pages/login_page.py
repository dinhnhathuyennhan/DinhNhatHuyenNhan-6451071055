"""Page Object cho màn hình đăng nhập Văn phòng điện tử UTC."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import LOGIN_URL, TIMEOUT


class LoginPage:
    # Locators (xác minh từ DOM thực tế của trang)
    USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='userpwd']")
    SUBMIT = (By.CSS_SELECTOR, "input.submit_login, input[type='submit']")
    HIDDEN_REDIRECT = (By.CSS_SELECTOR, "input[name='r']")
    OAUTH_LINK = (By.PARTIAL_LINK_TEXT, "Đăng nhập bằng e-mail UTC")
    FORGOT_LINK = (By.PARTIAL_LINK_TEXT, "quên mật khẩu")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def open(self):
        self.driver.get(LOGIN_URL)
        self.wait.until(EC.presence_of_element_located(self.USERNAME))
        return self

    def set_username(self, value):
        el = self.driver.find_element(*self.USERNAME)
        el.clear()
        if value:
            el.send_keys(value)
        return self

    def set_password(self, value):
        el = self.driver.find_element(*self.PASSWORD)
        el.clear()
        if value:
            el.send_keys(value)
        return self

    def submit(self):
        self.driver.find_element(*self.SUBMIT).click()
        return self

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.submit()
        return self

    # ----- Trạng thái / kiểm tra -----
    def page_text(self):
        return self.driver.find_element(By.TAG_NAME, "body").text

    def wait_for_text(self, text):
        """Chờ tới khi text xuất hiện trong body; trả về True/False.

        Bọc try/except bên trong mỗi lần poll để không thoát sớm khi trang
        đang reload sau POST (StaleElement/NoSuchElement trong lúc điều hướng).
        """
        def _has_text(d):
            try:
                return text in d.find_element(By.TAG_NAME, "body").text
            except Exception:
                return False

        try:
            self.wait.until(_has_text)
            return True
        except Exception:
            return False

    def is_on_login_page(self):
        """Còn ở trang Login nghĩa là CHƯA đăng nhập thành công."""
        try:
            self.driver.find_element(*self.PASSWORD)
            return "/Login" in self.driver.current_url or "Đăng nhập" in self.driver.title
        except Exception:
            return False

    def password_value(self):
        return self.driver.find_element(*self.PASSWORD).get_attribute("value")

    def redirect_value(self):
        return self.driver.find_element(*self.HIDDEN_REDIRECT).get_attribute("value")

    def oauth_url(self):
        return self.driver.find_element(*self.OAUTH_LINK).get_attribute("href")
