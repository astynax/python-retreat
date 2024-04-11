class U(dict):
    def __setitem__(self, key: str, value):
        super().__setitem__(key[::-1], value)


class Meta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return U()

    def __new__(cls, name, bases, body):
        print(f"meta called for {name}")
        return super().__new__(cls, name, bases, body)


class A(metaclass=Meta):
    pass


class B(A):
    foo = 42
    hello = "world"


if __name__ == '__main__':
    print(B.__dict__)
