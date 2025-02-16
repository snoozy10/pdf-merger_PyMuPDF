"""
Simple PDF-merger for everyday needs
Creator: S. N. Sabrina Nabila
Library used: PyMuPDF
"""
import os
import pymupdf  # PyMuPDF (Previously imported as fitz)

'''
Define paths and global variables
'''
# Name of the folder containing possible target folders;
# Folder location: Working Directory
parent_folder = "pdfsToMerge"

# The name of the folder containing the PDFs to merge in the next run
target_folder = "test-merge-1"  # Example folder 1
# target_folder = "test-merge-2"    # Example folder 2

# Create the absolute path for the target folder
merge_folder_abspath = os.path.join(os.getcwd(), parent_folder, target_folder)

# Define the name of the output file
output_filename = target_folder + "_merged.pdf"  # Comment this for custom name
# output_filename = "anything-you-want.pdf"      # Uncomment this for custom name

# Initialize an empty list to store the PDF names and filepaths (currently packaged as PDF class)
pdfs_to_merge = []

'''
Set messages to display
'''
# Error message if less than 2 PDFs is found in target-folder
str_merge_err = "ERROR: Not enough files to merge. Exiting application..."

# Warning string if output_filename already exists
str_merge_overwrite_warn = f"\nWARNING: '{output_filename}' already exists.\nDo you want to overwrite it? (yes/no): "

# Display string if user doesn't want to overwrite existing file with output_filename
str_merge_overwrite_cancel = f"\nOperation cancelled. The file '{output_filename}' was not overwritten."

# Display strings for path errors
str_path_invalid = f"\nERROR: Invalid path. '{merge_folder_abspath}' doesn't exist"
str_path_not_folder = f"\nERROR: No folder named '{merge_folder_abspath}' exists"


'''
Define classes and functions
'''


class Pdf:
    def __init__(self, filename, abspath):
        self.filename = filename
        self.abspath = abspath

    @staticmethod
    def is_pdf(filename):
        if filename.lower().endswith('.pdf'):
            return True


def populate_pdf_list():
    def populate_checks():
        assert os.path.exists(merge_folder_abspath), str_path_invalid
        assert os.path.isdir(merge_folder_abspath), str_path_not_folder
        print(f"Listing PDFs in\t:\t{merge_folder_abspath}")

    populate_checks()
    # Loop through each file in the folder
    for filename in os.listdir(merge_folder_abspath):
        # Check if the file has a .pdf extension (case-insensitive)
        if Pdf.is_pdf(filename):
            abspath = os.path.join(merge_folder_abspath, filename)
            pdf = Pdf(filename=filename, abspath=abspath)
            pdfs_to_merge.append(pdf)
    # Now pdfs_to_merge contains the filename and path of all the PDFs in target_folder
    print(f"PDFs to merge\t:\t{len(pdfs_to_merge)} files")


def merge_pdfs():
    def merge_checks():
        # Make sure that there is at least 2 pdfs to merge
        assert len(pdfs_to_merge) > 1, str_merge_err
        # Check if the file already exists
        if os.path.exists(output_filename):
            response = input(
                str_merge_overwrite_warn).strip().lower()
            if response not in ["y", "yes"]:
                print(str_merge_overwrite_cancel)
                exit()

    def merge_success():
        print("\nOperation successful!")
        print(f"Merged file\t:\t{output_filename}")
        print(f"Location\t:\t{os.getcwd()}")

    merge_checks()
    out = pymupdf.open()
    for pdf in pdfs_to_merge:
        pdf = pymupdf.open(pdf.abspath)
        out.insert_pdf(pdf, annots=False, links=True)
        pdf.close()
    out.save(output_filename)
    merge_success()


def run():
    populate_pdf_list()
    merge_pdfs()


if __name__ == "__main__":
    run()
