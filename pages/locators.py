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
    TEXT_CHECK = (By.XPATH, "//h1[@class='Heading Heading_level_1 ProductHeader__title']")
    FAVORITES_BUTTON_1 = (By.XPATH, "//span[@class='ProductCardButton__icon ProductCardButton__icon_default']")
    FAVORITES_BUTTON_2 = (
        By.XPATH,
        "//span[@class='ProductCardButton__icon ProductCardButton__icon_default ProductCardButton__icon_active']")
    FAVORITES_BUTTON_3 = (By.XPATH, "//span[@class='ProductCardButton__icon ProductCardButton__icon_default']")
    TEXT_CHECK_AIR = (By.XPATH, "//h1[@class='Heading Heading_level_1 ProductHeader__title']")
    FAVORITES_BUTTON_4 = (By.XPATH, "//span[@class='ProductCardButton__icon ProductCardButton__icon_default']")
    EDITORIAL_FAVORITES = (By.XPATH,
                           "//button[@class='js--FavouritesLeftSidebar__button-remove-all  Button  jsButton Button_theme_secondary-ghost Button_size_m Button_with-icon Button_full-width']")
    BUY_EVERYTHING_BUTTON = (By.XPATH,
                             "//button[@class='js--FavouritesLeftSidebar__button-buy-all  Button  jsButton Button_theme_primary-ghost Button_size_m Button_with-icon Button_full-width']")
    BASKET_BUTTON = (By.XPATH, "//*[@data-name='basket']")
    BASKET_CHECK = (By.XPATH, "//*[@class='ProductPrice__price OrderFinalPrice__price-current__price']")
