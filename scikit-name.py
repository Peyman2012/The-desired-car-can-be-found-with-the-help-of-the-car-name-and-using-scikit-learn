import  pandas as pd
from sklearn import tree
import time

df=pd.read_csv('C:\\Users\\peyman\\pythonProject16\\Write_price_car_from_database_for.csv')

n_input='Honda Accord'
y_input=2018
m_input=50
a_input=0
o_input=3
max_price=100
min_price=8

# y_input=int(input("Enter a Year:"))
# m_input=float(input("Enter a Miles:"))
# a_input=int(input("Enter a Accident:"))
# o_input=int(input("Enter a Owners:"))
# max_price=float(input("Your maximum payment: "))
# min_price=float(input("Your minimum payment: "))

def_name=df[df['Name Car']==n_input]

Miles_Car=def_name['Miles Car']
Year_Car=def_name['Year Car']
Accident_Car=def_name['Accident Car']
Owner_Car=def_name['Owner Car']
Price_Car=def_name['Price Car']
Name_car=def_name['Name Car']
Color_Exterior=def_name['Color Exterior']
Color_Interior=def_name['Color Interior']
Person_Car=def_name['Person Car']
Model_Car = def_name['Model Car']
print("Please waite....")
print()
time.sleep(5)
a=Miles_Car.index.get_level_values(0)
# print(a)

x=[]
y=[]

for i in a:
    x.append([Miles_Car[i],Year_Car[i],Accident_Car[i],Owner_Car[i]])
    y.append([Price_Car[i]])

time.sleep(5)
print(f'''So....
The specifications of the car you want are:
Car year: {y_input}
Car operation: {m_input} Miles
Number of accidents: {a_input}
Number of owners: {o_input} person
Min Price {min_price} and Max Price: {max_price}''')
def_name=df[df['Name Car']==n_input]
print("Please waite....")
print()
time.sleep(5)

clf = tree.DecisionTreeRegressor()
clf = clf.fit(x,y)
new_data=[[m_input, y_input, a_input, o_input]]
answer = clf.predict(new_data)

list_answer = []
for item in answer:
    list_answer.append(item)

print("Result : ")
if list_answer[0]>=min_price and list_answer[0]<=max_price:
    df_price = def_name[def_name['Price Car'] ==list_answer[0]]
    search_price=def_name['Name Car'].tolist()
    search_color_ex=def_name['Color Exterior'].tolist()
    search_color_in = def_name['Color Interior'].tolist()
    search_model=def_name['Model Car'].tolist()
    search_person=def_name['Person Car'].tolist()
    print(f'''Name Car: {search_price[0]}   and
Model Car : {search_model[0]}   and
Color Exterior : {search_color_ex[0]}   and        ==> Price Car : {list_answer[0]}$
Color Interior :{search_color_in[0]} and
Person Car : {search_person[0]}
 ''')
else:
        print(f'''We are sorry!!!!
The car is not available at the price you want
The car with the specifications you asked for is available at the price: {list_answer[0]}$''')