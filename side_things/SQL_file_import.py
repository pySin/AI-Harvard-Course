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
                                Synonyms TEXT,
                                dbXrefs TEXT,
                                chromosome TEXT,
                                map_location TEXT,
                                description TEXT,
                                type_of_gene TEXT,
                                Symbol_from_nomenclature_authority TEXT,
                                Full_name_from_nomenclature_authority TEXT,
                                Nomenclature_status TEXT,
                                Other_designations TEXT,
                                Modification_date TEXT,
                                Feature_type TEXT
                             """

    query = f"CREATE TABLE IF NOT EXISTS {table_name} ()"

# conn = mysql.connector.connect(host='localhost', user='root',
#                                password='dance')  # MySQL connection.
# cursor = conn.cursor()


# read_first_line(FILE_PATH)
