import pdfkit as pdf

#pdf.from_string('hello', 'string.pdf')

# ALERT: if you apply css width and height
# to an image...
# wkHTMLtoPDF will not load the image and
# the image will not appear in the pdf!!!
#pdf.from_file('Index.html','output.pdf')

url = 'file:///C:/Users/DhruvVohra/Desktop/htmltopdf/qwerty.html'
pdf.from_url(url, 'outside.pdf')