class numStr:
    result = ''
    add = []
    subtract = []
    multiply = []
    divide = []

    def addStr(self):
      for oneStr in self.add:
         print(oneStr)

    def calculate(self):
      if len(self.add) > 0:
         self.addStr()

result = numStr()
result.add = ['1234','5678']
result.calculate()
