import time
import os
import sys
import subprocess
import math
MacOS = "1"
Windows= "2"

print("⚠ Please state your Operating System due to compatibility issues ⚠")
print("")
print("Mac OS/Any Linux Distro or flavour (1)   Windows (2)")
Opsys = input(">>> ")
if Opsys == MacOS:
    def clear_console():
        os.system('clear')
if Opsys == Windows:
    def clear_console():
        os.system('cls')  


clear_console()
print ("════════════════════════════════════════════════════════════════════")
print ("Welcome to Python Math formula Solver! (♥ Made with Love by Emil Toth ♥)")
print ("════════════════════════════════════════════════════════════════════")
name = input("Please tell me your name first! \n════════════════════════════════════════════════════════════════════\n>>>  ")
clear_console()
print ("\n Hello " + name + ", In what Subject are you having difficulties today?")
print ("Physics (1)")
Problem = input(">>> ")
Physics = "1"
Kinetic = "1"
One = ("1")
clear_console()
if Problem == Physics:
    print ("So you are having Difficulties in Physics, What do you want me to calculate?")
    print(" ")
    print ("---KINETIC ENERGY---" + "\n The Kinetic Energy (1) The Velocity (2) The Mass (3)")
    InPhysic = input(">>> ")
clear_console()
if InPhysic == 1:
    print ("Please tell me the Mass of your Object")
    print(" ")
    Mass = input("In Kilograms >>> ")
    print(" ")
    print ("Please tell me the Velocity of your Object")
    print(" ")
    EnergyVelocity = input("in km/h (will be converted automatically) >>> ")
    clear_console()
    print("Your Problem is beeing solved in 2 seconds!")
    time.sleep(1)
    clear_console()
    print("Your Problem is beeing solved in 1 second!")
    time.sleep(1)
    clear_console()
    Meterpersec = float(EnergyVelocity) / 3.6
    time.sleep(0.1)
    print(str(Meterpersec) + " are your m/s")
    time.sleep(2)
    QuadratMetersec = float(Meterpersec) * float(Meterpersec)
    ResultKineticEnergy = 0.5 * float(Mass) * QuadratMetersec
    print(str(ResultKineticEnergy) + " Joule  is your Kinetic Energy!")
    print("A SUMMED UP RESULT OF YOUR CALCULATION IS LOADING!")
    time.sleep(3)
    clear_console()
    print("Here is a data Result of your Calculation!")
    print("")
    print("You were calculating the Kinetic Energy")
    print("")
    print("Your Mass was " + str(Mass) + "kg")
    print("")
    print("Your Velocity was " + str(EnergyVelocity) + " km/h" + "  and converted " + str(Meterpersec) + " m/s" )
    print("")
    print("Your Final Result, the Kinetic Energy, was " + str(ResultKineticEnergy) + " Joule")
    print("")
    print("")
    print("The Formula used was the standard formula for calculating the Kinetic Energy in physics. also known as 0,5 ⋅ mv²")
    print("-------------")
    print("♥ Thank you for using PythonMathSolver made with Love by Emil Toth ♥")


if InPhysic == "2":
    clear_console()
    print("Please Tell me the Mass of your Object (In Kilograms)")
    Mass = input(">>> ")
    print("Please Tell me the Kinetic Energy of your Object (In Joule)")
    KineticEnergy = input(">>> ")
    clear_console()
    print("Your Problem is beeing solved in 2 seconds!")
    time.sleep(1)
    clear_console()
    print("Your Problem is beeing solved in 1 second!")
    time.sleep(1)
    clear_console()
    PreResult = 2 * float(KineticEnergy) / float(Mass)
    Result = math.sqrt(PreResult)
    print(str(Result) + " are your m/s")
    kmh = Result * 3.6
    print(str(kmh) + " are your km/h")
    print("A SUMMED UP RESULT OF YOUR CALCULATION IS LOADING!")
    time.sleep(3)
    clear_console()
    print("Here is a Result of your Calculation!")
    print("")
    print("You were calculating the Velocity with your Kinetic Energy and Mass of your Object")
    print("")
    print("Your Kinetic Energy was " + str(KineticEnergy) + " Joule")
    print("")
    print("Your Mass was " + str(Mass) + " kg")
    print("")
    print("Your Final Result, the Velocity, was " + str(Result) + " m/s  or " + str(kmh) + " km/h")
    print("")
    print("")
    print("The Formula used was the standard formula to calculate the Velocity from the Kinetic Energy and the Mass in Physics also known as 2 ⋅ Ekin : m = Preresult  √Preresult = Endresult")
    print("-------------")
    print("♥ Thank you for using PythonMathSolver made with Love by Emil Toth ♥")


