from xlrd import open_workbook
import pandas
from os import listdir
from os.path import isfile, join

import csv


def from_xls_to_csv_file(filename):
    xls = pandas.ExcelFile("DataSet/XLS/"+filename)
    df = xls.parse(sheet_name="Feuil1", index_col = None, na_values=['NA'], encoding = "utf-8")
    df.to_csv("DataSet/CSV/"+filename.replace('xls', 'csv'), encoding="utf-8")


def from_xls_to_csv_folder(foldername):
    for file in listdir(foldername):
        print(file)
        from_xls_to_csv_file(file)