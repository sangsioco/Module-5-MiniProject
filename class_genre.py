class Genre:
    def __init__(self, name, description, category):
        self._name = name
        self._description = description
        self._category = category

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_category(self):
        return self._category

    def set_category(self, category):
        self._category = category