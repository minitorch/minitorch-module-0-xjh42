from minitorch import Module, Parameter

class OtherModule(Module):
    pass


class MyModule(Module):
    def __init__(self):
        # Must initialize the super class!
        super().__init__()

        # Type 1, a parameter.
        self.parameter1 = Parameter(15)

        # Type 2, user data
        self.data = 25


        # Type 3. another Module
        self.sub_module = OtherModule()

def main() -> None:
    print(MyModule().named_parameters())

main()