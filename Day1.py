'''
band Name Generator

Oct 1 || 2022

Program Description: the purpose of this progam is to create band names from varible provided by the users input 

the band name will start with the name of the city where the person is from, then will end with the name of there pet

things that will be used: Varibles, Input, Commenting. 
'''
#Input
print('Welcome to the Band Name Generator')#welcoming the user to the program and giving a introduction to what to expect 

cityName = input("What's the name of the city you grew up in?")#prompting the user for input. 

petName = input("What is your pets name: ")#prompting the user for there pets name 

#Process 
bandName = cityName + " " + petName #creating a varible joining the two input together 

#Output
print(" The Band Name could be \"" + bandName + "\"")#output time 

