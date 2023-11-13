
import csv
import random
import time
from datetime import datetime, timedelta

class ExamCenter:
    def __init__(self):
        self.rooms = list(range(1, 21))
        self.students = []
        self.csv_filename = "exam_results.csv"
        self.current_time = datetime.now()

    def assign_room(self):
        if not self.rooms:
            return None
        room = random.choice(self.rooms)
        self.rooms.remove(room)
        return room

    def start_exam(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        student_info = {
            "first_name": first_name,
            "last_name": last_name,
            "entry_time": self.current_time.strftime("%H:%M:%S"),
        }

        room = self.assign_room()
        if room is not None:
            student_info["room_number"] = room

        # Calculate the exit time (30 minutes from entry time)
        exit_time = self.current_time + timedelta(minutes=30)
        student_info["exit_time"] = exit_time.strftime("%H:%M:%S")

        # Store student info
        self.students.append(student_info)

        # Display student's information
        print(f"Hello {first_name} {last_name},")
        print(f"Exam Time: {self.current_time.strftime('%H:%M:%S')}")
        print(f"Exit Time: {exit_time.strftime('%H:%M:%S')}")
        if room is not None:
            print(f"Room Number: {room}")

    def write_to_csv(self):
        with open(self.csv_filename, mode="w", newline="") as csv_file:
            fieldnames = ["first_name", "last_name", "entry_time", "exit_time", "room_number"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.students)

    def display_csv(self):
        with open(self.csv_filename, mode="r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(f"Name: {row['first_name']} {row['last_name']}, Room: {row['room_number']}")

    def run_exam(self):
        print("Welcome to the Exam Center!")
        for _ in range(20):
            self.start_exam()
        self.write_to_csv()
        print("\nExam results written to 'exam_results.csv'.")
        print("\nExam Results:")
        self.display_csv()

if __name__ == "__main__":
    exam_center = ExamCenter()
    exam_center.run_exam()
