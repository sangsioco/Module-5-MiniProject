
class Author:
    def __init__(self, name, biography):
        self._name = name
        self._biography = biography

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_biography(self):
        return self._biography

    def set_biography(self, biography):
        self._biography = biography

