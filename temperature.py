def convert(number, choice):
    if choice == "f":
        result = number - 32 * (5/9)
    elif choice == "c":
        result = number * (9/5) + 32
        print(result)

temperature = input("Do you want to convert:\n\na) Farenheit to Celsius\nb) Celsius to Farenheit\n\nInput here: ")
number = float(input("\nWhat is the temperature you would like to convert?\n\nInput Here: "))

f_to_c = ["farenheit to celsius", "a", "a)"]
c_to_f = ["celsius to farenheit", "b", "b)"]

if temperature in f_to_c:
    convert(number, "f")
elif temperature in c_to_f:
    convert(number, "c")