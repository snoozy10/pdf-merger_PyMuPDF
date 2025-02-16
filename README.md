# PDF-merger using PyMuPDF v1.25.3
This is a straightforward PDF merging tool that uses a high-performance Python library [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/).

# What it does
Want to merge PDFs without uploading sensitive information to unknown servers?
<br>Do it locally using a simple python program!

For project setup, refer to [Project Setup and Running Guide](https://github.com/snoozy10/pdf-merger_PyMuPDF/wiki/Project-Setup-and-Running-Guide).

# How to merge PDFs
1. Create a folder inside the existing folder **pdfsToMerge**.
<br>*[e.g. test-merge-1]*

1. Place your PDFs in the new folder. Make sure to name the PDFs in the desired merge order.
<br>*[e.g. in folder pdfsToMerge/test-merge-1,&nbsp;&nbsp;&nbsp;dummy-pdf-1.pdf&nbsp;&nbsp;&&nbsp;&nbsp;dummy-pdf-2.pdf]*

1. In main.py, set `target-folder` to your newly created folder's name.
<br>*[e.g. to merge pdfs in test-merge-1, `target-folder` = "test-merge-1"]*

1. Run `main.py`.
<br>By default, your output will be saved as *target-folder*_merged in the root folder.
<br>*[e.g. inside project directory, test-merge-1_merged.pdf,*
<br>*merging order:&nbsp;&nbsp;&nbsp;1. dummy-pdf-1.pdf&nbsp;&nbsp;&nbsp;2. dummy-pdf-2.pdf]*

