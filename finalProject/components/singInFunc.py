from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class SignIn:
    def __init__(self, username , password):
        Firebase = firebase_admin.initialize_app(credentials.Certificate("components/ServiceAccountKey.json"))
        self.db = firestore.client()

        self.username = username
        self.password = password
        self.data = self.db.collection('done').document('users').get().to_dict()
        self.password = self.data['password']
        self.username = self.data['username']


    def check(self):
        if self.username == self.username and self.password == self.password:
            return True
        else:
            return False