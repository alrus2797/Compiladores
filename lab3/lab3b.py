a = input("Ingrese una expresion: ")
a = a+'\n'
i = 0
preanalisis = a[0]
def error():
	print("Error de sintaxis")
	exit()
#	raise Exception("Error de sintaxis")

def is_term(char):
	return '0' <= char <= '9'


def exp():
	if is_term(preanalisis):
		term()
#		parea(preanalisis)
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
	elif preanalisis == '\n':
		parea('\n')
	else:
		error()

def term():
#	print("Curr: ", preanalisis)
	if '0' <= preanalisis <= '9':
		print(preanalisis)
		parea(preanalisis)
	else:
		error()

def parea(t):
	global preanalisis
	global i
	if preanalisis == t:
		if preanalisis == '\n':
			print("Accepted")
		elif i < len(a):
			i += 1
			preanalisis = a[i]
		else:
			error()
	else:
		error()

exp()
