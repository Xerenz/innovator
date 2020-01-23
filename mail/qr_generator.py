from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing 
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF

from PyPDF2 import PdfFileWriter, PdfFileReader

import json
import io


def generateQR(value, file):
	packet = io.BytesIO()
	can = canvas.Canvas(packet)

	qrcode = qr.QrCodeWidget(value)
	bounds = qrcode.getBounds()
	width = bounds[2] - bounds[0]
	height = bounds[3] - bounds[1]

	d = Drawing(100, 100, transform=[300./width,0,0,300./height,0,0])
	d.add(qrcode)
	renderPDF.draw(d, can, 390, 430)

	can.save()

	packet.seek(0)

	new_pdf = PdfFileReader(packet)
	pdf = PdfFileReader(open(file, 'rb'))

	page = pdf.getPage(0)
	page2 = new_pdf.getPage(0)

	page.mergePage(page2)

	return page


if __name__ == '__main__':
	with open('data.json') as f:
		data = json.load(f)

		for d in data:
			output = PdfFileWriter()
			page = generateQR(d["phone"], "./tickets/" + d["name"].upper() + ".pdf")
			output.addPage(page)

			with open("./qr_tickets/" + d["name"] + '.pdf', 'wb') as f:
				output.write(f)
				print("Ticket generated for", d["name"])