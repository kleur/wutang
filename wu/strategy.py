
from wu import temporal

def split_months(records):
    units = dict()
    for record in records:
        y = record.date.year
        n = record.date.month
        key = str(y) + '_' + str(n)
        if(units.has_key(key)):
            month = units.get(key)
            month.records.append(record)
        else:
            units.update({key:temporal.Month('Month', y, [record], n)})
    return units

def split_quarters(records):
    units = dict()
    for record in records:
        y = record.date.year
        n = record.quarter
        key = str(y) + '_' + str(n)
        if(units.has_key(key)):
            quarter = units.get(key)
            quarter.records.append(record)
        else:
            units.update({key:temporal.Quarter('Quarter', y, [record], n)})
    return units


