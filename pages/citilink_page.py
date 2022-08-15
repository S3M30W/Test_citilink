from base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from time import sleep


class SearchHelper(base_page.BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_the_registration_button(self):
        registration_field = self.is_present(BasePageLocators.ENTER_BUTTON)
        registration_field.click()
        return registration_field

    def enter_word_EMAIL(self, word: str) -> WebElement:
        EMAIL_field = self.is_present(BasePageLocators.EMAIL_LINE)
        EMAIL_field.click()
        EMAIL_field.send_keys(word)  # (word, Keys.ENTER) Keys.RETURN-Нажать Enter
        return EMAIL_field

    def enter_word_PASS(self, word: str) -> WebElement:
        PASS_field = self.is_present(BasePageLocators.PASS_LINE)
        PASS_field.send_keys(word)  # (word, Keys.ENTER) Keys.RETURN-Нажать Enter
        return PASS_field

    def click_on_the_registration_COME(self):
        COME_field = self.is_present(BasePageLocators.COME_BUTTON)
        COME_field.click()
        return COME_field

    def PAGE_opening_check(self):
        opening_check = self.is_present(BasePageLocators.OPENING_CHECK)
        return opening_check

    def enter_word_Search(self, word: str) -> WebElement:
        PASS_field = self.is_present(BasePageLocators.SEARCH_LINE)
        PASS_field.send_keys(word, Keys.ENTER)  # (word, Keys.ENTER) Keys.RETURN-Нажать Enter
        return PASS_field

    def PAGE_txte_check(self):
        opening_txte = self.is_present(BasePageLocators.TEXT_CHECK)
        return opening_txte

    def click_on_the_favorites_button(self):
        favorites_button = self.is_present(BasePageLocators.FAVORITES_BUTTON_1)
        favorites_button.click()
        return favorites_button

    def click_on_the_favorites_button2(self):
        favorites_button2 = self.is_present(BasePageLocators.FAVORITES_BUTTON_2)
        favorites_button2.click()
        return favorites_button2

    def click_on_the_favorites_button3(self):
        favorites_button3 = self.is_present(BasePageLocators.FAVORITES_BUTTON_3)
        favorites_button3.click()
        return favorites_button3

    def PAGE_txte_check_Air(self):
        opening_txte_Air = self.is_present(BasePageLocators.TEXT_CHECK_AIR)
        return opening_txte_Air

    def click_on_the_favorites_in_button(self):
        favorites_button4 = self.is_present(BasePageLocators.FAVORITES_BUTTON_4)
        favorites_button4.click()
        return favorites_button4

    def click_on_the_favorites_editorial(self):
        editorial_favorites_button4 = self.is_present(BasePageLocators.EDITORIAL_FAVORITES)
        editorial_favorites_button4.click()
        return editorial_favorites_button4

    def click_on_the_buy_everything(self):
        buy_everything = self.is_present(BasePageLocators.BUY_EVERYTHING_BUTTON)
        buy_everything.click()
        return buy_everything

    def click_on_the_BUTTON_basket(self):
        BUTTON_basket = self.is_present(BasePageLocators.BASKET_BUTTON)
        BUTTON_basket.click()
        return BUTTON_basket

    def txte_check_basket(self):
        opening_txte_Air = self.is_present(BasePageLocators.BASKET_CHECK)
        return opening_txte_Air

    def click_on_favorites_BUTTON_all_delete(self):
        all_delete = self.is_present(BasePageLocators.DELETE_ALL_BUTTON)
        all_delete.click()
        return all_delete

    def click_on_basket_BUTTON_delete(self):
        basket_BUTTON_delete = self.is_present(BasePageLocators.DELETE_ALL_BASKET)
        basket_BUTTON_delete.click()
        return basket_BUTTON_delete

    def click_on_basket_BUTTON_delete_all(self):
        basket_BUTTON_delete_all = self.is_present(BasePageLocators.DELETE_ALL_BUTTON)
        basket_BUTTON_delete_all.click()
        return basket_BUTTON_delete_all

    def check_on_basket_delete_all(self):
        basket_BUTTON_delete_all = self.is_present(BasePageLocators.BAY_BASKET)
        basket_BUTTON_delete_all.click()
        return basket_BUTTON_delete_all

    def click_on_the_favorites_basket(self):
        favorites_basket = self.is_present(BasePageLocators.BASKET_CHECK)
        favorites_basket.click()
        return favorites_basket

    def click_on_BUTTON_go_in_basket(self):
        go_in_basket = self.is_present(BasePageLocators.BASKET_BUTTON)
        go_in_basket.click()
        return go_in_basket

    def click_on_BUTTON_add_from_basket_to_favorites(self):
        go_in_basket = self.is_present(BasePageLocators.ADD_FROM_BASKET_TO_FAVORITES)
        go_in_basket.click()
        return go_in_basket

