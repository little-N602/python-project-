# Luis Nigoa
# PA 6
#the promt that user would need to enter the cost of groceries and give them the coupon percentage 
amount = int(input("ente the cost of groceries: $"))
coupon_percentage = 0.0
# if else statent that would determind the dicount depending on how much it is as well as protocal if there is no amount.
if amount <= 0:
    print("You entered an invalid cost of groceries")
else:
    coupon_percentage = 0.0
    
    if amount < 10:
        coupon_percentage = 0.0
    elif 10 <= amount <= 60:
        coupon_percentage = 0.08
    elif 60 <= amount <= 150:
        coupon_percentage = 0.10
    elif 150 <= amount <= 210:
        coupon_percentage = 0.12    
    elif amount > 210:
        coupon_percentage = 0.14
coup_amount= amount*coupon_percentage
#these command display after the input the coupon dicount they get and how much they win in the discount 
print(f"Your coupon percentage is:{coupon_percentage*100:.0f}%")
print(f"You win a discount coupon of:{coup_amount:.2f}")