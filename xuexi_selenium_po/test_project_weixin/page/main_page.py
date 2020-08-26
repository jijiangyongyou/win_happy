from selenium import webdriver
from selenium.webdriver.common.by import By

from xuexi_selenium_po.test_project_weixin.page.base_page import BasePage
from xuexi_selenium_po.test_project_weixin.page.contact_page import ContactPage


class MainPage(BasePage):
    # _url就是私有变量  不会被调用到
    _url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    def go_to_contact(self):

        self.find(By.ID, "menu_contacts").click()

        return ContactPage(self.driver)
