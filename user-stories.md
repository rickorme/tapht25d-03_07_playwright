# User Stories for Agile Helper app
As a Scrum Manager, I want to select the last day of the sprint and from there select Sprint Retrospective, so that I can read how to do a "sprint retrospective".


## Global Layout

### User Story 1

STORY:

    As a user, I want to see the title "Agile helper" in the header of every page so that I always know which app I am using.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Check that the header element contains the text "Agile helper"

## Language    


### User Story 2

STORY:

    As a user, I want to click a British flag in the header to change all app text to English.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button in the header containing the British flag
    3. Check that the text on the page updates to English (e.g., the navigation buttons read "First", "Somewhere in the middle", "Last")

### User Story 3

STORY:

    As a user, I want to click a Swedish flag in the header to change all app text to Swedish.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button in the header containing the Swedish flag
    3. Check that the text on the page updates to Swedish translations


## Navigation and Home Page

### User Story 4

STORY:

    As a user, I want to see a Home page with navigation buttons for "First", "Somewhere in the middle", and "Last" day of the sprint, so that I can access the correct tools and information for my current sprint day.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Check that the buttons "First", "Somewhere in the middle", and "Last" are visible

### User Story 5

STORY:

    As a user, I want to click "Choose another day" on any of the sub-pages so that I can easily navigate back to the Home page.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button with the text "Somewhere in the middle"
    3. Check that the page content changes to display the tasks specific to that phase, along with a "Choose another day" button


## First Day of Sprint

### User Story 6

STORY:

    As a user, I want to click "Begin the sprint with Sprint Planning" to open an info box with guidelines and a link to a "planning poker online" tool, so that I can effectively facilitate the planning session.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button with the text "First"
    3. Click on the button whose text contains "Begin the sprint with Sprint Planning"
    4. Check that a <dialog> element appears on the page, which contains a heading for Sprint Planning and a hyperlink to a "planning poker online" tool

 
### User Story 7

STORY:

    As a user, I want to click "Now we are done. Begin The Sprint!" inside the Sprint Planning info box to close it once the meeting is over.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button with the text "First"
    3. Click on the button whose text contains "Begin the sprint with Sprint Planning"
    4. Click on the button inside the <dialog> with the text "Now we are done. Begin The Sprint!"
    5. Check that the <dialog> element is closed and no longer visible on the page


## Daily Standup (Available on all sub-pages)

### User Story 8

STORY:

    As a user, I want to click "Start every day with Daily Standup" to open an info box containing guidelines on how to run the meeting.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button with the text "Somewhere in the middle"
    3. Click on the button whose text contains "Start every day with Daily Standup"
    4. Check that a <dialog> element appears on the page, containing instructions for the daily standup


### User Story 9

STORY:

    As a user, I want to click a "Start/Begin meeting: 10 minutes" button inside the Standup info box to start a visual countdown timer next to a "Time left" label, ensuring the meeting stays on track.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button with the text "Somewhere in the middle"
    3. Click on the button whose text contains "Start every day with Daily Standup"
    4. Click on the button inside the <dialog> whose text contains "Begin meeting: 10 minutes"
    5. Check that a countdown timer starts ticking down from 10 minutes next to the text "Time left"

### User Story 10

STORY:

    As a user, I want to click "Ok we're done" to close the Standup info box and automatically clear/reset the timer.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button with the text "Somewhere in the middle"
    3. Click on the button whose text contains "Start every day with Daily Standup"
    4. Click on the button inside the <dialog> with the text "Now the meeting is finished"
    5. Check that the <dialog> element closes and the countdown timer is cleared from the screen


## Last Day of Sprint

### User Story 11

STORY:

    As a user, I want to click "Present your work to the Product Owner during Sprint Review" to open an info box with review guidelines.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button with the text "Last"
    3. Click on the button whose text contains "Present your work to the Product Owner during Sprint Review"
    4. Check that a <dialog> element appears on the page, which contains guidelines for the Sprint Review


### User Story 12

STORY:

    As a user, I want to click "Ok, we're done. Onwards to retrospective" to close the Sprint Review info box.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button with the text "Last"
    3. Click on the button whose text contains "Present your work to the Product Owner during Sprint Review"
    4. Click on the button inside the <dialog> with the text "Ok, we're done. Onwards to retrospective"
    5. Check that the <dialog> element is closed and no longer visible on the page

### User Story 13

STORY:

    As a user, I want to click "End the sprint by evaluating your work in Sprint Retrospective" to open an info box with retrospective guidelines.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button with the text "Last"
    3. Click on the button whose text contains "End the sprint by evaluating your work in Sprint Retrospective"
    4. Check that a <dialog> element appears on the page, which contains guidelines for the Sprint Retrospective


### User Story 14

STORY:

    As a user, I want to click "The Sprint is complete" to close the Sprint Retrospective info box.

SCENARIO:

    1. Navigate to the webpage https://lejonmanen.github.io/agile-helper/
    2. Click on the button with the text "Last"
    3. Click on the button whose text contains "End the sprint by evaluating your work in Sprint Retrospective"
    4. Click on the button inside the <dialog> with the text "The Sprint is complete"
    5. Check that the <dialog> element is closed and no longer visible on the page
