import csv
from bank.models import Banks, Branches

def run():
    fhand = open('bank_branches.csv')
    reader= csv.reader(fhand)
    Banks.objects.all().delete()
    Branches.objects.all().delete()
    for row in reader:
        print(row[1])
        ba, created = Banks.objects.get_or_create(id=row[1], name=row[7])
        ba.save()
        b, created = Branches.objects.get_or_create(ifsc=row[0], bank_id=row[1], branch=row[2], address=row[3], city=row[4], district=row[5], state=row[6])
        b.save()
    
      
