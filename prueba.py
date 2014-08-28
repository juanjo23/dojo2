#def task_0521():
#	"""
#	Escribe una comprension que evalue
#	una lista cuyo elemento i es el valor correspondiente a la clave k
#	en el elemento i del diccionario en la lista  
#	"""
#	dlist = [{'James':'Sean', 'directos':'Terence'}, {'James':'Royer', 'Director', 'Lewis'}]



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

