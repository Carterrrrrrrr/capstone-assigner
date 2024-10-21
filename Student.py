import csv
from Presentation import Presentation

class Student:
    #class attributes list of all students 
    all_students = []
    
    def __init__ (self, name, advisor, request):
        # all students have 4 attributes 
        self.name = name
        self.advisor = advisor
        self.request = request
        self.schedule = {
            "1": None,
            "2": None,
            "3": None
        }
        Student.all_students.append(self)
    
    def __repr__(self):
        out = f"\n\n{self.name}'s Sched:"
        for x in self.schedule.values():
            out += f"\n\t{x}"
        return out

    def set_schedule(self, schedule):
        self.schedule = schedule

    def get_schedule(self):
        return self.schedule
    
    
    def assign_student(self):
        for req in self.request:
            if req != 'any':
                options = Presentation.all_presentations.get(req)
                for option in options:
                    if len(option.roster)<int(option.room_size):
                        if option.presentation_name not in self.schedule.values():
                            if self.schedule[option.period] is None:
                                self.schedule[option.period] = option.presentation_name #put in sched
                                option.roster.append(self.name) #add to roster 
                                break

    def assign_rnd_presentation(self):
        for x in self.schedule:
            if self.schedule[x] is None:
                for prez in Presentation.get_available_prez():
                    if prez.period == x and len(prez.roster)<int(prez.room_size):
                        if prez.presentation_name not in self.schedule.values():
                            self.schedule[prez.period] = prez.presentation_name #put in sched
                            prez.roster.append(self.name) #add to roster 
                            break

    # def assign_rnd_presentation(self):
    #     for x in self.schedule:
    #         if self.schedule[x] is None:
    #             print(f"{self.name}'s period {x} is free")
    #             list_prez = [Presentation.all_presentations.values()]
    #             for prez in list_prez:
    #                 if prez.period == x and len(prez.roster)<int(prez.room_size):
    #                     if prez not in self.schedule.values():
    #                         print(f"adding: {prez.presentation_name} during {prez.period}")
    #                         print(f"")
    #                         self.schedule[prez.period] = prez #put in sched
    #                         prez.roster.append(self.name) #add to roster 
    #                         break 
      

    @classmethod
    def make_students_from_csv(cls, filename: str):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            students = list(reader)
        #for each line in the csv file
        for student in students:
            #make an object with data from that line
            Student( #calling the init (constructor) method
                #format: parameter name = line[csv_field_name]
                name = (student.get(('name'))),
                advisor = (student.get('Advisor')),
                request = [student.get('req1'), student.get('req2'), student.get('req3'), student.get('req4'), student.get('req5'), student.get('req6')]
            )
