# PDF-merger using PyMuPDF v1.25.3
This is a straightforward PDF merging tool that uses a high-performance Python library "[PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)".

# How to use
1. Create a folder inside the existing folder "**pdfsToMerge**"
   <br>*[e.g. test-merge-1]*

1. Place your PDFs in the new folder. Make sure to name the PDFs in the desired output order.
   <br>*[e.g. in folder pdfsToMerge/test-merge-1, dummy-pdf-1.pdf & dummy-pdf-2.pdf]*

1. In main.py, set `target-folder` to your newly created folder's name.
   <br>*[e.g. to merge pdfs in test-merge-1, `target-folder` = "test-merge-1"]*

1. Run `main.py`.
   <br>By default, your output will be saved as *target-folder*_merged in the root folder.
   <br>*[e.g. inside project directory, test-merge-1_merged.pdf]*

