from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_name = "uid"
    textbox_password_name = "password"
    button_login_name = "btnLogin"
    button_reset_name = "btnReset"
    link_logout_xpath = "//a[normalize-space()='Log out']"

    def __init__(self, driver):
        self.driver = driver

    def setreset(self):
        self.driver.find_element(by=By.NAME, value=self.button_reset_name).click()

    def setusername(self, username):
        self.driver.find_element(by=By.NAME, value=self.textbox_username_name).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(by=By.NAME, value=self.textbox_password_name).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(by=By.NAME, value=self.button_login_name).click()

    def clicklogout(self):
        self.driver.find_element(by=By.XPATH, value=self.link_logout_xpath).click()