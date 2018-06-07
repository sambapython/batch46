a=10
b=20
def fun(c,d):
	print c,d
	res=c+d
	print res
	return c
print a,b
for i in [1,2,3,0,4,5,6]:
	print "iteration started"
	if i!=0:
		print 10/i 
	print "iteration ended"
import pdb; pdb.set_trace()
fun(10,20)
print "program ended"