import random


def n_ints(n):
    res = []
    for i in range(n):
        res.append(random.randint(-100, 100))
    return res

def w_sets_of_n_ints(w, n):
    res = []
    for i in range(w):
        res.append(n_ints(n))
    return res

def all_add(ins_set):
    outs = []
    for ins in ins_set:
        expr = []
        for elmnt in ins:
            expr.append(elmnt)
            expr.append("+")
        expr.pop() 
        outs.append(eval("".join(str(x) for x in expr)))
    return outs


def all_sub(ins_set):
    outs = []
    for ins in ins_set:
        expr = []
        for elmnt in ins:
            expr.append(elmnt)
            expr.append("-")
        expr.pop() 
        outs.append(eval("".join(str(x) for x in expr)))
    return outs

def all_mult(ins_set):
    outs = []
    for ins in ins_set:
        expr = []
        for elmnt in ins:
            expr.append(elmnt)
            expr.append("*")
        expr.pop() 
        outs.append(eval("".join(str(x) for x in expr)))
    return outs

def combo_op(n):
    ops = ["+", "-", "*"]
    combo = []
    for i in range(n-1):
        combo.append(ops[random.randint(0,2)])
    return combo

# generates outputs on 2-d array of integer inputs and an array of operations
def gen_outs(ins_set, ops):
    outs = []
    for ins in ins_set:
        expr = []
        ind = 0
        for elmnt in ops:
            expr.append(ins[ind])
            expr.append(elmnt)
            ind += 1
        expr.append(ins[ind]) 
        outs.append(eval("".join(str(x) for x in expr)))
    return outs
