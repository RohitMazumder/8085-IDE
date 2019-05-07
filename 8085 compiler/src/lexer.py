labels={}
def lex(filecontents):
	filecontents=list(filecontents)
	tokens=[]
	#Implementations left#
	#Stack keywords
	#Rotate
	#16 bit operations
	#JUMP operations
	keywords=["STA","MVI","MOV","LDA","ADD","ADC","ADI","ACI","SUB","SBB","SBI","INR","DCR","CMP",
				"CPI","ANA","ANI","XRA","XRI","ORA","ORI","JMP","JNZ","JZ","JC","JNC"]
	next_state={"STA":1,"MVI":5,"MOV":2,"LDA":1,"ADD":2,"ADC":2,"ADI":3,"ACI":3,"SUB":2,"SBB":2,
				"SBI":3,"INR":2,"DCR":2,"CMP":2,"CPI":3,"ANA":2,"ANI":3,"XRA":2,"XRI":3,"ORA":2,"ORI":3,"JMP":6,"JNZ":6,"JZ":6,"JC":6,"JNC":6}
	### Token codes used : ###
	# ADR: String
	# VL8: 8-bit Data
	# REG: Register 
	tok=""
	string=""
	state=0
	d8=""
	lab=""
	### State descriptions ###
	# state = 0; Keywords and variables
	# state = 1; String Address datatype
	# state = 2: String register name
	# state = 3: String 8-bit data
	# state = 4: String 16-bit data
	# state = 5: Exceptional state
	# state = 6: Label 
	for c in filecontents:
		tok=tok+c
		if(tok in (" ",",")):
			tok=""
		elif(c==":"):
			tok=tok[:-1]
			tokens.append("LAB:"+tok)
			labels[tok]=len(tokens)
			tok=""
			state=0
		elif (tok=="\n"):
			if(state==1):
				tokens.append("ADR:"+string)
				string=""
			elif(state==3):
				tokens.append("VL8:"+d8)
				d8=""
			elif(state==6):
				tokens.append("LAB:"+lab)
				lab=""
			tok=""
			state=0
		elif(tok.isdigit() and state in (1,2)):
			if(state==2):
				state=3
				d8+=c
				tok=""
			if(state==1):
				string+=c
		elif(tok in keywords):
			tokens.append(tok)
			state=next_state[tok]
			tok=""
		elif(tok=="HLT"):
			#print(tokens)
			return tokens
		elif (state==1):
			string+=c
			tok=""
		elif (state==2):
			tokens.append("REG:"+tok)
			tok=""
		elif(state==3):
			d8+=tok
			tok=""
		elif(state==5):
			tokens.append("REG:"+tok)
			tok=""
			state=3
		elif(state==6):
			lab+=c
			tok=""
	return tokens





