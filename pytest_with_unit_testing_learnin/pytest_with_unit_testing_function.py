# import requests
class Calculator:
    def __init__(self, api_url):
        self.api_url = api_url
    
    def add_numbers(self,number1):
        # response = requests.get(self.api_url)
        # number2 = response.json()['number']
        number2= self.api_url.num()
        result = number1 + number2
        return result

# Mock object for the API
class MockAPI:
    def __init__(self, number):
        self.number = number
    
    def num(self):
        # return {'number': self.number}
        return self.number






