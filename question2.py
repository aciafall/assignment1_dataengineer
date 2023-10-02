import re


# test 1
pattern1=r'[^a-zA-z0-9]'
input1 = "ABCDEFabcdef123450"
input2 = "BCD@Fabcdef123450"

print(re.search(pattern1,input2))

# test 2
pattern2=r'ab+'
input3=["bab","abbbbb","baaaa"]
i=0
for i in range(len(input3)):
    print(re.search(pattern2,input3[i]))

# test 3
pattern3=r'^6.*6$'
input4=["65117896","78238936","56666665"]
i=0
for i in range(len(input4)):
    print(re.findall(pattern3,input4[i]))

# test 4
pattern4=r'\b\d{2,4}\b'
input5="xercises number 1, 23, 345, and 45678 are important"
print(re.findall(pattern4,input5))

# test 5
pattern5=r'\b0+(\d+)'
input6=["010.01.010.100","210.08.090.194"]
i=0
for i in range(len(input6)):
    input6[i]=re.sub(pattern5,r'\1',input6[i])
print(input6)

# pattern5=r'\b1+(\d+)'
# input6=["010.01.010.100","210.08.090.194"]
# i=0
# for i in range(len(input6)):
#     print(re.findall(pattern5,input6[i]))

# test 6
pattern6=r'[ _]'
input7="Python Exercises Of Regular_Expression"
input7=re.sub(pattern6, lambda x: '_' if x.group(0) == ' ' else ' ', input7)

# test 7
pattern7=r'(\d{4})-(\d{2})-(\d{2})'
input8="2022-09-10"
input8=re.sub(pattern7,r'\3-\2-\1',input8)
print(input8)

# test 8
pattern8=r'\b[aeAE]\w+'
input9="The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly"
re.findall(pattern8,input9)
print(re.findall(pattern8,input9))

#test 9
pattern9=r'“(.*?)”'
input10="Regex can be used in programming languages such as “Python”, “SQL”, “Javascript”, “R”, “Google Analytics”, “Google Data Studio”, and throughout the coding process."
print(re.findall(pattern9,input10))

#test 10
pattern10=r'https?://\S+'
input11="Find more Examples at Github https://www.github.com or W3School https://www.w3schools.com/"
print(re.findall(pattern10,input11))