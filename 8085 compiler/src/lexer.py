def lex(filecontents):
	filecontents=list(filecontents)
	tokens=[]
	### Token codes used : ###
	# ADR: Address String
	# REG: Register
	# VL8 : 8-bit Data
	tok=""
	string=""
	state=0
	d8=""
	### State descriptions ###
	# state = 0: Keywords
	# state = 1: String Address datatype
	# state = 2: String register name
	# state = 3: String 8-bit data
	# state = 4: String 16-bit data
	for c in filecontents:
		tok=tok+c
		if(tok==" "):
			tok=""
		elif (tok=="\n"):
			if(state==1):
				tokens.append("ADR:"+string)
				string=""
			elif(state==3):
				tokens.append("VL8:"+d8)
				d8=""
			tok=""
			state=0
		elif(tok.isdigit()):
			if(state==2):
				state=3
				d8+=c
				tok=""
			if(state==1):
				string+=c

		elif (tok=="STA"):
			tokens.append("STA")
			tok=""
			state=1
		elif(tok=="MVI"):
			tokens.append("MVI")
			tok=""
			state=2
		elif(tok=="MOV"):
			tokens.append("MOV")
			tok=""
			state=2
		elif(tok=="HLT"):
			#print (tokens)
			return tokens;
		elif (state==1):
			string+=c
			tok=""
		elif (state==2):
			tokens.append("REG:"+tok)
			tok=""
		elif(state==3):
			d8+=tok
			tok=""
	return tokens





