#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """Coucou"""
    @abstractmethod
    def sound(self):
        """
        Méthode abstraite qui doit être implémentée par toutes les sous-classes.
        """
        pass


class Dog(Animal):
    """coucou"""

    def sound(self):
        """
        Implémente la méthode sound pour renvoyer le son d'un chien.
        """
        return "Bark"


class Cat(Animal):
    """coucou"""

    def sound(self):
        """
        Implémente la méthode sound pour renvoyer le son d'un chat.
        """
        return "Meow"
