from pyresparser import ResumeParser
import os
# from docx import Document


filed='/Users/sherazhasan/Desktop/test3/scripts-archive/ZaidResume.pdf'

data = ResumeParser(filed).get_extracted_data()
print(data)


    