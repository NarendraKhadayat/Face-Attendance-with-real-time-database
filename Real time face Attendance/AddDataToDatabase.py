import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "####"
})

ref = db.reference('Students')

data = {
    "053":
        {
            "name": "Narendra Khadayat",
            "enroll": "0511CS211053",
            "admission_year": 2021,
            "semester": "VI",
            "year": 3,
            "branch": "CSE",
            "total_attendance": 5,
            "last_attendance": "2024-03-11 10:10:30"
        },
    "032":
        {
            "name": "Divyansh Chouhan",
            "enroll": "0511CS211032",
            "admission_year": 2021,
            "semester": "VI",
            "year": 3,
            "branch": "CSE",
            "total_attendance": 6,
            "last_attendance": "2024-03-11 10:10:30"
        },
    "026":
        {
            "name": "Deepak Patel",
            "enroll": "0511CS211026",
            "admission_year": 2021,
            "semester": "VI",
            "year": 3,
            "branch": "CSE",
            "total_attendance": 1,
            "last_attendance": "2024-03-11 10:10:30"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
