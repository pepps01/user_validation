from random import *

try:
    no_of_users = int(input("Choose how many users 1 or 2? "))

    if no_of_users <1 and no_of_users>2:
        print(" Please enter 1 or 2")
        no_of_users = int(input("Choose how many users 1 or 2? "))
    
    ALPHABETS = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9"
    user_data ={}    

    counter = 0 
    def validate_entry(entry):
        if entry < 2:
            return False
        return entry


    while counter <= 1:
        firstname = input("Enter your firstname: ")
        lastname = input("Enter your Lastname: ")
        email = input("Enter your email: ")
        password_random_generator = ""
        
        password_counter = 0
        number_of_password_strings = 5

        while password_counter < number_of_password_strings:
            password_random_generator += choice(ALPHABETS.split(","))
            password_counter = password_counter + 1 

        user_data['password'] = firstname[0:2] + lastname[0:2] + str(password_random_generator)
        user_data['firstname'] = validate_entry(firstname)
        user_data['lastname'] = validate_entry(lastname)
        user_data['email'] = validate_entry(email)

        password_change = input(" This is your password '{}': Do you want to change your password? Y/N".format(user_data['password']))

        if len(password_change) != 9:
            print("Please enter correct credentials")
            break

        if password_change.upper() == "N":
            for x in user_data:
                print("{} : {}".format(x, user_data[x]))
          
        else:            
            password = input("Enter to change your password: (password must be equal to or greater than 7 Characters) ")

            if len(password) < 7:
                password = input("Please password must be equal to or greater than 7 Characters) ")

                if len(password) >= 7:
                    for x in user_data:
                        print("{} : {}".format(x, user_data[x]))
                    if counter == 1:
                        break
            else:
                for x in user_data:
                    print("{} : {}".format(x, user_data[x]))
                if counter == 1:
                    break

        if counter == 1:
            break        
    counter = counter +1
            
except ValueError:
    print("Did not expect this value ")