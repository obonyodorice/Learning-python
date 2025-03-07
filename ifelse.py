 
# a = int(input('Enter a number:'))

# def num(a): 
#     if a%2 == 0:
#         print('The number is even')
#     else:
#         print('The number is odd')

# num(a)
    
# weight= input('Enter your weight:')
# unit=input('The unit is (K) or (P) for pounds:')
# if unit.upper()== "K":
#     convert= weight/0.45
#     print('UNit in lbs'+str(convert))
# else:
#     convert=weight*0.45
#     print('UNit is kgs'+str(convert))


# income=input('Enter income:')
# good_credit=input('Enter credit:')
class applicant:

    def __init__(self,income,good_credit):
        self.income=income
        self.good_credit=good_credit

    def remarks(self):
        return f' Has good Income of{self.income} and Credit  of {self.good_credit}.He is eliguble for loan'
    
Dorice= applicant('income','good_credit')
Dorice.income=input ('Income is:')  
Dorice.good_credit=input('Enter your Credit:') 


print(f'Income is: {Dorice.income}')
print(f'Credit is: {Dorice.good_credit}')

print(Dorice.remarks())

