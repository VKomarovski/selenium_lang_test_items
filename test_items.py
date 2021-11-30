import time


def test_should_be_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')

    # почему просто assert ответ преподавателя в комментариях https://stepik.org/lesson/237240/step/9?auth=registration&discussion=1378429&unit=209628
