from time import sleep

from playwright.sync_api import Page

from common import login, go_to_attendance


def test_bulk_approve(page: Page):
    login(page)
    go_to_attendance(page)
    go_to_daily_attendance(page)
    select_all(page)
    sleep(2)
    submit(page)
    sleep(2)


def go_to_daily_attendance(page: Page):
    page.locator("//a[@data-title='Weekly Attendance']").hover()
    page.locator("//a[@data-title='Weekly Attendance']").click()


def select_all(page: Page):
    page.locator("//input[@class='selectall hidden']/parent::*").click()


def submit(page: Page):
    page.locator("//button[@id='saveMultipleAttendance']").click()
