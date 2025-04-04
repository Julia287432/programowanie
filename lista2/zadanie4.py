from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, pages_per_file):
    with open(input_pdf, 'rb') as file:
        reader = PdfReader(file)
        total_pages = len(reader.pages)
        part_num = 1

        for start in range(0, total_pages, pages_per_file):
            writer = PdfWriter()
            for i in range(start, min(start + pages_per_file, total_pages)):
                writer.add_page(reader.pages[i])
            
            output_filename = f"part_{part_num}.pdf"
            with open(output_filename, 'wb') as output_file:
                writer.write(output_file)
            print(f"Zapisano część {part_num} do {output_filename}")
            part_num += 1

if __name__ == "__main__":
    input_pdf = input("Podaj ścieżkę do pliku PDF: ")
    pages_per_file = int(input("Podaj liczbę stron w jednym pliku: "))
    split_pdf(input_pdf, pages_per_file)

#C:/Users/julia/OneDrive/Pulpit/pdf.pdf
