
import os


months = {'Jan' : '1', 'Feb' : '2', 'Mar' : '3', 'Apr' : '4', 'May' : '5', 'Jun' : '6', 'Jul' : '7','Aug' : '8', 'Sep' : '9', 'Oct' : '10', 'Nov' : '11', 'Dec' : '12'}
keys = list(months.keys())
values = list(months.values())


home = '/Users/palwindersingh/Documents/test'


def walk_directory():
    for root, dirs, files in os.walk(home, topdown=False):
        for name in dirs:
            fullPath = os.path.join(root, name)
            
            print(fullPath)
            name = name[0].upper() + name[1:3]

            if name in keys:
                search = name
                location = keys.index(search)

                

            
                print(name + ' found at index ' + str(location+1) + ' its value is: ' + values[location])
                print('changing folder name from '+ name + ' to ' + values[location])

                newName = os.path.join(root, values[location])

                os.rename(fullPath, newName)
            else:
                print('DNE')

               
walk_directory()
        