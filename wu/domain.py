class Category:
    name = "no-name"
    keywords = []

class Record:
    date="unknown"
    quarter="unknown"
    description="unknown"
    amount="unknown"
    kind="unknown"
    category="unknown"

    def prettyprint(self):
        print("date: %s Q%s amount: %s category: %s" % (self.date.strftime('%Y-%m-%d'), self.quarter, self.amount, self.category))
        if self.category == "unknown":
            print(" descr: %s" % (self.description))

class Repository:
    def __init__(self, bookyears):
        self.bookyears = bookyears

class BookYear:
    def __init__(self, number, months):
        self.number = number
        self.months = months

class Month:
    def __init__(self, number, records):
        self.number = number
        self.records = records
