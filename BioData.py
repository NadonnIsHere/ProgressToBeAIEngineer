name =  ("Name: Nazneen Bafadhal")
age =  ("Age: 15")
hobby = ("Hobby: Learning")
Future_career = ("I will be: AI Engineer")
user_feedback = input("Your Feedback: ")

print("Hello, my name is", name)
print("I am", age, "years old.") 
print("My hobby is", hobby, "because I believe knowledge is the power of everything.")
print("In the future I will be an", Future_career)
print("I think that's all from me. If you want to contact me, @nazneenbafadhal <- my email.")
print("Your feedback here ->", user_feedback)

# Simpan feedback ke file
with open("feedback.txt", "a") as file:
    file.write(user_feedback + "\n")
