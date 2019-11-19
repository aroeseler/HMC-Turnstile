# Daniel Sealand
# 18 November 2019
# Migrating Firebase functionality from website to Pi

class FirebaseFunctions:
    # reset count entry in database to 0
    def resetCount(self, database):
        database.update('/count', "value", 0)

    def updateCount(self, database, count):
        database.put('/count', "value", count)
