from PageObject.Loginpage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from Utilities.Add_customer_utils import Add_customer


class Test_003_Add_Customer:
    baseurl = ReadConfig.getApplicationURL()
    user_id = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def add_new_customer(self, setup):
        self.driver = setup
