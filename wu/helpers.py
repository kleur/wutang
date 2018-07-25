from wu import domain

def to_amount(raw_amount, pos):
    from decimal import Decimal
    if(pos == "Af"):
        raw_amount = "-" + raw_amount
    raw_amount = raw_amount.replace(",", ".")
    raw_amount = Decimal(raw_amount)
    return raw_amount

def make_record(date, amount, kind, description):
    myRecord = domain.Record()
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

def import_csv(filename):
    import csv
    rows = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            rows.append(row)
    return rows

def to_records(rows):
    records = []
    for row in rows:
        record = to_record(row)
        records.append(record)
    return records