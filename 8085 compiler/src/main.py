from sys import *
from lexer import lex,labels
from parse import parse 
import register
import os

def open_file(filename):
	data=open(filename,"r").read()
	return data

def run(path):
	data=open_file(path)
	toks=lex(data)
	print("\n####### Console #######\n ")
	file=open("out.txt","w+")
	file.write("\n####### Console #######\n ")
	file.close()
	parse(toks,labels)
	file=open("out.txt","a")
	file.write(str(register.flag))
	file.close()
