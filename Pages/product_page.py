from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, context):
        self.driver = context.driver

    def select_first_item(self):
        first_item = self.driver.find_element(By.CSS_SELECTOR, ".s-result-list [data-index='0'] h2 a")
        first_item.click()

    def select_second_item(self):
        second_item = self.driver.find_element(By.CSS_SELECTOR, ".s-result-list [data-index='1'] h2 a")
        second_item.click()

    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()

    def add_first_item_to_cart(self):
        self.select_first_item()
        self.add_to_cart()

    def add_second_item_to_cart(self):
        self.select_second_item()
        self.add_to_cart()

    def get_product_page_price(self):
        price_element = self.driver.find_element(By.ID, "priceblock_ourprice")
        return price_element.text

    def verify_cart(self):
        # Navigate to the cart page
        self.driver.find_element(By.ID, "nav-cart-count").click()
        
        # Get the price from the cart page
        cart_price_element = self.driver.find_element(By.CSS_SELECTOR, ".sc-product-price")
        cart_price = cart_price_element.text
        
        # Get the expected price from the product page
        product_page_price = self.get_product_page_price()
        
        # Assert that the prices match
        assert product_page_price == cart_price, f"Product page price {product_page_price} does not match cart price {cart_price}"
