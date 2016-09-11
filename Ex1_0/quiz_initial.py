#!/usr/bin/env python
"""
###############################################################################
# FILE NAME : quiz_initial.py
# AUTHOR : J.Enochs
# CREATION DATE : 19-Aug-2016
# LAST MODIFIED : 08-Sep-2016
# DESCRIPTION : Initail assessment quiz to see how much python the class 
#               remembers.  No internet or other external references allowed.
#                              <<<<< TO USE THIS SCRIPT >>>>>
#               STEP 1 - Enter a value for question_count (# questions on your
#                  test). All variables are near the top of the script. This is
#                  the only variable you modify. 
#               STEP 2 - Modify the instructions.  The show_instructions() 
#                  function is the first function after main()
#               STEP 3 - If you entered a question_count of 10 then modify 
#                  functions q1() - q10() accordingly.  The program will ignore 
#                  unused questions.  Do NOT delete unsed questions!
###############################################################################/
"""
import os
import sys
import random
import socket
import shelve
import inspect
import textwrap
from time import sleep
from blessings import Terminal 

question_count = 5  # MODIFY - MAX 50
reviewCounter = 0
under_review = False
retake = False
ipAdr = "192.168.10.20"
offline = False
port = 5050
t = Terminal()
answers = {}
name = "none"
fs = 0

def main():
    get_name()
    show_instructions()
    show_questions()
    grade_exam()
    shelve_results()

def show_instructions():
    """
    MODIFY THE FOLLOWING INSTRUCTIONS ACCORDINGLY (inst string variable)
    """
    inst = "    These questions refer to python 2.7 (no additional modules loaded).  The questions are designed to see how much you remember about the python language.  There's one correct answer per question.  This quiz is not timed.\n\n"

    check_previous_results()
    os.system("clear")
    print t.white("\n\n\nINSTRUCTIONS:\n")
    print(textwrap.fill(inst))
    x = raw_input("\n\n\n          Press 'enter' to begin.")

def q1():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q2():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "What does running Python with the -tt option do?\n\n\
    (A) Runs the code in an interactive tty terminal.\n\
    (B) Raises TabError exceptions when tabs and spaces are used inconsistently.\n\
    (C) Causes the program to terminate when an error is raised (same as -t).\n\
    (D) Runs the program in debug mode.\n\
    (E) Supresses all warning messages.\n\n\n"
    answer = "B" 

    end_dialog(answer)

def q3():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "What does prefixing a function name with a single underscore do?\n\n\
    (A) Nothing. A single leading underscore has no special meaning.\n\
    (B) Identifiers prefixed with a single underscore perform special functions.\n\
    (C) Makes all of the function's members private.\n\
    (D) Prevents it from being imported by the 'from module import *' statement.\n\
    (E) Pre-loads the function into memory for faster execution.\n\n\n"
    answer = "D" 

    end_dialog(answer)

def q4():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q5():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q6():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q7():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q8():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q9():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q10():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q11():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q12():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q13():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q14():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q15():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q16():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q17():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q18():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q19():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q20():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q21():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q22():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q23():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q24():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q25():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q26():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q27():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q28():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q29():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q30():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q31():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q32():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q33():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q34():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q35():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q36():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q37():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q38():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q39():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q40():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q41():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q42():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q43():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q44():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q45():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q46():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q47():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q48():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q49():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def q50():
    # QUESTION AND ANSWERS SECTION: Modify accoringly and carefully
    print "Which of the following statements is FALSE?\n\n\
    (A) Python is an interpreted language.\n\
    (B) You can use 'for' and 'while' loops but there's no 'do while' statement.\n\
    (C) You can use 'if', 'else', 'elif', and switch statements.\n\
    (D) The python package manager is called pip.\n\
    (E) Numbers of type decimal require an additional module.\n\n\n"
    answer = "C" 

    end_dialog(answer)

def show_questions():
    global reviewCounter
    answers["question_count"] = question_count
    randomRange = range(1,question_count + 1)
    if under_review == False:
        random.shuffle(randomRange)
    for n in randomRange:
        os.system("clear")
        reviewCounter = reviewCounter + 1
        print "\nQUESTION {} of {}:\n\n".format(reviewCounter, question_count)
        eval("q" + str(n) + "()") 
    reviewCounter = 0

def grade_exam():
    global fs
    correct_answers = 0
    for n in range(1,question_count + 1):
        tup = answers[n]; correct, given = tup
        if correct == given:
            correct_answers += 1
        
    percentage = int(correct_answers * (100.0 / question_count))
    if fs == 0:
        fs = percentage

    while 1:
        os.system("clear")
        print "\n\n\n     You answered {0:d} out of {1:d} questions correctly. [ {2:d}% ]\n\n".format(correct_answers, question_count, fs)
        if percentage != 100:
            query = raw_input("Would you like to review your exam and see the correct answers? y/n: ")
        else:
            print "                     PERFECT SCORE !!!\n\n\n"
            query = raw_input("Would you like to review your exam? y/n: ")
        if query.lower() == "y":
            review()
            break
        elif query.lower() == "n":
            break
        else:
            print t.yellow("\n\n               Valid choices are y/n. Try again.")
            sleep(2)

def review():
    global under_review
    under_review = True
    show_questions()
    under_review = False

def end_dialog(answer):
    caller = inspect.currentframe().f_back.f_code.co_name
    question_number = int(caller[1:])
    global answers
    if not under_review:
        while 1:
            ans = raw_input("Answer: ").lower()
            if (ans == "a") or (ans == "b") or (ans == "c") or (ans == "d") or (ans == "e"):
                answerTuple = (answer.upper(), ans.upper())
                answers[question_number] = answerTuple
                break
            else:
                print t.yellow("\n\n     Valid choices are A-E. Try again.")
                sleep(1)
    else:
        tup = answers[question_number]; correct, given = tup
        print t.yellow("               <<< REVIEW >>>\n")
        print "          The correct answer is: {}".format(answer.upper())
        print "          Your answer was:",
        if correct != given:
            print t.red("({})".format(given))
        else:
            print t.green("CORRECT")
        if reviewCounter != question_count:
            pause()
        else:
            print "\n\n\n  <<< REVIEW COMPLETE >>>"

def check_previous_results():
    global retake
    global fs
    if os.path.isfile("python_shelve.db"):
        retake = True
        while 1:
            os.system("clear")
            print t.white("\n\n You've already taken this quiz.  What would you like to do?\n\n\
    (1) Review my previous results\n\
    (2) Take the quiz again.  This will not change your official score.\n\
    (3) Exit\n\n")
            ans = raw_input("   Selection: ")
            if ans == "1" or ans == "2" or ans == "3":
                break
            else:
                print t.yellow("\n\n          Valid choices are 1 - 3, try again.")
                sleep(2)
        if ans == "1":
            get_results()
            review()
            correct_answers = 0
            for n in range(1,question_count + 1):
                tup = answers[n]; correct, given = tup
                if correct == given:
                    correct_answers += 1
            percentage = int(correct_answers * (100.0 / question_count))
            if fs == 0:
                fs = percentage
            print "      Final Score: {}\n\n".format(fs)
            sys.exit()
        elif ans == "2":
            pass
        else:
            os.system("clear")
            sys.exit()

def shelve_results():
    d = shelve.open("python_shelve.db")
    try:
        d["inital_quiz"] = answers
    finally:
        d.close()
    if offline == False and not retake:
        T1=Client()
        T1.SubmitScore()
    print "      Final Score: {}\n\n".format(fs)

def get_results():
    global answers
    g = shelve.open("python_shelve.db")
    try:
        answers = g["inital_quiz"]
    finally:
        g.close()
    question_count = answers["question_count"]
        
def pause():
    hold_hold = raw_input("\n\n\nPress any key to continue...")

class Client():
    def __init__(self,Address=(ipAdr,port)):
        global ipAdr
        global port
        global offline
        self.s = socket.socket()
        try:
            self.s.settimeout(6)
            self.s.connect(Address)
            self.s.settimeout(None)
        except Exception as e:
            while 1:
                os.system("clear")
                print t.yellow("\n\n Connection using default IP failed.  What would you like to do?\n\n\
    (1) Enter a new IP address and port\n\
    (2) Take the quiz without connection to the test server\n\
    (3) Exit\n\n")
                ans = raw_input("   Selection: ")
                if ans == "1" or ans == "2" or ans == "3":
                    break
                else:
                    print t.yellow("\n\n          Valid choices are 1 - 3, try again.")
                    sleep(2)
            if ans == "1":
                ipAdr = raw_input("\nEnter IP address: ")
                port = raw_input("\nEnter port number: ")
                main()
            elif ans == "2":
                offline = True
            else:
                os.system("clear")
                self.s.close()
                sys.exit()

    def SubmitName(self):
        if offline == True:
            return
        data = "00{}".format(name)
        try:
            self.s.send(data)
        except Exception as e:
            print t.yellow("Connection to exam server failed!")
        finally:
            self.s.close()
    def SubmitScore(self):
        if offline == True:
            return
        data = "01{}".format(str(fs))
        try:
            self.s.send(data)
        except Exception as e:
            print t.yellow("Connection to exam server failed!")
        finally:
            self.s.close()

def get_name():
    global name
    os.system('clear')
    T2=Client()
    if offline == True:
        return
    name = raw_input("Please enter your name: ")
    T2.SubmitName()

if __name__ == "__main__":
    main()
