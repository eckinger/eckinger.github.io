from termcolor import colored
from pypdf import PdfReader
import os
DIR = 'oxy/pdfs'

def count_instances(fname, target):
    reader = PdfReader(fname)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
        words = text.split()
        
    return sum(1 for i in range(len(words))
            if words[i:i+len(target)] == target)

search_term = "carbon capture"
for filename in os.listdir(DIR):
    f = os.path.join(DIR, filename)
    if (filename[-4:] != '.pdf'): continue
    try:
        num_instances = count_instances(f, search_term.split())
    except FileNotFoundError as e:
        print(colored('E> File Not Found Error', 'red'))
    if num_instances > 0:
        print(colored(str(count_instances(f, search_term.split())) +
                      ' instances of \"' + search_term + '\" in ' + f,
                      'green'))
    else:
        continue
        print(colored('0 instances of \"' + search_term + '\" in ' + f,
                      'yellow'))
