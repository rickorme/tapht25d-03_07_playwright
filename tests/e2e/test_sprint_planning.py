import re
from playwright.sync_api import Page, expect

url = "https://lejonmanen.github.io/agile-helper/"

def test_can_view_sprint_planning(page: Page):

    # navigate to the sprint planning page
    page.goto(url, timeout=2000)

    # Find & click the button with the test_id "language-en"
    engish_button = page.get_by_test_id("language-en")
    expect(engish_button).to_be_visible()
    engish_button.click()

    # Find & click the button with the test_id "btn-first"
    first_button = page.get_by_test_id("btn-first")
    expect(first_button).to_be_visible()
    first_button.click()

    # click the button containing the text "Sprint planning"
    # planning_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    planning_button = page.locator("button").filter(has_text="Sprint planning")
    expect(planning_button).to_be_visible()
    planning_button.click()

    # test that the heading "Sprint planning" is visible
    heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(heading).to_be_visible(timeout=100)
