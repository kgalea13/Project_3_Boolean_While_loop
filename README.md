# Project_3_Boolean_While_loop
A project that focuses on boolean logic with while loops. 


Project Objectives
• Decision-making with if, if-else, if-elif-

• Data validation (and correction and use of default) for user input using a while loop.
• Nicely formatted output report using f-string.
• Multiple input data sets (i.e., for multiple Employees).
• Inside-out incremental development of the program.
Python Language Elements:
• Follow python naming conventions for variables and constants.
• Use good descriptive naming for variables/constants.
• Top comment must include your name, project number, lab section, and brief project
description.
Project Overview
A company has three tiers of sales staff, denoted by B (beginning), M (mid‐level), and P
(professional). Employees have been assigned a tier based on their past record. Below is the
monthly salary schedule for each tier. Let N represent the number of items sold.
Tier B: The salary plus commission for items sold. If N > 9, then add
$50 per item for items 10 through 15, and $75 per item for all
items above 15. If N < 10, there will be a message “WARNING:
Sales must improve.”
Tier M: The base salary plus commission for items sold. If N > 14, then
add $60 per item for items 15 through 20, and $100 per item
for all items above 20. If N < 15, there will be a message,
1
“WARNING: Sales must improve in order to stay in Tier M.
Tier P: The base salary plus commission for items sold. If N > 19 then
add $75 per item for items 20 through 25, and $125 per item
for all items above 25. If N < 20, there will be a message that
“WARNING: Sales must improve to stay in Tier P”.
Write a program that will:

• Ask the user to enter the employee’s name.
• Ask the user to input a Tier. It should accept B, M, P, b, m, or p. In other words,
the user may use either upper or lower case designations for the tier. Read the
input. If the Tier value is not legitimate, a message to that effect should be
printed and no other information printed.
• Ask the user to input the base salary for the employee, and read it as a
float.
• Ask the user for the number of items sold, and read that value as an integer.
• Based on the tier, base salary, and number of items sold, compute and report the
monthly pay.
• Print out the name, tier, number of items sold, and payment for the month.
Deliverables
The deliverable for this project is the following file:
proj02_LastName.py
Be sure to use the specified file name and to submit it for grading via eLearning before the
project deadline.
Stages of the Program Development
0) The program hardcodes “input” data for ONE employee, does appropriate calculations &
produces the output.
1) AFTER STAGE 0 WORKS CORRECTLY
Program gathers input data for ONE employee from the user instead of using hardcoded
“input” data but does not do any data validation on the input
2) AFTER STAGE 1 WORKS CORRECTLY
Add data correction & validation (see rules below) for the input gathering (for ONE
employee)
3) AFTER STAGE 2 WORKS CORRECTLY
Add looping so that the program can handle as many employees as the user provides.
(After handling one employee, the program asks whether the user wants to enter data for
another employee, then proceeds accordingly).
2
Stage 3 version of the program is the one that you should submit to get the full 100 points.
INPUT (for 1 employee)
Use appropriate prompts to get these 4 data items from user:
Employee’s name, monthly base salary, his/her tier, and number of items sold,
INPUT CORRECTION & VALIDATION (added in stage 2)
• Tiers letters must be one of: B, M, P (in prompt, you asked for B or M or P)
o Before checking for validity, do 2 things to “help the user” by fixing certain
things:
▪ Grab just the 0th char they entered (in case they type in Low) char0 =
input_str[0]
▪ Capitalize that first char (in case they entered a) cap_char = char0.upper()
• If it’s invalid, keep asking the user for a valid tier letter until they enter something
correct.
• Each of the 3 tier types will have its own validation loop.
• Number of items sold must be a positive number.
o If it’s invalid, keep asking the user for a valid number of items sold until they
enter something correct.
INPUT - MULTIPLE EMPLOYEES (added in stage 3)
• After handling a single TIER (IPO for it: input/validate the data, do calculations, print
enter the tier designation), ask the user if they wish to enter another employee (YES or
NO).
• If they say YES (or Yes or yes or YEs or yeS or …) or Y (or y), then go around the big
loop again.
o Use the 2 String methods to 1) grab just the 1st char and 2) capitalize it) to reduce
the number of cases that need to be checked to just ‘Y’ (so that’d include yup,
yea, yo, yellow, . . .)
• Any other response (like No/no/N/n/nope/naw/whatever/who cares/red/green/…) will be
assumed to be a NO.


