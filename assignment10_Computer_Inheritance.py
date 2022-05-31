class Computer:
    computer_model_name=""
    computer_ram_size=""
    computer_harddisc=""

    def getSpecs(self):
        self.computer_model_name = input("Model name : ")
        self.computer_ram_size = input("Ram size : ")
        self.computer_harddisc = input("Hard disk space : ")

    def displaySpec(self):
        print("\n__Specs__")
        print("Model name :",self.computer_model_name)
        print("Ram size :",self.computer_ram_size)
        print("Hard disc size :",self.computer_harddisc)
class Desktop(Computer):
    desktop_weight=""
    def getDesktopWeight(self):
        self.desktop_weight=input("Desktop Weight : ")
    def displayDesktopWeight(self):
        print("Desktop weight : ",self.desktop_weight)

class Laptop(Computer):
    laptop_weight = ""

    def getLaptopWeight(self):
        self.laptop_weight =input("Laptop Weight : ")

    def displayLaptopWeight(self):
        print("Laptop weight : ", self.laptop_weight)

obj_laptop=Laptop()
obj_desktop=Desktop()

print("\nAdd specs of Desktop")
obj_desktop.getSpecs()
obj_desktop.getDesktopWeight()
print("\n___Dektop___")
obj_desktop.displaySpec()
obj_desktop.displayDesktopWeight()

print("\nAdd specs of Laptop")
obj_laptop.getSpecs()
obj_laptop.getLaptopWeight()
print("\n___Laptop___")
obj_laptop.displaySpec()
obj_laptop.displayLaptopWeight()



# Output: 
# Add specs of Desktop
# Model name : Dell desktop1
# Ram size : 4gb
# Hard disk space : 256gb
# Desktop Weight : 2kg
#
# __Dektop__
#
# _Specs_
# Model name : Dell desktop1
# Ram size : 4gb
# Hard disc size : 256gb
# Desktop weight :  2kg
#
# Add specs of Laptop
# Model name : Dell laptop1
# Ram size : 8gb
# Hard disk space : 500gb
# Laptop Weight : 500gm
#
# __Laptop__
#
# _Specs_
# Model name : Dell laptop1
# Ram size : 8gb
# Hard disc size : 500gb
# Laptop weight :  500gm