import json

class Person(object):
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

class Student(Person):
    def __init__(self,name,age,email,studentid):
        super().__init__(name, age, email)
        self.studentid = studentid

    def to_dict(self): #had to ask evil sentient computer (chatgpt) about this, tried for a while to do without this function but kept erroring with "non serializable data"
        return {       #finally i got the right format but gpt was still wrong so i compared to your dictionary notes
            'name' : self.name,
            'age' : self.age,
            'email' : self.email,
            'studentid' : self.studentid
        }
    
class Saver(object):
    def save(data, filename = 'studentnew.json'): #had to ask for help here bc i kept getting filename error code, it was a missed typo smh
        with open(filename, 'w') as f:  #my second error was the kernel, it wouldnt register then i had to restart the kernel and it worked fine
            json.dump(data,f, indent=4) 

student = Student('Grace', 23,'gebrisco@cpp.edu', 123456789)

filename = 'student.json'
with open('student.json', 'w') as f:
    json.dump(student.to_dict(), f, indent=4)

with open('student.json') as f:
    data_classes = json.load(f)
    print (json.dumps(data_classes, indent=2))