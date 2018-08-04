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

    def prettyprint(self):
        print("-------------------------")
        print(self.get_header())
        print("-------------------------")
        for r in self.records:
            r.prettyprint()
        print("-------------------------")
        print(self.get_totals_line())
        print("-------------------------")
        categories = self.split_categories(self.records)
        for k in categories.keys():
            print("%s : %s" % (k, categories.get(k)))
        print("\n")



    def get_header(self):
        return "Month %s" % self.number

    def get_totals_line(self):
        total_in = 0
        total_out = 0
        amounts = self.get_amounts(self.records)
        for a in amounts:
            if a > 0:
                total_in += a
            else:
                total_out += a
        return "total in: %s total out: %s end total: %s" % (total_in, total_out, self.get_total(amounts))

    def get_total(self, amounts):
        total = 0
        for a in amounts:
            total += a
        return total

    def get_amounts(self, records):
        amounts = []
        for r in records:
            amounts.append(r.amount)
        return amounts

    def split_categories(self, records):
        categories = dict()
        for r in records:
            key = r.category
            if categories.has_key(key):
                categories[key] += r.amount
            else:
                categories.update({key:r.amount})
        return categories
