import re
from playwright.sync_api import Page, expect

url = "https://lejonmanen.github.io/agile-helper/"

def test_can_view_sprint_planning(page: Page):
    # navigate to the sprint planning page
    # click the button with the text "Första"
    # click the button containing the text "Sprint planning"
    # test that the heading "Sprint planning" is visible

    page.goto(url, timeout=2000)
    first_button = page.get_by_test_id("btn-first")
    expect(first_button).to_be_visible()

    planning_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(planning_button).to_be_visible()
    planning_button.click()

    heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(heading).to_be_visible(timeout=100)
