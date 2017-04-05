# dailyQuote Repo
I have a passion for quotes. I collect them and have always kept notes on all of my favorite quotes and will browse them from time to time. The thought came to me that it would be great to start work every day with a quote from my quote list, so I wrote a python script that will have command prompt pop up with one of the quotes from my list that I keep in a text file. As I continue to add quotes to that file they get added to the quotes that randomly get selected to pop up each day.

# How to Use this script
Download and save the DailyQuote.py file somewhere and save your quotes.txt file in the same folder/file location.

Then go to your Windows settings and open up "Task Scheduler".
Under Actions on the right you must click "Create Task..."

    Fill in the name and Description how you like ex: Run Quote Script, daily quote script
    Then under the "Triggers" tab create a new Trigger.
      Set Begin the task: to "On workstation unlock"
      and check the "Stop task if it runs longer than:" and set to "1 hour"

    Then under the "Actions" tab create a new Action.
      Select Action: "Start a program"
      then browse to where you have the DailyQuote.py script and select that. Click OK.
    Click OK and create this task.

You should be good to go. Lock your computer and on unlock you should get a random quote from your quotes.txt file.

# Conditions/Logic assumptions
Each quote must be on a separate line in your quotes.txt file and each quote is one line.
There are quotes in your quotes.txt file.
There are no blank lines in your quotes.txt file.

## Thanks and I hope you like my daily quote popup!
