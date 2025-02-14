import os
import pymupdf  # PyMuPDF

# Define the folder path containing your PDF files
pdf_parent_folder = "pdfsToMerge"
# target_folder = "test-merge-1"
target_folder = "Vesterling-AG"
pdf_folder_path = os.path.join(os.getcwd(), pdf_parent_folder, target_folder)

# Define the output file name
output_filename = target_folder + "_merged.pdf"

# Initialize an empty list to store the filepaths of PDF documents
pdfs_to_merge = []

# Error message for assert failure
err_msg = "No files to merge! Exiting application..."


class PdfFile:
    def __init__(self, filename, full_path):
        self.filename = filename
        self.full_path = full_path


def create_pdf_list():
    # Loop through each file in the folder
    for filename in os.listdir(pdf_folder_path):
        # Check if the file has a .pdf extension (case-insensitive)
        if filename.lower().endswith('.pdf'):
            full_path = os.path.join(pdf_folder_path, filename)
            pdf_file = PdfFile(filename=filename, full_path=full_path)
            pdfs_to_merge.append(pdf_file)

    # Now pdf_docs contains the path for all the PDF documents loaded from the folder
    print(f"PDFs to merge\t:\t{len(pdfs_to_merge)}")


def merge_pdfs():
    # Check if the file already exists
    if os.path.exists(output_filename):
        response = input(f"\nWARNING! '{output_filename}' already exists.\nDo you want to overwrite it? (yes/no): ").strip().lower()
        if response not in ["y", "yes"]:
            print("Operation cancelled. The file was not overwritten.")
            exit()

    out = pymupdf.open()
    for pdf in pdfs_to_merge:
        pdf = pymupdf.open(pdf.full_path)
        out.insert_pdf(pdf, annots=False, links=True)
        pdf.close()
    out.save(output_filename)
    print("\nOperation successful!")
    print(f"Merged file\t:\t{output_filename}")
    print(f"Location\t:\t{os.getcwd()}")


if os.path.exists(pdf_folder_path) and os.path.isdir(pdf_folder_path):
    print(f"Listing PDFs in\t:\t{pdf_folder_path}")
    create_pdf_list()
    assert len(pdfs_to_merge) > 1, err_msg
    merge_pdfs()
