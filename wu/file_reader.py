import csv
import yaml

def import_csv(filename):
    rows = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            rows.append(row)
    return rows

def import_yaml2(filename):
    with open("categories.yaml", 'r') as stream:
        try:
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)

def import_yaml(filename):
    roots = []
    stream = open(filename, "r")
    docs = yaml.load_all(stream)
    for doc in docs:
        roots.append(doc)
    return roots
