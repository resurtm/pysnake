class Manager:
    resource_names = {}

    def __init__(self):
        self.resources = {}
        for k, v in self.resource_names.items():
            self.resources[k] = self.load_resource(**v) if type(v) is dict else self.load_resource(v)

    def __getitem__(self, item: str):
        if type(item) is not str:
            raise TypeError('Index must be a string')
        if item not in self.resources:
            raise KeyError('This resource does not exist')
        return self.resources[item]

    @staticmethod
    def load_resource(name: str, **kwargs):
        raise NotImplementedError
