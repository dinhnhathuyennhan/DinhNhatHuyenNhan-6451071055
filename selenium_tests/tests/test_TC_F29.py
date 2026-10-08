"""TC_F29: Thông báo sai user vs sai password nên giống nhau (chống dò tài khoản)."""
import config as cfg


def test_TC_F29_error_message_no_user_enumeration(login_page):
    login_page.login("chac_chan_khong_ton_tai_abcxyz", "whatever123")
    assert login_page.wait_for_text(cfg.MSG_WRONG_CREDENTIAL), (
        "Thông báo nên là thông điệp chung, không tiết lộ tài khoản có tồn tại hay không"
    )
