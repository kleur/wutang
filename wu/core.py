# -*- coding: utf-8 -*-
from wu import helpers

categories = []

class Category:
    name = "no-name"
    keywords = []

def get_hmm():
    """Get a thought."""
    helpers.print_dawg()
    return 'hmmm...'

def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())

def execute_me():
    init_categories()
    records = helpers.import_csv()
    apply_categories(records)

def apply_category(record):
    for c in categories:
        keywords = c.keywords
        for keyword in keywords:
            if keyword in record.description:
                record.category = c.name
    record.prettyprint()

def apply_categories(records):
    for r in records:
        apply_category(r)

def create_category(name, keywords):
    category = Category()
    category.name = name
    category.keywords = keywords
    return category

def init_categories():
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