import calendar

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
        descr = "<< descr: %s >>" % (self.description) if self.category == "unknown" else ""
        print(self.to_string() + descr)

    def to_string(self):
        return "date: %s Q%s amount: %s category: %s " % (self.date.strftime('%Y-%m-%d'), self.quarter, self.amount, self.category)
