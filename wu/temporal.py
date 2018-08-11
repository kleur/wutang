import calendar

class TemporalUnit:
    def __init__(self, year, unit, records):
        self.year = year
        self.unit = unit
        self.records = records

    def prettyprint(self):
        lines = self.get_lines()
        for line in lines:
            print(line)

    def get_lines(self):
        lines = []
        lines.append("-------------------------")
        lines.append(self.get_header())
        lines.append("-------------------------")
        for r in self.records:
            lines.append(r.to_string_short(True))
        lines.append("-------------------------")
        lines.append(self.get_totals_line())
        lines.append("-------------------------")
        categories = self.split_categories(self.records)
        for k in categories.keys():
            lines.append("%s : %s" % (k, categories.get(k)))
        lines.append("\n")
        return lines

    def get_header(self):
        return "%s %s" % (self.unit, self.year)

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

class Month(TemporalUnit):
    def __init__(self, unit, year, records, number):
        TemporalUnit.__init__(self, year, unit, records)
        self.name = calendar.month_name[number]
        self.number = number

    def get_header(self):
        return "%s %s" % (self.name, self.year)

class Quarter(TemporalUnit):
    def __init__(self, unit, year, records, number):
        TemporalUnit.__init__(self, year, unit, records)
        self.name = 'Q' + str(number)
        self.number = number

    def get_header(self):
        return "%s %s" % (self.name, self.year)