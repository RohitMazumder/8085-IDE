def lex(filecontents):
	filecontents=list(filecontents)
	tokens=[]
	tok=""
	string=""
	state=0
	### State descriptions ###
	# state = 0; Keywords and variables
	# state = 1; String Address datatype
	# state = 2:
	for c in filecontents:
		tok=tok+c
		if(tok==" "):
			if(state==0):
				tok=""
		elif (tok=="\n"):
			tok=""
		elif (tok=="STA"):
			tokens.append("STA")
			tok=""
		elif (tok=="\""):
			if(state==0):
				state=1
			elif(state==1):
				tokens.append("Ad:"+string)
				tok=""
				state=0
				string=""
		elif (state==1):
			string+=c
			tok=""
	return tokens





