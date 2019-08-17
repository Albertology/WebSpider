def list_between(start : int, end : int):
    '''Generates a list with values between
       start-end
    '''
    return [[i] for i in range(start, end+1)]


shortcuts = {'/d':list_between(ord('0'), ord('9')),
             '/l':list_between(ord('a'), ord('z')),
             '/L':list_between(ord('A'), ord('Z'))

             }
class State:
    '''Dumb class that simply holds the values of the current state of the interpretation
       [a-zA-Z]
       *
       
    '''
    def __init__(self):
        self.special = False
        self.in_set = False
        self.set_char = False
        self.last_char = ''
        self.last_last_char = ''
        
     
class Alternative:
    '''Dumb class that holds the interpreted regex

       For each character in it's composition it has a list with the posibilities of it sorted
    '''
    def __init__(self):
        '''Initiates the length and creates an empty list which will
           be used for charcter storage
        '''
        self.contents = []


            
def interpret(expression : str):
    '''Interprets the expression'''
    alt = Alternative()
    stat = State()
    current_contents = []
    for char in expression:
        if stat.special == True:
            if stat.in_set == False:
                alt.contents.append(shortcuts.get('/'+char, [ord(char)]))
                stat.special = False
            else:
                current_contents.append([ord(char)])
                stat.special = False
        else:
            if stat.in_set == False:
                if char == '/':
                    stat.special = True
                elif char == '[':
                    stat.in_set = True
                else:
                    alt.contents.append([ord(char)])                    
            else:
                if stat.set_char == False:
                    if char == '/':
                        stat.special = True
                    elif char == '-':
                        stat.set_char = True
                    elif  char == ']':
                        stat.in_set = False
                        alt.contents.append(list(current_contents))
                        current_contents.clear()
                    else:
                        current_contents.append([ord(char)])
                else:
                    stat.set_char = False
                    if char != ']':
                        
                        current_contents += list_between(ord(stat.last_last_char)+1,ord(char))
                    else:
                        current_contents.append([ord('!')])
                        alt.contents.append(list(current_contents))
                        current_contents.clear
                        stat.in_set = False
        stat.last_last_char = stat.last_char
        stat.last_char = char
        
    return alt
