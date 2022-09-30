import json
import csv

categories_list = []

with open("categories.csv") as f:
    csv = csv.DictReader(f)
    for row in csv:
        fields = {"name": row["name"]}

        categories = {
            "model": "ads.categories",
            "pk": int(row['id']),
            "fields": fields
        }

        categories_list.append(categories)

with open("categories.json", "w") as f:
    json.dump(categories_list, f, ensure_ascii=False, indent=2)
