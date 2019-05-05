def parse(toks,reg):
	size={"STA":2,"MVI":3,"MOV":3}
	i=0
	while(i<len(toks)):
		if (toks[i]=="STA"):
			print(toks[i+1][4:]+" : "+str(reg["A"]))
		elif(toks[i]=="MVI"):
			REG=toks[i+1][4:]; VALUE=toks[i+2][4:]
			reg[REG]=VALUE
			#print(reg[REG])
		elif(toks[i]=="MOV"):
			dest=toks[i+1][4:];source=toks[i+2][4:];
			reg[dest]=reg[source]
			#print(dest+" "+str(reg[dest]))
		i+=size[toks[i]]

