
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("./serviceaccountkey.json")
app = firebase_admin.initialize_app(cred, {'storageBucket':'network-management-syste-a8cde.appspot.com'})

bucket = storage.bucket()
