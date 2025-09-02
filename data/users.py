import os

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), '..', 'resources')
PICTURE = "avatar.jpg"
PICTURE_PATH = os.path.join(RESOURCES_DIR, PICTURE)

class UserData:
    def __init__(self, h1, first_name, last_name, full_name, email, gender, 
                 mobile, picture, picture_path, hobbies, subjects, date_of_birth, date_of_birth_short):
        self.h1 = h1
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email
        self.gender = gender
        self.mobile = mobile
        self.picture = picture
        self.picture_path = picture_path
        self.hobbies = hobbies
        self.subjects = subjects
        self.date_of_birth = date_of_birth
        self.date_of_birth_short = date_of_birth_short

FORM_DATA = {
    "h1": "Practice Form",
    "first_name": "Margaret",
    "last_name": "Abercrombie",
    "full_name": "Margaret Abercrombie",
    "email": "margaret.abercrombie@example.com",
    "gender": "Female",
    "mobile": "1234567890",
    "picture": PICTURE,
    "picture_path": PICTURE_PATH,
    "hobbies": ["Sports", "Reading", "Music"],
    "subjects": "Social Studies",
    "date_of_birth": {
        "day": "08",
        "month": "March",
        "year": 1999,
        },
    "date_of_birth_short": "08 Mar 1999",
    }
user = UserData(**FORM_DATA)