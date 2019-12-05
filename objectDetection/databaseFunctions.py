# Daniel Sealand
# 18 November 2019
# Migrating Firebase functionality from website to Pi

class FirebaseFunctions:

    # retrieve current count value
    def getCount(self, database):
        return database.get('/count/value', None)

    # update value of count in database to count
    def updateCount(self, database, count):
        database.put('/count', "value", count)
    
    # push history entry to database
    def pushEntry(self, database, value, weekday, hour, minute, meal):
        entry = {
            value: value,
            weekday: weekday,
            hour: hour,
            minute: minute,
            meal: meal
        }
        database.put('/history', entry)

#    def getMeal(self, date, time):
#        # returns string of current meal based on current time
#        if time.hour <= 19 and time.hour >= 17:
#            return "dinner"
#        if date.day == 0 or date.day == 6:
#            if (time.hour == 12 and time.minute <= 45) or (time.hour == 10 and time.minute >= 30) or (time.hour == 11):
#                return "brunch"
#            return "closed"
#        
#        else if (time.hour == 7 and time.minute >= 30) or (time.hour == 9 and time.minute <= 30) or (time.hour == 8):
#            return "breakfast"
#        else if (time.hour == 11 and time.minute >= 15) or (time.hour == 13 and time.minute <= 15) or (time.hour == 12):
#            return "lunch"
#        return "closed"
