#!/usr/bin/env python3
import argparse
import generator
import exp_interpreter
import requests

def read_file(filename):
    if filename != '':
        with open(filename, 'r') as file:
            return file.read()
    else:
        return ''
def ListString(string):
    returned_list = [] 
    gathered_string = '' 
    waiting = False
    quote_type = ''
    
    for char in string:
        if char == "'" and waiting == False:
            waiting = True
            quote_type = "'"
            gathered_string = ''
        elif char == '"' and waiting == False:
            waiting == True
            quote_type = '"'
            gathered_string = ''
        elif char == quote_type  and waiting == True:
            waiting = False
            returned_list.append(gathered_string)
            gathered_string = ''
        else:
            gathered_string += char
        
    return returned_list

parser = argparse.ArgumentParser(description='Scans websites for pages')
parser.add_argument('website', type=str, help='website to scan')
parser.add_argument('expressions', type=str, help='list off expressions')
parser.add_argument('--extension', type=str, default='', help='file extension')
parser.add_argument('--max_length', type=int, default=1, help='max name length for non-specified expressions')
parser.add_argument('--last_file', type=bool, default=False, help='Is the last part a file?')
parser.add_argument('--wrong_pages', type=str, default='', help='Path to the file with wrong pages')
parser.add_argument('--display_possible', type=bool, default=False, help='Does it display possible sites?')
args = parser.parse_args()

generators = []

args.expressions = ListString(args.expressions)

wrong = read_file(args.wrong_pages)

def query_site(website):
     response = requests.get(website)
     if response.text not in wrong:
         if response.status_code == 200:
             print('Found website at {}'.format(website))
         else:
             if args.display_possible == True:
                    print('Possible website at'.format(website))
     return response
    
for i in range(len(args.expressions)):
    if args.expressions[i] == '': 
        args.expressions[i] = '[a-zA-Z0-9]' * args.max_length
        
for i in range(len(args.expressions)):
    generators.append(generator.Generator(exp_interpreter.interpret(args.expressions[i])))

for length in range(len(args.expressions)):
    last = '-'
    while last != '':
        to_add = True
        website = ''
        ok = True
        website += args.website + '/'
        if args.last_file == False:
            for j in range(length+1):
                if generators[j].current_string != '':
                    website += generators[j].current_string + '/'
                else:
                    ok = False
                    break    
            website += args.extension
            if ok == True:
                query_site(website)
        else:
            for j in range(length):
                if generators[j].current_string != '':
                    website += generators[j].current_string + '/'
                else:
                    ok = False
                    break
            website += generators[length]
            website += args.extension
            if ok == True:
                query_site(website)
                
        for i in range(length+1):
            if to_add == True:
                generators[i].generate_next()
                if generators[i].current_string != '':
                    to_add = False
            if to_add == False:
                break
        last = generators[length].current_string
            

