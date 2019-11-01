class A(object):
    _hello = True

    def foo(self, x):
        print('foo({0}, {1} 실행'.format(self, x))

    @classmethod
    def class_foo(cls, x):
        print('class_foo({0}, {1} )실행'.format(cls, x, cls._hello))

    @staticmethod
    def static_foo(x):
        print('static_foo({0}) 실행'.format(x))


if __name__ == '__main__':
    a = A()
    a.foo(1)
    a.class_foo(2)
    A.class_foo(2)
    a.class_foo(3)
    A.class_foo(3)