# # # Name = Taluba Aron Hopson
# # # Student ID = 101747537

import csv
import random
import time
from datetime import datetime, timedelta

class ExamCenter:
    def __init__(self, last_name, first_name, entry_time, exit_time, room_number):
        self.last_name = last_name
        self.first_name = first_name
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.room_number = room_number

    @classmethod #decorator is used to declare a method in the class
    def write_file(cls, students):
    # Open the 'exam_results.csv' file in write ('w') mode
        with open('exam_results.csv', mode='w', newline='') as file:
            #This creates a CSV writer object named writer that is associated with the file
            writer = csv.writer(file) 
             #This line creates the header row in the CSV file.
            writer.writerow(["First Name", "Last Name", "Entry Time", "Exit Time", "Room Number"])
            #This loop iterates through the students list
            for student in students:
                writer.writerow([student.first_name, student.last_name, student.entry_time, student.exit_time, student.room_number])

    @classmethod #decorator is used to declare a method in the class
    def read_file(cls):
    # Open the 'exam_results.csv' file in read ('r') mode
        with open('exam_results.csv', mode='r') as file:
        # Create a CSV reader object for the file
            reader = csv.reader(file)
        # Iterate through each row in the CSV file
            for row in reader:
            # Print the content of each row
                print(row)


def main():
    students = []

    while True:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        # Get the current time as the entry time
        entry_time = datetime.now()
        # Calculate the exit time by adding 30 minutes to the entry time
        exit_time = entry_time + timedelta(minutes=30)
        # Generate a random room number (between 1 and 20)
        room_number = random.randint(1, 20)

        # Create a student object with the entered data and add it to the list of students
        student = ExamCenter(last_name, first_name, entry_time, exit_time, room_number)
        students.append(student)

        print(f"Hello {first_name} {last_name}!")
        print(f"Entry Time: {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Exit Time: {exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Room Number: {room_number}\n")
        # Pause for 1 second before the next interaction
        time.sleep(1)
        
        another_student = input("Do you want to enter another student? (yes/no): ").lower()
        # If the response is not "yes," exit the loop
        if another_student != "yes":
            break

    # Write the student details to a CSV file
    ExamCenter.write_file(students)
    # Notify the user that the data has been written to the file
    print("Student details written to 'exam_results.csv'\n")

    input("Press Enter to read and display the CSV file...")
    # Read and display the CSV file
    ExamCenter.read_file()

if __name__ == "__main__":
    main()
