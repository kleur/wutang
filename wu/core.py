# -*- coding: utf-8 -*-
from wu import helpers

def execute_me():
    categories = helpers.init_categories('categories.yaml')
    records = helpers.init_records('finance_records.csv')
    apply_categories(categories, records)

def apply_category(categories, record):
    for c in categories:
        keywords = c.keywords
        for keyword in keywords:
            if keyword in record.description:
                record.category = c.name
    record.prettyprint()

def apply_categories(categories, records):
    for r in records:
        apply_category(categories, r)

#TODO: split records into months