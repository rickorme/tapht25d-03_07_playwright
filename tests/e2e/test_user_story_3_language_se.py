import re
from playwright.sync_api import Page, expect

url = "https://lejonmanen.github.io/agile-helper/"

def test_can_switch_language_se(page: Page):

    # navigate to the sprint planning page
    page.goto(url, timeout=2000)

    # Find & click the button with the test_id "language-sv"
    swedish_button = page.get_by_test_id("language-sv")
    expect(swedish_button).to_be_visible()
    swedish_button.click()

    # test that the button now have Swedish labels
    button_first = page.get_by_test_id("btn-first")
    button_middle = page.get_by_test_id("btn-middle")
    button_last = page.get_by_test_id("btn-last")
    expect(button_first).to_be_visible()
    expect(button_middle).to_be_visible()
    expect(button_last).to_be_visible()
    expect(button_first).to_have_text("Första", ignore_case=True)
    expect(button_middle).to_have_text("Någonstans mitt i", ignore_case=True)
    expect(button_last).to_have_text("Sista", ignore_case=True)