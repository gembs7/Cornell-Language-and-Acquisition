output = ''' COPY AND PASTE DATA HERE BEFORE RUNNING CODE. MAKE SURE THAT YOUR COPY STARTS WITH A TITLE,
NOT THE WORDS GLIMMAX PROCEDURE. YOUR DATA SHOULD END WITH THE DATE AND PAGE NUMBER. '''

from tkinter import *
from tkinter import simpledialog

pvalue_i = output.find('Pr > |t|')
tvalue_i = output.find('t Value')
df_i = output.find('DF')
StandardE_i = output.find('Error')
Estimate_i = output.find('Estimate')

question1 = simpledialog.askstring("input string", "Copy and paste the title at top of Data Chunk:")
number_of_chunks = simpledialog.askinteger("input integer", "How many data chunks?:")

output0 = output.replace("<", "0")
output1 = output0.replace(str(question1), "")
try:
    output2 = output1.replace("Standard", "")
except:
    output2 = output1

outputlist = output2.split()
outputlist2 = outputlist.copy()
the = outputlist2.index('SAS') - 1
procedure = outputlist2.index('Procedure') + 1
remove_list = outputlist2[the:procedure]
outputlist1 = [i for i in outputlist2 if i not in remove_list]
# print(outputlist1)


# try:

# Pr = [i for i, n in enumerate(outputlist) if n == 'Pr'][a]
#  greaterthan = [i for i, n in enumerate(outputlist) if n == '>'][a]
# print(greaterthan)
#   absolutet = [i for i, n in enumerate(outputlist) if n == '|t|'][a]
#    # print(absolutet)
#     t = Pr - 2
#      Value = [i for i, n in enumerate(outputlist) if n == 'Value'][a]

#       nameadjust1 = ''.join([outputlist[i] for i in [Pr, greaterthan, absolutet]])
#       nameadjust2 = ''.join([outputlist[i] for i in [t, Value]])

#        outputlist1[Pr] = nameadjust1
#        outputlist1[t] = nameadjust2

#        a = a + 1
# print(a)


# except:
#    pass

# print(outputlist1)

floats = []
for item in outputlist1:
    try:
        floats.append(float(item))
    except (ValueError, TypeError):
        pass

# print(floats)

page_number = simpledialog.askinteger("input integer", "Insert page number of 1st data chunk (bottom right of chunk):")

a = float(0)
try:
    for element in range(number_of_chunks - 1):
        c = float(page_number + 1)
        find = floats.index(c + a)
        del floats[find]
        a = a + 1.0
except:
    pass

numbers = [int(i) for i in floats]

Variables = simpledialog.askinteger("input integer", "How many columns are there?")
var = []
for i in range(Variables):
    var.append(outputlist1[i])
# print(var)


# print(numbers)

print(numbers)
print(floats)

# Estimate = ['Estimate']
# Error = ['Error']
# DF = ['DF']
# tValue = ['T-Value']
# pValue = ['Pr>|t|']

headings = var
print(headings)


sizing = Variables
subfloats = [floats[n:n + sizing] for n in range(0, len(floats), sizing)]
print(subfloats)

import pandas as pd

df = pd.DataFrame(subfloats, columns=headings)
print(df)

file_path = simpledialog.askstring('input string', r'Copy and paste the file path to your Excel file (be sure to remove quotes around path): ')

df.to_excel(file_path, index=False, header=True)