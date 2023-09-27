import random

#Bot command functions
#------------------------------------------------------------
def roll(num_1, num_2): #Roll random number

    num_1 = int(num_1)
    num_2 = int(num_2)

    rolled_number = random.randint(num_1, num_2)

    output_string = (f"You asked for a random number between {num_1} and {num_2}.\nYour roll: {rolled_number}!")

    return output_string

def coinflip(msg = None): #Flip a coin
    heads_or_tails = {
        1: "Heads",
        2: "Tails"
    }
    
    tts_on_or_off = False

    if msg != None:
        tts_on_or_off = True


    selection = random.randint(1,2)

    output_string = (f"You got {heads_or_tails[selection]}")

    return output_string, tts_on_or_off

def spin_wheel(user_input, author): #Spins a wheel and outputs the order of results

    #Checks if user has a nick name. If so, uses the nickname
    if author.nick != None:
        name = str(author.nick)
    else:
        name = str(author)

    user_list = make_options_into_list(user_input)
    output_string = f"{name}'s Results:\n"

    for i in range(len(user_list)):

        option = random.randint(0, len(user_list)-1)

        output_string += f"{i+1}) {user_list[option]}\n"

        del user_list[option]

    return output_string

def random_from_list(user_dictionary, author): #Chooses a random value from a given list
    
    try:
        if author not in user_dictionary or user_dictionary[author] == None:
            return "You do not currently have a list. Please create one using the !createlist command", None
        else:
            length = len(user_dictionary[author])
            choice = random.randint(0, length-1)

            choice_to_delete = user_dictionary[author][choice]
            output_string = f"Your result: {choice_to_delete}"

            return (output_string, choice)
    except:
        return "You either don't currently have a list or there was an error. Try again, or use !createlist command to create a list", None

def show_list(user_dictionary, author): #Shows what the current user's list is

    if author not in user_dictionary or user_dictionary[author] == []:
        return "You don't have a list. Please make one using the !createlist command"
    else:
        return f"Your list: {user_dictionary[author]}"

#___________________________________________________________________

#Helper functions
def make_options_into_list(arguments):
    user_list = []

    for arg in arguments:
        user_list.append(arg)

    return user_list