def printlist():
	mylist = []
	mylist.append(11)
	mylist.append(21)
	mylist.append(31)
	mylist.append(41)
	mylist.append(51)
	mylist.append(61)

	cnt=0
	for m in mylist:
		print("This is a element of mylist[%d] %d" % (cnt,m))
		cnt += 1

	for i in range(len(mylist)):
		mylist[i] = i
		print(mylist[i])

## main ##
printlist()
