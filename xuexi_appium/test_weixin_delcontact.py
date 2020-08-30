from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


def delcontact():
    with open("./datas/delcontacts.yml") as f:
        datas = yaml.safe_load(f)
    return datas


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 保持登陆的状态
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('name', delcontact())
    def test_delcontact(self, name):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/guu').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fk1').send_keys(name)
        sleep(2)
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        searchnum = len(eles)
        if searchnum < 2:
            print('没有可删除的人员')
            return
        eles[1].click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/guk').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/azd').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/duq').click()
        sleep(2)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/b_4').click()
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        searchnum1 = len(eles1)
        assert searchnum1 == searchnum - 1
