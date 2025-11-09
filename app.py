# app.py
def greet_user(name):
    return f"Hello, {name}! Welcome to Git practice."

if __name__ == "__main__":
    username = input("Enter your name: ")
    print(greet_user(username))
