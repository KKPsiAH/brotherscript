# Defines what a brother is and what an officer is
class brother:
    def __init__(self, name, pronouns = None, initiation_class = None, hometown = None, instrument = None,
                 major = None, minor=None, picture=None):
        self.name = name # We will only require a name and make every other piece of information optional
        self.pronouns = pronouns if pronouns is not None else None
        self.initiation_class = initiation_class if initiation_class is not None else None
        self.hometown = hometown if hometown is not None else None
        self.instrument = instrument if instrument is not None else None
        self.major = major if major is not None else None
        self.minor = minor if minor is not None else None
        self.picture = picture if picture is not None else None

class officer:
    def __init__(self, officer_brother, position, email_address, blurb):
        self.officer_brother:brother = officer_brother
        self.position = position
        self.email_address = email_address
        self.blurb = blurb