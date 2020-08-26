from selenium.webdriver.common.by import By

from xuexi_selenium_po.test_project_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    def go_to_add_department(self):
        from xuexi_selenium_po.test_project_weixin.page.add_department_page import AddDepartment
        return AddDepartment(self.driver)

    def get_department_list(self):
        name_list = self.finds(By.CSS_SELECTOR, ".jstree-anchor")
        list1 = []

        for name in name_list:
            list1.append(name.text)
        return list1
