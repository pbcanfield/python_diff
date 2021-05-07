class FileParser:
    def __init__(self, filename):
        
        try:
            file = open(filename, 'r')
        except FileNotFoundError:
            print ("The file: %s could not be found." % filename)
            self.__file = None 
        else:
            self.__file = file
            self.parse_strings()

    def __del__(self):
        if self.__file != None:
            self.__file.close()
    
    def is_valid(self):
        return not (self.__file == None)

    def parse_strings(self):
        self.__strings = [s.rstrip() for s in self.__file]
    
    def get_strings(self):
        return self.__strings
    