import casegen
import synth
import matplotlib.pyplot as plt
import numpy as np


# INS SETS 5X5 

# arithmetic test cases all add
add_ins = casegen.w_sets_of_n_ints(5, 5)
all_add_cases = (add_ins, casegen.all_add(add_ins))
ad = synth.main(all_add_cases[0], all_add_cases[1])

# arithmetic test cases all subtract
sub_ins = casegen.w_sets_of_n_ints(5, 5)
all_sub_cases = (sub_ins, casegen.all_sub(sub_ins))
su = synth.main(all_sub_cases[0], all_sub_cases[1])

# arithmetic test cases all multiply
mult_ins = casegen.w_sets_of_n_ints(5, 5)
all_mult_cases = (mult_ins, casegen.all_mult(mult_ins))
mu = synth.main(all_mult_cases[0], all_mult_cases[1])

# arithmetic test cases random size 5x2
combo_ins_a = casegen.w_sets_of_n_ints(5, 2)
combo_case_a = (combo_ins_a, casegen.gen_outs(combo_ins_a, casegen.combo_op(2)))
a = synth.main(combo_case_a[0], combo_case_a[1])

# arithmetic test cases random size 5x3
combo_ins_b = casegen.w_sets_of_n_ints(5, 5)
combo_case_b = (combo_ins_b, casegen.gen_outs(combo_ins_b, casegen.combo_op(5)))
b = synth.main(combo_case_b[0], combo_case_b[1])

# arithmetic test cases random size 5x4
combo_ins_c = casegen.w_sets_of_n_ints(5, 7)
combo_case_c = (combo_ins_c, casegen.gen_outs(combo_ins_c, casegen.combo_op(7)))
c = synth.main(combo_case_c[0], combo_case_c[1])

# arithmetic test cases random size 5x5
combo_ins_d = casegen.w_sets_of_n_ints(5, 9)
combo_case_d = (combo_ins_d, casegen.gen_outs(combo_ins_d, casegen.combo_op(9)))
d = synth.main(combo_case_d[0], combo_case_d[1])

# arithmetic test cases random size 5x8
combo_ins_e = casegen.w_sets_of_n_ints(5, 11)
combo_case_e = (combo_ins_e, casegen.gen_outs(combo_ins_e, casegen.combo_op(11)))
e = synth.main(combo_case_e[0], combo_case_e[1])

# arithmetic test cases random size 5x10
combo_ins_f = casegen.w_sets_of_n_ints(5, 13)
combo_case_f = (combo_ins_f, casegen.gen_outs(combo_ins_f, casegen.combo_op(13)))
f = synth.main(combo_case_f[0], combo_case_f[1])

# arithmetic test cases random size 5x15
combo_ins_g = casegen.w_sets_of_n_ints(5, 15)
combo_case_g = (combo_ins_g, casegen.gen_outs(combo_ins_g, casegen.combo_op(15)))
g = synth.main(combo_case_g[0], combo_case_g[1])


x_axis = np.array([5, 5, 5, 2, 5, 7, 9, 11, 13, 15])
y_axis = np.array([ad, su, mu, a, b, c, d, e, f, g])


plt.scatter(x_axis, y_axis)

#print(x_axis, y_axis)
plt.show()



