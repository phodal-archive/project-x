from flask_login import (UserMixin)

import models


class User(UserMixin):
    def __init__(self, name=None, email=None, password=None, active=True):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.isAdmin = False
        self.id = None

    def save(self):
        newuser = models.User(name=self.name, email=self.email, password=self.password, active=self.active)
        newuser.save()
        print "new user id = %s " % newuser.id
        self.id = newuser.id
        return self.id

    def get_by_email(self, email):
        db_user = models.User.objects.get(email=email)
        if db_user:
            self.email = db_user.email
            self.active = db_user.active
            self.id = db_user.id
            return self
        else:
            return None

    def is_exist(self, new_mail):
        all_user = models.User.objects(email=new_mail).count()
        if all_user >= 1:
            return False
        else:
            return True

    def get_by_email_w_password(self, email):

        try:
            db_user = models.User.objects.get(email=email)

            if db_user:
                self.email = db_user.email
                self.active = db_user.active
                self.password = db_user.password
                self.id = db_user.id
                return self
            else:
                return None
        except:
            print "there was an error"
            return None

    def get_mongo_doc(self):
        if self.id:
            return models.User.objects.with_id(self.id)
        else:
            return None

    def get_by_id(self, id):
        db_user = models.User.objects.with_id(id)
        if db_user:
            self.email = db_user.email
            self.active = db_user.active
            self.id = db_user.id

            return self
        else:
            return None
