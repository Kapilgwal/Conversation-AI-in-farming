import os
from PyPDF2 import PdfReader

def readFiles(directory_path):
    
    text = ""
    for filename in os.listdir(directory_path):
    # Check if the file is a PDF
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory_path, filename)
        
        # Open the PDF file
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
            
                for page in reader.pages:
                    text += page.extract_text()
    
    return text

directory_path = "D:/COLLEGE PROJECTS/PROJECT/data"
text = readFiles(directory_path=directory_path)

# -------------------------------------------------------------------------------

from spacy.lang.en import English

nlp = English()

# Add a sentencizer
nlp.add_pipe("sentencizer")

doc = nlp(text)
lst = list(doc.sents)
# print(lst)
print(len(lst))
# -------------------------------------------------------------------------------