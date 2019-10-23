import pyrebase

class Firebase():

    def __init__(self):
        self._config = {
                "apiKey": "",
                "authDomain": "",
                "databaseURL": "",
                "storageBucket": "",
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
