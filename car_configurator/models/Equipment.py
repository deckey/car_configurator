class EquipmentComponent(dict):
    ''' Abstract component class '''

    def __init__(self, *args, **kwargs):
        self.name = args[0]

    def get_name(self):
        return self.name


class EquipmentLeaf(EquipmentComponent):
    ''' Concrete child component, inherits from abstract component'''

    def __init__(self, *args, **kwargs):
        EquipmentComponent.__init__(self, *args, **kwargs)
        self.price = 0

    def set_price(self, amount):
        self.price = amount


class EquipmentComposite(EquipmentComponent):
    ''' Recursive tree structure concrete class '''

    def __init__(self, *args, **kwargs):
        EquipmentComponent.__init__(self, *args, **kwargs)
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def add_children(self, children, prices):
        for child, price in zip(children, prices):
            element = EquipmentLeaf(child)
            element.set_price(price)
            self.children.append(element)

    def get_children(self):
        return self.children
