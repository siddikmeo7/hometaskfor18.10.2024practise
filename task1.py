import time

def message (msg):
    print("Processing...")
    time.sleep(5)
    print(msg)
    print("Proggramm is done!")

while True:
    user_input = input("Enter the message(type 'exit' to exit): ")
    if user_input == 'exit':
        break
    message(user_input)
print("The proggram is exited!")