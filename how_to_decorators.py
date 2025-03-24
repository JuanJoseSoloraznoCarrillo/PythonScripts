# -*- coding: UTF-8 -*-
# ************************************************************************************************************#
# ALL RIGHTS RESERVED.                                                                                        #
# The reproduction, transmission or use of this document or its                                               #
# contents is not permitted without express written authority.                                                #
# Offenders will be liable for damages. All rights, including rights                                          #
# created by patent grant or registration of a utility model or design,                                       #
# are reserved.                                                                                               #
# ------------------------------------------------------------------------------------------------------------#
# Author: Solorzano, Juan Jose                                                                                #
# Date:                                                                                                       #  
# Summary:
# Python dependencies: Python > 3.11
# ************************************************************************************************************#

def day(fnc):
    def wrapper():
        print("Today is:",end="\t")
        fnc() # You already know that fnc is a callable object.
    return wrapper # returns the inner function

def dayName():
    print("Monday")
# Examples:
whatDay = day(dayName) # the function dayName is being decorated by the function day. 
whatDay()

#fancy decorators using @ character in python
@day
def otherDayName():
    print("wednesday")

otherDayName() 

# Decorators are callable that accepts and returns callable, since classes are callable, decorators are also used
# to decorate classes.
# Examples:

class DecoratorClass:
    def __init__(self,func):
        self.func = func
    @classmethod
    def __call__(self):
        print("You're in the call method")
        self.func() # func is must be callable 
        
@DecoratorClass
def myFunction():
    print("Running myFunction")

myFunction()

def MyMainFunction(hello):
    return 0