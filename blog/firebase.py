import pyrebase

class Firebase():

    def __init__(self):
        self._config = {
                "apiKey": "AIzaSyAZ1xdxRxoWCKmOLIyRQSK3L5PPRfOUGPg",
                "authDomain": "flask-blog-e0abe.firebaseapp.com",
                "databaseURL": "https://flask-blog-e0abe.firebaseio.com",
                "storageBucket": "flask-blog-e0abe.appspot.com",
        }
        self.fr = pyrebase.initialize_app(self._config)
        self._auth = self.fr.auth()
        self._db = self.fr.database()
    def sign_in(self, email, password):
        try:
            user = self._auth.sign_in_with_email_and_password(email, password)
            print(user)
            return user
        except:
            print('burtgelgui hereglech')
            return None
