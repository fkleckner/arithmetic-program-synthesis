import json
class IncorrectResult(Exception):
	pass


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

# returns ints/strings
def add(x, y):
	return x + y

def mult(x, y):
	return x * y

# returns only ints
def minus(x, y):
	return x - y

# returns bools
def LT(x, y):
	return x < y

def EQ(x, y):
	return x == y

# for bools only returns bools
def NOT(x):
	return not x

def AND(x, y):
	return x and y

def OR(x, y):
	return x or y


# here operation is a function, prev are a list of previous operations, fun_list is the ongoing list
# of operations done and ins
def try_op_inner(operation, prev, fun_list, ins, outs):

	results = []
	count = 0
	old_ins = []
	for x in ins:
		old_ins.append(x.copy())
	# doing operation on all the inputs and previous calculations
	for inputs in ins:
		results.append(operation(prev[count], ins[count].pop(0)))
		count += 1

	# result is a new round of calculations
	fun_list.append(operation)
	try_op(ins, outs, results, fun_list)


def try_op(ins, outs, prev_results, fun_list):
	while len(ins[0]) > 0:
		new_fun = fun_list.copy()
		try:
			try_op_inner(add, prev_results, new_fun, ins, outs)
		except (TypeError, IncorrectResult):
			try:
				try_op_inner(minus, prev_results, new_fun, ins, outs)
				#return False
			except (TypeError, IncorrectResult):
				try:
					try_op_inner(mult, prev_results, new_fun, ins, outs)
					#return False
				except (TypeError, IncorrectResult):
					try:
						try_op_inner(LT, prev_results, new_fun, ins, outs)
						#return False
					except (TypeError, IncorrectResult):
						try:
							try_op_inner(EQ, prev_results, new_fun, ins, outs)
							#return False
						except (TypeError, IncorrectResult):
							try:
								try_op_inner(NOT, prev_results, new_fun, ins, outs)
								#return False
							except (TypeError, IncorrectResult):
								try:
									try_op_inner(AND, prev_results, new_fun, ins, outs)
									#return False
								except (TypeError, IncorrectResult):
									try:
										try_op_inner(OR, prev_results, new_fun, ins, outs)
									except (TypeError, IncorrectResult):
										continue
	else:
		# if not equal raise IncorrectResult! - general except, because want to do the same in both circumstances
		outs_counter = 0
		for result in prev_results:
			if result != outs[outs_counter]:
				raise IncorrectResult
			else:
				outs_counter += 1


		return fun_list


def main():

	data = parse()
	prev_results = []
	for x in data[0][0]:
		prev_results.append(x.pop(0))
	print(try_op(data[0][0], data[0][1], prev_results, []))

main()
