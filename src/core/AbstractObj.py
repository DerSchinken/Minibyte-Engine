from abc import ABC, abstractmethod


class AbstractObj(ABC):
    objects: list = []  # Using shared class var for better manageability

    def __init__(self, *args, **kwargs):
        self.parent = kwargs.get("parent")
        self.position = kwargs.get("position")

        if not kwargs.get("__ObjControllerInstance"):
            self.objects.append(self)

        self.init_object(*args, **kwargs)

    @abstractmethod
    def init_object(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_position(self) -> int:
        pass

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.objects = []


class Test:
    tests = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.tests = []


class NewTest1(Test):
    def __init__(self):
        self.tests.append("test")


class NewTest2(Test):
    def __init__(self):
        self.tests.append("test2")


x = Test()
y = NewTest1()
z = NewTest2()
NewTest1()
NewTest2()

print(x.tests, y.tests, z.tests)