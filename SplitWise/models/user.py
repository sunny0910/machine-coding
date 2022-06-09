class User:
    def __init__(self, user_id, name, email, phone):
        self._id = user_id
        self._name = name
        self._email = email
        self._phone = phone

    def get_id(self):
        return self._id

    def set_id(self, user_id):
        self._id = user_id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_email(self, email):
        self._email = email

    def get_email(self):
        return self._email

    def set_phone(self, phone):
        self._phone = phone

    def get_phone(self):
        return self._phone
