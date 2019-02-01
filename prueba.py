
def task_0521(k):
	"""
	Encuentra un valor en un diccionario a partir de su clave, dentro de una lista
	>>> task_0521('James')
	Sean
	Royer
	Pearse
	"""
	dlist = [{'James':'Sean', 'directos':'Terence'}, {'James':'Royer', 'Director': 'Lewis'}, {'James':'Pearse', 'Director':'Royer'}]

	for i in dlist:
		if(k in i.keys()):
			print( i[k] )



def task_0522(k):
	"""
	Realiza una comprension que evalue de una lista cuyos elementos son diccionarios la llave
	y compare si esta presente en los dos diccionarios
	>>> task_0522('Bilbo')
	True
	>>> task_0522('Frodo')
	False
	"""
	dlist=[{'Bilbo':'Ian', 'Frodo':'Elijah'}, {'Bilbo':'Martin', 'Thorin': 'Richard'}];
	cont = 0
	for i in dlist:
		if(k in i.keys()):
			cont = cont+1

	if cont == len(dlist):
		return True
	else:
		return False


def twice(z):
	return 2*z

