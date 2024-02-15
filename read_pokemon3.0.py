#Created by Matthew Shawn Oliveira Krischlunas
#Date created 12/13/23
print("Welcome to PokeBuilder. We are going to build a competitive ready Pokemon at LV100.\n")
again = "y"

while again.lower() == "y":
    retry = "n"

    while retry.lower() == "n":
        pokeName = input("Enter a pokemon name: ") #we are going to create our base global variables for our Pokemon

        try:
            myfile = open(f"PokeDex\\{pokeName}\\{pokeName}Forms.txt")
            Forms = []
            Names = myfile.readline()
            while Names != '-999':
                Names = Names.rstrip('\n')
                Forms += [Names]
                Names = myfile.readline()
            else:
                for x in range(len(Forms)):#using len function to get how many times we need to do the loop, by the exsact number
                    print(f"{x} = {Forms[x]}")
                myfile.close()
                x = int(input(f"Enter the number of wich {pokeName} you want to train: "))
                pokeName = (f"{Forms[x]}")
        except FileNotFoundError:
            pass

        Name = pokeName #Using pokeName for the Name of our pokemon but also being used to call our .txt files.
        #we are guiding our infile to read spesifcly where we want it to read in our computer. the last 4 folders are important.
        infile = open(f"PokeDex\\{pokeName}\\{pokeName}Type.txt")
            
        

        Type1 = infile.readline() #reading our .txt lines into data.
        Type1 = Type1.rstrip('\n')#using rstrip() to remove the \n when printed and if we have a dualtype pokemon Type will look preaty.
        Type2 = infile.readline()

        try: #Super long or statment makes it easy to get our second type. if second type isn't founf the try statement passes it to except.
            Type2 == ("Normal" or "Fighting" or "Flying" or "Posion" or "Ground" or "Rock" or "Bug" or "Ghost" or "Steel" or "Fire" or "Water"
                      or "Grass" or "Electric" or "Psychic" or "Ice" or "Dragon" or "Dark" or "Fairy")
            Type = (f"{Type1}\\{Type2}")#If second type is True then our pokemon will show two types.

        except NameError: #If second Type isn't found then our pokemon will only show one Type.
            Type = (f"{Type1}")
        infile.close() #closeing our first .txt file.

        count = 1#counter is super important to see how many abilites our pokemon will have. most can have up to 3 abilites.
        infile = open(f"PokeDex\\{pokeName}\\{pokeName}Ability{count}.txt")
        Ability1 = infile.readline()#All pokemon have at least 1 ability.
        infile.close

        try:#This was a pain to get working but try and except worked like a dream to see how many abilites our pokemon would have.
            count = count + 1#This counter will go up regardless if a ability is found, because the try statement will finish this block up.
            infile = open(f"PokeDex\\{pokeName}\\{pokeName}Ability{count}.txt")
            Ability2 = infile.readline()
            infile.close
        except FileNotFoundError:
            count = count - 1#Now if a second ability .txt isnt found then the counter will go back down by 1. This was the important in makeing this 
                             #program function. try and except for the win!!!
        try:
            count = count + 1
            infile = open(f"PokeDex\\{pokeName}\\{pokeName}Ability{count}.txt")
            Ability3 = infile.readline()
            infile.close
        except FileNotFoundError:
            count = count - 1


        print(f"{pokeName} has {count} abilities")#fString being used with pokeName and counter to find the numner of abilities our pokemon will have.

        if count == 3:#if-elif-else statments seemed to work best here to get our abilites to display and the number of them.
            print(Ability1)#Displaying the number of abilites to the user so that they can make a informed desicion on building there base pokemon.
            print(Ability2)
            print(Ability3)
            print(f"What ability would you like {pokeName} to have?\n")
            select = int(input("Enter 1 for ability1, 2 for ability2, and 3 for ability3: "))#input selection on what ability they would like.
            if select == 3:#This is our first nested if-else statment.
                Ability = Ability3

            elif select == 2:
                Ability = Ability2

            else:
                Ability = Ability1

        elif count == 2:#our second if else statement with now two selections.
            print(Ability1)
            print(Ability2)
            print(f"What ability would you like {pokeName} to have?\n")
            select = int(input("Enter 1 for ability1 or 2 for ability2: "))
            if select == 2:#our second nested if-else statment.
                Ability = Ability2

            else:
                Ability = Ability1
        else:#if our pokemon only has 1 abiliy then it will be automaticly selected as Ability1
            Ability = Ability1

        Stat = [0, 1, 2, 3, 4, 5] #0 is HP, 1 is Attack, 2 is Defense, 3 is Sp.Attack, 4 is Sp.Defense, 5 is Speed 
        infile = open(f"PokeDex\\{pokeName}\\{pokeName}Stats.txt")#infile for getting pokemons stats
        Stat[0] = int(infile.readline())#we have to turn these variables into integers so we can use them for math equations down the road.
        Stat[1] = int(infile.readline())#Pokemons stats make or break a pokemon in battle and we want to build on these numbers to 
        Stat[2] = int(infile.readline())#complete our build down the road.
        Stat[3] = int(infile.readline())
        Stat[4] = int(infile.readline())
        Stat[5] = int(infile.readline())
        infile.close()#closeing our infile.
        Base_Total = Stat[0] + Stat[1] + Stat[2] + Stat[3] + Stat[4] + Stat[5]#Thought it would be fun to display our pokemons base total.
        #maybe we can use it later for something.

        print(f"This is {pokeName}'s base build before we input Natures, EV's and IV's.\n")#now we display our base for our pokemon that we want to work with!
        print(f"""Name:{Name}
Type:{Type}
{Ability}
HP:{Stat[0]}
Attak:{Stat[1]}
Defense:{Stat[2]}
Sp.Attack:{Stat[3]}
Sp.Defense:{Stat[4]}
Speed:{Stat[5]}
Base Total:{Base_Total}""")
        print(input("Press enter to contine"))

        #we are going to do a for loop for our pokemon's stats at LV100

        if Name == "Shedinja":
            for x in range(1,6):
                Stat[x] = Stat[x] * 2 + 5
        else:
            for x in range(6):
                if x == 0:
                    Stat[x] = Stat[x] * 2 + 110
                else:
                    Stat[x] = Stat[x] * 2 + 5

        #Next we are going to ask the user to input what IVs thy want for each stat
        IV = [0, 1, 2, 3, 4, 5]
        Stats = ["HP", "Attack", "Defense", "Sp.Attack", "Sp.Defense", "Speed"]

        if Name == "Shedinja":
            for x in range(1,6):
                IV[x] = int(input(f"Enter a value from 0 - 31 for your IV value in {Stats[x]}: "))
                Stat[x] += IV[x]
        else:
            for x in range(6):
                IV[x] = int(input(f"Enter a value from 0 - 31 for your IV value in {Stats[x]}: "))
                Stat[x] += IV[x]

        #Now we enter our EV Values for each stat.
        EVs = 127
        EV = [0, 1, 2, 3, 4, 5]

        print(f"At the moment this is what {Name}'s stats look like.")
        print(f"""HP:{Stat[0]}
Attak:{Stat[1]}
Defense:{Stat[2]}
Sp.Attack:{Stat[3]}
Sp.Defense:{Stat[4]}
Speed:{Stat[5]}""")
        print(input("Press enter to contine to input EV values"))

        if Name == "Shedinja":
            print(f"You have {EVs} IV points to work with.")
            for x in range(1,6):
                EV[x] = int(input(f"Enter a value from 0 - 63 for your EV value in {Stats[x]}: "))
                Stat[x] += EV[x]
                EVs -= EV[x]
                print(f"you have {EVs} pounts left to use")
                if EVs == 0:
                    for y in range(x+1,6):
                        EV[y] = 0
                    break
                else:
                    print()
        else:
            print(f"You have {EVs} IV points to work with.")
            for x in range(6):
                EV[x] = int(input(f"Enter a value from 0 - 63 for your EV value in {Stats[x]}: "))
                Stat[x] += EV[x]
                EVs -= EV[x]
                print(f"you have {EVs} pounts left to use")
                if EVs == 0:
                    for y in range(x+1,6): #kept getting 20 in speed if no number was inputed so this code fixed that problem
                        EV[y] = 0
                    break
                else:
                    print()

        #Next nature is calculated into our Stats
        print("What nature would you like your pokemon to have?")
        print(f"These are the natures that will have a postive and negative effect on {pokeName} stats.\n")

        print("""For stat Attack Stat boost
Adamant = Sp.Attack-, Lonely = Defense-
Brave = Speed-, Naughty = Sp.Defense-\n""")

        print("""For stat Defense Stat boost
Impish = Sp.Attack-, Bold = Attack-
Relaxed = Speed-, Lax = Sp.Defense-\n""")

        print("""For stat Sp.Attack Stat boost
Modest = Attack-, Mild = Defense-
Quite = Speed-, Rash = Sp.Defense-\n""")

        print("""For stat Sp.Defense Stat boost
Careful = Sp.Attack-, Gentle = Defense-
Calm = Attack-, Sassy = Speed-\n""")

        print("""For stat Speed Stat boost
Jolly = Sp.Attack-, Hasty = Defense-
Timid = Attack-, Naive = Sp.Defense-\n""")

        print("""For Nutral growth
Bashful, Docile, Hardy, Quirky, Serious\n""")

        Nature = input("Enter the nature you want for {pokeName}: ")

        if Nature == "Adamant" or Nature == "adamant":
                Value = .10
                Stat[1] += int(Stat[1] * Value)
                Stat[3] -= int(Stat[3] * Value)
                
               

        elif Nature == "Lonely" or Nature == "lonely":
            Value = .10
            Stat[1] += int(Stat[1] * Value)
            Stat[2] -= int(Stat[2] * Value)
            
            

        elif Nature == "Brave" or Nature == "brave":
            Value = .10
            Stat[1] += int(Stat[1] * Value)
            Stat[5] -= int(Stat[5] * Value)
            

        elif Nature == "Naughty" or Nature == "naughty":
            Value = .10
            Stat[1] += int(Stat[1] * Value)
            Stat[4] -= int(Stat[4] * Value)
             

        elif Nature == "Bold" or Nature == "bold":
            Value = .10
            Stat[2] += int(Stat[2] * Value)
            Stat[1] -= int(Stat[1] * Value)
            

        elif Nature == "Relaxed" or Nature == "relaxed":
            Value = .10
            Stat[2] += int(Stat[2] * Value)
            Stat[5] -= int(Stat[5] * Value)
            

        elif Nature == "Impish" or Nature == "impish":
            Value = .10
            Stat[2] += int(Stat[2] * Value)
            Stat[3] -= int(Stat[3] * Value)
            

        elif Nature == "Lax" or Nature == "lax":
            Value = .10
            Stat[2] += int(Stat[2] * Value)
            Stat[4] -= int(Stat[4] * Value)
            
            
        elif Nature == "Timid" or Nature == "timid":
            Value = .10
            Stat[5] += int(Stat[5] * Value)
            Stat[1] -= int(Stat[1] * Value)
            

        elif Nature == "Hasty" or Nature == "hasty":
            Value = .10
            Stat[5] += int(Stat[5] * Value)
            Stat[2] -= int(Stat[2] * Value)
            

        elif Nature == "Jolly" or Nature == "jolly":
            Value = .10
            Stat[5] += int(Stat[5] * Value)
            Stat[3] -= int(Stat[3] * Value)
            
            
        elif Nature == "Naive" or Nature == "naive":
            Value = .10
            Stat[5] += int(Stat[5] * Value)
            Stat[4] -= int(Stat[4] * Value)
           

        elif Nature == "Modest" or Nature == "modest":
            Value = .10
            Stat[3] += int(Stat[3] * Value)
            Stat[1] -= int(Stat[1] * Value)
            

        elif Nature == "Mild" or Nature == "mild":
            Value = .10
            Stat[3] += int(Stat[3] * Value)
            Stat[2] -= int(Stat[2] * Value)
            
           
        elif Nature == "Quite" or Nature == "quite":
            Value = .10
            Stat[3] += int(Stat[3] * Value)
            Stat[5] -= int(Stat[5] * Value)
            

        elif Nature == "Rash" or Nature == "rash":
            Value = .10
            Stat[3] += int(Stat[3] * Value)
            Stat[4] -= int(Stat[4] * Value)
            

        elif Nature == "Calm" or Nature == "calm":
            Value = .10
            Stat[4] += int(Stat[4] * Value)
            Stat[1] -= int(Stat[1] * Value)
            

        elif Nature == "Gentle" or Nature == "gentle":
            Value = .10
            Stat[4] += int(Stat[4] * Value)
            Stat[2] -= int(Stat[2] * Value)
            
               
        elif Nature == "Sassy" or Nature == "sassy":
            Value = .10
            Stat[4] += int(Stat[4] * Value)
            Stat[5] -= int(Stat[5] * Value)
            
            
        elif Nature == "Careful" or Nature == "careful":
            Value = .10
            Stat[4] += int(Stat[4] * Value)
            Stat[3] -= int(Stat[3] * Value)
        else:
            pass

        print(f"This is {pokeName}'s base build before we input Natures, EV's and IV's.\n")#our final product.
        print(f"""Name:{Name}
Type:{Type}
{Ability}
{Nature}
HP:{Stat[0]}
Attak:{Stat[1]}
Defense:{Stat[2]}
Sp.Attack:{Stat[3]}
Sp.Defense:{Stat[4]}
Speed:{Stat[5]}
Base Total:{Base_Total}""")

        print(f"Are you happy with the results of {pokeName}?")
        retry = input("If not, then Enter 'n' to retry: \n")
    else:
        bottle = ["HP Up", "Protein", "Iron", "Calcium", "Zinc", "Carbos"]
        feathers = ["Health Feather", "Muscle Feather", "Resist Feather", "Genius Feather", "Cleaver Feather", "Swift Feather"]

        myfile = open(f"Build_Ready\\{pokeName}.txt", "a")
        myfile.write(f"""Name:{Name}
Type:{Type}
{Ability}
{Nature}
HP:{Stat[0]}
Attak:{Stat[1]}
Defense:{Stat[2]}
Sp.Attack:{Stat[3]}
Sp.Defense:{Stat[4]}
Speed:{Stat[5]}
Base Total:{Base_Total}""")
        myfile.write(" \n\n")

        for x in range(6):
            myfile.write(f"You will need to put in {EV[x] *4} points in {Stats[x]} EVs\n")
            EV[x] *= 4
            EVr = EV[x] % 10
            EV[x] = ((EV[x] - EVr) / 10)
            myfile.write(f"You will need {EV[x]:.0f} {bottle[x]} and {EVr} {feathers[x]} to get {Stat[x]} points in {Stats[x]}.\n\n")
        print(f"Data has been writen to {pokeName}.txt")
        myfile.close()

        print("Would you like to create another pokemon?")
        again = input("Enter 'y' to contine: ")
else:
    print("The program is finished.")
