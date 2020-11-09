# Group Maker
##### This console application generates group distributions given a file containing a list of students, a file containing a list of topics and a number of groups. Each student and topic gets randomly asinged to a group. Students and topics are equally asigned between groups and the remaining are placed in a random group. Typically the applicationn will return distinct group distributions each time it is run even with the same input.

This console application was made with Python version 3.8.5  
To run it you must have installed an interpreter for Python version 3.X.X  
The the files and number of groups are passed as arguments in the console.  
Argument 1: file with students  
Argument 2: file with topics  
Argument 3: number of groups  

**Example command:**  
``$ python3 group_maker.py students.txt topics.txt 3``  

**Example output**  
Grupo 1 (Estudiantes: 2, Temas: 1)  
&nbsp;&nbsp;	Estudiantes:  
&nbsp;&nbsp;&nbsp;&nbsp;		1. 001-juan perez  
&nbsp;&nbsp;&nbsp;&nbsp;		2. carlos  
&nbsp;&nbsp;	Temas:  
&nbsp;&nbsp;&nbsp;&nbsp;		1. Estadistica aplicada  
Grupo 2 (Estudiantes: 2, Temas: 1)  
&nbsp;&nbsp;	Estudiantes:  
&nbsp;&nbsp;&nbsp;&nbsp;		1. juana  
&nbsp;&nbsp;&nbsp;&nbsp;		2. pedro  
&nbsp;&nbsp;	Temas:  
&nbsp;&nbsp;&nbsp;&nbsp;		1. matematica discreta  
Grupo 3 (Estudiantes: 3, Temas: 2)  
&nbsp;&nbsp;	Estudiantes:  
&nbsp;&nbsp;&nbsp;&nbsp;		1. tomas  
&nbsp;&nbsp;&nbsp;&nbsp;		2. alfredo  
&nbsp;&nbsp;&nbsp;&nbsp;		3. maria  
&nbsp;&nbsp;	Temas:  
&nbsp;&nbsp;&nbsp;&nbsp;		1. Politica nacional  
&nbsp;&nbsp;&nbsp;&nbsp;		2. tema libre  

