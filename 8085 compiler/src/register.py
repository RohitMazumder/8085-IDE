flag={"S":0,"Z":0,"AC":0,"P":0,"CY":0}
mem={}

class Register:

        def __int__(self):
                self.value=0
                self.binary='0b00000000'

        def set(self,val):
                if val<=255:
                        self.value=val
                        self.fbinary()

        

        def fbinary(self):
                self.binary=bin(self.value)
                if len(self.binary)<10:
                        x=len(self.binary)-2
                        y=self.binary[2:]
                        self.binary='0b'+('0'*(8-x))+y  

        
        def __add__(self,other):
                set_ac(self,other)
                self.value=self.value+other.value
                if (self.value>255):
                        self.value=self.value-256
                        flag['CY']=1
                else:
                        flag['CY']=0
                self.fbinary()
                set_flag(self)
                return self

        def __sub__(self,other):
                if other.value<=self.value:
                        self.value=self.value-other.value
                        flag['CY']=0
                else:
                        self.value=256+self.value-other.value
                        flag['CY']=1
                self.fbinary()
                set_flag(self)
                return self

def set_ac(a,b):
        #print(id(a))
        x=a.value&15
        y=b.value&15
        if (x+y>15):
                flag['AC']=1
        else:
                flag['AC']=0

def set_flag(a):
        x=0
        if (a.value==0):
                flag['Z']=1
        else:
                flag['Z']=0
        if (a.binary[2:][0]=='1'):
                flag['S']=1
        else:
                flag['S']=0

        n=a.value
        while (n!=0): 
                n &= (n-1)
                x+=1

                if x%2==0:
                        flag['P']=1
                else:
                        flag['P']=0



def STA(add):
        global A
        if add>=0000 and add<=65535:
                print(str(hex(add))+" : "+str(hex(A.value)))
                
def MVI(x,a):
        x.set(a)


def MOV(x,a):
        x.set(a.value)
        

def ADD(B):
        global A
        A=A+B
        set_flag(A)

def ADC(B):
    global A,W
    W.set(flag["CY"])
    A=A+B+W
    set_flag(A)

def JNZ():
        if (flag["Z"]==0):
                return 'true'
        else :
                return 'false'

def JZ():
        if (flag["Z"]==0):
                return 'false'
        else :
                return 'true'

def JNC():
        if (flag["CY"]==0):
                return 'true'
        else :
                return 'false'

def JC():
        if (flag["Z"]==0):
                return 'false'
        else :
                return 'true'

def DCR(B):
        global W
        W.set(1)
        temp=flag["CY"]
        B=B-W
        flag["CY"]=temp
        set_flag(B)

def INR(B):
        global W
        W.set(1)
        B=B+W
        set_flag(B)




A,B,C,D,E,H,L,M,W,Z=Register(),Register(),Register(),Register(),Register(),Register(),Register(),Register(),Register(),Register()
