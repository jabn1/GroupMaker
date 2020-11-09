import sys
import math
import random

arguments = sys.argv[1:]
if len(arguments) != 3:
    print(f'Error: group_maker.py expected 3 arguments and recieved {len(arguments)}')

try:  
    group_count = int(arguments[2])
except ValueError as err:
    print('Error while parsing amount of groups:',err)
    sys.exit()
except:
    print('Unexpected error while parsing amount of groups')
    sys.exit()

student_lines = []
topic_lines = []

try:
    file1 = open(arguments[0])
    file2 = open(arguments[1])
    student_lines = file1.readlines()
    topic_lines = file2.readlines()
    file1.close()
    file2.close()
except FileNotFoundError as err:
    print('File reading error: ',err)
    sys.exit()
except:
    print('Unexpected error while reading files')
    sys.exit()

students = []
topics = []

student_lines = [s.strip() for s in student_lines]
topic_lines = [t.strip() for t in topic_lines]

for s in student_lines:
    if s ==  '':
        break
    students.append(s)
for t in topic_lines:
    if t == '':
        break
    topics.append(t)

if len(students) < group_count:
    print('Error: The amount of groups cannot be greater than the amount of students')
    sys.exit()
if len(topics) < group_count:
    print('Error: The amount of groups cannot be greater than the amount of topics')
    sys.exit()
if len(students) < 1 or len(topics) < 1 or group_count < 1:
    print('Error: There must be atleast one group,student and topic')
    sys.exit()

class Group:
    def __init__(self):
        self.students = []
        self.topics = []

def rand_element(a_list):
    return a_list.pop(random.randint(0,len(a_list)-1))

min_stu_per_group = math.floor(len(students)/group_count)
remainder_stu = len(students)%group_count

min_top_per_group = math.floor(len(topics)/group_count)
remainder_top = len(topics)%group_count 

groups = []
for i in range(group_count):
    group = Group()
    for j in range(min_stu_per_group):
        group.students.append(rand_element(students))
    for j in range(min_top_per_group):
        group.topics.append(rand_element(topics))
    groups.append(group)

group_positions = list(range(group_count))
for i in range(remainder_stu):
    groups[rand_element(group_positions)].students.append(rand_element(students))

group_positions = list(range(group_count))
for i in range(remainder_top):
    groups[rand_element(group_positions)].topics.append(rand_element(topics))

count = 1
for group in groups:
    print(f'Grupo {count} (Estudiantes: {len(group.students)}, Temas: {len(group.topics)})')
    print('\tEstudiantes:')
    scount = 1
    for student in group.students:
        print(f'\t\t{scount}. {student}')
        scount += 1
    print('\tTemas:')
    tcount = 1
    for topic in group.topics:
        print(f'\t\t{tcount}. {topic}')
        tcount += 1
    count += 1