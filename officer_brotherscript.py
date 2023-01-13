from airium import Airium
import csv

img_prefix = "img\\people\\"

b1_name = ""
b1_filename = ""
b1_pronouns = ""
b1_position = ""
b1_email = ""
b1_class = ""
b1_major = ""
b1_instrument = ""
b1_blurb = ""

b2_name = ""
b2_filename = ""
b2_pronouns = ""
b2_position = ""
b2_email = ""
b2_class = ""
b2_major = ""
b2_instrument = ""
b2_blurb = ""

count = 1
csv_count = 0

a = Airium()

for row in open('officers.csv'):
    csv_count += 1
num_elected = 8
num_appointed = 8
b_count = 0

with open('officers.csv',newline='', encoding="utf-8-sig") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if count == 1:
            b1_name = row[0]
            b1_filename = b1_name.replace(' ', '_') + ".JPG"
            b1_pronouns = row[1]
            b1_position = row[2]
            b1_email = row[3]
            b1_class = row[4]
            b1_major = row[5]
            b1_instrument = row[6]
            b1_blurb = row[7]
            count += 1
            b_count += 1
            if b_count <= num_elected:
                div_id = "officer-row"
            else:
                div_id = "officer-row-2"
            if b_count == csv_count:
                with a.div(id = div_id):
                    with a.div(id = "officer-card"):
                        with a.div(klass = "card"):
                            a.img(klass = "card-img-top", src = img_prefix + b1_filename, alt = b1_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                            with a.div(klass = "card-body"):
                                with a.h3(klass = "card-text"):
                                    a(b1_name)
                                with a.h6(klass = "card-text"):
                                    a("<i>" + b1_pronouns + "</i>")
                                with a.h5(klass = "card-text"):
                                    a("<strong>" + b1_position + "</strong>")
                                with a.h6(klass = "card-text"):
                                    a("<strong>" + b1_email + "</strong>")
                                with a.p(klass = "card-text"):
                                    a("<strong>Semester initiated: " + b1_class + "</strong>")
                                with a.p(klass = "card-text"):
                                    a("<strong>Major(s): " + b1_major + "</strong>")
                                with a.p(klass = "card-text"):
                                    a("<strong>Main instrument: " + b1_instrument + "</strong>")
                                if(b1_blurb != "N/A"):
                                    with a.p(klass = "card-text"):
                                        a("<i>" + b1_blurb + "</i>")
        elif count == 2:
            b2_name = row[0]
            b2_filename = b2_name.replace(' ', '_') + ".JPG"
            b2_pronouns = row[1]
            b2_position = row[2]
            b2_email = row[3]
            b2_class = row[4]
            b2_major = row[5]
            b2_instrument = row[6]
            b2_blurb = row[7]
            count = 1
            b_count += 1
            if b_count <= num_elected:
                div_id = "officer-row"
            else:
                div_id = "officer-row-2"
            with a.div(id = div_id):
                with a.div(id = "officer-card"):
                    with a.div(klass = "card"):
                        a.img(klass = "card-img-top", src = img_prefix + b1_filename, alt = b1_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                        with a.div(klass = "card-body"):
                            with a.h3(klass = "card-text"):
                                a(b1_name)
                            with a.h6(klass = "card-text"):
                                a("<i>" + b1_pronouns + "</i>")
                            with a.h5(klass = "card-text"):
                                a("<strong>" + b1_position + "</strong>")
                            with a.h6(klass = "card-text"):
                                a("<strong>" + b1_email + "</strong>")
                            with a.p(klass = "card-text"):
                                a("<strong>Semester initiated: " + b1_class + "</strong>")
                            with a.p(klass = "card-text"):
                                a("<strong>Major(s): " + b1_major + "</strong>")
                            with a.p(klass = "card-text"):
                                a("<strong>Main instrument: " + b1_instrument + "</strong>")
                            if(b1_blurb != "N/A"):
                                with a.p(klass = "card-text"):
                                    a("<i>" + b1_blurb + "</i>")
                with a.div(id = "officer-card"):
                    with a.div(klass = "card"):
                        a.img(klass = "card-img-top", src = img_prefix + b2_filename, alt = b2_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                        with a.div(klass = "card-body"):
                            with a.h3(klass = "card-text"):
                                a(b2_name)
                            with a.h6(klass = "card-text"):
                                a("<i>" + b2_pronouns + "</i>")
                            with a.h5(klass = "card-text"):
                                a("<strong>" + b2_position + "</strong>")
                            with a.h6(klass = "card-text"):
                                a("<strong>" + b2_email + "</strong>")
                            with a.p(klass = "card-text"):
                                a("<strong>Semester initiated: " + b2_class + "</strong>")
                            with a.p(klass = "card-text"):
                                a("<strong>Major(s): " + b2_major + "</strong>")
                            with a.p(klass = "card-text"):
                                a("<strong>Main instrument: " + b2_instrument + "</strong>")
                            if(b2_blurb != "N/A"):
                                with a.p(klass = "card-text"):
                                    a("<i>" + b2_blurb + "</i>")
            a.break_source_line()
            
html = str(a).encode('utf-8')

with open('generated_officers.html', 'wb') as f:
    f.write(html)