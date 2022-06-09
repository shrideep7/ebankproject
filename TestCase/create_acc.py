import time
import random
import string

from PageObject.Loginpage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from Utilities.Add_customer_utils import Add_customer


class Test_001_login:
    baseurl = ReadConfig.getApplicationURL()
    user_id = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("************Test_001_login running****************")
        self.logger.info("************** test_login is going to check********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.logger.info("**************successfully entered into url************")
        self.LP = LoginPage(self.driver)

        self.LP.setusername(self.user_id)
        self.LP.setpassword(self.password)
        self.LP.clicklogin()
        self.logger.info("**************successful login ************* ")
        self.cust = Add_customer(self.driver)
        self.cust.customer_menu_click()
        self.logger.info("**************successfully grabbed add customer page ")
        time.sleep(3)

        self.cust.customer_name("SHRIDHAR")
        self.cust.gender_option("male")
        self.cust.date_of_birth("25-08-1999")
        self.cust.address("plot number 207 anand nagar 1  majarewadi road sloapur ")
        self.cust.city("solapur")
        self.cust.state("maharashtra")
        self.cust.pin_number("413003")
        self.cust.mobile_number("8347032974")
        self.email = random_generator() + "@gmail.com"
        self.cust.email_id(self.email)
        self.cust.email_password("shri123")
        self.cust.click_submit()
        self.logger.info("added all information about customer. ")
        self.cust_id = self.cust.customer_id()
        self.logger.info("customer id is created ")
        self.cust.new_account()
        self.logger.info("**************creating account and  making deposit ")
        self.cust.add_cust_id(self.cust_id)
        self.cust.account_pref("Current")
        self.cust.initial_deposit("20000")
        self.cust.deposit_submit()


        self.LP.clicklogout()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        self.driver.close()
        self.logger.info("**************successfully passed the test")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
