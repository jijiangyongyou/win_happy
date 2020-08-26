from selenium import webdriver
from selenium.webdriver.common.by import By

from xuexi_selenium_po.test_project_weixin.page.base_page import BasePage
from selenium.webdriver.support.select import Select

from xuexi_selenium_po.test_project_weixin.page.contact_page import ContactPage


class AddDepartment(BasePage):
    def add_department(self,department):
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        self.find(By.NAME, 'name').send_keys(department)
        self.find(By.CSS_SELECTOR, '.js_parent_party_name').click()
        self.find(By.CSS_SELECTOR, '.qui_dialog_body [id="1688853082989370_anchor"]').click()
        self.find(By.LINK_TEXT, '确定').click()
        return ContactPage()

    def get_department_error_message(self):
        return self.driver.find_element(By.ID,'js_tips').text