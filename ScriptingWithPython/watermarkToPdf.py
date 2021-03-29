import PyPDF2

'''Add watermark to pdf'''

template = PyPDF2.PdfFileReader(open(input(r"Locatia relativa a fisierului pe care vrei sa adaugi watermark: "), 'rb'))
wmark = PyPDF2.PdfFileReader(open(input(r"Locatia relativa a fisierului watermark: "), 'rb'))
out = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(wmark.getPage(0))
    out.addPage(page)
    
    with open('PDF\PdfWtm4.pdf', "wb") as file:
        out.write(file)