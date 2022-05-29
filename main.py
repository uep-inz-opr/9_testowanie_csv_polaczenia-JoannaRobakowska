import csv

def wczytaj(self):
	dane = []


with open('phoneCalls.csv', 'r') as fin:
	reader = csv.reader(fin, delimiter= "'")
	headers = next(reader)

	for row in reader:
		from_subsr =int(row[0])
		if from_subsr == 0:
			from_subsr += 1
		else:
			dane.append(row[0])


def najwiecej_polaczen(self):
	return max(((int(dane), numbers.count(dane)) for dane in set(dane)), key = lambda x: x[1])		

if __name__ == "__main__":
print(Polaczenia(input()).pobierz_najczesciej_dzwoniacego())