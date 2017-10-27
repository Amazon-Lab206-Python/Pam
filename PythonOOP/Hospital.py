import random
class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []

    def admit(self, a_patient):
        if len(self.patients) >= self.capacity:
            print "Apologies. The Hospital is Full."
        else:
            self.patients.append(a_patient)
            a_patient.bed += random.randint(1,300)
            print "Admission Complete. Your ID is", a_patient.id, "and your bed number is", a_patient.bed
        print self.patients
        return self

    def discharge(self, name):
        for patient in self.patients:
            if patient.name == name:
                self.patients.remove(patient)
                patient.bed = 0
                print "Thank you for coming,", patient.name
        print self.patients

class Patient(object):
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = random.randint(1,1000)
        self.bed = 0

    def displayInfo(self):
        print "***Patient Info***"
        print "Name:", self.name
        print "Allergies:", self.allergies
        print "ID Number:", self.id
        print "Bed Number", self.bed

h1 = Hospital("General", 300)
p1 = Patient("Pam", "Bees")
p2 = Patient("Sam", "None")
p3 = Patient("Noah", "Gluten")

h1.admit(p1).admit(p2).admit(p3)
p1.displayInfo()
p2.displayInfo()
p3.displayInfo()
h1.discharge("Pam")
