import csv

instamojo_list = []
firebase_list = []

with open('innova.csv') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		firebase_list.append(row)

with open('Transaction.csv') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		instamojo_list.append(row[9])

unique = []

for i in set(instamojo_list):
	for reg in firebase_list:
		if i in reg:
			unique.append(reg)

with open('innovator summit.csv', 'w') as f:
	writer = csv.writer(f, delimiter=',')
	for row in unique:
		writer.writerow(row)