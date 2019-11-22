import time
from firebase import firebase
from databaseFunctions import FirebaseFunctions
from datetime import datetime

# create time object
time = datetime.time()
date = datetime.date()

while True:
    # push new history entry every 5 seconds
    if (t.second % 5) == 0:
        meal = firebase.getMeal(date, time)
        database.pushEntry(firebase, count, t.day, t.hour, t.minute, meal)