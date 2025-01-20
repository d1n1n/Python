class Converter():
    _counter = 0

    @staticmethod
    def cToF(celcius):
        Converter._counter +=1
        return (celcius*(9/5)+32)
    
    @staticmethod
    def fToC(farenheit):
        Converter._counter +=1
        return((farenheit-32)*5/9)
    
    @staticmethod
    def getCounter():
        return Converter._counter 
    
print(Converter.cToF(25))   # 77.0
print(Converter.fToC(77))   # 25.0
print(Converter.getCounter())  # 2