#-*-coding:utf-8;-*-
#py3

"""
A copy of byteReaderPy3_new.py, for convenience
"""

readpath=r"File to read here"
with open(readpath,'rb') as f:
    dbyte=f.read()
input("Byte Reader\nPath: %s\nSize: %d bytes  press ENTER..."%(readpath,len(dbyte)))
def reverse(astring):
    i=len(astring)-1
    res=""
    while i>-1:
        res+=astring[i]
        i-=1
    return res
def byte2bit(abyte):
    num=[128,64,32,16,8,4,2,1]
    bits=""
    for x in num:
        if abyte>=x:
            bits+="1"
            abyte-=x
        else:
            bits+="0"
    return bits
def bit2byte(bits):
    num=[128,64,32,16,8,4,2,1]
    abyte=0
    for x in range(8):
        if bits[x]=="1":
            abyte+=num[x]
    return abyte
def byte2print(thebyte):
    #s="{"+",".join([str(i) for i in range(256) if len(repr(chr(i)))!=3 and i!=92])+"}"
    return "".join([chr(i) if (31<i<127 or (160<i and i!=173)) else "." for i in thebyte])
for i in range(0,500,10): #len(dbyte),10):
    hex1=" ".join(["%02X"%j for j in dbyte[i:i+5]])
    hex2=" ".join(["%02X"%j for j in dbyte[i+5:i+10]])
    s1=byte2print(dbyte[i:i+5])
    s2=byte2print(dbyte[i+5:i+10])
    #print([i]+list(dbyte[i:i+10])+[s1,s2])
    print( ("%05d %s  %s  %s %s") % (i//10,hex1,hex2,s1,s2) )
#for x in range(256):
#    print x,byte2bit(x)
#print(reverse("0101"))
#for x in range(200):
"""
#old
for x in range(len(dbyte)):
    bits=byte2bit(dbyte[x])
    print("%3d|%3d|%3d|%s|%s"%(x,dbyte[x],bit2byte(reverse(bits)),bits,repr(chr(dbyte[x]))[1:-1].replace("\\x","")))
"""

