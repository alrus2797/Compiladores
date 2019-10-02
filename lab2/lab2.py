NOT_MATCH_TEXT = "error"
MATCH_TEXT = "accept"

table = {
	(1,'digit')	: 2,
	(1,'alpha')	: 3,
	(1,'fdc')	: NOT_MATCH_TEXT,
	(2,'digit') : NOT_MATCH_TEXT,
	(2,'alpha') : NOT_MATCH_TEXT,
	(2,'fdc')	: NOT_MATCH_TEXT,
	(3,'digit') : 3,
	(3,'alpha') : 3,
	(3,'alpha') : MATCH_TEXT,
}

def clean_text(text):
	text = text.replace('\n','')
	text = text.replace(' ', '')
	return text

def is_digit(char):
	ascii_value = ord(char)
	return ascii_value >= 48 and ascii_value <= 57

def is_alpha(char):
	ascci_value = ord(char)
	return (ascci_value >= 65 and ascci_value <= 90) or (ascci_value >= 97 and ascci_value <= 122)

def is_minus(char):
	return char == '-'

def is_period(char):
	return char == '.'

def which_is(char):
	if is_digit(char): return "digit"
	else: return "alpha"

def diagram_recognition(text):
	state = 1
	i = 0
	while i < len(text):
		symbol = text[i]
		if state == 1:
			if is_digit(symbol): state = 2
			elif is_alpha(symbol): state = 3
			else: return NOT_MATCH_TEXT
		elif state == 2: return NOT_MATCH_TEXT
		elif state == 3:
			if is_alpha(symbol): state = 3
			elif is_digit(symbol): state = 3
			else: return NOT_MATCH_TEXT
		i += 1
	if state != 3: return NOT_MATCH_TEXT
	else: return True

def table_recognition(text):
	state = 1
	i = 0
	while state != MATCH_TEXT:
		symbol = text[i]
		if is_digit(symbol): _in = 'digit'
		elif is_alpha(symbol): _in = 'alpha'
		elif i == len(text) - 1: _in = 'fdc'
		else: return NOT_MATCH_TEXT
		state = table[(state, _in)]
		if state == NOT_MATCH_TEXT: return NOT_MATCH_TEXT
		i += 1
	return MATCH_TEXT


def number_recognition(text):
	state = 1
	i = 0
	while i < len(text):
		symbol = text[i]
		if state == 1:
			if is_digit(symbol)		: state = 2
			elif is_minus(symbol)	: state = 3
			elif is_alpha(symbol)	: state = 4
			elif is_period(symbbol)	: state = 5
			else: return NOT_MATCH_TEXT
		elif state == 2:
			if is_digit(symbol)		: state = 2
			elif is_period(symbol)	: state = 5
			else: return NOT_MATCH_TEXT
		elif state == 3:
			if is_digit(symbol)		: state = 2
			else: return NOT_MATCH_TEXT
		elif state == 4:
			return NOT_MATCH_TEXT
		elif state == 5:
			if is_digit(symbol)		: state = 6
		elif state == 6:
			if is_digit(symbol)		: state = 6
			else: return NOT_MATCH_TEXT
		i += 1
	if state == 2 or state == 6: return MATCH_TEXT
	else: return NOT_MATCH_TEXT
			
			
		
arch = open("text.txt",'r')

arch_text = arch.read()

arch_text = clean_text(arch_text)

#a
def pa():
	res = diagram_recognition(arch_text)
	print(res)

#b
def pb():
	res = table_recognition(arch_text)
	print(res)

#c
def pc():
	res = number_recognition(arch_text)
	print(res)

pc()

