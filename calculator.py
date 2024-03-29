# Finance Calculator

import math

border = "-" * 100  
print(border)
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("   Bond    - to calculate the amount you'll have to pay on a home loan")
print(border)

user_entry = input("Enter either 'i' for Investment or 'b' for Bond from the menu above to proceed : ").lower()

#Error message if user hasn't entered 'investment' or 'bond'
if user_entry != "i" and user_entry != "b" :
    print("You have not entered a valid input. Please try again.") 

#Calculating the total amount of money if the user inputs investment 
if user_entry == "i" :
    deposit  = float(input("Please enter the amount of money you are depositing (in £) : "))
    rate     = float(input("Please enter the interest rate (in %) : "))
    time     = float(input("Please enter the number of years you plan on investing for : "))
    interest = input("Please enter 's' if you would like simple interest or 'c' for compound interest? : ").lower() 

    # Calculation of the total amount of money depending on the user's interest input
    if interest == "s" :
        total_amount = float(deposit * (1 + (rate / 100) * time))
        print(f"Your total simple amount after {rate} years is : £ {total_amount}")

    elif interest == "c" :
        total_amount = float(deposit * math.pow((1 + (rate / 100)), time))
        print(f"Your total compounded amount after {rate} years is : £ {total_amount}")

    else :
        print("You have not entered a valid input, please try again.")

    

#Calulating the total amount of money if the user inputs bond 
if user_entry == "b" :
    present_value = float(input("Please enter the present value of your house : "))
    rate          = float(input("Please enter the interest rate (in %) : "))
    time          = float(input("Please enter the number of months you plan to take to repay the bond : "))
    
    i_rate = (rate / 100) / 12  #Calculating the monthly interest rate
    repayment = float((i_rate * present_value) / (1 - ((1 + i_rate) ** (-1 * time))))

    print(f"Your total monthly repayment will be £{repayment}")
