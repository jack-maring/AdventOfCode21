class Packet:

    def __init__(self, raw):
        self.raw=raw
        self.version=self.binToTen(raw[:3])
        self.typeID=self.binToTen(raw[3:6])
        self.lengthTypeID=None if self.typeID==4 else int(raw[6])

        if self.lengthTypeID!=None:
            self.subPacks=[]


    def binToTen(self, num):
        count=0

        for i in range(len(num)-1, -1, -1):
            count+=(2**i)*int(num[i])

        return count


hex=open("Inputs/Day_16.txt", "r").read()

key={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
res=""
for i in hex:
    res+=key[i]

pack=Packet(res)
print(pack.raw)





