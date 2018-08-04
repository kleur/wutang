# -*- coding: utf-8 -*-
from wu import helpers

def execute_me():
    categories = helpers.init_categories('categories.yaml')
    records = helpers.init_records('finance_records.csv')
    records_categorized = apply_categories(categories, records)
    helpers.split_months(records_categorized)

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

#TODO: split records into months