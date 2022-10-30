import json

from playwright.sync_api import Page


CONFIG_FILE = "config.json"


def login(page: Page):
    config = load_config()
    page.goto("https://2.mihi.info/Account/Login")
    page.locator("(//div[@id='loginForm']//input[@id='txtUserName'])[1]").fill(config["username"])
    page.locator("(//div[@id='loginForm']//input[@class='password'])[1]").fill(config["password"])
    page.locator("(//div[@id='loginForm']//input[@id='CompanyCode'])[1]").fill(config["company_code"])
    page.locator("(//div[@id='loginForm']//button[@id='loginBtn'])[1]").click()


def load_config():
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)
    return config


def go_to_attendance(page: Page):
    page.locator("//div[@id='db_banner']//div[@class='banner-details']").click()
    page.locator("(//a[@data-title='Attendance'])[1]").click()
    page.locator("(//a[@data-title='Attendance'])[1]").click()
