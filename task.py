import os
import pikepdf as pk
import json
from pdf2docx import Converter

def crack_pdf():
    with open(cwd+"/password.json") as f:
        data = json.load(f)
    passw = data["password"]
    path_1 = cwd+"/PDF_PP_text.pdf"
    path_2 = cwd+"/output/pdf_without_password.pdf"
    pdf = pk.open(path_1, password = passw)
    pdf.save(path_2)

def convert_to_docx():
    li = os.listdir(cwd+"/output")
    for i in li:
        if i.endswith(".pdf"):
            n = i.split(".")
            name = n[0]
    path_input = cwd+"/output/"+name+".pdf"
    path_output = cwd+"/output/pdf_to_doc.docx"
    cv = Converter(path_input)
    cv.convert(path_output, start=0, end=None)
    cv.close()

if __name__ == "__main__":
    cwd = os.getcwd()
    crack_pdf()
    convert_to_docx()