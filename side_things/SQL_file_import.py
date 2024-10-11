# SQL file import
import mysql.connector

FILE_PATH = r"C:\Users\1\Desktop\Bioinformatics\Autism Spectrum Disorder RNA-seq\NCBI_gene_info_human"


def read_first_line(file_path):
    with open(file_path, "r") as o_file:
        first_line = o_file.readline().split(",")
    return first_line


def create_table_sql_query(table_name: str):

    columns_with_datatypes = """
                                tax_id INT,
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

    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_datatypes})"
    return query


def create_table(table_name):
    query = create_table_sql_query(table_name)

    conn = mysql.connector.connect(host='localhost', user='root',
                                   password='dance')  # MySQL connection.
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def create_insert_query(values_line):
    query = f"INSERT INTO asd_rna_seq.gen_human VALUES({values_line})"
    return query


def insert_values():
    o_file = open(FILE_PATH, "r")
    first_line_omit = o_file.readline()

    # x = 0
    is_line = True
    while is_line:
        line = o_file.readline()
        if not line:
            is_line = False
        # if x == 5:
        #     is_line = False
        # x += 1

        query = create_insert_query(line)
        conn = mysql.connector.connect(host='localhost', user='root',
                                       password='dance')  # MySQL connection.
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


insert_values()
# read_first_line(FILE_PATH)
# create_table("asd_rna_seq.gen_human")

# op_file = open(FILE_PATH, "r")
# l1 = op_file.readline().split(",")
# l2 = op_file.readline().split(",")

# print(l1)
# print(l2)
# print(len(l1))
# print(len(l2))
