import datetime
#initialize an empty list to store task
projectlist = []



#In the construction of this code third party code has been used
#to enhance the program code. The original code and idea can be found here
#https://elite.law.ac.uk/ultra/courses/_69892651_1/outline/edit/document/_12395134_1?courseId=_69892651_1&view=content
#consolidate task in unit 6.
#The code itself allows users to add task, view task, mark task as completed

#function to display project task management system
def display_process():
   print("\nWelcome to the SMART Project Task Management System!")
   print("1. Add projects to the Project List")
   print("2. View the projects")
   print("3. Mark projects as completed")
   print("4. Delete project")
   print("5. Exit")
   
   
 
#function to add project
#error handling code is included
def add_project(projectlist):
  try:
      project_name = input("Enter the name of the project: ")
      priority = input("Enter the priority (High, Medium, Low): ")
      due_date = input("Enter the due date (YYYY-MM-DD): ")

      
      #adds user input to the project list storage
      projectlist.append({"name": project_name, "completed": False, "priority": priority, "due_date":due_date})
      print(f"Project '{project_name}' Added Successfully!")
  except Exception as e:
      print(f"An error occurred: {e}")


#function to view projects
def view_project(projectlist):
  try:
      if not projectlist:
        print("No projects found.")
      else:
        print(projectlist)
  except Exception as e:
      print(f"An error occurred: {e}")

        
        
#function to mark projects as completed
def mark_completed(projectlist):
  try:
     view_project(projectlist)
     index = int(input("Enter the index of the project to mark as completed: "))
     if 1 <= index <= len(projectlist):
        #code to find the specific index and mark as completed
        projectlist[index - 1]["completed"] = True
        print(f"Project '{projectlist[index - 1]['name']}' marked as completed.")
     else:
        print("Invalid index.")
  except Exception as e:
      print(f"An error occurred: {e}")

        
 #function to delete a project       
def delete_project(projectlist):
   try:
      view_project(projectlist)
      index = int(input("Enter the index of the project to delete: "))
      if 1 <= index <= len(projectlist):
        deleted_project = projectlist.pop(index - 1)
        print(f"Project '{deleted_project['name']}' deleted.")
      else:
        print("Invalid index.")
   except Exception as e:
      print(f"An error occurred: {e}")
      
# function to view upcoming tasks
def view_upcoming_tasks(projectlist):
    try:
        #code to get the current date and time
        today = datetime.date.today()
        upcoming_tasks = [project for project in projectlist if project.get("due_date") and datetime.datetime.strptime(project["due_date"], "%Y-%m-%d").date() > today]
        if upcoming_tasks:
            print("Upcoming tasks:")
            for task in upcoming_tasks:
                print(
                    f"Name: {task['name']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")
        else:
            print("No upcoming tasks.")
    except Exception as e:
        print(f"An error occurred: {e}")

 
 #Main program loop           
while True:
  try:
      display_process()
      options = input("Kindly select Options 1 - 6: ")

      if options == '1':
        add_project(projectlist)

      elif options == '2':
        view_project(projectlist)


      elif options == '3':
         mark_completed(projectlist)
        

      elif options == '4':
         delete_project(projectlist)
        

      elif options == '5':
         print("Exiting Program...")
         break
      else:
        print("Invalid option. Please enter a number between 1 and 5.")
  except Exception as e:
      print(f"An error occurred: {e}")
      

