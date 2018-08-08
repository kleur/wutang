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

    def prettyprint(self, incl_descr):
        print(self.to_string() + (self.get_descr_str() if incl_descr else ""))

    def prettyprint_short(self, incl_descr):
        print("%s Q%s %s %s" % (self.date.strftime('%Y-%m-%d'), self.quarter, self.amount, self.category) + (" " + self.description if incl_descr else ""))

    def print_unknown_from(self, amount):
        if(self.category == "unknown"):
            self.print_from(amount)

    def print_from(self, amount):
        if(self.amount > abs(amount)):
            print(self.to_string() + self.get_descr_str())

    def get_descr_str(self):
        return "descr: %s" % (self.description)

    def to_string(self):
        return "date: %s Q%s amount: %s category: %s " % (self.date.strftime('%Y-%m-%d'), self.quarter, self.amount, self.category)
