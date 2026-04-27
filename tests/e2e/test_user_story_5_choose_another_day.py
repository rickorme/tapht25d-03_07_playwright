import re
from playwright.sync_api import Page, expect

url = "https://lejonmanen.github.io/agile-helper/"

def test_choose_another_day(page: Page):

    # navigate to the sprint planning page
    page.goto(url, timeout=2000)

    # Find & click the button with the test_id "language-en"
    engish_button = page.get_by_test_id("language-en")
    expect(engish_button).to_be_visible()
    engish_button.click()

    # Find & click the button with the test_id "btn-middle"
    button_middle = page.get_by_test_id("btn-middle")
    expect(button_middle).to_be_visible()
    button_middle.click()

    # TEMPORARY DEBUGGING: Print all button text
    # run pytest with -s to see the output in the cconsole
    # print("\n--- START BUTTON TEXT DUMP ---")
    # buttons = page.get_by_role("button").all()
    # for btn in buttons:
    #     print(f"Found button with text: '{btn.inner_text()}'")
    # print("--- END BUTTON TEXT DUMP ---\n")


    # Check the page content has changed to be relevant for a "middle" day
    button_choose_another_day = page.get_by_test_id("btn-restart")
    
    # FIX: Use locator combined with a text filter to handle the <strong> tag seamlessly
    button_daily_standup = page.locator("button").filter(has_text="Start every day with Daily standup")
    
    expect(page.get_by_text("Any day during the sprint.")).to_be_visible()
    expect(button_choose_another_day).to_be_visible()
    page.pause()
    expect(button_daily_standup).to_be_visible()