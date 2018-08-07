# -*- coding: utf-8 -*-
from wu import helpers
from wu import strategy

def execute_me():
    categories = helpers.init_categories('test_input/categories.yaml')
    records = helpers.init_records('test_input/finance_records.csv')
    records_categorized = apply_categories(categories, records)
    units = strategy.split_months(records_categorized)
    helpers.print_units(units)

def apply_category(categories, record):
    for c in categories:
        keywords = c.keywords
        for keyword in keywords:
            if keyword in record.description:
                record.category = c.name
    return record

def apply_categories(categories, records):
    categorized = []
    for r in records:
        categorized.append(apply_category(categories, r))
    return categorized

#TODO: introduce main categories > sub categories
#TODO: calculate percentages