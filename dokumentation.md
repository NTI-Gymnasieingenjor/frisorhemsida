# Project documentation

## Branches

In this project we make use of two branches: `master` and `development`. This is so that we can push code to `development` without making any changes to the current GitLab Pages-website, aka `master`. If we are forced to push code for various reasons we can do it easily without risk of intervening with the current live webpage.


### Live Server

#

`Live server` is a good way to check changes quickly.

When you're working on a webpage and want to see your changes quickly you don't look at the online webpage  after commiting and pushing the code. Rather you would work on it locally berfore pushing your changes to the real deal. However making changes and then having to save your code and then refreshing your browser every singe time is not a very efficient way to work in the long run.

VS Code's `Live Server` is an extenstion that allows you to set upp a live server that displays your website in a browser. Except with this it updates live when you save your code and not when you refresh your browser. This can save lots of time and makes the overall workflow way smother.

Setup:

- In VS Code go to extensions on your left menu or press [CTRL + Shift + X]

- Search for "`Live Server`"

- Click on the first one and press install 

- `IMPORTANT:` Open the file you wish to see live with "Open Folder" and `not` "Open File"

- Open your desired file

- Press the `"Go Live"` button in the bottom right corner

- After a few seconds it will show your current file in your standard browser

### Live Share

#

Two or more people on the same code.

Live Share makes it possible for two or more people to work on the same code at the same time on diffrent set-ups. This is incredibly useful when people have to participate from home. One person can host and other people can join in and work on the same thing.

However it's not perfect as only the one hosting can actually execute code. If many changes are made at the same time and somebody want to revert with [CTRL + Z] it could mess with what other people are working on. We use this mostly to pinpoint mistakes and add thing from home. You could also make a read only session if you only want people to read.

Setup:

- In VS Code go to extensions on your left menu or press [CTRL + Shift + X]

- Search for "`Live Share`"

- Click on the first one and press install 

- On your left menu you should now see an added icon `"Live Share"`

- Decide if you want to join a session or start one 

- Starting a session:
    - Press "Start collaboration session.."
    - On the bottom right you will see that VS Code copied the link
    - Send the link to whomever you wish to join

 - Joining a session:
    - Press "Join collaboration session..."
    - In the pop-up window paste the URL you got and VS Code does the rest

#