#
# Preps New Book list for Yahoo Pipes
#  Trivially Simple
#
# opens csv file, dumps out xml
import csv

try:
    f = csv.reader(open('books_in.csv','r'))
except:
    print "Input file not opened"
    exit;
 
try:
    o = open('new_books.csv','w')
except:
    print "Output file not opened"

f.next()
o.write('URL,TITLE\n')
for r in f:
    o.write("http://catalogue.library.brocku.ca/search/a?searchtype=c&searcharg="+r[1].replace(' ','+')+','+r[2]+'\n')

print "done"
