# -*- coding: utf-8 -*-
from wu import helpers
from wu import domain
from wu import csv_reader

def execute_me():
    categories = init_categories()
    rows = csv_reader.import_csv('finance_records.csv')
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

def init_categories():
    categories = []
    categories.append(create_category("sparen", ["spaarrekening"]))
    categories.append(create_category("wonen", ["YMERE", "DRINKWATER", "moneys"]))
    categories.append(create_category("verzekering", ["D.S.W. Zorgverzekeraar"]))
    categories.append(create_category("telecom", ["Telfort"]))
    categories.append(create_category("auto", ["TEXACO"]))
    categories.append(create_category("supermarkt", ["Albert Heijn", "DEEN"]))
    categories.append(create_category("media", ["Netflix", "videoland"]))
    categories.append(create_category("sport", ["Basic Fit"]))
    categories.append(create_category("lunch", ["Vitam"]))
    categories.append(create_category("diversen", ["DEBETRENTE"]))
    categories.append(create_category("contributie", ["Reunistenbijdrage"]))
    categories.append(create_category("contributie", ["Reunistenbijdrage"]))
    return categories