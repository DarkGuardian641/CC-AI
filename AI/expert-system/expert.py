import collections
import collections.abc
collections.Mapping = collections.abc.Mapping
collections.MutableMapping = collections.abc.MutableMapping
collections.Sequence = collections.abc.Sequence

from experta import *

class Patient(Fact):
    """Info about the patient"""
    pass

class HospitalExpertSystem(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="find_disease")

    # Rule for cold
    @Rule(Fact(action='find_disease'),
          Patient(fever='no', cough='yes', sneezing='yes', headache='no'),
          salience=3)
    def cold(self):
        print("Diagnosis: You may have a common cold.")
        print("Advice: Rest, drink fluids, and consider over-the-counter cold remedies.")
        self.halt()

    # Rule for flu
    @Rule(Fact(action='find_disease'),
          Patient(fever='yes', cough='yes', sneezing='no', headache='yes'),
          salience=3)
    def flu(self):
        print("Diagnosis: You may have the flu.")
        print("Advice: Rest, drink plenty of fluids, and consult a doctor if symptoms persist.")
        self.halt()

    # Rule for allergy
    @Rule(Fact(action='find_disease'),
          Patient(fever='no', cough='no', sneezing='yes', headache='no'),
          salience=3)
    def allergy(self):
        print("Diagnosis: You may have an allergy.")
        print("Advice: Avoid allergens and consider antihistamines.")
        self.halt()

    # Rule for unknown (lowest salience)
    @Rule(Fact(action='find_disease'),
          Patient(),
          salience=0)
    def unknown(self):
        print("Diagnosis: Unable to determine. Please consult a doctor for further diagnosis.")
        self.halt()

# Run the expert system immediately
engine = HospitalExpertSystem()
engine.reset()

# Collect user input
fever = input("Do you have a fever? (yes/no): ").strip().lower()
cough = input("Do you have a cough? (yes/no): ").strip().lower()
sneezing = input("Are you sneezing? (yes/no): ").strip().lower()
headache = input("Do you have a headache? (yes/no): ").strip().lower()

engine.declare(Patient(fever=fever, cough=cough, sneezing=sneezing, headache=headache))
engine.run()
