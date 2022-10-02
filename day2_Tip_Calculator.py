'''
Day2
Tip Calculator 

Mm0)

10/2/2022
'''
print(f'Welcome to the Tip Calculator ')

#input
costInput = float(input(" How much was the bill? "))
preTip = int(input(" What precentage of tip would you like to give? 10, 12, or 15?"))
pplInput = int(input("how many people to split the bill? "))

#process
tip = costInput * (preTip/100)
print(tip)
cost =  (costInput + tip) / pplInput 
print(cost)
cost = round(cost,2)
#output
print(f' Each person should pay: {round(cost, 2)}')