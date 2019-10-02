#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAS '+'
#define MENOS '-'
#define NUM 256
#define FIN -1

char lexema[80];
int tok;

int scanner();
void parea(int);
void term();
void resto();
void error();

bool is_digit(int c){
	return isdigit(c);
}


void exp(){
	if (tok == NUM){
		term();
		resto();
	}
	else
		error();
}

void resto(){
	if (tok == MAS)
	{
		parea(MAS);
		term();
		printf("+");
		resto();
	}
	else if (tok == MENOS)
	{
		parea(MENOS);
		term();
		printf("-");
		resto();
	}
	else
	{
		
	}
}

void term(){
	if (tok == NUM){
		printf("%s", lexema);
		parea(NUM);
	}
	else
		error();
}

void error(){
	printf("Error de sintaxis\n");
	exit(0);
}

void parea(int t){
	if (tok == t)
		tok = scanner();
	else
		error();
}

int scanner(){
	int c, i;
	do c = getchar(); while(c == ' ');

	if (c == '\n')
		return FIN;
	if (c == MAS || c == MENOS)
		return c;
	if (is_digit(c)){
		i = 0;
		do{
			lexema[i++] = 0;
			c = getchar();
		}
		while (is_digit(c));

		lexema[i] = 0;
		ungetc(c, stdin);
		return NUM;	
	}
}

int main(int argc, char const *argv[])
{
	tok = scanner();
	exp();
	return 0;
}
