class Every:
    def __getattribute__(self, name):
        return self

    def __call_(self, *_args, **_kwargs):
        return self

    def __iter__(self):
        return self

    def __next__(self):
        return self

    def __add__(self, other):
        return self
