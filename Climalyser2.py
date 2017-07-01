from time import sleep
from datetime import datetime
import webbrowser

def climalyser():
    total = 0
    print("REMEMBER: Use your Latest Home Utility Stats")

    eletric=(int(input("What is your Daily Average Electricity Usage? (In kWh) ")))
    
    if eletric >= 3:
        total = total+5

    elif eletric <= 2:
        total = total+3
        
    #Average: 2
    sleep(1)
    
    heat=input("What type of Fuel do you use to heat your home: Coal, Wood, Oil, Briquettes, Natural Gas, Electricity?")

    if heat == "Coal" or heat == "Oil" or heat == "Briquettes":
        total = total+5

    elif heat == "Wood" or heat == "Natural Gas" or heat == "Electricity": 
        total = total+2

    
    #Electricity or Natural Gas or Wood
    sleep(1)
    water=(int(input("What is your Daily Average Water Usage? (In Litres)")))

    if water >= 381:
        total = total+5

    elif water <= 380:
        total = total+3

    
    #Average: 380
    sleep(1)
    ecology=input("In your local area is there any ongoing Raw Sewage or Pollution output in to the local biodiversity?")

    if ecology == "Yes" or ecology == "yes":
        total = total+5

    elif ecology == "No" or ecology == "no":
        total = total+2


    sleep(1)
    transport=(int(input("How much time would you spend commuting everyday? (in Minutes,  ) ")))

    if transport >= 31:
        total = total+3

    elif transport <= 30:
        total = total+2

    
    #Average: 25
    sleep(1)
    total = total/25
    result = total*100
    result = str(result)
  
    if result >= "70":
        print("POOR Quality")

    elif result <= "59":
        print("GOOD Quality")

    else:
        print("ERROR")

    save=["Climate Change in your Life:"]
    save.append(result)
    print (save)

    target1 = open('yourlocalclimate.txt', 'w')

    target1.write(result)

    target1.close()

    print(result)
    sleep(20)
    

print("Welcome to 'Climalyser' the Local Climate Change Prediction Software")
sleep(2)
print("This software has been developed by Daniel O'Brien from Meteodeep")
sleep(2)
print("'Climalyser' is simply 'smart' survey software!! To operate you simply enter a figure from your Utility Bill reading that recognises your own use of energy compared to the national average and how it can effect the environment around you...")
sleep(2)
print("We will be regularly updating the software with bug fixes and updates/improvements")
sleep(2)
print("NOTE: A knowledge of your local area and household utility usage is required to use this software!!")
sleep(2)
print("Be sure to contact us for feedback!")

menu=input("Where would you like to go from here, 'Climalyser' or 'Website'")

if menu == "Climalyser":
    climalyser()
    
elif menu == "Website":
    webbrowser.open_new_tab("tinyurl.com/meteodeep")

else:
    print("ERROR")


print("Thank You for using this Software, find the text file 'yourlocalclimate.txt' on your computer and this contains your RESULT out of 100 percent!!")
sleep(1)
print("Please Remember to fill in our 'World Climate' Survey on our website from the number (percentage) on the text file created (your result)")
sleep(2)
print("SHUTTING DOWN NOW!!")
