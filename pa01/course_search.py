'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
#import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        elif command in ['c', 'courses']:
            course = input("enter a coursenum:")
            schedule = schedule.course_num([course])
        elif command in ['i', 'instructor']:
            instructor = input('enter instructor\'s lastname to see courses they teach')
            schedule = schedule.lastname([instructor])
        elif command in ['ti', 'title']:
            title = input('enter a title')
            schedule = schedule.title([title])
        elif command in ['d', 'description']:
            description = input('enter a description')
            schedule = schedule.description([description])
<<<<<<< HEAD
        elif command in ['n', 'name']:
            course_name = input("enter a course name:")
            schedule = schedule.name([course_name])
=======
            

>>>>>>> 665046fde34b8f330c0c29742cabd16b886ce356
        else:
            print('command',command,'is not supported')
            continue
        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''print_course prints a brief description of the course '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
<<<<<<< HEAD
    topmenu()
    
=======
    topmenu()
>>>>>>> 665046fde34b8f330c0c29742cabd16b886ce356
