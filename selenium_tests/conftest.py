"""Fixtures dùng chung cho pytest + Selenium."""
import os
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.insert(0, os.path.dirname(__file__))  # cho phép import config / pages

from config import HEADLESS  # noqa: E402
from pages.login_page import LoginPage  # noqa: E402


@pytest.fixture
def driver():
    opts = Options()
    if HEADLESS:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1366,900")
    opts.add_argument("--lang=vi-VN")
    # Selenium Manager tự tải chromedriver phù hợp với Chrome đã cài
    drv = webdriver.Chrome(options=opts)
    drv.set_page_load_timeout(40)
    yield drv
    drv.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver).open()
