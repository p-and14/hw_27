import json
import csv

ads_list = []

with open("ads.csv") as f:
    csv = csv.DictReader(f)
    for row in csv:
        fields = {
            "name": row['name'],
            "author": row['author'],
            "price": int(row['price']),
            "description": row['description'],
            "address": row['address'],
            'is_published': True if row['is_published'] == 'TRUE' else False,
        }

        ad = {
            "model": "ads.ad",
            "pk": int(row['Id']),
            "fields": fields
        }

        ads_list.append(ad)

with open("ads.json", "w") as f:
    json.dump(ads_list, f, ensure_ascii=False, indent=2)
