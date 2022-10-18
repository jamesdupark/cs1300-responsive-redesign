

class mph():
    def __init__(self, prop_set=[], x=0, y=3):
        self.prop_set=set(prop_set)
        self.x=x
        self.y=y

    def add_prop(self, str):
        self.prop_set.add(str)


a = mph()
b = mph()
c = mph(set())
d = mph({'hi', 'bye'})
a.add_prop('hi')
print(a.prop_set)
print(b.prop_set)
print(c.prop_set)
print(d.prop_set)