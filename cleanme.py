import csv

csvfile = open('./data-cleaning/data/cleanme.csv', 'r')
outfile = open('./data-cleaning/data/cleanme_cleaned.csv', 'w')

reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

writer.writeheader()

for row in reader:
# Changing text fields to uppercase
    row['first_name'] = row['first_name'].upper()
# Adding leading zeroes to zip codes with less than 5 digits
    row['zip'] = row['zip'].zfill(5)
# Removing non-breaking spaces 
    row['city'] = row['city'].replace("&nbsp;", " ")
# Outputting contributions of $1,000 or more
    if int(row["amount"]) >= 1000:
        
        writer.writerow(row)
