import argparse

# look afterwards:  https://stackoverflow.com/questions/30956688/python-argparse-customizing-error-messages
# https://stackoverflow.com/questions/53445769/argparse-define-custom-actions-or-types-with-additional-arguments

## This class has converter properties, takes parsed argument and converts it    
class Converter:
    def __init__(self):
        self.single_digits = ["zero", "one", "two", "three",  
                     "four", "five", "six", "seven",  
                     "eight", "nine"]

    # Converts the arg/input from number to word
    def num_to_word(self, num):
        # if num == None or (num <0) or (not isinstance(num, int)):
        x = 0
        word = ""

        while (x < len(num)):
            word+= self.single_digits[ord(num[x]) - 48]
            x+=1

        print(word)
        return word

    # Checks: if argument type invalid throw error
    def numbertype(self,v):
        # if not isinstance(value, int):
        if (int(v) <0) or v=='-0':
            raise argparse.ArgumentTypeError('Value has to be positive integer')
        return v

# This class builds a parser and parses argument     
class Parameter:

    # def create_parser(self):

    # Take argument and process it or throw error
    def parsefunc(self, args):
        converter = Converter()
        parser = argparse.ArgumentParser(description='Convert a number to word')
        parser.add_argument("num", help="the number", type=converter.numbertype)
        parser.add_argument("-v","--verbosity", help="increase output verbosity", action="count", default=0)
      # parser.add_argument("-v","--verbosity", help=argparse.SUPPRESS, action="count", default=0)
        return parser.parse_args(args)

    # def __init__(self):
    #     self.number= None

    # def requestInput(self):
    #     number=input("Enter a number to convert: ")

    #     try:
    #         number = int(number)


    #     return self.number


        


