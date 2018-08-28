class SweetPotato:
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments =[]
    def __str__(self):
        return "地瓜 状态%s里面的作料%s几分熟(%d)"%(self.cookedString,str(self.condiments),self.cookedLevel)
    def cook(self,cookedTime):
        self.cookedLevel +=cookedTime
        if self.cookedLevel>=0 and self.cookedLevel<3:
            self.cookedString = "生的"
        elif self.cookedLevel>=3 and self.cookedLevel<5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel>=5 and self.cookedLevel<8:
            self.cookedString = "熟了"
        elif self.cookedLevel >= 8:
            self.cookedString = "烤糊了~"
    def addCondiments(self,item):
        self.condiments.append(item)

di_gua = SweetPotato()
di_gua.cook(1)
di_gua.cook(1)
di_gua.addCondiments("孜然")

print(di_gua)
di_gua.cook(1)
di_gua.cook(1)
di_gua.addCondiments("番茄")

print(di_gua)