import pyttsx3
import PyPDF2

#Opening the file:
file = open("Tutorial_EDIT_Python.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(file)

pages = pdf_reader.numPages
speaker = pyttsx3.init()

#Reading the selected pages:
for num in range(7, pages):
    page = pdf_reader.pages[7]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()