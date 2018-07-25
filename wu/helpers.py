def to_amount(raw_amount, pos):
    from decimal import Decimal
    if(pos == "Af"):
        raw_amount = "-" + raw_amount
    raw_amount = raw_amount.replace(",", ".")
    raw_amount = Decimal(raw_amount)
    return raw_amount

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

def make_record(date, amount, kind, description):
    myRecord = Record()
    myRecord.date = date
    myRecord.amount = amount
    myRecord.kind = kind
    myRecord.description = description
    return myRecord

def to_record(row):
    date = row[0]
    amount = to_amount(row[6], row[5])
    kind = row[7]
    desc_str = row[1] + " " + row[8]
    return make_record(date, amount, kind, desc_str)

def import_csv():
    records = []
    import csv
    with open('finance_records.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            record = to_record(row)
            records.append(record)
    return records