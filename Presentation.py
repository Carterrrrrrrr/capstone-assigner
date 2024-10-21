import csv
import random

class Presentation:
    #class attributes dicitonary of all pres
    all_presentations={}

    def __init__(self, presentation_name, period, room_size):
        self.presentation_name = presentation_name
        self.period = period
        self.room_size = room_size
        self.roster = []
        #add the pres to the dicitonary item whose key = presentation_name
        if Presentation.all_presentations.get(presentation_name) is None:
            Presentation.all_presentations[presentation_name] = []
        Presentation.all_presentations.get(presentation_name).append(self)
    
    def __repr__(self):
        out = f"\n\n{self.presentation_name}:"
        for x in self.roster:
            out += f"\n\t{x}"
        return out
    
    # def __repr__(self):
    #     return f"{self.presentation_name} roster: {self.roster}"

    @classmethod
    def get_available_prez(cls):
        clean_list = []
        for prez in Presentation.all_presentations.values():
            if len(prez[0].roster)<int(prez[0].room_size):
                clean_list.append(prez[0])
            if len(prez[1].roster)<int(prez[1].room_size):
                clean_list.append(prez[1])
        random.shuffle(clean_list)
        return clean_list

    def isRoom(self):
        if (self.room_size<len(self.roster)):
            return True
        return False

    def set_period(self, period):
        self.period = period

    def get_period(self):
        return self.period

    def set_room_size(self, room_size):
        self.room_size = room_size

    def get_room_size(self):
        return self.room_size
    
    def set_roster(self, roster):
        self.roster = roster

    def get_roster(self):
        return self.roster

    @classmethod
    def make_presenations_from_csv(cls, filename: str):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            presentations = list(reader)
        for presentation in presentations:
            Presentation(
                period=(presentation.get(('period'))),
                presentation_name = (presentation.get('name')),
                room_size = presentation.get('room size')
            )