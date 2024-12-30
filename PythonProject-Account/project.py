def menu():
    print('1.Balansa bax')
    print('2.Mexaric')
    print('3.Medaxil')
    print('4.Sifreni yenile')
    print('5.Emeliyyatlara bax')
    
person={
    "name":"Nihat Ahmedov",
    "password":"0709",
    "balance":1200,
}

def login(person):
    while True:
        password=input("Enter your password:")
        if password == person["password"]:
            print("Daxil oldunuz")
            break
        else:
            print("Wrong name or password")
            
dict_balans={'medaxil':[],
             'mexaric':[]}

def view_balance(person):
    return("Your balance is: ",person["balance"])


def remove_balance(person):
    while True:
        mexaric=int(input('Mexaric etmek istediyiniz reqemi daxil edin: '))
        if mexaric <= 1200:
            person['balance']=int(person['balance'])-mexaric
            dict_balans['mexaric'].append(mexaric)
            print(dict_balans)
            return 'new_balance: ',person['balance']
        else:
            print('Duzgun mebleg daxil edin')


def add_balance(person):
    medaxil=int(input('Medaxil etmek istediyiniz reqemi daxil edin: '))
    # for i in dict_balans:
    dict_balans['medaxil'].append(medaxil)
    print(dict_balans)
    person['balance']=int(person['balance'])+medaxil
    return 'new_balance: ',person['balance']


def update_password(person):
    print('Sifrenizi yenileyin')
    new_parol=input('yeni parol daxil edin: ')
    person['password']=new_parol
    return 'new password= ',person['password']


def view_action(dict_balans):
    print('1.Emeliyyatlara bax: ')
    for x, y in dict_balans.items():
        if x == 'medaxil':
            print('Medaxil: ',f'{[y]} AZN medaxil oldu')
        elif x == 'mexaric':
            print('Mexaric: ',f'{y} AZN mexaric oldu')
login(person)

while True:
        menu()
        choice = int(input("Secim edin: "))
        if choice == 'exit':
                print('Exiting')
                break
        elif choice == 1:                
                print(view_balance(person))
        elif choice == 2:
                print(remove_balance(person))
        elif choice == 3:
                print(add_balance(person))
        elif choice == 4:
            print('Logout')
            print(update_password(person))
            login(person)
        elif choice == 5:
            print(view_action(dict_balans))
        else:
            print('Invalid choice')