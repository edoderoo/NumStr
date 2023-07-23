class numStr:
    result = '0'
    add = []
    subtract = []
    multiply = []
    divide = []

    def addStr(self):
      for oneStr in self.add:
         transfer = 0
         resStr = ''
         cursorRes = len(self.result)
         cursorOne = len(oneStr)
         while (cursorRes>0) or (cursorOne>0):
            digit = transfer
            if cursorRes>0: digit += int(self.result[cursorRes-1:cursorRes])
            if cursorOne>0: digit += int(oneStr[cursorOne-1:cursorOne])
            transfer, digit = divmod(digit, 10)
            resStr = chr(48 + digit) + resStr
            cursorOne -= 1
            cursorRes -= 1
         if transfer>0:
            resStr = chr(48 + transfer) + resStr
         self.result = resStr

    def subtractStr(self):
      for oneStr in self.subtract:
         transfer = 0
         resStr = ''
         cursorRes = len(self.result)
         cursorOne = len(oneStr)
         while (cursorRes>0) or (cursorOne>0):
            digit = transfer
            if cursorRes>0: digit += int(self.result[cursorRes-1:cursorRes])
            if cursorOne>0: digit -= int(oneStr[cursorOne-1:cursorOne])
            transfer, digit = divmod(digit, 10)
            resStr = chr(48 + digit) + resStr
            cursorOne -= 1
            cursorRes -= 1
         if transfer<0:
            resStr = chr(48 + transfer) + resStr
         while resStr[0:1]=='0':
           resStr=resStr[1:]
         self.result = resStr
          

    def calculate(self):
      if len(self.add) > 0:
         self.addStr()
      if len(self.subtract) > 0:
         self.subtractStr()

def test():
   added      = random.randint(0,99999999999)
   subtracted = random.randint(0,99999999999)
   resulted = added-subtracted
   result=numStr()
   result.add = [str(added)]
   result.subtract = [str(subtracted)]
   result.calculate()
   if str(resulted) != result.result:
      print('%d - %d = %s' %(added,subtracted,result.result))

import random
random.seed()
for i in range(1,10):
  test()

result = numStr()
result.add = ['125']
result.subtract = ['116']
result.calculate()
print(result.result)
