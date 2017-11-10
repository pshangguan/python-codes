import re

def find_symbol(sym,string):
    if re.search(r"\b" + re.escape(sym) + r"\b",l):
        return True
    else:
	return False

with open('symbols.txt','r') as sy:
	for s in sy:
		s = s.replace("\n","")
		print(s)
 
		with open('7.txt', 'r') as fh:
#		    user_input = raw_input('Enter a name: ')
		    for l in fh:
#        print(l)
			if find_symbol(s,l):
				break
		    else:
			print("add new symbol %s" % s)

with open('symbols.txt','r') as sy:
	for s in sy:
		s = s.replace("\n","")
		print(s)
 
		with open('7.txt', 'r') as fh:
#		    user_input = raw_input('Enter a name: ')
		    for l in fh:
#        print(l)
			if find_symbol(s,l):
				break
		    else:
			print("add new symbol %s" % s)

