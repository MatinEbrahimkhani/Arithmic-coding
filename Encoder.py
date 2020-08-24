from converter import FloatBinary
class Encoder():
    """this is the Encoder module"""
    def __init__(self, string ,_probrangeDict):
        self._string=string
        self._probrangedict =_probrangeDict
        self._converter = FloatBinary()


    def encode(self):
        low=0.0
        high=1.0
        probrange=high-low
        for character in self._string:                                              ### for each charecter to be encoded
            low += probrange * self._probrangedict[character]['low']                ### updating the lower bound
            high = low + probrange * (self._probrangedict[character]['prob'])       ### updating the higher bound
            probrange=high - low                                                    ### updating the range length

        return self._minlength_binfraction_generator(high , low)                    ### returning the Tagnumber
    
    
    
    
    def _minlength_binfraction_generator(self,high , low):
        """
        This Method returns the minimum lenghth binary difraction avalible in a range between the higher and lower bound 
        BFS (Breadth First Search) is used for finding the shortest binary sequence of the range 
        the sequences that are bigger than the higher boundry can most certainly be pruned  (Condition #1)
        the sequences that are bigger than the higher boundry can most certainly be pruned  (Condition #2)

        """
        states=['0.0','0.1']                                                ### intial states for the BFS queue

        while True:
            binfraction = states.pop(0)                                     ### poping from the queue
            value = self._converter.binaryTOfloat(binfraction)
            
            if  low < value and value < high :                              ### if in bounds (suits as an answer)
                return binfraction

            valwith1=self._converter.binaryTOfloat(binfraction+ '1')        ### value with a 1 added to the end 
            valwith0=self._converter.binaryTOfloat( binfraction+ '0')       ### value with a 0 added to the end 
            
            if (low - valwith0) < (valwith1 - valwith0) :
                states.append(binfraction + '0' )                           ### pushing to queue
            
            if valwith1 <high  :
                states.append(binfraction + '1' )                           ### pushing to queue
            
            
        
        