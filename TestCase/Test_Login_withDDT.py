from PageObject.Loginpage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from Utilities import xlutils


class Test_002_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    path = ".//TestData/LoginDatafor_ebank.xlsx"

    def test_login_by_DDT(self, setup):
        self.driver = setup
        self.LP = LoginPage(self.driver)
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.rows = xlutils.getrowcount(self.path, 'Sheet1')
        print("number of rows :", self.rows)
        self.user_id = xlutils.readData(self.path, "Sheet1", 2, 1)
        self.user_password = xlutils.readData(self.path, 'Sheet1', 2, 2)
        self.logger.info("*************started test_login_by_DDT************* ")


        self.LP.setusername(self.user_id)
        self.LP.setpassword(self.user_password)
        self.LP.clicklogin()

        act_title = self.driver.title
        exp_title = "Guru99 Bank Manager HomePage"
        if act_title == exp_title:
            self.LP.clicklogout()
            alertwindow = self.driver.switch_to.alert
            alertwindow.accept()

            self.driver.close()

        self.logger.info("*************end of login ddt test case")
        self.logger.info("******************** completed Test_002_Login_DDT")
