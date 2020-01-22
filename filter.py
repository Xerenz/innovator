import csv
import itertools

mapping = {
	'Innovator Summit Ticket - Track-2 - Professional' : ('Combo Track-2', 'Professional'),
	'Innovator Summit Ticket - Track-2 - Student' : ('Combo Track-2', 'Student'),
	'Professional - Session Ticket' : ('Talks Only', 'Professional'),
	'Professional - Workshop ticket' : ('Workshops Only', 'Professional'),
	'Student - Session Ticket' : ('Talks Only', 'Student'),
	'Student - Workshop ticket' : ('Workshops Only', 'Student'),
	"Innovator's Summit Ticket - Track-1 - Student" : ('Combo Track-1', 'Student'),
	"Innovator's Summit Ticket - Track-1 - Professional" : ('Combo Track-1', 'Professional'),
	'Link/Purpose' : ('none', 'none'),
	'Sponsor' : ('none', 'none')
}

with open('Transactions2.csv') as f:
	reader = csv.reader(f, delimiter=',')
	instamojo_list = [row for row in reader]


with open('firebase-db.csv') as f:
	reader = csv.reader(f, delimiter=',')
	firebase_list = [row for row in reader]

valid_entries = []

print(firebase_list[0])

# 6, 8
for row in instamojo_list:
	t, p = mapping[row[6]]

	for fire_row in firebase_list:
		if (fire_row[1] == row[8] and
			fire_row[4] == row[9] and
			t == fire_row[5] and 
			p == fire_row[3]):
			valid_entries.append(fire_row)

print(len(valid_entries))

valid_entries.sort()

valid_entries = [k for k, _ in itertools.groupby(valid_entries)]

print(len(valid_entries))


with open('sorted.csv', 'w') as f:
	writer = csv.writer(f, delimiter=',')
	for row in valid_entries:
		writer.writerow(row)
