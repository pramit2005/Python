class Students:
    total_students=0
    def __init__(self,name,standard):
        self.name=name
        self.standard=standard
        Students.total_students+=1
    @classmethod
    def show_total(cls):
        print(f'The total number of students are: {cls.total_students}')
s1=Students('Pramit',12)
s2=Students('Sarkar',11)
Students.show_total()





