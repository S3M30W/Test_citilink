from selenium.webdriver.common.by import By


class BasePageLocators():
    ENTER_BUTTON = (By.XPATH,
                    "// div[@class ='IconAndTextWithCount__text_mainHeader IconAndTextWithCount__text' and contains (text(),'Войти')]")
    EMAIL_LINE = (By.XPATH, "//input[@name='login']")
    PASS_LINE = (By.XPATH, "//input[@name='pass']")
