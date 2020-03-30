
def check (number):
	divisable =True
	current=20
	while (all([divisable==True, current>0])):
		if (number % current > 0):
			divisable=False
			return divisable
		current=current -1
	return divisable

def small ():
	good=False
	start=1
	while (good == False):
		good=check(start)
		start=start+1
	return start - 1
print(small())
