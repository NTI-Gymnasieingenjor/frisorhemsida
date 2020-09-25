# Project documentation

## Branches

In this project we make use of two branches: `master` and `development`. This is so that we can push code to `development` without making any changes to the current GitLab Pages-website, aka `master`. If we are forced to push code for various reasons we can do it easily without risk of intervening with the current live webpage.

### Run Validation 

#

Both the HTML and CSS codes are validated through automatic tests. Tests can look on the code locally or online depending on what file you run.

How to run a validation test:

    - In "tests" located in the repository you can find four different validation tests

    - Just execute one of the four files in your respective code environment to validate the code locally or online:

        - "css_local_validation" tests the CSS code locally in the "public/css" folder with Selenium in chrome
        
        - "css_online_validation" tests the CSS code online with Selenium in chrome

        - "html_local_validation" tests the HTML code locally in the "public" folder with Selenium in chrome

        - "html_online_validation" tests the HTML code online with Selenium in chrome

    - All of these tests will give feedback in the terminal directly from the respective validators


### Run tests 

#

Tests are for checking if everything is on the page. (Right now we need to start them manually before we push)

    How to start website tests with Selenium in Python:

        - Install Python 3.8.5 (during installation check box Add Python to path, then reboot your system)

        - If you want to test website locally from index.html (execute tests_local.py in your code environment)

        - If you want to test website online from URL (execute tests_online.py in your code environment)

        - The test passes when you get message "Code is working excellent" otherwise it will show error code with specific line

    How to create website tests with Selenium in Python (method is same for local and online tests):

        - Open tests folder in your code environment

        - Create a variable named element

        - If you want to find text on a website you can use " driver.find_element_by_xpath("//*[contains(text(), 'yourText')]") "

        - If you want to find text/photos on a website you can use " driver.find_element_by_id('yourIdInHtml') " (remember to add id in respective html file)

### Selenium

#

Extension for Python

Selenium is a tool used to control websites with code. With the extension for Python we can use Python code to remotely access a website and do things such as clicks. This is great for things such as our automatic HTML Validator etc.

Setup: 

    - Open the Command Prompt

    - Type "pip install selenium"

    - To use, type "from selenium import ..."
    
    - See code comments for more information regarding the use of Selenium        

### Live Server

#

`Live server` is a good way to check changes quickly.

When you're working on a webpage and want to see your changes quickly you don't look at the online webpage after committing and pushing the code. Rather you would work on it locally before pushing your changes to the real deal. However making changes and then having to save your code and then refreshing your browser every singe time is not a very efficient way to work in the long run.

VS Code's `Live Server` is an extension that allows you to set up a live server that displays your website in a browser. Except with this it updates live when you save your code and not when you refresh your browser. This can save lots of time and makes the overall workflow way smoother.

Setup:

    - In VS Code go to extensions on your left menu or press [CTRL + Shift + X]

    - Search for "Live Server"

    - Click on the first one and press install 

    - IMPORTANT: Open the file you wish to see live with "Open Folder" and NOT "Open File"

    - Open your desired file

    - Press the "Go Live" button in the bottom right corner

    - After a few seconds it will show your current file in your standard browser

### Live Share

#

Two or more people on the same code.

Live Share makes it possible for two or more people to work on the same code at the same time on different set-ups. This is incredibly useful when people have to participate from home. One person can host and other people can join in and work on the same thing.

However it's not perfect as only the one hosting can actually execute code. If many changes are made at the same time and somebody wants to revert with [CTRL + Z] it could mess with what other people are working on. We use this mostly to pinpoint mistakes and add things from home. You could also make a read only session if you only want people to read.

Setup:

    - In VS Code go to extensions on your left menu or press [CTRL + Shift + X]

    - Search for "Live Share"

    - Click on the first one and press install 

    - On your left menu you should now see an added icon "Live Share"

    - Decide if you want to join a session or start your own

    - Starting a session:
        - Press "Start collaboration session.."
        - On the bottom right you will see that VS Code copied the link
        - Send the link to whomever you wish to join

    - Joining a session:
        - Press "Join collaboration session..."
        - In the pop-up window paste the URL you got and VS Code does the rest




