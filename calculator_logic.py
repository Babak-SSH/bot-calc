def calculate(exp):#they are in order
    while ('!' in exp):
        cord = exp.index('!')
        i = cord
        while (i != 0 and exp[i-1].isdigit() == True):
            i -= 1
        num = int(exp[i:cord])
        exp = exp.replace(exp[i:cord+1],str(fac(num)))
    while ('(' in exp):
        exp = parent(exp)
    while ('*' in exp):
        exp = operator(exp,'*')
    while ('/' in exp):
        exp = operator(exp,'/')
    while ('+' in exp):
        exp = operator(exp,'+')
    while ('-' in exp):
        exp = operator(exp,'-')
    return exp


def parent(exp_tmp): #runs until there are parenthesis
    cord_s = exp_tmp.index('(')
    cord_e = len(exp_tmp) - exp_tmp[::-1].index(')') - 1
    anw = calculate(exp_tmp[cord_s + 1:cord_e])
    exp_tmp = exp_tmp.replace(exp_tmp[cord_s:cord_e + 1],str(anw))
    return exp_tmp

def operator(exp_tmp,opr):#operators (+, -, /, *)
    cord = exp_tmp.index(opr)
    i = cord
    j = cord
    while (i != 0 and exp_tmp[i-1].isdigit() == True):
        i -= 1
    while (j != len(exp_tmp) - 1 and exp_tmp[j+1].isdigit() == True):
        j += 1
    old = exp_tmp[i:j+1]
    x,y = exp_tmp[i:j+1].split(opr)
    if (opr == '*'):
        multi = int(x) * int(y)
    elif (opr == '/'):
        multi = int(x) / int(y)
    elif (opr == '+'):
        multi = int(x) + int(y)
    elif (opr == '-'):
        multi = int(x) - int(y)
    exp_tmp = exp_tmp.replace(old,str(multi))
    return exp_tmp


def fac(num):#factoriel algorithm written with recursion
    if (num == 0):
        return 1
    else:
        return num * fac(num-1)