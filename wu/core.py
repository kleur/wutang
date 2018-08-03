# -*- coding: utf-8 -*-
from wu import helpers
from wu import domain
from wu import file_reader

def execute_me():
    categories = init_categories('categories.yaml')
    rows = file_reader.import_csv('finance_records.csv')
    records = helpers.to_records(rows)
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

def create_category(name, keywords):
    category = domain.Category()
    category.name = name
    category.keywords = keywords
    return category

def init_categories(filename):
    categories = []
    cats = file_reader.import_yaml(filename)
    for cat in cats:
        for k,v in cat.items():
            categories.append(create_category(k, v))
            print(k, "->", v)
    return categories