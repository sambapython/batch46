def fun(a,b):
	"""
	10,20->30
	"s1","s2"->s1s2
	"s1",20->None
	20,"s2"->None
	"""
	try:
		return a+b
	except:
		return None