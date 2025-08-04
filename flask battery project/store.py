from datetime import datetime
import random

def generatecolloqialnumber(userinput, userinput2):
    userinput = int(userinput)
    userinput2 = int(userinput2)
    result = userinput + userinput2
    resultsarr = ["total is"]
    resultsarr.append(result)
    return resultsarr

def datefunction():
    date = datetime.now()
    return date

def subtractnumber(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    total = number1 - number2
    realtotal = {"total Subtraction": total}
    return realtotal

def batteries(battery_id, battery_type):
    battery_temperature = random.randint(0, 95)
    total = {
        "battery_id": battery_id,
        "battery_temperature": battery_temperature,
        "battery_type": "temp"
    }

    for key, value in total.items():
        if key == "battery_id" and str(value) == str(battery_id):
            return total
        else:
            return {}
