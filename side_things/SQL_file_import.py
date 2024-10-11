# SQL file import
import mysql.connector

file_path = r"C:\Users\1\Desktop\Bioinformatics\Autism Spectrum Disorder RNA-seq\NCBI_gene_info_human"

o_file = open(file_path, "r")
lines = o_file.readlines()
print(len(lines))

conn = mysql.connector.connect(host='localhost', user='root',
                               password='dance')  # MySQL connection.
print(conn)
