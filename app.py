from my_classes import Car
from crud import save, load, update, search_car_from_data, edit_car,delete

def create_car():
    global errors
    errors = []
    model  = input("car model: ")
    year = input("car year: ")
    color = input("car color: ")
    numberplate= input("car numberplate: ")
    holder_name= input("car holder name: ")
    last_garage_visit= input("car last garage visit: ")
    last_treatment= input("car last treatment: ")

    car = Car(model=model,year=year,color = color,numberplate=numberplate,holder_name=holder_name,last_garage_visit=last_garage_visit,last_treatment=last_treatment)
    errors = []
    for key in car.get_dict().keys():
        value = getattr(car,key)
        if value == "" or value.isspace() == True:
            errors.append(key)
    if len(errors) == 0:
        update(car)
    else:
        print("")
        print(f"Car {', '.join(errors)} is empty!")
        print("")
        input("Press Any Key To Continue")
        

def edit_info():
    global errors
    avaiabllevariable = ["model","year","color","numberplate","holder_name","last_garage_visit","last_treatment"]
    errors = []
    car_numberplate = input("Car number plate: ")
    variable = input("Which Section To Change: ")
    new_value = input("New Value: ")
    values = [car_numberplate,variable,new_value]
    for value in values:
        if value == "" or value.isspace() == True:
            errors.append(value)

    if len(errors) > 0:
        print("")
        print(f"One or more values are empty!")
        print("")
        input("Press Any Key To Continue")
    
    elif variable not in avaiabllevariable:
        print("")
        print(f'{variable} is not an car info value!')
        print("")
        input("Press Any Key To Continue")

    else:
        edit_car(car_numberplate, variable, new_value)

while True:
    choice = input("""Grage Database:
1. create car
2. search car
3. update car last visit
4. update car last treatment
5. delete car
6. exit""").title()
    print("")
    if choice == "1":
        create_car()
    elif choice == "2":
        data = load()
        print(search_car_from_data(numberplate = input("car numberplate: "),datafile = data).get_dict())
    elif choice == "3":
        edit_car(numberplate=input("car number plate: "),variable="last_garage_visit",new_value=input("last visit: "))
    elif choice == "4":
        edit_car(numberplate=input("car number plate: "),variable="last_treatment",new_value=input("last visit: "))
    elif  choice == "5":
        delete(input("Car number plate: "))
    elif choice == "6":
        exit()
