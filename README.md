# arithmetic-program-synthesis
Developed a basic arithmetic program synthesizer in Python for COMP 597 at McGill.

## Usage:
### Synthesizer:
main(ins, outs) 
- ins: 2d array of int
- outs: 1d array of int

### Example:
main([[1,2], [0,0,0,5], [2,2]], [3, 5, 2])
- output: 



For case generation:

case ins = casegen.w_sets_of_n_ints(number of sets, number of inputs)
case outs = casegen.gen_outs(case ins, casegen.combo_op(number of inputs))
