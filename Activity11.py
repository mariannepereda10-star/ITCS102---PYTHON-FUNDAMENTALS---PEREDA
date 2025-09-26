name = input ("Enter your name:")
print("Welcome",name, "!","We will determine your temperature for today\n(cold, lukewarm, warm, hot, and above boiling hot) ")
temp = eval(input("Please enter your temperature today -->"))
loc = input("Enter your location: (Herta, DLL):")
if temp >= 1 and temp <= 20:
    print("The temperature in",loc,"is cold\nPlease bring some jacket it's freezing!\nYou might also want to grab a scarf and gloves to stay warm.\nStay safe and take care",name,"!")
elif temp >= 21 and temp <= 30:
    print("The temperature in",loc,"is lukewarm, but not too chilly.\nBringing a light layer would be a good idea. Stay safe and take care",name,"!")  
elif temp >= 31 and temp <= 40:
    print("The temperature in",loc,"is warm and sunny.\nYou can dress lightly and enjoy the day. Don't forget your sunscreen and stay hydrated!\nStay safe and have fun",name,"!")
elif temp >= 41 and temp <= 50:  
    print("The temperature in",loc,"is scorching hot! Stay cool and hydrated by drinking plenty of water.\nWear light, breathable clothing and don't forget your sunscreen.\nStay safe and take care",name,"!")
elif temp >= 51 and temp <= 200:  
    print("Caution: The temperature in",loc,"is extremely hot, almost boiling point!\nTake extreme precautions to avoid heatstroke and burns.\nStay indoors if possible, and stay hydrated.Stay safe and take care",name,"!")
else:
    print("Invalid Temperature")  