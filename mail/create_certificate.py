from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import csv
import json

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# Adding custom fonts. 1st parm is the name of the font and 2nd is the path to the ttf font file.
pdfmetrics.registerFont(TTFont('monst', 'montserrat.bold.ttf'))


# Function to return a pdf page with the parameters added into it.
def createpage(name):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    
    
    #can.setFont('RobotoL', 17)                # Setting the font and size of text.
    #can.drawString(300, 310, name)           # Drawing a string onto the page. (x, y, string)

    # can.setFont('RobotoL', 48)
    # can.drawString(700, 350, name)
    #can.drawString(2110, 785, seat)
    #can.drawString(2110, 648, food)

    #can.setFont('RobotoL', 60)
    #can.drawString(1600, 648, seat)

    # =======================================================================================================
    # Code to centre a string between a starting and ending coordinates.

    can.setFont('monst', 50)
    can.setFillColorRGB(1, 1, 1)
    name = name.split(' ')

    # You'll have to determine the following values with the help of the helper file, get_pdf_coordinates.py
    start = 40
    # end = 1560
    # length_of_one_letter = 70           # Use some 'monospaced' font so that each letter will have the same length.
    y = 75

    # mid = start + (end - start)/2
    # half_string_size = (len(name)/2)*length_of_one_letter
    # x = mid - half_string_size
    can.drawString(start, y, name[0])
    if (len(name) == 2):
        y = 25
        can.drawString(start, y, name[1])
    # =======================================================================================================
    

    can.save()                               # Save the canvas


    packet.seek(0)
    # Creating a pdf with just the canvas we just created.
    new_pdf = PdfFileReader(packet)

    # Read your existing PDF (ticket.pdf)
    existing_pdf = PdfFileReader(open("ticket without name.pdf", "rb"))
    # Add the canvas on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)

    return page


def create_one(name):
    name = name.upper()
    output = PdfFileWriter()

    page = createpage(name)
    output.addPage(page)                     # Adding that page to the pdf.

    # Writing it to a file.
    outputStream = open("./tickets/" + name + ".pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    print('certificate generated for ' + name)    

with open('data.json') as f:
    data = json.load(f)
    
    for d in data:
        create_one(d["name"])