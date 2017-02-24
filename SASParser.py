
# coding: utf-8

# In[7]:

def SAS_Program(filename):
    '''eg. SAS_Program('SASbreast.txt')'''
    data=open(filename).read()
    data=data.split(sep="@")
    # Extract variable name from the SAS input code and dump into a list called newdata
    newdata=[]
    for i in range(len(data)):
        i=i+1
        if i==len(data):
            break
        newdata.append(data[i][0+3:data[i].find("$")-1])
    # remove leadiing numbers before names
    newdata1=[]
    for i in range(len(newdata)):
        if i>1:
            newdata1.append(newdata[i][newdata[i].find(" "):])
        else:
            newdata1.append(newdata[i])
    # remove leading/trailing zeros, leaving a list of variable names
    names=[]
    for i in newdata1:
        names.append(i.strip())
    names=tuple(names)

    # """
    #         Not sure if these are needed. When I imported the output of
    #         this function into R, some of the vars had the quotes oddly placed

    # """
    # names=str(names)
    # names=names.replace("(","")
    # names=names.replace(")","")


    # Get Beginning Index Postion of Variable (Phyton based indexing)
    start0=[]
    start1=[]
    start=[]
    for i in range(len(data[1:])):
        start0.append(data[1:][i][1:4]) 
    for i in range(len(start0)):
        start1.append(start0[i].split(" "))
    for i in range(len(start1)):
        start.append(int(start1[i][0])-1)

    # Get Width of variable
    new=[]
    width=[]
    end=[]
    for i in range(len(data)):
        if i>0:
            new.append(data[i][data[i].find("char"):data[i].find(".")]) #This line would limit code to character data
    for i in range(len(new)):
        width.append(int(new[i][new[i].find("r")+1:]))
        end.append(start[i]+width[i])
    # Outputs a list called Columns as such: [('VarName1', (StartPosVar1,EndPosVar1)), ('VarName2', (StartPosVar2,EndPosVar2)),... ]
    columns=[]
    for i in range(len(names)):
        columns.append(tuple( [ names[i], tuple( [start[i], end[i]] ) ] ))
    return columns

