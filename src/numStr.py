class numStr:
    result = ''
    add = []
    subtract = []
    multiply = []
    divide = []

    def addStr(self):
      transfer = 0
      resStr = ''
      for oneStr in self.add:
         if self.result=='': self.result='0' 
         cursorRes = len(self.result)
         cursorOne = len(oneStr)
         while (cursorRes>0) and (cursorOne>0):
            digit = transfer
            if cursorRes>0: digit += int(self.result[cursorRes-1:cursorRes])
            if cursorOne>0: digit += int(oneStr[cursorOne-1:cursorOne])
            transfer, digit = divmod(digit, 10)
            resStr = chr(int('0') + digit) + resStr
            cursorOne -= 1
            cursorRes -= 1
      self.result = resStr      

    def calculate(self):
      if len(self.add) > 0:
         self.addStr()

result = numStr()
result.add = ['1234','5678']
result.calculate()
print(result.result)
