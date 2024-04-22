from Utils.webdriver import WebDriver

class BasePage:
    def __init__(self, context):
        self.driver = context.driver
        self.base_url = "https://www.amazon.com/"

    def open_amazon(self):
        self.driver.get(self.base_url)

    def search_item(self, item):
        search_field = self.driver.find_element_by_id("twotabsearchtextbox")
        search_field.clear()
        search_field.send_keys(item)
        search_field.submit()
