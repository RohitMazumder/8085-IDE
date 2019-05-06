import register

def parse(toks):
	size={"STA":2,"MVI":3,"MOV":3,"LDA":2,"ADD":2,"ADC":2,"ADI":2,"ACI":2,"SUB":2,"SBB":2,
				"SBI":2,"INR":2,"DCR":2,"CMP":2,"CPI":3,"ANA":2,"ANI":3,"XRA":2,"XRI":3,"ORA":2,"ORI":3}
	i=0
	while(i<len(toks)):
		if (toks[i] in ("STA")):
			f=getattr(register,toks[i])
			adr=toks[i+1][4:]
			if(adr[-1] in ['H','h'] ):
				adr=adr[:-1]
			x=int(adr,16)
			f(x)

		elif(toks[i]=="MVI"):
			f=getattr(register,toks[i])
			val=toks[i+2][4:]
			if(val[-1] in ['H','h'] ):
				val=val[:-1]
			x=int(val,16)
			f(getarg(toks[i+1][4:]),x)

		elif(toks[i]=="MOV"):
			f=getattr(register,toks[i])
			f(getarg(toks[i+1][4:]),getarg(toks[i+2][4:]))

		elif(toks[i]=="ADD"):
			f=getattr(register,toks[i])
			f(getarg(toks[i+1][4:]))

		i+=size[toks[i]]

		


def getarg(x):
    if x=='A':return register.A
    if x=='B':return register.B
    if x=='C':return register.C
    if x=='D':return register.D
    if x=='E':return register.E
    if x=='H':return register.H
    if x=='L':return register.L
    if x=='M':return register.M
