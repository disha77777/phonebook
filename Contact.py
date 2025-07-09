class Contact:
    phone = []
    def __init__(name,self, number):
        self.name = name 
        self.number = number
    
    @classmethod 
    def delete(cls, name):
        for contact in cls.phone:
            if contact['name']==name:
                cls.phone.remove(contact)
    
    @classmethod
    def add(cls, name, phone):
        Contact = {"name":name, "phone":phone}
        cls.phone.append(Contact)
    
    @classmethod
    def check(cls,name):
        if name in cls.phone: 
            print("Exists")

Contact.add("barry",98712345)
Contact.add("lia",87678677)
print(Contact.phone)