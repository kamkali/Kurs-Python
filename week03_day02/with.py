class ClassWith:
    def __init__(self, name='name'):
        self.name = name

    def __enter__(self):
        print("inside __enter__:", self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Inside exit")


def test_with():
    print("Start")
    obj = ClassWith('Adam')
    with obj as x:
        print("Inside with", x.name)
    print('Stop')


if __name__ == '__main__':
    test_with()
