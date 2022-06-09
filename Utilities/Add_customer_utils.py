from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_customer:
    new_customer_xpath = "/html/body/div[3]/div/ul/li[2]/a"
    customer_name_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input"
    dateofbirth_xpath = "//*[@id='dob']"
    rd_male_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]"
    rd_female_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]"
    address_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[7]/td[2]/textarea"
    city_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[8]/td[2]/input"
    state_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[9]/td[2]/input"
    pin_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[10]/td[2]/input"
    mobile_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[11]/td[2]/input"
    Email_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[12]/td[2]/input"
    password_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[13]/td[2]/input"
    submit_xpath = '/html/body/table/tbody/tr/td/table/tbody/tr[14]/td[2]/input[1]'
    customer_id_xpath = '//*[@id="customer"]/tbody/tr[4]/td[2]'
    new_acc_xpath = '/html/body/div[3]/div/ul/li[5]/a'
    customer_id_input_xpath = '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input'
    acc_pref_xpath = '/html/body/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select'
    deposit_xpath = '/html/body/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input'
    depo_submit_xpath = '/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]'

    continue_xpath = "//*[@id='customer']/tbody/tr[14]/td/a"
    logout_xpath = "/html/body/div[3]/div/ul/li[15]/a"
    add_xpath = "//*[@id='dismiss-button']/div"

    def __init__(self, driver):
        self.driver = driver

    def initial_deposit(self, amt):
        self.driver.find_element(by=By.XPATH, value=self.deposit_xpath).send_keys(amt)

    def deposit_submit(self):
        self.driver.find_element(by=By.XPATH, value=self.depo_submit_xpath).click()

    def account_pref(self, acc_pref):
        a = Select(self.driver.find_element(by=By.XPATH, value=self.acc_pref_xpath))
        a.select_by_visible_text(acc_pref)

    def add_cust_id(self, cust_id):
        self.driver.find_element(by=By.XPATH, value=self.customer_id_input_xpath).send_keys(cust_id)

    def new_account(self):
        self.driver.find_element(by=By.XPATH, value=self.new_acc_xpath).click()

    def customer_id(self):
        st = self.driver.find_element(by=By.XPATH, value=self.customer_id_xpath).text
        return int(st)

    def adv_close(self):
        self.driver.find_element(by=By.XPATH, value=self.add_xpath).click()

    def customer_menu_click(self):
        self.driver.find_element(by=By.XPATH, value=self.new_customer_xpath).click()

    def customer_name(self, name):
        self.driver.find_element(by=By.XPATH, value=self.customer_name_xpath).send_keys(name)

    def date_of_birth(self, dob):
        self.driver.find_element(by=By.XPATH, value=self.dateofbirth_xpath).send_keys(dob)

    def gender_option(self, gender):
        if gender == "male":
            self.driver.find_element(by=By.XPATH, value=self.rd_male_xpath).click()
        else:
            self.driver.find_element(by=By.XPATH, value=self.rd_female_xpath).click()

    def address(self, address):
        self.driver.find_element(by=By.XPATH, value=self.address_xpath).send_keys(address)

    def city(self, city):
        self.driver.find_element(by=By.XPATH, value=self.city_xpath).send_keys(city)

    def state(self, state):
        self.driver.find_element(by=By.XPATH, value=self.state_xpath).send_keys(state)

    def pin_number(self, pin):
        self.driver.find_element(by=By.XPATH, value=self.pin_xpath).send_keys(pin)

    def mobile_number(self, number):
        self.driver.find_element(by=By.XPATH, value=self.mobile_xpath).send_keys(number)

    def email_id(self, email):
        self.driver.find_element(by=By.XPATH, value=self.Email_xpath).send_keys(email)

    def email_password(self, password):
        self.driver.find_element(by=By.XPATH, value=self.password_xpath).send_keys(password)

    def click_submit(self):
        self.driver.find_element(by=By.XPATH, value=self.submit_xpath).click()

    def click_continue(self):
        self.driver.find_element(by=By.XPATH, value=self.continue_xpath).click()
