
from docx import Document
from docx.shared import Pt

def resize_font(docx_path, resize_factor):
    # Load the DOCX document
    doc = Document(docx_path)
    last_font_size = doc.paragraphs[0].runs[0].font.size
    if last_font_size == None:
        last_font_size = 11

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.font.size != None:
                current_font_size = run.font.size
                last_font_size = current_font_size
            else:
                current_font_size = last_font_size
            amplified_font_size = Pt(current_font_size * resize_factor)
            run.font.size = amplified_font_size

    # Save the modified document
    output_path = f'amplified_document.docx'
    doc.save(output_path)
    print(f"Resized document saved to: {output_path}")

if __name__ == "__main__":
    # Input: DOCX file path and resizing factor
    docx_path = input("Enter the DOCX file path: ")
    resize_factor = float(input("Enter the resizing factor (e.g., 1.5 for 1.5x): "))

    # Resize font and save the modified document
    resize_font(docx_path, resize_factor)
