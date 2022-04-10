class Parent1():
    def assign_s_one(self, str1):
        self.str1 = str1

    def show_str_one(self):
        return self.str1

class Parent2():
    def assign_s_two(self, str2):
        self.str2 = str2

    def show_str_two(self):
        return self.str2


class Child(Parent1, Parent2):
    def assign_s_three(self, str3):
        self.str3 = str3

    def show_str_three(self):
        return self.str3

c1 = Child()
c1.assign_s_one("I am Parent 1")
c1.assign_s_two("I am Parent 2")
c1.assign_s_three("I am Parent 3")
c1.show_str_three()
# c1.show_str_one()
# c1.show_str_two()