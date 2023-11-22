from airium import Airium
import brothers as br

class page:
    def __init__(self, a):
        self.a: Airium = a
        
    def add_brothers(self, img_prefix, brother:br.brother):
        with self.a.div(id = "brother-card"):
            with self.a.div(klass = "card"):
                self.a.img(klass = "card-img-top", src=(img_prefix+brother.picture), alt=brother.name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
                with(self.a.div(klass = "card-body")):
                    with(self.a.h3(klass = "card-text")):
                        self.a(brother.name)
                    with(self.a.h6(klass = "card-text")):
                        self.a(f"<i>{brother.pronouns}</i>")
                    with(self.a.h5(klass = "card-text")):
                        self.a(brother.initiation_class)
                    with(self.a.h5(klass = "card-text")):
                        self.a(brother.instrument)
                    with(self.a.h5(klass = "card-text")):
                        self.a(f"Majors(s): {brother.major}")
                    if(brother.minor != "N/A"):
                        with(self.a.h5(klass = "card-text")):
                           self.a(f"Minors(s): {brother.minor}")
    
    # TODO: Flesh out officer card functions
    # def add_brother_officers(self, img_prefix, officer:br.officer):
    #     with self.a.div(id = "brother-card"):
    #         with self.a.div(klass = "card"):
    #             self.a.img(klass = "card-img-top", src=(img_prefix+officer.picture), alt=officer.name, onerror="this.onerror=null;this.src='img\\\logos\\\KappaKappaPsiForCards.png'")
    #             with(self.a.div(klass = "card-body")):
    #                 with(self.a.h3(klass = "card-text")):
    #                     self.a(officer.officer_brother.name)
    #                 with(self.a.h6(klass = "card-text")):
    #                     self.a(f"<i>{officer.officer_brother.pronouns}</i>")
    #                 with(self.a.h5(klass = "card-text")):
    #                     self.a(f"<strong>{officer.position}</strong>")
    #                 with(self.a.h5(klass = "card-text")):
    #                     self.a(f"<strong>{officer.email_address}</strong>")
    #                 with(self.a.h5(klass = "card-text")):
    #                     self.a(f"<strong>{officer.officer_brother.initiation_class}</strong>")
    #                 with(self.a.h5(klass = "card-text")):
    #                     self.a(officer.officer_brother.instrument)
    #                 with(self.a.h5(klass = "card-text")):
    #                     self.a(f"Majors(s): {officer.officer_brother.major}")
