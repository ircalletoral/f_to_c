#Initial Statement
print("*****************************************")
print("Good evening,")
p_temp = input("Please enter the patient's temperature in F: ")
print("*****************************************")

#Digit Check and Main computing line
#I spent like 1 hour finding the best way to check for digits, at the end I chose to check
#For the absence of letters, this worked. What would be a way to check for no letters or spaces?
#With this code, the input twenty 25 will gve me an error code, and I would like for it to be redirected to the negative answer
if p_temp.isalpha() == False:
    #Convert to float if applicable
    p_temp = float(p_temp)
    if p_temp >= 99.5:
        print("The patient has a high temperature")
    elif p_temp < 99.5 and p_temp >= 95.0:
        print("The patient has a normal temperature")
    else:
        #I wanted to add this, mainly because hypothermia can still be very dangerous. Hope it was ok
        print("The patient has a low temperature")
else:
    print("Please enter your answer as a digit, e.x 27.0")

print("Thank you for using our services, have a great day")
