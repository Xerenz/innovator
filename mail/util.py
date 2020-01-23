import csv
import json

def csv_to_json(file):
	data = []

	with open(file) as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			doc = {}
			doc['name'] = row[7]
			doc['email'] = row[8]
			doc['phone'] = row[9]
			doc['topic'] = row[6]

			data.append(doc)

	out = json.dumps(data, indent=4)
	with open('data.json', 'w') as f: 
		f.write(out)
