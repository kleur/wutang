from wu import domain
from wu import file_reader
import datetime
import math

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


def print_months(months):
    for k in months.keys():
        month = months.get(k)
        month.prettyprint()

def split_months(records):
    months = dict()
    for record in records:
        y = record.date.year
        m = record.date.month
        key = str(y) + '_' + str(m)
        if(months.has_key(key)):
            month = months.get(key)
            month.records.append(record)
        else:
            months.update({key:domain.Month(m, [record])})

    print_months(months)
    return months


def to_records(rows):
    records = []
    for row in rows:
        record = to_record(row)
        records.append(record)
    return records

def to_record(row):
    date = to_date(row[0])
    amount = to_amount(row[6], row[5])
    kind = row[7]
    desc_str = row[1] + " " + row[8]
    return make_record(date, amount, kind, desc_str)

def to_date(date_string):
    year = date_string[:4]
    month = date_string[4:6]
    day = date_string[-2:]
    date_object = datetime.datetime(int(year), int(month), int(day))
    return date_object

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
    myRecord.quarter = int(math.ceil(date.month/3))
    myRecord.amount = amount
    myRecord.kind = kind
    myRecord.description = description
    return myRecord

def create_category(name, keywords):
    category = domain.Category()
    category.name = name
    category.keywords = keywords
    return category