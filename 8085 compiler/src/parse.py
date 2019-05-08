import register

def parse(toks,labels):
	size={"STA":2,"MVI":3,"MOV":3,"LDA":2,"ADD":2,"ADC":2,"ADI":2,"ACI":2,"SUB":2,"SBB":2,"SUI":2,
				"SBI":2,"INR":2,"DCR":2,"CMP":2,"CPI":3,"ANA":2,"ANI":3,"XRA":2,"XRI":3,"ORA":2,"ORI":3,"JMP":0,"JNZ":2,"JZ":2,"JC":2,"JNC":2}
	i=0
	change_flag=1
	while(i<len(toks)):
		change_flag=1
		if(toks[i][0:3]!="LAB"):
			
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

			elif(toks[i] in ("ADD","ADC","DCR","INR","SUB","SBB")):
				f=getattr(register,toks[i])
				f(getarg(toks[i+1][4:]))

			elif(toks[i] in ("JMP")):
				lab=toks[i+1][4:]
				i=labels[lab]
				change_flag=0

			elif(toks[i] in ("JNZ","JZ","JNC","JC")):
				f=getattr(register,toks[i])
				flag=f()
				#print(flag)
				if (flag=='true'):
					i=labels[toks[i+1][4:]]
					#print(i)
					change_flag=0
			#print(i)
			if(change_flag==1):		
				i+=size[toks[i]]
		else:
			i+=1
		


def getarg(x):
    if x=='A':return register.A
    if x=='B':return register.B
    if x=='C':return register.C
    if x=='D':return register.D
    if x=='E':return register.E
    if x=='H':return register.H
    if x=='L':return register.L
    if x=='M':return register.M
