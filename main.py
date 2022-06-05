import csv

def wczytaj(self):
    calls_dict_sum = dict()

with open('phoneCalls.csv', 'r') as fin:
	reader = csv.reader(fin, delimiter= "'")
	headers = next(reader)

	for row in reader:
		from_subsr =int(row[0])
        if from_subsr not in calls_dict_sum:
          calls_dict_sum[from_subsr] = 0
        calls_dict_sum[from_subsr] += 1
    return calls_dict_sum


def pobierz_najczesciej_dzwoniacego(self):
    return max(self.data_dict.items(), key= lambda x: x[1])	

if __name__ == "__main__":
print(wczytaj(input()).pobierz_najczesciej_dzwoniacego())