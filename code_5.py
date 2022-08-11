class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"


class ScienceExam:
    string = "Maths , English"
    def __init__(self,marks,time,*parts):
        self.marks = marks
        

        self.time = time
        self.parts = parts

        for i in parts:
            self.string+= " ,"  
            self.string+=i
             
    def examParts(self):
        k =   1
        for i in self.string.split(','):
            print(f"Part {k} - {i}")
            k+=1
    def examSyllabus(self):
        return self.string

    def __str__(self):
        return f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {len(self.parts)+2}"
engineering = ScienceExam(100,90,"Physics","HigherMaths")

print(engineering)

print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())