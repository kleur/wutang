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
