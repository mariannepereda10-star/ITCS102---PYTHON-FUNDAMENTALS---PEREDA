print("COUNTDOWN TIMER SIMULATOR")
num = eval(input("Enter the starting number for countdown: "))
import time

for ely in range (num, 0, -1):
    print(ely)
    time.sleep(1)
    
print("Liftoff", "!")   