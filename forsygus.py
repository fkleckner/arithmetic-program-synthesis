import casegen
import synth

'''
# arithmetic test cases all add
add_ins = casegen.w_sets_of_n_ints(5, 5)
all_add_cases = (add_ins, casegen.all_add(add_ins))

ad = open("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/hw2bms/add_all.sl", "x")
ad.write(str(all_add_cases))
ad.close()


# arithmetic test cases all subtract
sub_ins = casegen.w_sets_of_n_ints(5, 5)
all_sub_cases = (sub_ins, casegen.all_sub(sub_ins))

su = open("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/hw2bms/sub_all.sl", "x")
su.write(str(all_sub_cases))
su.close()


# arithmetic test cases all multiply
mult_ins = casegen.w_sets_of_n_ints(5, 5)
all_mult_cases = (mult_ins, casegen.all_mult(mult_ins))

mu = open("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/hw2bms/mult_all.sl", "x")
mu.write(str(all_mult_cases))
mu.close()
'''

# arithmetic test cases random size 5x2
combo_ins_a = casegen.w_sets_of_n_ints(5, 2)
combo_case_a = (combo_ins_a, casegen.gen_outs(combo_ins_a, casegen.combo_op(2)))
'''
a = open("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/hw2bms/combo_a.sl", "x")
a.write(str(combo_case_a))
a.close()
'''

# arithmetic test cases random size 5x3
combo_ins_b = casegen.w_sets_of_n_ints(5, 3)
combo_case_b = (combo_ins_b, casegen.gen_outs(combo_ins_b, casegen.combo_op(3)))
'''
b = open("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/hw2bms/combo_b.sl", "x")
b.write(str(combo_case_b))
b.close()
'''

# arithmetic test cases random size 5x4
combo_ins_c = casegen.w_sets_of_n_ints(5, 4)
combo_case_c = (combo_ins_c, casegen.gen_outs(combo_ins_c, casegen.combo_op(4)))
'''
c = open("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/hw2bms/combo_c.sl", "x")
c.write(str(combo_case_c))
c.close()
'''

# arithmetic test cases random size 5x5
combo_ins_d = casegen.w_sets_of_n_ints(5, 5)
combo_case_d = (combo_ins_d, casegen.gen_outs(combo_ins_d, casegen.combo_op(5)))
'''
d = open("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/hw2bms/combo_d.sl", "x")
d.write(str(combo_case_d))
d.close()
'''
'''
# arithmetic test cases random size 5x8
combo_ins_e = casegen.w_sets_of_n_ints(5, 11)
combo_case_e = (combo_ins_e, casegen.gen_outs(combo_ins_e, casegen.combo_op(11)))

e = open("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/hw2bms/combo_e.sl", "x")
e.write(str(combo_case_e))
e.close()


# arithmetic test cases random size 5x10
combo_ins_f = casegen.w_sets_of_n_ints(5, 13)
combo_case_f = (combo_ins_f, casegen.gen_outs(combo_ins_f, casegen.combo_op(13)))

f = open("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/hw2bms/combo_f.sl", "x")
f.write(str(combo_case_f))
f.close()


# arithmetic test cases random size 5x15
combo_ins_g = casegen.w_sets_of_n_ints(5, 15)
combo_case_g = (combo_ins_g, casegen.gen_outs(combo_ins_g, casegen.combo_op(15)))

g = open("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/hw2bms/combo_g.sl", "x")
g.write(str(combo_case_g))
g.close()
'''

def create_smt_string(numvars, ins, outs):
    pot_vars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j" ,"k", "l", "m", "n", "o"]
    smt = "(set-logic LIA) \n(synth-fun f ("
    for i in range(numvars):
        smt += "(" + pot_vars[i]+ " Int) "
    smt += ") Int \n((Start Int)) \n ((Start Int ("
    for i in range(numvars):
        smt += str(i) + " "
    for i in range(numvars):
        smt += pot_vars[i] + " "
    smt +=  "\n\t(+ Start Start)\n\t(- Start Start)\n\t(* Start Start)))))"
    for x in range(5):
        smt += "\n(constraint (= (f "
        for i in range(numvars):
            tarin = ins[x][i]
            if tarin < 0:
                smt += "(- " + str(tarin*(-1)) + ") "
            else:
                smt += str(tarin) + " "
        smt += ") "
        tarout = outs[x]
        if tarout < 0:
            smt += "(- " + str(tarout*(-1)) + ") ))"
        else:
            smt += str(tarout) + " ))"
    smt += "\n(check-synth)"
    return smt

data = [combo_case_a, combo_case_b, combo_case_c, combo_case_d]
datanames = ["combo_case_two", "combo_case_three", "combo_case_four", "combo_case_five"]

for x in range(len(data)):
    filex = open(("/Users/finnkleckner/Library/CloudStorage/OneDrive-McGillUniversity/year4/COMP597/hw2/easygen/"+datanames[x]+".sl"), "x")
    filex.write(create_smt_string(len(data[x][0][0]), data[x][0], data[x][1]))
    filex.close()

