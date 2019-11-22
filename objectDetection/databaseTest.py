import time
from firebase import firebase
from databaseFunctions import FirebaseFunctions
from datetime import time
from datetime import datetime
import pytz

# create time object
time = time()
date = datetime.now(pytz.utc)

firebase = firebase.FirebaseApplication("https://flipper-glob-webpage.firebaseio.com")

print(date)

#while True:
    # push new history entry every 5 seconds
    #if (time.second % 5) == 0:
        # meal = firebase.getMeal(date, time)
    #    print time.second
    #    database.pushEntry(firebase, 0, date.day, time.hour, time.minute, "test")