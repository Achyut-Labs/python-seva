# Todo APP Basic
import os

tasks = []


def addTask(t):
    tasks.append(t)

def listTask():
   print(tasks)

# a function named add_task that will add task in the list of disctionary with user and task
def add_task(user, task):
    pass



def main():

    while True:
        try:
          response = input('Please enter the task you wanna add for future: ')
          addTask(response)

          response = input('Do you have more task to add?:  yes/no  ')
          if response.lower() == 'no':
              os.system('cls' if os.name == 'nt' else 'clear')
              listTask()
              print('Thanks for using this APP!')
              exit()

        except ValueError as err:
          print(err)

        listTask()


if __name__ == "__main__":
    main()
