import time
from firebase import firebase
from databaseFunctions import FirebaseFunctions
import pytz

firebase = firebase.FirebaseApplication("https://flipper-glob-webpage.firebaseio.com")
database = FirebaseFunctions()

def updateTest():
    return database.updateCount(firebase, 100)

while True:
    print("update")
    time.sleep(5.0 - (time.time() % 5.0))