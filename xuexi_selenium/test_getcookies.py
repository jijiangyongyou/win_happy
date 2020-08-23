from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDome():
    def setup_method(self, method):
        #复用浏览器  要先关闭所有窗口在命令行输入： /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)

    def teardown_method(self, method):
        self.driver.quit()

    def test_cookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
