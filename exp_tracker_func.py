import os  # import = Python keyword to load a module
           # os = built-in module that gives functions to work with operating system (like checking files, paths, etc.)

def initialize_file():  # def = define a function
                        # initialize_file = function name (our custom name)
                        # () = no parameters required here
                        # : = starts the body of the function
    if not os.path.exists('expenses.txt'):  # if = conditional statement
                                            # not = logical operator (reverses True/False)
                                            # os.path.exists(...) = function that checks if a file exists
                                            # 'expenses.txt' = string (the filename we check)
                                            # whole line means → run the block only if file does NOT exist
        with open('expenses.txt','w') as file:  # with = context manager (auto closes file safely)
                                                # open() = built-in function to open a file
                                                # 'expenses.txt' = file name
                                                # 'w' = mode "write" (creates new file or clears if exists)
                                                # as file = assign opened file object to variable file
            file.write('Date, Amount, Category, Description\n')  # file.write() = method to write text into file
                                                                 # 'Date, Amount, Category, Description\n' = header text
                                                                 # \n = newline character (line break)

def add_expense(date, amount, category, description):  # Function with 4 parameters
                                                       # date = expected to be string like '2025-09-25'
                                                       # amount = number/string like 12.5
                                                       # category = string like 'Food'
                                                       # description = string like 'Lunch'
    with open('expenses.txt','a') as file:  # open() = function to open file
                                            # 'expenses.txt' = filename
                                            # 'a' = append mode (adds data at end without deleting old)
                                            # as file = variable name to use inside this block
        file.write(f'{date},{amount},{category},{description}\n')  # file.write() = writes text to file
                                                                   # f'...' = f-string (embed variables inside string)
                                                                   # {date},{amount},{category},{description} = insert values separated by commas
                                                                   # \n = newline
    print('expense added')  # print() = built-in function to display text on screen
                            # 'expense added' = confirmation message string

def view_expenses():  # define function named view_expenses, no parameters
    with open('expenses.txt','r') as file:  # open file in 'r' mode = read mode
                                            # file variable = handle to interact with file
        lines = file.readlines()  # file.readlines() = reads all lines and returns list
                                  # lines = variable now contains list of strings (each line is one element)
        print(lines[0])  # print() = output text to console
                         # lines[0] = first element of list = header line
        for line in lines[1:]:  # for = loop keyword
                                # line = loop variable (each line one by one)
                                # lines[1:] = slicing list (skip first element, take all others)
            print(line)  # print() = display each expense line from file

def filter_expenses(filter_by, filter_value):  # Function with 2 parameters
                                               # filter_by = string ('date' or 'category')
                                               # filter_value = value to match (e.g. '2025-09-25' or 'Food')
    with open('expenses.txt','r') as file:  # open file in read mode
        lines = file.readlines()  # readlines() = returns list of all lines
        print(lines[0])  # print first element = header row
        for line in lines[1:]:  # loop through each expense line only (skip header)
            data = line.split(',')  # line.split(',') = split string by comma → list of fields
                                    # data variable = holds list like [date, amount, category, description]
            if filter_by == 'date' and filter_value == data[0]:  # if = condition
                                                                # filter_by == 'date' → checks type of filter
                                                                # and = logical AND (both must be true)
                                                                # filter_value == data[0] → checks date column matches
                print(line)  # print expense line if matches
            elif filter_by == 'category' and filter_value == data[2]:  # elif = else if condition
                                                                      # filter_by == 'category' → check filter type
                                                                      # and filter_value == data[2] → check category column
                print(line)  # print expense line if matches

def delete_expense(date, amount, category, description):  # Function with 4 parameters to identify line
    lines = []  # initialize empty list variable
    with open('expenses.txt','r') as file:  # open file in read mode
        lines = file.readlines()  # read all lines and store in list
    with open('expenses.txt','w') as file:  # open file in write mode (this clears file first)
        for line in lines:  # loop through every line
            if line != f'{date},{amount},{category},{description}':  # condition: keep line if NOT equal to given string
                                                                     # f'...' builds same string pattern as written in file
                                                                     # ⚠ Problem: actual file line has '\n' at end so may never match
                file.write(line)  # write line back into file
                print('expense deleted')  # print message (⚠ inside loop, so prints many times)

import datetime  # import datetime module (for working with dates/times)

def monthly_summary():  # Function to calculate total expenses for current month
    current_month = datetime.datetime.now().strftime('%Y-%m')  # datetime.datetime.now() = get current date/time
                                                               # .strftime('%Y-%m') = format to "YYYY-MM"
                                                               # current_month = string like "2025-09"
    total_expense = 0.0  # float variable, stores sum of monthly expenses
    category_expense = {}  # dictionary variable, key=category, value=sum of that category

    with open('expenses.txt','r') as file:  # open file in read mode
        lines = file.readlines()  # read all lines into list
        for line in lines:  # loop over every line (including header)
            data = line.strip().split(',')  # line.strip() = remove whitespace/newline
                                            # .split(',') = break into list at commas
                                            # data variable = list of fields [date, amount, category, desc]
            if data[0].startswith(current_month):  # if = condition
                                                   # data[0] = first column (date string)
                                                   # .startswith(current_month) = check if date begins with year-month
                amount = float(data[1])  # convert second column string to float number
                category = data[2]  # third column = category string
                total_expense += amount  # add amount to total_expense
                if category in category_expense:  # if category already in dictionary
                    category_expense[category] += amount  # add amount to existing total
                else:  # if not already in dictionary
                    category_expense[category] = amount  # create new key with value amount
    print(f'Total expense for {current_month}:{total_expense}')  # print summary total using f-string
    for category, amount in category_expense.items():  # loop dictionary items (category=key, amount=value)
        print(f'{category}:{amount}')  # print each category and its total
