import os
import pymupdf  # PyMuPDF

# Define the folder path containing your PDF files
pdf_parent_folder = "pdfsToMerge"
# target_folder = "test-merge-1"
target_folder = "test-merge-2"
pdf_folder_path = os.path.join(os.getcwd(), pdf_parent_folder, target_folder)

# Define the output file name
output_filename = target_folder + "_merged.pdf"

# Initialize an empty list to store the filepaths of PDF documents
pdf_paths = []

# Error message for assert failure
err_msg = "No files to merge! Exiting application..."


def create_pathlist():
    # Loop through each file in the folder
    for filename in os.listdir(pdf_folder_path):
        # Check if the file has a .pdf extension (case-insensitive)
        if filename.lower().endswith('.pdf'):
            full_path = os.path.join(pdf_folder_path, filename)
            pdf_paths.append(full_path)

    # Now pdf_docs contains all the PDF documents loaded from the folder
    print(f"Number of PDFs\t:\t{len(pdf_paths)}")


def merge_pdfs():
    # Check if the file already exists
    if os.path.exists(output_filename):
        response = input(f"'{output_filename}' already exists. Do you want to overwrite it? (yes/no): ").strip().lower()
        if response not in ["y", "yes"]:
            print("Operation cancelled. The file was not overwritten.")
            exit()

    out = pymupdf.open()
    for filename in pdf_paths:
        pdf = pymupdf.open(filename)
        out.insert_pdf(pdf, annots=False, links=True)
        pdf.close()
    out.save(output_filename)


if os.path.exists(pdf_folder_path) and os.path.isdir(pdf_folder_path):
    print(f"Listing PDFs in\t:\t{pdf_folder_path}")
    create_pathlist()
    assert len(pdf_paths) > 0, err_msg
    merge_pdfs()
