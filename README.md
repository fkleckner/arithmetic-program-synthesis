# arithmetic-program-synthesis
Developed a basic arithmetic program synthesizer in Python for COMP 597 at McGill.

To run the synthesizer do main(ins, outs) where ins are a 2-dimensional array of integers, and outs is a 1-dimensional array of integers.
For case generation:
case ins = casegen.w_sets_of_n_ints(number of sets, number of inputs)
case outs = casegen.gen_outs(case ins, casegen.combo_op(number of inputs))
