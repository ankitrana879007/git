list_of_employees=[]

def add_employee():
    check=True      #check if employee id is unique or not
    print('Enter Employee Details')
    id=int(input('ID:'))
    name=str(input('Name:'))
    age=int(input('Age:'))
    position=str(input('Position:'))
    salary=int(input('Salary:'))

    if not list_of_employees:        
        check=True
    else:
        for employee in list_of_employees:
            if id==employee['id']:
                check=False
                break

    if check==True:
        employee={
            'id':id,
            'name':name,
            'age':age,
            'position':position,
            'salary':salary
        }
        list_of_employees.append(employee)
        print('Employee added successfully')
    else:
        print('Id already exists.')
def update_employee():
    id=int(input('Enter ID:'))
    for employee in list_of_employees:
        if id == employee['id']:
            print('Which information you want to update:')
            print('1.Name')
            print('2.Age')
            print('3.position')
            print('4.Salary')
            ch=input('Select any one to update:')
            if ch=='1':
                print(f'Name:{employee['name']}')
                employee['name']=input('Enter new name:')
            elif ch=='2':
                print(f'age:{employee['age']}')
                employee['age']=input('Enter new age:')
            elif ch=='3':
                print(f'Position:{employee['position']}')
                employee['position']=input('Enter new position:')
            elif ch=='4':
                print(f'salary:{employee['salary']}')
                employee['salary']=input('Enter new salary:')
            else:
                print('Please select valid value')
            
            print('Employee detail updated successfully')
            print()
            return
    print('Employee not found')

def delete_employee():
    id=int(input('Enter ID:'))
    for employee in list_of_employees:
        if id == employee['id']:
            list_of_employees.remove(employee)
            print('Employee deleted successfully')
            return
    print('Employee not found')
def display_employees():
    if len(list_of_employees)==0:
        print('No employees to display')
        return
    print('Id \t\t Name \t\t Age \t\t Position \t\t Salary')
    for employee in list_of_employees:
        print(f'{employee['id']} \t\t {employee['name']} \t\t {employee['age']} \t\t {employee['position']} \t\t {employee['salary']}')