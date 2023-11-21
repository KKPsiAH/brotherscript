from airium import Airium
import brothers as br
import brothers_page as page
import csv

img_prefix = "img\\people\\"

brother_dict = {}

def create_brother_from_csv_row(row):
    b = br.brother(name= row[0], 
                   picture= (row[0].replace(' ', '_')+".JPG"),
                   pronouns= row[1],
                   initiation_class= row[2],
                   hometown= row[3],
                   instrument= row[4],
                   major= row[5],
                   minor= row[6])
    return b 

def build_brother_dict(csv_file: str):
    with open(csv_file, newline='', encoding="utf-8-sig") as csvfile:
        csvreader = csv.reader(csvfile)
        index = 0
        current_column = 1
        brother_row_col_dict = {}
        for row in csvreader:
            match current_column:
                case 1:
                    brother_row_col_dict[current_column] = create_brother_from_csv_row(row)
                    current_column += 1
                case 2:
                    brother_row_col_dict[current_column] = create_brother_from_csv_row(row)
                    current_column += 1
                case 3:
                    brother_row_col_dict[current_column] = create_brother_from_csv_row(row)
                    current_column += 1
                case 4:
                    brother_row_col_dict[current_column] = create_brother_from_csv_row(row)
                    brother_dict[index] = brother_row_col_dict
                    index += 1
                    current_column = 1
                    brother_row_col_dict = {}

def brother_row_builder(p: page.page, brother_row_col_dict: dict):
    column = 1
    while(column < 5):
        p.add_brothers(img_prefix = img_prefix,brother = brother_row_col_dict[column])
        column+= 1            

build_brother_dict('active.csv')

p = page.page(a = Airium())

for index in brother_dict.keys():
    with p.a.div(id = "brother-row"):
        with p.a.div(id = "brother-row-group"):
            brother_row_builder(p, brother_dict[index])
    p.a.break_source_line()

html = str(p.a).encode('utf-8')

with open('generated_active.html', 'wb') as f:
    f.write(html)