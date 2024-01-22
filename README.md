# arithmetic-program-synthesis
Developed a basic arithmetic program synthesizer in Python for COMP 597 at McGill. The program takes two inputs: an array of arrays containing operands and an array containing results. The program prints operations that correspond to the input/output sets. 

## Usage:
### Synthesizer:
main(ins, outs) 
- ins: 2d array of int
- outs: 1d array of int

### Example:
For:
- ins = [[1,2], [0,5], [2,2]]
- outs = [3, 5, 2]
  
main(ins, outs) prints "+"

For:
- ins = [["a","b","b"], ["aa","d","b"]]
- outs = ["aaabb", "aaaaaadb"]
  
main(ins, outs) prints "*", 3, "+"

### Case Generation:
- case ins = casegen.w_sets_of_n_ints(number of sets, number of inputs)
- case outs = casegen.gen_outs(case ins, casegen.combo_op(number of inputs))
