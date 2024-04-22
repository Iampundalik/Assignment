Feature: Amazon Shopping Cart Automation

  Scenario: Adding a "Monitor" Item in Cart and verifying sub total
    Given I open Amazon.com
    When I search for "Monitor"
    And I select the first item from the list
    And I add the item to cart
    Then I verify the price and subtotal in the cart

  Scenario: Adding a "Laptop" Item in Cart and verifying sub total
    Given I open Amazon.com
    When I search for "Laptop"
    And I select the second item from the list
    And I add the item to cart
    Then I verify the price and subtotal in the cart

  Scenario: Adding two items in Cart and verifying sub total
    Given I open Amazon.com
    When I search for "Headphones"
    And I select the first item from the list
    And I add the first item to cart
    And I search for "Keyboard"
    And I select the first item from the list
    And I add the second item to cart
    Then I verify the prices and subtotal in the cart
