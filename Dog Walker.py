import sys
import random

#shopping items was chosen as the list name as the items the user buys from
#shops will be appended to this list. Other options for the name could have
#been groceries or shopping cart but i felt like shopping_items defined it best
shopping_items=[]

#the function name clear_screen was chosen as it clearly defines what it is
#doing.the clear function will completely clear the screen, allowing a fresh
#start
def clear_screen():
    sys.stdout.write("\n" *80)

#this function will be called on everytime the program is required to go to the
#next screen. It will inform the user to click enter to continue, and then when an
#input is detected it will action the continue. This function was called skip as it
#enables the user to skip to the next page.
def skip ():
        sys.stdout.write("\nClick enter to continue")
        sys.stdin.readline().strip().upper()


#This function allows the program to add ascii art to each page.
#Reference: https://ascii.co.uk/art/dog
def dog_art1():
    sys.stdout.write(" "*15 +"                            ;\ \n")
    sys.stdout.write(" "*15 +"                            |' \ \n")
    sys.stdout.write(" "*15 +"         _                  ; : ; \n")
    sys.stdout.write(" "*15 +"        / `-.              /: : | \n")
    sys.stdout.write(" "*15 +"       |  ,-.`-.          ,': : | \n")
    sys.stdout.write(" "*15 +"       \  :  `. `.       ,'-. : | \n")
    sys.stdout.write(" "*15 +"        \ ;    ;  `-.__,'    `-.| \n")
    sys.stdout.write(" "*15 +"         \ ;   ;  :::  ,::'`:.  `. \n")
    sys.stdout.write(" "*15 +"          \ `-. :  `    :.    `.  \ \n")
    sys.stdout.write(" "*15 +"           \   \    ,   ;   ,:    (\ \n")
    sys.stdout.write(" "*15 +"            \   :., :.    ,'o)): ` `-. \n")
    sys.stdout.write(" "*15 +"           ,/,' ;' ,::\"`.`---\'   `.  `-._ \n")
    sys.stdout.write(" "*15 +"         ,/  :  ; '\"      `;'          ,--`. \n")
    sys.stdout.write(" "*15 +"        ;/   :; ;             ,:'     (   ,:)\n")
    sys.stdout.write(" "*14 +"         ,.,:.    ; ,:.,  ,-._ `.     \"\"'/ \n")
    sys.stdout.write(" "*15 +"          '::'     `:'`  ,'(  \`._____.-'\"' \n")
    sys.stdout.write(" "*15 +"             ;,   ;  `.  `. `._`-.  \\ \n")
    sys.stdout.write(" "*15 +"            ;:.  ;:       `-._`-.\  \`. \n")
    sys.stdout.write(" "*15 +"              '`:. :        |' `. `\  ) \ \n")
    sys.stdout.write(" "*15 +"                 ` ;:       |    `--\__,' \n")
    sys.stdout.write(" "*15 +"                   '`      ,' \n")
    sys.stdout.write(" "*15 +"                        ,-' \n")
    sys.stdout.write("\n"*10)

#This function allows the program to add ascii art to each page.
#Reference: https://ascii.co.uk/art/dog
def dog_art2():
    
    sys.stdout.write(" "*13 +"                              ,.  , \n")
    sys.stdout.write(" "*13 +"                          .-. \ \| \ \n")
    sys.stdout.write(" "*13 +"              ,---._    _,-.> `.\ \ ( \n")
    sys.stdout.write(" "*13 +"             (__,'  `   `>-         -\ \n")
    sys.stdout.write(" "*13 +"                      ,-'             `-. \n")
    sys.stdout.write(" "*13 +"          ,-'       ,  ,    .       .    `. \n")
    sys.stdout.write(" "*13 +"        ,'\       ,' ,-'    `-.      ;    :`. \n")
    sys.stdout.write(" "*13 +"       (__;     ,',,'      ,   `     : `. :  \ \n")
    sys.stdout.write(" "*13 +"              ,' |  _,'   /_    `    :  ; :   \ \n")
    sys.stdout.write(" "*13 +"             /  ,',' |   /  \        '     ;   \ \n")
    sys.stdout.write(" "*13 +"            /   | |(o|  /  (o)          |  |    ; \n")
    sys.stdout.write(" "*13 +"           /     ___-^-^-----.          |  |    | \n")
    sys.stdout.write(" "*13 +"          (   ,---. `-.           :.    |       : \n")
    sys.stdout.write(" "*13 +"           ;,'      )  `          :..   |        | \n")
    sys.stdout.write(" "*13 +"           :\      /              :.    |        ; \n")
    sys.stdout.write(" "*13 +"           :.`-.__,              ,:`    |        | \n")
    sys.stdout.write(" "*13 +"           ;`.    .             ':'      \      , \n")
    sys.stdout.write(" "*13 +"          /   `-.__\           '      ,   \     \. \n")
    sys.stdout.write(" "*13 +"         (   ,'    \`--,-----.       /     \     \`. \n")
    sys.stdout.write(" "*13 +"          `-'       \,' ,'   /    / |       \     |  \n")
    sys.stdout.write(" "*13 +"                    /  '   ,'    /-.|        `.   ;\n")
    sys.stdout.write(" "*13 +"                   (      /`----'   |          `--' \n") 
    sys.stdout.write(" "*13 +"                    `.__,' \n")
    sys.stdout.write("\n"*8)                     

#running the the variable i chose to use to control the while loop for the
#phase of the program. This variable will be changed to False once the user
#decides to go home, ending the loop.
running = True

#total_money is the variable storing the value of money saved up during the time the
#program runs. This will update throughout the program as the user makes more money.
total_money = int(0)

#This function stores the main program. This function calls on all other functions
#houses most of the code for the program to run.
def main():
    clear_screen()
    sys.stdout.write(" "*15 +"         ______\n")                 
    sys.stdout.write(" "*15 +"         |  _  \ \n")                
    sys.stdout.write(" "*15 +"         | | | |___   __ _\n")      
    sys.stdout.write(" "*15 +"         | | | / _ \ / _` |\n")     
    sys.stdout.write(" "*15 +"         | |/ / (_) | (_| |\n")     
    sys.stdout.write(" "*15 +"         |___/ \___/ \__, |\n")     
    sys.stdout.write(" "*15 +"                      __/ |\n")     
    sys.stdout.write(" "*15 +"                     |___/ \n")     
    sys.stdout.write(" "*15 +"     _    _       _ _\n")             
    sys.stdout.write(" "*15 +"    | |  | |     | | |\n")            
    sys.stdout.write(" "*15 +"    | |  | | __ _| | | _____ _ __\n") 
    sys.stdout.write(" "*15 +"    | |/\| |/ _` | | |/ / _ \ '__|\n")
    sys.stdout.write(" "*15 +"    \  /\  / (_| | |   <  __/ |\n")   
    sys.stdout.write(" "*15 +"    \/  \/ \__,_|_|_|\_\___|_|\n")
    sys.stdout.write("\n"*5)
    sys.stdout.write(" "*15 +"                      __\n")  
    sys.stdout.write(" "*15 +"          (\,--------'()'--o\n")  
    sys.stdout.write(" "*15 +"           (_    ___    /~\" \n")  
    sys.stdout.write(" "*15 +"            (_)_)  (_)_)\n")
    sys.stdout.write("\n"*10)
    sys.stdout.write("Welcome to Dog Walker! What is your characters name? ")

    #the variable user_name was chosen as it describes the characters name.
    #this could have been name or character but chose user-name as it was
    #well defined.
    user_name = sys.stdin.readline().strip()
    clear_screen()
    dog_art1()
    sys.stdout.write("Hi "+ user_name +", how many dogs will you walk today? ")

    #dog_amount has been chosen as this variable as it shows how many dogs the
    #user is going to be walking. 
    dog_amount = sys.stdin.readline().strip()
    clear_screen()
    dog_art2()
    sys.stdout.write("How much will you charge each customer per dog? ")
    #cost_per_dog clearly defines this variable, it is how much the user is
    #going to charge per dog.
    cost_per_dog = sys.stdin.readline().strip()

    #the total_payout variable holds the value of dog_amount * cost_per_dog,
    #showing the user how muich money they will make if they are successful.
    total_payout = (float(dog_amount)*float(cost_per_dog))
    
    clear_screen()
    dog_art1()
    sys.stdout.write("Great! If you are successful you will make $"+str(
        total_payout)+"\n")

    #running the the variable i chose to use to control the while loop for the
    #phase of the program. This variable will be changed to False once the user
    #decides to go home, ending the loop.
    running = True

    #this while loop will enable to program to continue giving the user the option
    #to keep choosing multiple options for walks until they decide to go home,
    #in which caser the program will terminate the while loop once
    #"running" = False
    while running == True:
        skip()
        clear_screen()
        dog_art2()

        sys.stdout.write("What a beautiful day! Where would you like to go?\n")
        sys.stdout.write("1: Park\n")
        sys.stdout.write("2: Beach\n")                 
        sys.stdout.write("3: Shops\n")
        sys.stdout.write("4: Home\n")
        #location_choice was chosen as the user will be choosing a location to
        #walk the dogs to. Other options could have been choice but decided to add
        #location as it gives more context to the variable
        location_choice = sys.stdin.readline().strip()

        #If the number 1 is inputed, this if statment will activate and run the part
        #of the program that takes the user to the park.
        if location_choice == ("1"):
            clear_screen()
            dog_art1()
            sys.stdout.write("Off to the park we go!\n")
            skip()
            clear_screen()
            dog_art2()
            sys.stdout.write("One of the dogs got off the lead!\n")
            skip()
            clear_screen()
            dog_art1()

            #random_number stores the value of a randomly generated number which the
            #user will need to try and guess before continuing.
            random_number = random.randint(1,5)
            #user_guess stores the input that the user choses. this input will be
            #compared with the rnadom generated number and if they match the user
            #will be able to continue
            user_guess = 0

            #This while loop enables the user to continue guessing a number until
            #they guess it right. Once they guess it right, they will be able
            #to go on with the rest of the program.
            while user_guess != random_number:
                sys.stdout.write("Guess a number between 1 and 5 to catch the dog\n")
                user_guess = int(sys.stdin.readline().strip())

                #This if statement will progress if the user_guess and random_number
                #match.
                if user_guess != random_number:
                    sys.stdout.write("The dog escaped again, try again!\n")
                
                #If the user guesses the correct answer, this else stament allows
                #the user to proceed with the program
                else:
                    sys.stdout.write("Great Guess, you caught it!\n")
                    

        #If the number 2 is inputed, this elif statment will activate and run the
        #part of the program that takes the user to the beach.
        elif location_choice == ("2"):
            clear_screen()
            dog_art2()
            sys.stdout.write("Off to the beach we go!\n")
            skip()
            clear_screen()
            dog_art1()

            #random_money_found is the variable i chose to hold the value of the
            #randomly generated number up to 10 in which the user finds in the game
            #The value in random_money will be added to the total_payout and total_mo
            #ney values to keep track of money throughout the game.
            random_money_found = random.randint(1,10)
            total_money = (random_money_found)+(total_payout)
            sys.stdout.write("While at the beach you find some money in the sand\n")
            skip()
            clear_screen()
            dog_art2()
            sys.stdout.write("Click enter to dig it up!\n")
            sys.stdin.readline()
            clear_screen()
            dog_art1()
            sys.stdout.write("Nice one, you find $"+str(random_money_found)+"\n")
            skip()
            clear_screen()
            dog_art2()
            sys.stdout.write("You add this to your total money\n")
            skip()
            clear_screen()
            dog_art1()
            sys.stdout.write("You now have a total of $"+str(total_money)+"!\n")
            skip()
            clear_screen()
            dog_art2()

        #If the number 3 is inputed, this elif statment will activate and run the
        #part of the program that takes the user to the shops, enablign them
        #to make a purchase.
        elif location_choice == ("3"):
            clear_screen()
            dog_art1()
            sys.stdout.write("Off to the shops we go!\n")
            skip()
            clear_screen()
            dog_art1()
            sys.stdout.write("What would you like to purchase? ")

            #Purchased_items is the varibale i created to hold the inout value from
            #the user. This value will be appended to the shopping_items list.
            purchased_items = sys.stdin.readline().strip()
            clear_screen()
            dog_art2()
            shopping_items.append(purchased_items)
            sys.stdout.write("You have ")
            for x in range(len(purchased_items)):
                sys.stdout.write(purchased_items[x])
            sys.stdout.write(" in your shopping cart")
            skip()
            clear_screen()
            dog_art1()

        #If the number 4 is inputed, this elif statment will activate and run the
        #part of the program that takes the user home. The variable "running" will
        # be changed to false, ending the while loop and ending the program.
        elif location_choice == ("4"):
            clear_screen()
            dog_art2()
            sys.stdout.write("Off home we go!\n")
            skip()
            clear_screen()
            dog_art1()
            sys.stdout.write("You have finished the day with $"+str(total_money)+
                             " Nice Work!!")
            running = False
    

main()










    


                              
                              
