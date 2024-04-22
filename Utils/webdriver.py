from selenium import webdriver

class WebDriver:
    @staticmethod
    def create_driver():
        options = webdriver.Chrome()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)

