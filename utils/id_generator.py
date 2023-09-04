class IDGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IDGenerator, cls).__new__(cls)
            cls._instance.id = 0
        return cls._instance

    def generate_id(self):
        self.id += 1
        return self.id


