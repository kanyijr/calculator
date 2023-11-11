class Calculator:
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2

    def add(self):
        try:
            res = self.x + self.y
        except TypeError as e:
            print("Error: ", e)    
        return res

    def subtract(self):
        try:
            res =  self.x - self.y 
        except TypeError as e:
            print("Error: ", e)    
        return res

    def multiply(self):
        try:
            res  = self.x * self.y
        except TypeError as e:
            print("Error: " , e)    
        return res

    def divide(self):
        try:
            res = self.x / self.y
        except ZeroDivisionError as e:
            print("Error: " ,e)   
        except TypeError as e:
            print("Error: ", e)     
        return res

    def power(self):
        return self.x ** self.y



print("Welcome User to Kanyi's Calculator!\n")
print("press q then enter to quit")
while True:
    print("Enter First Number: ")
    num1 = input()
    if num1 =="q":
        break
   
    
    num1 = float(num1)

    print("Enter second number: ")
    num2= input()
    if num2 == "q":
        break
    num2 = float(num2)
    calc = Calculator(num1, num2)
    print("Enter operation(reply with a number to choose operation): ")
    print("\n 1.Sum\n 2. Subtraction\n 3. Multiplication \n 4. Division\n 5. Power\n")
    op = input()
    if op == "q":
        break
    match op:
        case "1":
            res=calc.add()
            print("\n The result is: ",res)
            
        case "2":
            res=calc.subtract()
            print("\n The result is: ",res) 
              
        case "3":
            res=calc.multiply()
            print("\n The result is: ",res)
        
        case "4":
            res=calc.divide()
            print("\n The result is: ",res)  
        case "5":
            res=calc.power()
            print("\n The result is: ",res)        
    print("continue?(y/n) : ")
    ans = input()
    if ans == "n":
        break
        