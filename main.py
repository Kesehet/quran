import fitz  # PyMuPDF


def pdf_to_png(pdf_path, output_folder):
  # Open the PDF
  pdf = fitz.open(pdf_path)

  for page_number in range(len(pdf)):
    # Get the page
    page = pdf[page_number]

    # Render the page to an image
    pix = page.get_pixmap()

    # Save the image as a PNG
    output_path = f"{output_folder}/page_{page_number+1}.png"
    pix.save(output_path)
 
  pdf.close()
  print("Conversion completed.")

 
# Example usage
pdf_to_png("Holy Quran .pdf", "tajweed-quran")
