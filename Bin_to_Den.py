def BinToDen(binNum):
    placeVal = [] #list to store place value
    for i in range(len(binNum)-1,-1,-1):
        placeVal.append(2**i)
    total = 0
    for i in range(len(binNum)):
        total = total + int(binNum[i])*placeVal[i]
    return total
    

#main
BinNum = input("Enter the binary number:")
#do your validation for BinNum, check whether BinNub consists of only 1s or 0s
print(BinToDen(BinNum))


def DenToBin(denNum):
    binNum = ""
    while int(denNum) != 0:
        rem = int(denNum)%2
        binNum = str(rem) + binNum
        denNum = int(denNum) // 2
    return binNum
print(DenToBin("12"))

def HexToDen(hexNum):
    dict_hex = ['A':10,'B':11,'C':12,'D':13,'E':14,'F':15,\
                '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0]
    placeVal = [] #list to store place value
    for i in range(len(hexNum)-1,-1,-1):
        placeVal.append(16**i)
    total = 0
    for i in range(len(hexNum)):
        total = total + int(dict_hex[hexNum[i]])*placeVal[i]
    return total

def DenToHex(denNum):
    dict_hex = [10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',\
                1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',0:'0']
        hexNum = ""
    while int(denNum) != 0:
        rem = int(denNum)%16
        hexNum = str(rem) + hexNum
        denNum = int(dict_hex[denNum[i]]) // 16
    return binNum
print(DenToBin("12"))

    
    
