
class Number:
    def __init__(self, Num):
        self.value = Num
        self.divisorsAll = []           ##will be constructed by self.giveValues()
        self.divisorsPrime = []         ##
        self.divisorsPrimeQuantity = []     ##will be constructed by self.findValues()
        self.divisorsProper = []            ##
        self.original = 1                   ##

    def giveValues(self):
        for index in range(1, self.value + 1):
            if self.value % index == 0:
                self.divisorsAll.append(index)
                burn = 0
                for index2 in range(2, index):
                    if index % index2 != 0:
                        continue
                    else:
                        burn += 1
                if burn != 0:
                    continue
                else:
                    if index != 1:
                        self.divisorsPrime.append(index)
                    else:
                        continue
            else:        
                continue
        return self.divisorsAll, self.divisorsPrime
    def findValues(self):
        for index3 in range(len(self.divisorsAll) - 1):
            self.divisorsProper.append(self.divisorsAll[index3])
        sum3 = 0
        for index5 in self.divisorsProper:
            sum3 += index5
        self.original = sum3

        for index4 in self.divisorsPrime:
            burn1 = 1
            while self.value % (index4 ** burn1) == 0:
                burn1 += 1
            self.divisorsPrimeQuantity.append(burn1 - 1)
        return self.divisorsProper, self.divisorsPrimeQuantity, self.original

    def isPerfectNumber(self):
        sum = 0
        for index0 in self.divisorsProper:
            sum += index0
        if sum == self.value:
            return True
        else:
            return False
    def isPerfectNumber2(self):
        sum2 = 0
        for index0 in self.divisorsAll:
            sum2 += index0
        if sum2 / 2 == self.value:
            return True
        else:
            return False

    def printCharachteristicsOfNumber(self):
        print(
            'Όλοι οι διαιρέτες :  ', self.divisorsAll, '\n',
            'Proper διαιρέτες :  ', self.divisorsProper,'\n',
            'Πρώτοι διαιρέτες :  ', self.divisorsPrime, '\n',
            'Πολαπ/τα Πρώτων διαιρετών :  ', self.divisorsPrimeQuantity,'\n',
            self.value,' has the original number of : ', self.original, '\n'
        )