import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDome():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_weixin(self):
        db = shelve.open('mydb/logincookies')
        cookies = db['cookie']
        db.close()
        # 要先打开一个页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        for cookie in cookies:
            # expiry这个key是时间戳可能会有小数会报错
            if 'expiry' in cookie.keys():
                # 如果有就删除
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        self.driver.find_element(By.ID, 'js_upload_file_input').send_keys('/Users/weizhe/Downloads/tongxunlu.xlsx')
        assert 'tongxunlu.xlsx' == self.driver.find_element(By.ID, 'upload_file_name').text
        self.driver.find_element(By.CSS_SELECTOR, '#submit_csv').click()
        sleep(3)
