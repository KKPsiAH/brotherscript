from airium import Airium
import csv

img_prefix = "img\\people\\"

b1_name = ""
b1_filename = ""
b1_pronouns = ""
b1_class = ""
b1_hometown = ""
b1_instrument = ""
b1_majors = ""
b1_minors = ""

b2_name = ""
b2_filename = ""
b2_pronouns = ""
b2_class = ""
b2_hometown = ""
b2_instrument = ""
b2_majors = ""
b2_minors = ""

b3_name = ""
b3_filename = ""
b3_pronouns = ""
b3_class = ""
b3_hometown = ""
b3_instrument = ""
b3_majors = ""
b3_minors = ""

b4_name = ""
b4_filename = ""
b4_pronouns = ""
b4_class = ""
b4_hometown = ""
b4_instrument = ""
b4_majors = ""
b4_minors = ""

count = 1
csv_count = 0

a = Airium()

for row in open('conditionals.csv'):
    csv_count += 1

b_count = 0

with open('conditionals.csv',newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if count == 1:
            b1_name = row[0]
            b1_filename = b1_name.replace(' ', '_')
            b1_filename += ".JPG"
            b1_pronouns = row[1]
            b1_class = row[2]
            b1_hometown = row[3]
            b1_instrument = row[4]
            b1_majors = row[5]
            b1_minors = row[6]
            count += 1
            b_count += 1
            if b_count == csv_count:
                with a.div(id = "brother-row-2"):
                    with a.div(id = "brother-row-group"):
                        with a.div(id = "brother-card"):
                            with a.div(klass = "card"):
                                a.img(klass = "card-img-top", src=(img_prefix + b1_filename), alt=b1_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                                with(a.div(klass="card-body")):
                                        with(a.h3(klass="card-text")):
                                            a(b1_name)
                                        with(a.h6(klass="card-text")):
                                            a("<i>" + b1_pronouns + "</i>")
                                        with(a.h5(klass="card-text")):
                                            a(b1_class)
                                        with(a.h5(klass="card-text")):
                                            a(b1_hometown)
                                        with(a.h5(klass="card-text")):
                                            a(b1_instrument)
                                        with(a.h5(klass="card-text")):
                                            a("Major(s): " + b1_majors)
                                        if(b1_minors != "N/A"):
                                            with(a.h5(klass="card-text")):
                                                a("Minor(s): " + b1_minors)
        elif count == 2:
            b2_name = row[0]
            b2_filename = b2_name.replace(' ', '_')
            b2_filename += ".JPG"
            b2_pronouns = row[1]
            b2_class = row[2]
            b2_hometown = row[3]
            b2_instrument = row[4]
            b2_majors = row[5]
            b2_minors = row[6]
            count += 1
            b_count += 1
            if b_count == csv_count:
                with a.div(id = "brother-row-2"):
                    with a.div(id = "brother-row-group"):
                        with a.div(id = "brother-card"):
                            with a.div(klass = "card"):
                                a.img(klass = "card-img-top", src=(img_prefix + b1_filename), alt=b1_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                                with(a.div(klass="card-body")):
                                        with(a.h3(klass="card-text")):
                                            a(b1_name)
                                        with(a.h6(klass="card-text")):
                                            a("<i>" + b1_pronouns + "</i>")
                                        with(a.h5(klass="card-text")):
                                            a(b1_class)
                                        with(a.h5(klass="card-text")):
                                            a(b1_hometown)
                                        with(a.h5(klass="card-text")):
                                            a(b1_instrument)
                                        with(a.h5(klass="card-text")):
                                            a("Major(s): " + b1_majors)
                                        if(b1_minors != "N/A"):
                                            with(a.h5(klass="card-text")):
                                                a("Minor(s): " + b1_minors)
                        with a.div(id = "brother-card"):
                            with a.div(klass = "card"):
                                a.img(klass = "card-img-top", src=(img_prefix + b2_filename), alt=b2_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                                with(a.div(klass="card-body")):
                                        with(a.h3(klass="card-text")):
                                            a(b2_name)
                                        with(a.h6(klass="card-text")):
                                            a("<i>" + b2_pronouns + "</i>")
                                        with(a.h5(klass="card-text")):
                                            a(b2_class)
                                        with(a.h5(klass="card-text")):
                                            a(b2_hometown)
                                        with(a.h5(klass="card-text")):
                                            a(b2_instrument)
                                        with(a.h5(klass="card-text")):
                                            a("Major(s): " + b2_majors)
                                        if(b2_minors != "N/A"):
                                            with(a.h5(klass="card-text")):
                                                a("Minor(s): " + b2_minors)
        elif count == 3:
            b3_name = row[0]
            b3_filename = b3_name.replace(' ', '_')
            b3_filename += ".JPG"
            b3_pronouns = row[1]
            b3_class = row[2]
            b3_hometown = row[3]
            b3_instrument = row[4]
            b3_majors = row[5]
            b3_minors = row[6]
            count += 1
            b_count += 1
            if b_count == csv_count:
                with a.div(id = "brother-row-2"):
                    with a.div(id = "brother-row-group"):
                        with a.div(id = "brother-card"):
                            with a.div(klass = "card"):
                                a.img(klass = "card-img-top", src=(img_prefix + b1_filename), alt=b1_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                                with(a.div(klass="card-body")):
                                        with(a.h3(klass="card-text")):
                                            a(b1_name)
                                        with(a.h6(klass="card-text")):
                                            a("<i>" + b1_pronouns + "</i>")
                                        with(a.h5(klass="card-text")):
                                            a(b1_class)
                                        with(a.h5(klass="card-text")):
                                            a(b1_hometown)
                                        with(a.h5(klass="card-text")):
                                            a(b1_instrument)
                                        with(a.h5(klass="card-text")):
                                            a("Major(s): " + b1_majors)
                                        if(b1_minors != "N/A"):
                                            with(a.h5(klass="card-text")):
                                                a("Minor(s): " + b1_minors)
                        with a.div(id = "brother-card"):
                            with a.div(klass = "card"):
                                a.img(klass = "card-img-top", src=(img_prefix + b2_filename), alt=b2_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                                with(a.div(klass="card-body")):
                                        with(a.h3(klass="card-text")):
                                            a(b2_name)
                                        with(a.h6(klass="card-text")):
                                            a("<i>" + b2_pronouns + "</i>")
                                        with(a.h5(klass="card-text")):
                                            a(b2_class)
                                        with(a.h5(klass="card-text")):
                                            a(b2_hometown)
                                        with(a.h5(klass="card-text")):
                                            a(b2_instrument)
                                        with(a.h5(klass="card-text")):
                                            a("Major(s): " + b2_majors)
                                        if(b2_minors != "N/A"):
                                            with(a.h5(klass="card-text")):
                                                a("Minor(s): " + b2_minors)
                    with a.div(id = "brother-row-group"):
                        with a.div(id = "brother-card"):
                            with a.div(klass = "card"):
                                a.img(klass = "card-img-top", src=(img_prefix + b3_filename), alt=b3_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                                with(a.div(klass="card-body")):
                                        with(a.h3(klass="card-text")):
                                            a(b3_name)
                                        with(a.h6(klass="card-text")):
                                            a("<i>" + b3_pronouns + "</i>")
                                        with(a.h5(klass="card-text")):
                                            a(b3_class)
                                        with(a.h5(klass="card-text")):
                                            a(b3_hometown)
                                        with(a.h5(klass="card-text")):
                                            a(b3_instrument)
                                        with(a.h5(klass="card-text")):
                                            a("Major(s): " + b3_majors)
                                        if(b3_minors != "N/A"):
                                            with(a.h5(klass="card-text")):
                                                a("Minor(s): " + b3_minors)
        elif count == 4:
            b4_name = row[0]
            b4_filename = b4_name.replace(' ', '_')
            b4_filename += ".JPG"
            b4_pronouns = row[1]
            b4_class = row[2]
            b4_hometown = row[3]
            b4_instrument = row[4]
            b4_majors = row[5]
            b4_minors = row[6]
            count = 1
            b_count += 1
            with a.div(id = "brother-row-2"):
                with a.div(id = "brother-row-group"):
                    with a.div(id = "brother-card"):
                        with a.div(klass = "card"):
                            a.img(klass = "card-img-top", src=(img_prefix + b1_filename), alt=b1_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                            with(a.div(klass="card-body")):
                                    with(a.h3(klass="card-text")):
                                        a(b1_name)
                                    with(a.h6(klass="card-text")):
                                        a("<i>" + b1_pronouns + "</i>")
                                    with(a.h5(klass="card-text")):
                                        a(b1_class)
                                    with(a.h5(klass="card-text")):
                                        a(b1_hometown)
                                    with(a.h5(klass="card-text")):
                                        a(b1_instrument)
                                    with(a.h5(klass="card-text")):
                                        a("Major(s): " + b1_majors)
                                    if(b1_minors != "N/A"):
                                        with(a.h5(klass="card-text")):
                                            a("Minor(s): " + b1_minors)
                    with a.div(id = "brother-card"):
                        with a.div(klass = "card"):
                            a.img(klass = "card-img-top", src=(img_prefix + b2_filename), alt=b2_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                            with(a.div(klass="card-body")):
                                    with(a.h3(klass="card-text")):
                                        a(b2_name)
                                    with(a.h6(klass="card-text")):
                                        a("<i>" + b2_pronouns + "</i>")
                                    with(a.h5(klass="card-text")):
                                        a(b2_class)
                                    with(a.h5(klass="card-text")):
                                        a(b2_hometown)
                                    with(a.h5(klass="card-text")):
                                        a(b2_instrument)
                                    with(a.h5(klass="card-text")):
                                        a("Major(s): " + b2_majors)
                                    if(b2_minors != "N/A"):
                                        with(a.h5(klass="card-text")):
                                            a("Minor(s): " + b2_minors)
                with a.div(id = "brother-row-group"):
                    with a.div(id = "brother-card"):
                        with a.div(klass = "card"):
                            a.img(klass = "card-img-top", src=(img_prefix + b3_filename), alt=b3_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                            with(a.div(klass="card-body")):
                                    with(a.h3(klass="card-text")):
                                        a(b3_name)
                                    with(a.h6(klass="card-text")):
                                        a("<i>" + b3_pronouns + "</i>")
                                    with(a.h5(klass="card-text")):
                                        a(b3_class)
                                    with(a.h5(klass="card-text")):
                                        a(b3_hometown)
                                    with(a.h5(klass="card-text")):
                                        a(b3_instrument)
                                    with(a.h5(klass="card-text")):
                                        a("Major(s): " + b3_majors)
                                    if(b3_minors != "N/A"):
                                        with(a.h5(klass="card-text")):
                                            a("Minor(s): " + b3_minors)
                    with a.div(id = "brother-card"):
                        with a.div(klass = "card"):
                            a.img(klass = "card-img-top", src=(img_prefix + b4_filename), alt=b4_name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                            with(a.div(klass="card-body")):
                                    with(a.h3(klass="card-text")):
                                        a(b4_name)
                                    with(a.h6(klass="card-text")):
                                        a("<i>" + b4_pronouns + "</i>")
                                    with(a.h5(klass="card-text")):
                                        a(b4_class)
                                    with(a.h5(klass="card-text")):
                                        a(b4_hometown)
                                    with(a.h5(klass="card-text")):
                                        a(b4_instrument)
                                    with(a.h5(klass="card-text")):
                                        a("Major(s): " + b4_majors)
                                    if(b4_minors != "N/A"):
                                        with(a.h5(klass="card-text")):
                                            a("Minor(s): " + b4_minors)
            a.break_source_line()

html = str(a).encode('utf-8')

with open('generated_conditional.html', 'wb') as f:
    f.write(html)