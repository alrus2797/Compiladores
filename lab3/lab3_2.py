a = input("Ingrese una expresion: ")
i = 0
preanalisis = a[0]
def error():
	raise Exception("Error de sintaxis")

def is_term(char):
	return '0' <= char <= '9'


def exp():
	if is_term(preanalisis):
		parea(preanalisis)
		resto()
	else:
		error()

def resto():
	if preanalisis == '+':
		parea('+')
		term()
		print('+')
		resto()
	elif preanalisis == '-':
		parea('-')
		term()
		print('-')
		resto()
	elif preanalisis == '\n'
		parea('\n')
	else:
		error()

def term():
	if '0' <= preanalisis <= '9':
		parea(preanalisis)
	else:
		error()

def parea(t):
	global preanalisis
	if preanalisis == t:
		i += 1
		preanalisis = a[i]
	else:
		error

exp()
