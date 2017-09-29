import sys
import csv
import os
maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

dirname = "./allthenews/"
f = open('articles1.csv')
r = csv.reader(f)
csvitems = []
for i in r:
	csvitems.append(i)
f.close()
f = open('articles2.csv')
r = csv.reader(f)
csvitems2 = []
for i in r:
	csvitems2.append(i)
f.close()
f = open('articles3.csv')
r = csv.reader(f)
csvitems3 = []
for i in r:
	csvitems3.append(i)
f.close()
print len(csvitems)
print csvitems[0]
csvitems = csvitems[1:]
print len(csvitems2)
print csvitems2[0]
csvitems2 = csvitems2[1:]
print len(csvitems3)
print csvitems3[0]
csvitems3 = csvitems3[1:]
csvitems += csvitems2
csvitems += csvitems3
print len(csvitems)
# exit()
for i in xrange(len(csvitems)):
	if i % 5000 == 0:
		print i
	filename = str(i) + ".txt"
	if not os.path.exists(dirname+'/'+str(i/1000)):
		os.mkdir(dirname+'/'+str(i/1000))
	f = open(dirname + '/' + str(i/1000) + '/' + filename, 'w')
	f.write("Title:\n")
	# print csvitems[i][2]
	f.write(csvitems[i][2].replace("\n","").replace("\r",""))
	f.write("\nContent:\n")
	f.write(csvitems[i][9].replace("\n","").replace("\r",""))
	f.close()






