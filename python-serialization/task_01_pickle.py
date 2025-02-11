#!/usr/bin/python3
"""Class representing a custom object"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """initializes a new CustomObject instance"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """displays the attribute of the object"""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """serializes the object"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """deserializes the object"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None
