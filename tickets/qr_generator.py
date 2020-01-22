from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing 
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF

from PyPDF2 import PdfFileWriter, PdfFileReader

import json
import io

data = {
	'name' : 'Martin George',
	'food': 'NonVeg',
	'T-shirt' : 'L'
}

data = json.dumps(data)

def generateQR(value):
	packet = io.BytesIO()
	can = canvas.Canvas(packet)

	qrcode = qr.QrCodeWidget(value)
	bounds = qrcode.getBounds()
	width = bounds[2] - bounds[0]
	height = bounds[3] - bounds[1]

	d = Drawing(100, 100, transform=[100./width,0,0,100./height,0,0])
	d.add(qrcode)
	renderPDF.draw(d, can, 300, 405)

	can.save()

	packet.seek(0)

	new_pdf = PdfFileReader(packet)
	pdf = PdfFileReader(open('blank.pdf', 'rb'))

	page = pdf.getPage(0)
	page2 = new_pdf.getPage(0)

	page.mergePage(page2)

	return page

output = PdfFileWriter()
page = generateQR(data)
output.addPage(page)

with open('newPage.pdf', 'wb') as f:
	output.write(f)