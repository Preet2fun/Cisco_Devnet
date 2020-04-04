import csv


raw_csv = open('text.csv').read()
print(raw_csv)

exp_csv = open('text.csv')
data_read = csv.reader(exp_csv)

for data in data_read:
    print('{} is in {} with ip : {}'.format(data[0], data[2], data[1]))
