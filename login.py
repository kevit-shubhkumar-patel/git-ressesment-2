print("hello world from login.py file")
print("this login.py file is used for authentication and authorization of users")
print("hello world")
print("hello from login.py from user-auth branch")


try:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Simulate authentication logic
    if username == "admin" and password == "password":
        print("Login successful!")
    else:
        print("Login failed. Please try again.") 
except Exception as e:
    print(f"An error occurred: {e}")

