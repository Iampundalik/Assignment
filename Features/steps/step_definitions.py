from behave import *
from Pages.base_page import BasePage
from Pages.product_page import ProductPage

@given('I open Amazon.com')
def open_amazon(context):
    context.base_page = BasePage(context)
    context.base_page.open_amazon()

@when('I search for "{item}"')
def search_item(context, item):
    context.base_page.search_item(item)

@when('I select the first item from the list')
def select_first_item(context):
    context.product_page = ProductPage(context)
    context.product_page.select_first_item()

@when('I select the second item from the list')
def select_second_item(context):
    context.product_page.select_second_item()

@when('I add the item to cart')
def add_to_cart(context):
    context.product_page.add_to_cart()

@when('I add the first item to cart')
def add_first_item_to_cart(context):
    context.product_page.add_first_item_to_cart()

@when('I add the second item to cart')
def add_second_item_to_cart(context):
    context.product_page.add_second_item_to_cart()

@then('I verify the price and subtotal in the cart')
def verify_cart(context):
    context.product_page.verify_cart()
