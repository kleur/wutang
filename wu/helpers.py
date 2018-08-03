from wu import domain
from wu import file_reader

def init_records(filename):
    rows = file_reader.import_csv(filename)
    records = to_records(rows)
    return records

def init_categories(filename):
    categories = []
    cats = file_reader.import_yaml(filename)
    for cat in cats:
        for k,v in cat.items():
            categories.append(create_category(k, v))
    return categories

def to_records(rows):
    records = []
    for row in rows:
        record = to_record(row)
        records.append(record)
    return records

def to_record(row):
    date = row[0]
    amount = to_amount(row[6], row[5])
    kind = row[7]
    desc_str = row[1] + " " + row[8]
    return make_record(date, amount, kind, desc_str)

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

def create_category(name, keywords):
    category = domain.Category()
    category.name = name
    category.keywords = keywords
    return category