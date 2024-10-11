# SQL file import
import mysql.connector

FILE_PATH = r"C:\Users\1\Desktop\Bioinformatics\Autism Spectrum Disorder RNA-seq\NCBI_gene_info_human"


def read_first_line(file_path):
    o_file = open(file_path, "r")
    first_line = o_file.readline()

# lines = o_file.readlines()
# print(len(lines))


conn = mysql.connector.connect(host='localhost', user='root',
                               password='dance')  # MySQL connection.
cursor = conn.cursor()
