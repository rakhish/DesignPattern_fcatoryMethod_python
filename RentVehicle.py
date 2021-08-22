class rentBicycle:
    def __init__(self, vehicleName):
        self.vehicleName = vehicleName
    def rentPrice(self):
        if self.vehicleName == "Hero":
            print("Charges : 5$/hour ")
        elif self.vehicleName == "Moto":
            print(" Charges : 10$/hour")
        else:
            raise ValueError(vehicleName)


class rentCar:
    def __init__(self, vehicleName):
        self.vehicleName = vehicleName

    def rentPrice(self):
        if self.vehicleName == "Mercedes":
            print("Charges : 50$/hour ")
        elif self.vehicleName == "BMW":
            print(" Charges : 60$/hour")
        else:
            raise ValueError(vehicleName)

class rentBike:
       def __init__(self, vehicleName):
        self.vehicleName = vehicleName

        def rentPrice(self):
            if self.vehicleName == "Splendor":
                print("Charges : 15$/hour ")
            elif self.vehicleName == "Passion+":
                print(" Charges : 20$/hour")
            else:
                raise ValueError(vehicleName)

def get_vehicleName(vehicle = "Cycle"):
    vehicles = dict(bicycle = rentBicycle("Hero"), car = rentCar("BMW"), bike = rentBike("Splendor"))
    return vehicles[vehicle]

rentedVehicle = get_vehicleName("car")
print(rentedVehicle.rentPrice()) 