from sys import *
from lexer import lex,labels
from parse import parse 
import register

def open_file(filename):
	data=open(filename,"r").read()
	return data

def run():
	data=open_file(argv[1])
	toks=lex(data)
	print("\n####### Console #######\n ")
	parse(toks,labels)
	print(register.flag)

run()
