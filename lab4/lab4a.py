import readchar

#Defines
MAS     = "+"
MENOS   = "-"
NUM     = 256
FIN     = -1

def error():
	print("Error de sintaxis")

def exp():
	if tok == NUM:
		term()
		resto()
	else:
		error()

def resto():
	if tok == MAS:
		parea(MAS)
		term()
		print("+")
		resto()
	elif tok == MENOS:
		parea(MENOS)
		term()
		print("-")
		resto()
	else:
		pass

def term():
	if tok == NUM:
		print(lexema)
		parea(NUM)
	else:
		error()

def parea(t):
	if tok == t:
		tok = scanner()
	else:
		error()

def is_digit(char):
	a = ord(char)
	return 48 < a < 57

def replace(string, idx, char):
	return string[:idx] + char + string[idx + 1:]

def scanner():
	c = readchar.readchar()
	while c == ' ':
		c = readchar.readchar()
	
	if c == MAS or c == MENOS:
		return c
	
	if is_digit(c):
		i = 0
		while is_digit(c):
			i += 1
			lexema = replace(lexema, i, c)
			c = readchar.readchar()
		lexema = replace(lexema, i, )
	