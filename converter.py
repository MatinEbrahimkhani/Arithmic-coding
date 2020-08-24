class FloatBinary(object):
    """
    This class represents a simple Float Binary converter
    please note that by abinary is a string of binary numbers not the python datatype

    """
    def __init__(self,):
        return super().__init__()
    def floatTObinay(self,floatnumber): 
        whole, decimal = str(floatnumber).split(".") 
        whole = int(whole) 
        decimal = float('0.'+decimal)
        res = bin(whole).lstrip("0b") + "."

        while decimal > 0 :
            decimal*=2
            digit= decimal//1 
            res+=str(digit)[0]
            decimal-=digit
        return  res


    def binaryTOfloat(self,binarynumber):
        whole, decimal = str(binarynumber).split(".")
        whole = int(whole)
        result = float(whole)
        coefficient=1
        for dec in decimal:
            coefficient/=2
            result += coefficient * int(dec)
        return result

