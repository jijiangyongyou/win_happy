from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


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

    def test_addcontact(self):
        '''
        企业微信：添加联系人测试用例
        前提条件
            已登录状态（ noReset=True）
        打卡用例：
            1、打开【企业微信】应用
            2、进入【通讯录】
            3、点击【添加成员】
            4、在添加成员页面点击【手动输入添加】
            5、输入【姓名】【性别】【手机号】
            6、点击【保存】
            7、验证保存成功
        '''
        name = "个子"
        gender = '男'
        phonenum = "13960990004"

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        sleep(2)
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/eq7").send_keys(phonenum)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gur").click()
        # sleep(1)
        # toast 弹框,打印当前页面的布局结构 ，xml 结构
        # print(self.driver.page_source)
        toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == toasttext

    def test_delcontact(self):
        name = '小个子'
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
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/duq').click()
        sleep(2)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/b_4').click()
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        searchnum1 = len(eles1)
        assert searchnum1 == searchnum - 1
