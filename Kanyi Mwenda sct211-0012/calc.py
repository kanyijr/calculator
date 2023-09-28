
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
    print("Enter operation(reply with a number to choose operation): ")
    print("\n 1.Sum\n 2. Subtraction\n 3. Multiplication \n 4. Division\n")
    op = input()
    if op == "q":
        break
    match op:
        case "1":
            res=num1+num2
            print("\n The result is: ",res)
            
        case "2":
            res=num1-num2
            print("\n The result is: ",res) 
              
        case "3":
            res=num1*num2
            print("\n The result is: ",res)
        
        case "4":
            res=num1/num2
            print("\n The result is: ",res)    
    print("continue?(y/n) : ")
    ans = input()
    if ans == "n":
        break

        