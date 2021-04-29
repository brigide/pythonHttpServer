
class Contact:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone



    def getContact(self):
        contact = {
            "name": self.name,
            "address": self.address,
            "phone": self.phone
        }
        return contact



    @property           
    def name(self): 
        return self._name

    @name.setter
    def name(self, name):
        self._name = name



    @property           
    def address(self): 
        return self._address

    @address.setter
    def address(self, address):
        self._address = address



    @property           
    def phone(self): 
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

