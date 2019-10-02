import readchar

preanalisis = 0

def S():
	global preanalisis
	if preanalisis == 'x':
		parea('x')
		S()
	elif preanalisis == 'a':
		A()
		B()
		parea('c')
	else:
		error()

def A():
	global preanalisis
	if preanalisis == 'a':
		parea('a')
	else:
		error()

def B():
	global preanalisis
	if preanalisis == 'b':
		parea('b')
	else:
		error()

def error():
	print("Error de sintaxis")

def parea(t):
	global preanalisis
	if preanalisis == t:
		preanalisis=readchar.readchar()
		print("Caracter ingresado: ", preanalisis)
	else:
		error()

preanalisis = readchar.readchar()
print("Caracter ingresado: ", preanalisis)
S()

