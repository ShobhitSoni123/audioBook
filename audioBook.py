import pyttsx3
import PyPDF2

# Open the document
book = open('sample.pdf','rb')

# Read the Document
pdfReader = PyPDF2.PdfFileReader(book)

# init the speaker
speaker = pyttsx3.init()

# Get Desired Page
page = pdfReader.getPage(7)

# Extract Text
text = page.extractText()

#getting details of current voice
voices = speaker.getProperty('voices')     

# #changing index, changes voices. 0 for male
# speaker.setProperty('voice', voices[0].id) 

#changing index, changes voices. 1 for female
speaker.setProperty('voice', voices[1].id)  

#speaker will say the extracted text of the mentioned page number
speaker.say(text)

# This will run and be stopped after reading the document
speaker.runAndWait()