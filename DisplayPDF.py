import sys
import tkinter as tk
from tkPDFViewer import tkPDFViewer as pdf
from multiprocessing import Process
# from tkdocviewer import *

def DisplayPdf(path):
    print(path)
    notRoot = tk.Tk()
    notRoot.geometry("780x720")
    v1 = pdf.ShowPdf()
    v2 = v1.pdf_view(notRoot, pdf_location=path, width = 80, height = 100)

    v2.pack()
    notRoot.mainloop()

if __name__ == "__main__":
    # path = "E:\\Sem-4\\Lab_Assignments\\Python_Lab\\Experiment_01\\Write-up\\01_Aamir-Ansari_Python-Lab_Experiment-01.pdf"
    path = "E:\\Sem-3\\Data_Structures\\C_and_Data_Structures_-_Balaguruswamy.pdf"
    DisplayPdf(path)
