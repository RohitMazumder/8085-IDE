def parse(toks,reg):
	size={"STA":1}
	i=0
	while(i<len(toks)):
		if (toks[i]=="STA"):
			print(toks[i+1][3:]+" : "+str(reg["A"]))
		i+=size["STA"]

