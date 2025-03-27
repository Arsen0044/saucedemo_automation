import allure
import pytest
from Logs.Logger import Logger


@allure.suite("Purchase flow tests")
@allure.sub_suite("Purchase flow tests")
class TestPurchaseFlow:

    @allure.title("Test complete flow for purchasing")
    @allure.description("Complete purchasing process and verify order confirmation")
    @pytest.mark.parametrize("product_to_add", ["Sauce Labs Backpack"])
    def test_purchase_flow(self, login_with_standard_user, product_to_add):

        with allure.step("Get Product page"):
            Logger.log.info("Get Product page")
            product_page = login_with_standard_user

        with allure.step("Add item to the cart"):
            Logger.log.info("Add item to the cart")
            product_page.add_product_to_cart_by_name(product_to_add)

        with allure.step("Go to the cart and verify correct item added"):
            Logger.log.info("Navigate to the cart and proceed to checkout")
            cart_page = product_page.navigate_to_cart()

            Logger.log.info("Verify correct product in cart by name")
            assert cart_page.is_correct_product_in_cart_by_name(product_to_add)

        with allure.step("Proceed to checkout"):
            Logger.log.info("Proceed to checkout")
            checkout_page = cart_page.proceed_to_checkout()

        with allure.step("Fill in checkout information and place order"):
            Logger.log.info("Fill in checkout details and place the order")
            checkout_page.fill_in_checkout_details("John", "Doe", "12345")
            checkout_page.place_order()

        with allure.step("Verify order confirmation message"):
            Logger.log.info("Verify order confirmation is displayed")
            assert checkout_page.is_order_confirmation_visible(), "Order confirmation is not displayed"