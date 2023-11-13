# import csv
# import random
# import time
# from datetime import datetime, timedelta

# class ExamCenter:
#     def __init__(self, last_name, first_name, entry_time, exit_time, room_number):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.entry_time = entry_time
#         self.exit_time = exit_time
#         self.room_number = room_number

#     def write_file(self, students):
#         with open('exam_results.csv', mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["First Name", "Last Name", "Entry Time", "Exit Time", "Room Number"])
#             for student in students:
#                 writer.writerow([student.first_name, student.last_name, student.entry_time, student.exit_time, student.room_number])

#     def read_file(self):
#         with open('exam_results.csv', mode='r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 print(row)

# def main():
#     students = []

#     while True:
#         first_name = input("Enter your first name: ")
#         last_name = input("Enter your last name: ")
#         entry_time = datetime.now()
#         exit_time = entry_time + timedelta(minutes=30)
#         room_number = random.randint(1, 20)

#         student = ExamCenter(last_name, first_name, entry_time, exit_time, room_number)
#         students.append(student)

#         print(f"Hello {first_name} {last_name}!")
#         print(f"Entry Time: {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
#         print(f"Exit Time: {exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
#         print(f"Room Number: {room_number}\n")
#         time.sleep(1)
        
#         another_student = input("Do you want to enter another student? (yes/no): ").lower()
#         if another_student != "yes":
#             break

#     students[0].write_file(students)
#     print("Student details written to 'exam_results.csv'\n")

#     input("Press Enter to read and display the CSV file...")
#     students[0].read_file()

# if __name__ == "__main__":
#     main()


import requests
import time
def downloadSite(url, session): 
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")
def downloadAllsites(sites):
    with requests.Session() as session:
        for url in sites: downloadSite(url, session)
if __name__ == "__main__":
    sites = ["https://www.udayton.edu", ] * 80
    startTime = time.time()
    downloadAllsites(sites)
    duration = time.time() - startTime
    print(f"Downloaded {len(sites)} in {duration} seconds")
