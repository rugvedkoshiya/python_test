# ** is kwargs (kwyword arguments)
# kwargs is take input in dictionary
def func(**kwargs):
    for i,j in kwargs.items():
        print(f"{i} : {j}")

d = {'Name' : 'Rugved', 'Last Name' : 'Koshiya', 'Age' : 18}
func(**d)
# Output :
# Name : Rugved
# Last Name : Koshiya
# Age : 18

func(first_name = 'Rugved', last_name = 'Koshiya')
# Output :
# first_name : Rugved
# last_name : Koshiya