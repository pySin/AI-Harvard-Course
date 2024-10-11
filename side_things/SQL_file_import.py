# SQL file import
import mysql.connector

FILE_PATH = r"C:\Users\1\Desktop\Bioinformatics\Autism Spectrum Disorder RNA-seq\NCBI_gene_info_human"


def read_first_line(file_path):
    o_file = open(file_path, "r")
    # just_line = first_line = o_file.readline()
    # just_line_2 = second_line = o_file.readline()
    # print(f"Juss Line 1: {just_line}")
    # print(f"Juss Line 2: {just_line_2}")
    first_line = o_file.readline().split(",")
    second_line = o_file.readline().split(",")
    print(first_line)
    print(second_line)
    for i in range(len(first_line)):
        print(f"{first_line[i]} : {second_line[i]}")
    return first_line


def create_table_sql_query(table_name: str, ):

    columns_with_datatypes = """
                                #tax_id INT,
                                GeneID INT,
                                Symbol VARCHAR(255),
                                LocusTag VARCHAR(255),
                                Synonyms VARCHAR(255),
                                dbXrefs VARCHAR(255),
                                chromosome VARCHAR(10),
                                map_location VARCHAR(50),
                                description VARCHAR(100),
                                type_of_gene VARCHAR(255),
                                Symbol_from_nomenclature_authority VARCHAR(255),
                                Full_name_from_nomenclature_authority VARCHAR(255),
                                Nomenclature_status VARCHAR(20),
                                Other_designations VARCHAR(255),
                                Modification_date VARCHAR(55),
                                Feature_type VARCHAR(66)
                             """

    query = f"CREATE TABLE IF NOT EXISTS {table_name} ()"

# conn = mysql.connector.connect(host='localhost', user='root',
#                                password='dance')  # MySQL connection.
# cursor = conn.cursor()


read_first_line(FILE_PATH)
