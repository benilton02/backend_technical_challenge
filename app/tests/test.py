from unittest import TestCase, main
import requests, json



class TestApi(TestCase):

    def setUp(self) :
        self.server = "http://0.0.0.0:5000"
        self.hello = "/hello" 
        self.credit = "/credit"
        self.anything = "/anything"


    def test_hello(self):
        req = requests.get(self.server + self.hello)
        self.assertEqual(req.status_code, 200)


    def test_error_handler(self):
        req = requests.get(self.server + self.anything)
        self.assertEqual(req.status_code, 404)
    
       
    def test_credit_approved(self):
        """Credit approved. Age greater than 18 and credit less than 1.000.000,00 BRL"""        
        payload = {
            'name': 'Kakaroto', 
            'age': 24,   
            'credit': 10000
        }
        req_post = requests.post(self.server + self.credit, json = payload)
        self.assertEqual(req_post.status_code, 201)
        
        ticket = str(req_post.json()["ticket"])
        
        req_get = requests.get(self.server+ self.credit+ "/" + ticket)
        self.assertEqual(req_get.status_code, 200)

    
    def test_age_equal_eighteen_and_credit_equal_one_million(self):
        payload = {
            'name': 'Bulma', 
            'age': 18,   
            'credit':1000000
        }
        req_post = requests.post(self.server + self.credit, json = payload)
        self.assertEqual(req_post.status_code, 201)
        
        ticket = str(req_post.json()["ticket"])
        
        req_get = requests.get(self.server+ self.credit+ "/" + ticket)
        self.assertEqual(req_get.status_code, 200)

    
    def test_age_equal_eighteen_and_credit_less_one_million(self):
        payload = {
            'name': 'Freeza', 
            'age': 18,   
            'credit': 50000
        }
        req_post = requests.post(self.server + self.credit, json = payload)
        self.assertEqual(req_post.status_code, 201)
        
        ticket = str(req_post.json()["ticket"])
        
        req_get = requests.get(self.server+ self.credit+ "/" + ticket)
        self.assertEqual(req_get.status_code, 200)

    
    def test_age_equal_eighteen_and_credit_greater_one_million(self):
        payload = {
            'name': 'Trunks', 
            'age': 18,   
            'credit': 2000002
        }
        req_post = requests.post(self.server + self.credit, json = payload)
        self.assertEqual(req_post.status_code, 201)
        
        ticket = str(req_post.json()["ticket"])
        
        req_get = requests.get(self.server+ self.credit+ "/" + ticket)
        self.assertEqual(req_get.status_code, 200)

    
    def test_age_less_eighteen_and_credit_equal_one_million(self):
        payload = {
            'name': 'Gohan', 
            'age': 17,   
            'credit': 1000000
        }
        req_post = requests.post(self.server + self.credit, json = payload)
        self.assertEqual(req_post.status_code, 201)
        
        ticket = str(req_post.json()["ticket"])
        
        req_get = requests.get(self.server+ self.credit+ "/" + ticket)
        self.assertEqual(req_get.status_code, 200)

    
    def test_age_less_eighteen_and_credit_less_one_million(self):
        payload = {
            'name': 'Gohan', 
            'age': 17,   
            'credit': 25000
        }
        req_post = requests.post(self.server + self.credit, json = payload)
        self.assertEqual(req_post.status_code, 201)
        
        ticket = str(req_post.json()["ticket"])
        
        req_get = requests.get(self.server+ self.credit+ "/" + ticket)
        self.assertEqual(req_get.status_code, 200)

    
    def test_age_less_eighteen_and_credit_greater_one_million(self):
        payload = {
            'name': 'Gohan', 
            'age': 17,   
            'credit': 2500000
        }
        req_post = requests.post(self.server + self.credit, json = payload)
        self.assertEqual(req_post.status_code, 201)
        
        ticket = str(req_post.json()["ticket"])
        
        req_get = requests.get(self.server+ self.credit+ "/" + ticket)
        self.assertEqual(req_get.status_code, 200)

    
    def test_age_greater_eighteen_and_credit_equal_one_million(self):
        payload = {
            'name': 'Gohan', 
            'age': 20,   
            'credit': 1000000
        }
        req_post = requests.post(self.server + self.credit, json = payload)
        self.assertEqual(req_post.status_code, 201)
        
        ticket = str(req_post.json()["ticket"])
        
        req_get = requests.get(self.server+ self.credit+ "/" + ticket)
        self.assertEqual(req_get.status_code, 200)

    
    def test_age_greater_eighteen_and_credit_greater_one_million(self):
        payload = {
            'name': 'Gohan', 
            'age': 25,   
            'credit': 5000000
        }
        req_post = requests.post(self.server + self.credit, json = payload)
        self.assertEqual(req_post.status_code, 201)
        
        ticket = str(req_post.json()["ticket"])
        
        req_get = requests.get(self.server+ self.credit+ "/" + ticket)
        self.assertEqual(req_get.status_code, 200)

def execute_all():        
    main()