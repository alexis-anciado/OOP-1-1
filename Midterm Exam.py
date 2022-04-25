#Problem1

def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9/55) + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5/9

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    tempInCelsius = float(input("Enter the temperature in Celsius:"))
    convert1 = CelsiusToKelvin(tempInCelsius)
    print(str(convert1.conversion()) + " Kelvin")
    convert2 = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert2.conversion()) + " Fahrenheit")

    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit:"))
    convert3 = FahrenheitToCelsius(tempInFahrenheit)
    print(str(convert3.conversion()) + " Celsius")

    tempInKelvin = float(input("Enter the temperature in Kelvin:"))
    convert4 = KelvinToCelsius(tempInKelvin)
    print(str(convert4.conversion()) + " Celsius")

main()





#Problem2

from tkinter import *
window = Tk()
window.geometry("600x300")
window.title("Midterm in OOP")

lbl = Label(window, text="Enter your fullname:", fg="red")
lbl.place(x=50, y=90)

name_entry = StringVar()
def displayname():
    name = name_entry.get()
    textfield2.insert(END, name)

textfield = Entry(window, bd=3, font=("Arial", 16), textvariable=name_entry)
textfield.place(x=350, y=90)
btn = Button(window, text="Click to display your Fullname", fg="red", command=displayname)
btn.place(x=50, y=130)
textfield2 = Entry(window, bd=3, font=("Arial", 16))
textfield2.place(x=350, y=130)

window.mainloop()