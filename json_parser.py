import json
import db

with open('latin_america.json', encoding='utf-8') as f:
    data = json.load(f)

    for i in range(30):
        db.cursor.execute("INSERT INTO countries(region, population, city_name, country, description, image, cost_alone, cost_family) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                          (data[i]['region'], data[i]['population'], data[i]['name'], data[i]['country'], data[i]['descriptionFromReview'],
                           data[i]['image'], data[i]['cost_for_nomad_in_usd'], round(data[i]['cost_for_family_in_usd'])))
        db.connect.commit()