from sys import *
from lexer import lex
from parse import parse 

reg={"A":0,"B":0,"C":0,"D":0,"E":0,"H":0,"L":0}
def open_file(filename):
	data=open(filename,"r").read()
	return data

def run():
	data=open_file(argv[1])
	toks=lex(data)
	print("\n####### Console #######\n ")
	parse(toks,reg)
run()
