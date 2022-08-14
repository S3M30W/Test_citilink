from selenium.webdriver.common.by import By


class BasePageLocators():
    ENTER_BUTTON = (By.XPATH,
                    "// div[@class ='IconAndTextWithCount__text_mainHeader IconAndTextWithCount__text' and contains (text(),'Войти')]")
    EMAIL_LINE = (By.XPATH, "//input[@name='login']")
    PASS_LINE = (By.XPATH, "//input[@name='pass']")
    COME_BUTTON = (By.XPATH,
                   "//button[@type='submit' and @class='SignIn__button js--SignIn__action_sign-in Button jsButton Button_theme_primary Button_size_m Button_full-width']")
    OPENING_CHECK = (By.XPATH, "//div[@class='HeaderUserName__name']")
    SEARCH_LINE = (By.CSS_SELECTOR,
                   "div[class='MainHeader__search'] div div form div div [class='SearchQuickResult__input-wrapper'] div label input")
