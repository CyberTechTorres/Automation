#FAKE MADE UP PAYLOAD EXAMPLE
#!/usr/bin/python3/fakepayload
#Copyright 
#Written by: Andres Torres
#Github: https://github.com/cybertechtorres
def greet_user(name):
    print("Hello " + username)  # Error: 'username' is not defined

def calculate_sum(a, b):
    result = a + c  # Error: 'c' is not defined
    return result

def get_user_age():
    age = input("Enter your age: ")
    if age > 18:  # Error: comparing string input directly to int
        print("You are an adult.")
    else:
        pritn("You are a minor.")  # Typo in 'print'

def fetch_data(url):
    response = requests.get(ur1)  # Error: misspelled 'url'
    return response.json()

def main():
    greet_user()  # Error: missing required argument
    total = calculate_sum(5)  # Error: missing one argument
    data = fetch_data()  # Error: missing one argument
