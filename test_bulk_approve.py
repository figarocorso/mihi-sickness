from playwright.sync_api import Page

from common import login, go_to_attendance


def test_bulk_approve(page: Page):
    login(page)
    go_to_attendance(page)
    go_to_approval(page)
    select_all(page)

    page.locator("//button[@id='BulkActionUpdateByHR']").click()


def go_to_approval(page: Page):
    page.locator("//a[@data-title='Weekly Attendance Approval']").hover()
    page.locator("//a[@data-title='Weekly Attendance Approval']").click()


def select_all(page: Page):
    page.locator("//div[@id='dvSelectAll']").click()
