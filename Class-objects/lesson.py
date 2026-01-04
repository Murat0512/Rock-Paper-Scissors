

class ClassSchedule:
    def __init__(self, course, instructor):
        self.course =course
        self.instructor = instructor

    def display_course(self):
        print(f"Course: {self.course} , Instructor: {self.instructor}")

    
sched = ClassSchedule("Chemistry", "Mr. Doe")

sched.display_course() 
print(sched.course)



class ClassSchedule:
   def __init__(self, course, instructor):
       self._course = course # protected
       self._instructor = instructor # protected
  
   def display_course(self):
       print(f'Course: {self._course}, Instructor: {self._instructor}')
 
sched = ClassSchedule('Biology', 'Ms. Smith')
sched.display_course()

