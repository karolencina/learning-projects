class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"

class C(A, B):
    def __init__(self):
        super().__init__()


    def show_props(self):
            print(self.prop1)
            print(self.prop2)

    def show_name(self):
        print(self.name)

c = C()
c.show_name()