class MusicgenreDTO():
    def __init__(self):
        self.id = None
        self.description = None

    def is_Empty(self):
        return (self.id is None and self.description is None)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_description(self):
        return self.title

    def set_description(self, title):
        self.title = title
    
    def musicgenre_to_json(self):
        # To Be Complete
        pass