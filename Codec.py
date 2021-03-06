from Encoder import Encoder
from Decoder import Decoder

class Codec(object):
    """
    This object is a Arithmic coding encoder / decoder (Codec)
    You should first generate probranges with a custom string for further coding and decoding
    after generating the ranges you can  Code or decode any string
    you can test the codex for any string too

    """
    def __init__(self, *args, **kwargs):
        self._string=""
        self._inputsize=0
        self._probrangedict ={}
        self._probrange=[]
        
    def set_string(self,string):
        """
        This methods gets the strings and enters it to the encoder
        after calling this you can use the text within the encoder

        """
        assert type(string) == type("string") , " Invalid input, input type should be <str> "
        self._string = string
        if string[-1] != "$" :
            self._string+="$"

        self._inputsize= len(self._string)

    def generate_probranges(self):
        
        _dict= {}
        for char in self._string:
            _dict[char]= _dict.get(char,0) + 1
        
        countedlist=[]
        for item in _dict.items():
            countedlist.append(item)

        countedlist.sort(key = lambda x: x[1],reverse= True)

        lowrange=0
        for item in countedlist :                                           ### for each symbol avalible
            prob = item[1]/self._inputsize                                  ### setting the probability of symbol occurance
            highrange = lowrange + prob     
            #(character,probability,lowerbound,higherbound)
            self._probrange.append({      'char' : item[0],
                                          'prob' : prob,
                                          'low' : lowrange,
                                          'high' : highrange})
            
            self._probrangedict[item[0]]={'prob' : prob,
                                          'low' : lowrange,
                                          'high' : highrange}
            lowrange = highrange
    
            
            
            
    def encode(self,string):
        self.set_string(string)                             ### reciving the input stiring
        encoder= Encoder(self._string,self._probrangedict)  ### creating an Encoder 
        return encoder.encode()                             ### returning the binary Tagnumber generated by encoder given the stirng

    def decode(self,tagnumber):
        decoder = Decoder(self._string, self._probrange)    ### creating a Decoder
        return decoder.decode(tagnumber)                    ### returning the string, given the binary Tagnumber
    def Test(self,string):
        """
        Testing all of the required functionalities 
       
        """
       
        codec = Codec()
        codec.set_string(string)
        codec.generate_probranges()
        tag = codec.encode(string)
        result = codec.decode(tag)
        if string[-1] != "$" :
            string+="$"



        print("INPUT :\t\t"+string)
        print("TAG :\t\t",tag)
        print("DECODED :\t" + result)
        if result == string : print("SUCCESSFUL CODE AND DECODE")
        else : print("FAILED CODE OR DECODE")
        print("----------------------------------------")

