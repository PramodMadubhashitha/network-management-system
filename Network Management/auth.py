import pyrebase
config = {

        "apiKey": "AIzaSyBZEEKtWSgkYQjyfYKxKt4xkYZkM2xZwjI",
        "authDomain": "network-management-syste-a8cde.firebaseapp.com",
        "projectId": "network-management-syste-a8cde",
        "storageBucket": "network-management-syste-a8cde.appspot.com",
        "serviceAccount": "serviceaccountkey.json",
        "messagingSenderId": "709967088121",
        "appId": "1:709967088121:web:eadc51314f4a6e28b3d528",
        "measurementId": "G-ELR3L4MFPL"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
my_image = "IMG_0051.jpg"

storage.child(my_image).put(my_image)

# email = "test1@gmail.com"
# password = "123456789"
# auth.create_user_with_email_and_password(email, password)