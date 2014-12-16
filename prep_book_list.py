#
# Preps New Book list for Yahoo Pipes
#  Less trivially Simple
#
# opens csv file, dumps out CSV
import csv
import os


codes = {'h54': [] , 'm66' : []}


if __name__ == "__main__":
  print "Resolving",
  for f in os.listdir(os.getcwd()):
    if f[-3:] == "csv" and f != "new_books.csv":
      #infile = open(f,"r")
        infile = csv.reader(open(f,'r'), delimiter=',',quotechar='"')
        break
  if not infile:
    print " input file not found"
    exit
  print ""

for line in infile:
    if line[0].strip() in codes.keys():
        codes[line[0].strip()].append("http://catalogue.library.brocku.ca/search/a?searchtype=c&searcharg="+line[1].replace(' ','+')+','+'"'+line[2]+'"'+'\n')


for l in codes:
    o = open( l+'.csv', 'w')
    o.write('URL,TITLE\n')
    for items in codes[l]:
        o.write(items)
    o.close()

