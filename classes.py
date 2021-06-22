class Price():
    def __init__(self, value: int):
        self.value = value
    
    def get_price(self,isComma: bool = True,tax: int = 10,unit: str = "円",isFloat: bool = False):
        taxin = self.value * ( 100 + tax )/100
        if not isFloat:
            taxin = int(taxin)
        if isComma:
            taxin = "{:,}".format(taxin)
        else:
            taxin = str(taxin)
        p = taxin + unit
        return p

class PhoneNumber():
    def __init__(self, value: str):
        if len(value) > 11:
            print("phone number is too long!")
            raise
        if len(value) < 10:
            print("phone number is too short")  
            raise
        self.value = value
    
    def get_phoneNumber(self,isHyphen: bool = True):
        if isHyphen:
            if self.value.startswith("0120") or self.value.startswith("0570"):
                pn = self.value[:4]+"-"+self.value[4:7]+"-" + self.value[7:]
            else:
                pn = self.value[:-8]+"-"+self.value[-8:-4]+"-" + self.value[-4:]
        else:
            pn = self.value
        return pn