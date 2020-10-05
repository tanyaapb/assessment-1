"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

# Write your function here
def is_from_hometown(city_name):
    if type(city_name) is not str or len(city_name) <= 0:
        return False
    return city_name.lower() == "indore" 



"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

# Write your function here
def first_and_last_name(first_name, last_name):
    return str(first_name) + " " + str(last_name)

"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""

# Write your function here
def print_greeting(first_name, last_name, hometown):
    output = ""
    full_name = f"{first_name} {last_name}"
    if is_from_hometown(hometown):
        output = f"Hi {full_name} , we're from the same place!"
        print(output)
    
    output = f"Hi {full_name}, I'd like to visit {hometown}!"
    print(output)

"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""

# Write your function here
def is_fruit(fruit_name):
    if len(fruit_name) > 1:
        if fruit_name.lower() == "strawberry" or fruit_name.lower() == "raspberry" or fruit_name.lower() == "blackberry" or fruit_name.lower() == "currant":
            return True
    return False



"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""

# Write your function here


"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""

# Write your function here

def total_cost(base_price, state_name, tax_percent):

    extra_tax = 0
    if base_price <= 0:
        return base_price
    
    if state_name == "CA":
        extra_tax = float((base_price*3)/100)
    
    elif state_name == "PA":
        extra_tax = base_price + 2
    
    elif state_name == "MA":
        if base_price <= 100:
            extra_tax = 1
        else:
            extra_tax = 3
    
    # Assuming here "not given" could be only None as some states
    # can have 0 taxes
    if tax_percent is None:
        tax_percent = 5
    
    tax_ammount = (int(base_price)*(tax_percent))/100
    
    total_price = float(base_price + tax_ammount + extra_tax)
    return total_price

"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

# Write your function here

def add_args(list1, *argv):
    for arg in argv:
        list1.append(arg)
    return list1

"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""

# Write your function here
def word_to_tuple(word):
    def multiplied_word():
        multi_word = ""
        for __ in range(0,len(word)):
            multi_word += word
        return multi_word
    
    return (word, multiplied_word())
