class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def calculate_avg(self):
        total_marks = sum(self.marks)
        avg_marks = total_marks / len(self.marks)
        print("Average Marks for",self.name,":",avg_marks)

    def get_grade(self):
            avg_marks = sum(self.marks) / len(self.marks)
            if avg_marks >= 90:
                grade = "A"
            elif avg_marks >= 80:
                grade = "B"
            elif avg_marks >= 70:
                grade = "C"
            elif avg_marks >= 60:
                grade = "D"
            else:
                grade = "F"
            print("Grade for",self.name,":",grade)

student1 = Student("Lebin",[85,90,78])
student1.calculate_avg()
student1.get_grade()