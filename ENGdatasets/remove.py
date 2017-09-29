import os
name = ["The New York Times\n","Breitbart\n","London Times\n","U.S. official\n","U.S. sources\n","U.N. experts\n","January 5, 2017\n","January 6, 2017\n","January 9, 2017\n","January 10, 2017\n","January 11, 2017\n","January 13, 2017\n","January 17, 2017\n","January 18, 2017\n","January 19, 2017\n","January 24, 2017\n","January 25, 2017\n","January 26, 2017\n","January 27, 2017\n","January 30, 2017\n","January 31, 2017\n","February 1, 2017\n","February 9, 2017\n","February 10, 2017\n","February 13, 2017\n","February 14, 2017\n","February 15, 2017\n","February 16, 2017\n","February 17, 2017\n","February 21, 2017\n","February 22, 2017\n","February 23, 2017\n","February 24, 2017\n","February 27, 2017\n","February 28, 2017\n","March 2, 2017\n","March 3, 2017\n","March 6, 2017\n","March 9, 2017\n","March 13, 2017\n","March 16, 2017\n","March 17, 2017\n","March 27, 2017\n","March 29, 2017\n","March 30, 2017\n","March 31, 2017\n","April 3, 2017\n","April 4, 2017\n","April 10, 2017\n","April 25, 2017\n","April 26, 2017\n","April 27, 2017\n","April 28, 2017\n","May 1, 2017\n","May 3, 2017\n","May 4, 2017\n","May 5, 2017\n","May 8, 2017\n","May 10, 2017\n","May 11, 2017\n","May 12, 2017\n","May 15, 2017\n","May 16, 2017\n","May 17, 2017\n","May 18, 2017\n","May 19, 2017\n","May 22, 2017\n","May 23, 2017\n","May 26, 2017\n","June 1, 2017\n","August 15, 2016\n","June 3, 2016\n","August 16, 2016\n","August 17, 2016\n","August 19, 2016\n","August 22, 2016\n","August 23, 2016\n","August 24, 2016\n","August 25, 2016\n","August 26, 2016\n","August 29, 2016\n","August 30, 2016\n","August 31, 2016\n","September 1, 2016\n","September 2, 2016\n","September 6, 2016\n","September 7, 2016\n","September 8, 2016\n","September 12, 2016\n","September 13, 2016\n","September 15, 2016\n","September 16, 2016\n","September 19, 2016\n","September  23, 2016\n","September  28, 2016\n","September  30, 2016\n","October 10, 2016\n","November 8, 2016\n","November 11, 2016\n","November 14, 2016\n","November 15, 2016\n","November 28, 2016\n","November 30, 2016\n","December 2, 2016\n","December 5, 2016\n","December 9, 2016\n","December 13, 2016\n","December 14, 2016\n","Monday, June 1"]
alldir = os.listdir("./allthenews")
for dirname in alldir:
	if dirname == ".DS_Store":
		continue
	if int(dirname) % 10 == 0:
		print dirname
	path = "./allthenews/" + dirname
	allfile = os.listdir(path)
	for filename in allfile:
		f = open(path+'/'+filename)
		lines = f.readlines()
		f.close()
		if len(lines) <= 1:
			print path, filename
		if len(lines[1].split(' - ')) > 1:
			if lines[1].split(' - ')[-1] in name:
				lines[1] = ' - '.join(lines[1].split(' - ')[:-1]) + '\n'
		f = open(path+'/'+filename,'w')
		f.write(''.join(lines))
		f.close()
			# if lines[1].split(' - ')[-1] not in name:
				# name.append(lines[1].split(' - ')[-1])
# for i in xrange(len(name)):
	# print name[i]


