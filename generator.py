def String(generation, alternative):
    '''Creates the generator string'''
    string = ''
    for i in range(len(generation)):
        try:
            string += chr(alternative.contents[i][generation[i]][0])
        except:
            string += chr(alternative.contents[i][generation[i]])
    return string

class Generator:
    '''Generates the lexicographic parts of the URL

       After the interpretation of the expresion, the generator is initiated with
       a alternative
    '''
    
    def __init__(self, alternative):
        self.alternative = alternative
        self.current_generation = [0 for i in range(len(alternative.contents))]
        self.current_string = String(self.current_generation, self.alternative)
        
    def generate_next(self):
        '''Generates the next lexicographical word'''
        ok = True
        current_generation = list(self.current_generation)
        to_add = True
        for i in range(len(current_generation)):
            length = len(self.alternative.contents[i])
            if length > 1:
                if to_add == True:
                    current_generation[i] += 1
                    to_add = False
                    if current_generation[i] > length-1:
                        current_generation[i] = 0
                        to_add = True
            if to_add == False:
                break
        if to_add == True:
            ok = False
        self.current_generation = current_generation
        
        if ok == True:
            self.current_string = String(current_generation, self.alternative)
            return self.current_string
        else:
            self.current_generation = [0 for i in range(len(self.alternative.contents))]
            self.current_string = ''
            return self.current_string
