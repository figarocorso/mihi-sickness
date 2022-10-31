from time import sleep

from playwright.sync_api import Page, expect

from common import login, go_to_attendance


def test_bulk_approve(page: Page):
    login(page)
    go_to_attendance(page)
    go_to_approval(page)
    select_all(page)
    sleep(2)
    approve(page)
    sleep(2)


def go_to_approval(page: Page):
    page.locator("//a[@data-title='Weekly Attendance Approval']").hover()
    page.locator("//a[@data-title='Weekly Attendance Approval']").click()


def select_all(page: Page):
    page.locator("//div[@id='dvSelectAll']").click()


def approve(page: Page):
    submit = page.locator("//button[@id='BulkActionUpdateByHR']")
    try:
        expect(submit).to_be_enabled(timeout=2)
    except:
        print("Nothing to approve here")
        return
    submit.click()
    page.locator("//form[@id='AttendanceMultipleApprovalForm']/div[1]/div").click()
    page.locator("//form[@id='AttendanceMultipleApprovalForm']/div[1]//div[@data-value='1']").click()
    page.locator("//button[@id='btnSaveAttendanceMultipleApproval']").click()
