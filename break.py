correct_pass = "some_pass"
not_found = True

while not_found:
    passw = input("Enter your pass :")
    if passw == correct_pass:
        break

print("Password Matched!")
