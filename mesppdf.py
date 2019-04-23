from PyPDF4 import PdfFileWriter, PdfFileReader
import datetime as dt

print("Start time:", dt.datetime.now() )
out_number_of_pages = 400

out_create_new_pdf = True

out_pdf = PdfFileWriter()

current_pos = 0

pdf_number_of = 1

input_folder = "input/"
out_folder = "output/conv-tom-"

#read file list from file
pdf_to_open = [line.rstrip('\n') for line in open('input/lista.txt')]
print(pdf_to_open)

for pdf_to_convert in pdf_to_open:
    print("Working on:"+pdf_to_convert )
    input_pdf = PdfFileReader(open(input_folder + pdf_to_convert, "rb"))
    for i in range(input_pdf.numPages):
        if(out_create_new_pdf):

            out_create_new_pdf = False
            input_pdf = PdfFileReader(open(input_folder + pdf_to_convert, "rb"))
            out_pdf = PdfFileWriter()
            current_pos = 0

        out_pdf.addPage(input_pdf.getPage(i))
        current_pos += 1
        if(current_pos == (out_number_of_pages ) ):
            out_pdf.write(open(out_folder + str(pdf_number_of)+".pdf", 'wb'))
            print("Out new file", dt.datetime.now(), "File name:", out_folder + str(pdf_number_of)+".pdf" )
            pdf_number_of += 1
            out_create_new_pdf = True


out_pdf.write(open(out_folder + str(pdf_number_of)+".pdf", 'wb'))
print("Stop time:", dt.datetime.now())
out_create_new_pdf = True