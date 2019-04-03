def weight_on_planets():
    # write your code here
    Earth = int(input("What do you weigh on earth? "))
    Mars = Earth * 0.38
    Jupiter = Earth * 2.34
    statement = "On Jupiter you would weigh"
    print("\nOn Mars you would weigh", Mars, "pounds.\n"+statement, Jupiter, "pounds.\n")

   
   
if __name__ == '__main__':
   weight_on_planets()
