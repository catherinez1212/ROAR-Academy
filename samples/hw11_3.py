import os
import PyPDF2
path = os.path.dirname(os.path.abspath(__file__))
file_handle = open(r'C:\Users\61513\Documents\GitHub\ROAR-Academy\samples\Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb') 
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)   # this tells you total pages 

word_dict = {}

for i in range(page_number):
    page_object = pdfReader.pages[i]    # We just get page 0 as example 
    page_text = page_object.extract_text()
    page_text.replace('\n', ' ')
    page_text.replace('. ', ' ')
    page_text.replace(', ', ' ')
    page_text.replace('! ', ' ')
    page_text.replace('? ', ' ')
    word_list = page_text.split(' ')
    for word in word_list:
        if(word.isalpha()):
            if(word not in word_dict):
                word_dict[word] = 1
            else:
                word_dict[word] += 1

print(word_dict)
