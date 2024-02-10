import PyPDF2

with open('./dummy.pdf', 'rb') as file:      
# 'rb' is read binary, for pdf we append 'b' to it.
# so it converts the file to binary and PyPDF2 works with binary files.
    reader = PyPDF2.PdfFileReader(file)
    print(file)
    print(reader)
    print(reader.numPages)
    print(reader.getPage(0))

    page = reader.getPage(0)
    page.rotateClockwise(270)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('./rotated.pdf', 'wb') as new_file:
        writer.write(new_file)
