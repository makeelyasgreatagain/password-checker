import re

password = input("🔒 Please enter your password: ")
score = 5

if len(password) < 8:
    print("⚠️ Your password is too short. It should be at least 8 characters.")
    score -= 1

if re.search("[A-Z]", password) == None:
    print("⚠️ Add at least one upper case letter (A-Z) to strengthen your password.")
    score -= 1

if re.search("[a-z]", password) == None:
    print("⚠️ Include lower case letters (a-z) for better security.")
    score -= 1

if re.search("[0-9]", password) == None:
    print("⚠️ Consider adding numbers (0-9) to make your password harder to guess.")
    score -= 1

if re.search("[!@#$%^&*()_+=]", password) == None:
    print("⚠️ Add special characters to boost password strength.")
    score -= 1

print("\n🧮 Password strength score: ", score, "/ 5")
if score < 5:
    print("🚧 Your password could be stronger. Review the suggestions above and try again.")
else:
    print("✅ Excellent! Your password is strong. Just Remember to update it regulary.")
