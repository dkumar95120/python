class ShippingContainer:

    next_serial = 1337
    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def _next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty (cls, owner_code, *args, **kwargs):
        return cls(owner_code, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._next_serial()
        self.bic = self._make_bic_code(self.owner_code, self.serial)

    @staticmethod
    def _make_bic_code(owner_code, serial, category='U'):
        return owner_code + category + str(serial).zfill(6)


class RefrigeratedShipplingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0

    @staticmethod
    def _make_bic_code (owner_code, serial, category='R'):
        return owner_code + category + str(serial).zfill(6)

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShipplingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too high")
        self._celsius = value
