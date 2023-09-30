import pickle
from my_classes import Car

#save function
def save(data,file:str="db.pickle"):
    with open(file,"wb") as f:
        pickle.dump(data,f)

#load function
def load(file:str="db.pickle"):
    with open(file,"rb") as f:
        data = pickle.load(f)
        return data

#update function with first file create
def update(car,file:str="contacts.pickle"):
    try:
        datafile = load()
        datafile.append(car)
        save(data=datafile)
        print("")
        print("Car Saved!")
        print("")
        input("Press Any Key To Continue")
    except:
        savedata = [car]
        save(data=savedata)
        print("")
        print("Car Saved")
        print("")
        input("Press Any Key To Continue")
    

# delete/edit function requierment
def search_car_from_data(numberplate,datafile):
    for car in datafile:
        if car.numberplate == numberplate:
            return car
        
def edit_car(numberplate,variable,new_value):
    try:
        datafile=load()
        searched_car_edit = search_car_from_data(numberplate,datafile)
        setattr(searched_car_edit,variable,new_value)
        save(data=datafile)
        print("")
        print("Car Saved!")
        print("")
        input("Press Any Key To Continue")

    except:
        print("")
        print("Car Not Found!")
        print("")
        input("Press Any Key To Continue")
    
#delete function
def delete(numberplate:str):
    try:
        datafile=load()
        searched_car = search_car_from_data(numberplate,datafile)
        datafile.remove(searched_car)
        save(data=datafile)
        print("")
        print("Car Removed!")
        print("")
        input("Press Any Key To Continue")
    except:
        print("")
        print("Car Not Found!")
        print("")
        input("Press Any Key To Continue")
