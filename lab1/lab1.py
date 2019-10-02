def p1():
	frase = input("Ingrese su frase: ")
	for char in frase:
		print(char)

def p2(filename):
	file_text = open(filename,'r').read()
	for char in file_text:
		print(char)
def p3a(filename, num):
	file_text	= open(filename,'r').read()
	ciphered	= ""
	for char in file_text:
		ciphered_char = ord(char) + num
		ciphered += chr(ciphered_char)
	print(ciphered)
	out = open("output.txt",'w')
	out.write(ciphered)
def p3b(filename, num):
	file_text	= open(filename).read()
	ciphered	= ""
	for char in file_text:
		ciphered_char = ord(char) - num
		ciphered += chr(ciphered_char)
	print(ciphered)

def is_word(word):
	word = word.lower()
	for char in word:
		ascii_char = ord(char)
		if (ascii_char < 97 or ascii_char > 122):
			return False
	return True

def is_number(word):
	for char in word:
		ascii_char = ord(char)
		if (ascii_char < 48 or ascii_char > 57):
			return False
	return True
def is_special(word):
	specials = ["+","-","*","/","="]
	return word in specials

def p4(filename):
	file_text	= open(filename,'r').readlines()
	for line in file_text:
		words = line.split(" ")
		for word in words:
			current = word
			print(repr(current), current == ' ', current == '')
			if current == ' ' or current == '': continue
			elif current[-1] == '\n':
				current = current[:-1]

			if is_number(current): _type = "number"
			elif is_word(current): _type = "palabra"
			elif is_special(current): _type = "especial"
			else: _type = "Desc"
		print ("[{}]\t{}".format(current,_type))
# Execute problem
#p1()
#p2("text.txt")
#p3a("text.txt",3)
#p3b("output.txt",3)
p4("text.txt")

