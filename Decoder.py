from converter import FloatBinary
class Decoder():
    """this is the Encoder module"""
    def __init__(self, string ,_probrangeList):
        self._string=string
        self._probrange=_probrangeList
        self._converter = FloatBinary()

    def decode(self,binarytag):
         binarytag = self._converter.binaryTOfloat( binarytag )     ### Getting the float number of binary tag 
         result=""                                                  ### this is th final result
         detectedchar=""                                            ### the last detected symbol
         
         low=0.0                                                    ### intial lower bound
         high=1.0                                                   ### intial higher bound
         probrange=high-low                                         ### range of the detected string
         while detectedchar!='$' :                                  ### for each decoded charecter 
             for item in self._probrange :                          ### for each symbod avalible
                  if  low + (item['high'] * probrange) > binarytag :### if the tag meets the current symbol
                     detectedchar = item['char']                    
                    
                     low+= item['low']* probrange                   ### updating the high and low bounds for the next charecter 
                     high=low + item['prob']* probrange                 
                     probrange=high-low

                     break
             result+=detectedchar                                   ### adding the detected to final result 
         return result



