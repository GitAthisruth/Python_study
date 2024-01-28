import requests
class Employee:
    raise_amt=1.05

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    @property#property or getter method is used to consider this method as the property of this class.

    def email(self):
        return f"{self.first}.{self.last}@email.com"
    
    @property

    def fullname(self):
        return f"{self.first} {self.last}"

    @property

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
        # return int(self.pay*self.raise_amt)

    def monthly_schedule(self,month):
        response=requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok: #response is ok ie,[200]
            return response.text
        else: #[404]
            return "Bad Response"



# obj=Employee("a","b",78)

# print(obj.fullname)
# print(obj.apply_raise)


    
        