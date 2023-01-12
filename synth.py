from __future__ import annotations
import json
import time


# gives a dictionary of dictionaries
# the structure is { Task -x : {inputs : outputs} }
# will assume that for each Task x, the number of inputs and outputs is consistent
def parse():
	# Opening JSON file
	f = open('toy.json')

	# returns JSON object as a dictionary
	data = json.load(f)
	# Closing file
	f.close()
	parsed = []
	for task in data:
		ins = []
		outs = []
		for io in data[task]:
			ins.append(io['Input'])
			outs.append(io['Output'])
		parsed.append((ins, outs))
	# return the dictionary
	return parsed

def _exprs(expr, stack_depth, vals, ops):
    """ Generate postfix expressions recursively.
        `expr` is the expression so far, a list of values and operators.
        `stack_depth` is the depth of the stack created by expr.
        `vals` is a list of values remaining to add to the expression.
        `ops` is a list of possible operators to choose from.
    """
    if stack_depth == 1 and not vals:
        # This is a valid expression.
        yield expr
    if stack_depth > 0:
        # Try using an operator
        for o in ops:
            for e in _exprs(expr+[o], stack_depth-1, vals, ops):
                yield e
    if vals and stack_depth == 0:
        # Vals are available, push one on the stack
        for e in _exprs(expr+[vals[0]], stack_depth+1, vals[1:], ops):
            yield e

# this function simply creates a list of ascending integers to model input indeces
# ex: enum_indeces(6) = [0, 1, 2, 3, 4, 5]
def enum_indeces(n):
    ret = []
    for i in range(n):
        ret.append(i)
    return ret


def transform(ins, expression):
    new_exp = []
    ins_ind = 0
    for elmnt in expression:
        if type(elmnt) is int:
            new_exp.append(ins[ins_ind])
            ins_ind += 1
        else:
            new_exp.append(elmnt)
    return new_exp

def valid(ins, outs, expression):
    for i in range(len(outs)):
        e = transform(ins[i], expression)
        #print(e)
        if eval("".join(str(x) for x in e)) != outs[i]:
            return False
    return True

def main(ins, outs):
    st = time.time()
    # height of tree for n inputs is log_2(n)
    #operators = [Times, Sub, Plus]
    template_ins = enum_indeces(len(ins[0]))
    int_valid_ops = ["+", "-", "*"]
    expressions = _exprs([], 0, template_ins, int_valid_ops)

    for e in expressions:
        if valid(ins, outs, e):
            print(e)
    et = time.time()
    return (et-st)



