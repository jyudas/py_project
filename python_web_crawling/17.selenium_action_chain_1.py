#액션체인 연결하는방식

import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')

# 로그인 링크 클릭
driver.find_element_by_css_selector('.top-nav__login-link').click()
time.sleep(1)

# 아이디 박스, 비밀번호 박스, 로그인 버튼 찾아놓기
id_box = driver.find_element_by_css_selector('.login-container__login-input')
pw_box = driver.find_element_by_css_selector('.login-container__password-input')
login_button = driver.find_element_by_css_selector('.login-container__login-button')

# 액션 실행
(ActionChains(driver)
    .send_keys_to_element(id_box, 'codeit')
    .send_keys_to_element(pw_box, 'datascience')
    .click(login_button)
    .perform())

driver.quit()