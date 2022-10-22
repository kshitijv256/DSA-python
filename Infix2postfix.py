
# NOT USABLE YET!!!

def in2post():
    print('Enter the expression')
    inp = input("")
    list1 = list(inp)
    ops = ['**','/','*','+','-']
    list2 = []
    list3 = []
    for i in range(len(list1)):
         if list1[i] == '(':
             list2.append(list1[1])
             
         elif list1[i] == ')':
             for j in range(len(list2)):
                 if list2[-1] == '(':
                     list2.pop()
                     break
                 else:
                     list3.append(list2[-1])
                     list2.pop()

         elif list1[i] in ops:
             if list2[-1] in ops:
                 if ops.index(list2[-1]) < ops.index(list1[i]):
                     list3.append(list2[-1])
                     list2.pop()
                     list2.append(list1[i])
             else:
                 list2.append(list1[i])
         else:
             list3.append(list1[i])

    for i in list2:
         list3.append(list2[-1])

    str1 = ""
    for i in list3:
        str1 += i
    return print(str1)

in2post()