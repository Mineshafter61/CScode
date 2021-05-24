import random
def LicenseKey():
    l, c = [], []
    for i in range(9):
        randord = random.randint(65,90)
        l.append(randord*(i+1))
        c.append(chr(randord))
    chk = sum(l)%11
    chk = 'X' if x == 10 else str(chk)
    return ''.join(c+list(chk))

print(LicenseKey())
print(LicenseKey())
print(LicenseKey())


def menu():
    option = 0
    while option != 3:
        print('==== MENU ====')
        print('[1] Purchase of a new license for either a single-user or 3-user license')
        print('[2] Register an additional user to an active 3-user license')
        print('[3] End')
        option = int(input())
    return option


## Task3

option = menu()
if option == 1:
    licenceType = input('Enter licence type (S)ingle or (3)-user')
    newKey = LicenceKey()
    newKey = newKey+' 1' if licenceType == 'S' else newKey+' 3 1' if licenseType == '3' else print('error')
    print('Licence key issued:', newKey)
    licencefile = open('LICENCE-KEYS.txt', 'a')
    print(newKey, file=licencefile)
    licencefile.close()
    print('Licence saved in file')
    file = open('LICENCE-KEYS.txt', 'r')
    for line in file:
        print(line.strip())
    file.close()


## Task 4

elif option == 2:
    licences = []
    file = open("LICENCE-KEYS.txt", 'r')
    for line in file:
        licences.append(line.strip())
    file.close()
    find = input('Enter 3-user licence key:')
    for i in range(len(licences)):
        if licences[i][0:10] == find:
            print('YES')
            newLicence = licences[i][:-1] + str(int(licences[i][-1])+1)
            break
    licences[i] = newLicence
    file = open('LICENCE-KEYS.txt','w')
    for i in range(len(licences)):
        print(licences[i], file = file)
    file.close()


## Task 5

class Licence:
    def __init__(self, licencekey, licencetype, datepurchase, purchasername, macaddress, dateregister):
        self.__licencekey, self.__licencetype, self.__datepurchase, self.__purchasername, self.__macaddress, self.__dateregister = licencekey, licencetype, datepurchase, purchasername, macaddress, dateregister
    def getlicensekey(self):
        return licencekey
    def getlicencetype(self):
        return licencetype
    def getdatepurchase(self):
        return datepurchase
    def getpurchasername(self):
        return purchasername
    def getmacaddress(self):
        return macaddress
    def getdateregister(self):
        return dateregister

class SingleUser(Licence):
    def __init__(self, licencekey, licencetype, datepurchase, purchasername, macaddress, dateregister):
        super().__init__(licencekey, licencetype, datepurchase, purchasername, macaddress, dateregister)

