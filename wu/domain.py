class Category:
    name = "no-name"
    keywords = []

class Record:
    date="unknown"
    description="unknown"
    amount="unknown"
    kind="unknown"
    category="unknown"

    def prettyprint(self):
        print("date: %s amount: %s category: %s" % (self.date, self.amount, self.category))
        if self.category == "unknown":
            print(" descr: %s" % (self.description))