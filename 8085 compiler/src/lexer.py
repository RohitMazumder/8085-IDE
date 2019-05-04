def lex(filecontents):
	filecontents=list(filecontents)
	tokens=[]
	tok=""
	string=""
	state=0
	### State descriptions ###
	# state = 0; Keywords and variables
	# state = 1; String Address datatype
	# state = 2: MVI
	for c in filecontents:
		tok=tok+c
		if(tok==" "):
			tok=""
		elif (tok=="\n"):
			if(state==1):
				tokens.append("STR:"+string)
				string=""
			tok=""
			state=0
		elif (tok=="STA"):
			tokens.append("STA")
			tok=""
		elif(tok=="MVI"):
			tokens.append("MVI")
			tok=""
			state=2
		elif(tok=="MOV"):
			tokens.append("MOV")
			tok=""
			state=3
		elif(tok=="HLT"):
			return tokens;
		elif(tok.isdigit()):
			state=1
			tok=""
			string+=c
		elif (state==1):
			string+=c
			tok=""
		elif (state==2):
			tokens.append("REG:"+tok)
			tok=""
			state=1
		elif(state==3):
			tokens.append("REG:"+tok)
			tok=""
	return tokens





