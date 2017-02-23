Objective: Parse variable name, variable starting index position, and variable width from 
SAS programs that creates a SAS files from ASCII files

1. This code is meant to accept SAS code, specifically those that has an input statement 
which includes the SAS format @x VarName y. (for numeric variables)
or @x VarName $y. (for character variables), where x us the starting index position of the variable,
y is the length of the variable, and VarName is the name of the variable, then outputs three .txt files:
a) A list of variable names
b) A list of Index position number for the starting position of each variable 
c) A list of variable widths 