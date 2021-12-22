# About
This project aims to create a very basic webapp using Flask that allows for users to submit messages to a database as well as viewing them. 
## Setup
The following guide will provide instructions on how to reproduce this webapp on your own machine. The webapp was created with tools that may be Windows-specific. For this reason, there may be slight differences when following these instructions on Linux or Mac. Note that this setup process makes use of the Anaconda Prompt for Python as well as Flask, a tool used to create webapps. Other necessary packages include `sqlite3`.

First, head to the repository on GitHub at [https://github.com/michaelvchid/Flask-message-bank](https://github.com/michaelvchid/Flask-message-bank) (if you're viewing this on GitHub, you're most definitely on the correct page already). 
Next, look for the green button with the word "Code", and click it to bring a dropdown menu. Then, click download ZIP.

Once this is downloaded, unzip the folder and send the extracted folder to somewhere memorable or where you would like to store the project.

Next, open up the Anaconda Prompt and `cd` into the directory of the downloaded folder so that the current directory contains files such as "app.py" and "messages_db.sqlite".

Now that you are currently in the proper directory, enter on Anaconda Prompt `set FLASK_ENV=development`. The console shouldn't print anything out.

Lastly, enter `flask run`. After loading everything, the console will print out `Running on http://127.0.0.1:5000/`, or have a different address. Copy the address and past it into your favorite web browser. Then, you should be able to view the webapp and interact with it!

## Using The Webapp
On the webapp, three pages are accessible. The first is the introdution page with a simple guide stating that one link is used to submit messages, and the other is to view messages. 
When clicking on the "Submit a message" link, a new page will appear that allows the user to input a message and their name or social media handle. After clicking the submit button, the information will be sent to an SQLite database. 
Clicking on the "View messages" button will display a random subset of messages along with the name/handle of the person who submitted it. To erase all the messages in the database, simply delete the "messages_db.sqlite" file; for those that are familiar with handling such databases, it is also possible to delete certain messages, however this does involve further work as well as knowledge of SQL. 
However, this is enough to get the webapp up and running!
