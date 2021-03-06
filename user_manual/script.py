from pyvolve import *

# Read in a newick tree
t = read_tree(tree = "(t4:0.785,(t3:0.380,(t2:0.806,(t5:0.612,t1:0.660):0.762):0.921):0.207);")

# Construct state frequency vector. Optional!
f = EqualFrequencies("amino_acid")
freqs = f.construct_frequencies(type = "codon")

# Build the evolutionary model
m = Model("GY", {'state_freqs':freqs, 'omega':1.5, 'kappa':3.4})
m.construct_model()

# Initialize partitions
p = Partition(models = m, size = 10)

# Evolve, and call.
evolve = Evolver(partitions = p, tree = t)
for i in range(3):
    evolve(seqfile = "sequences" + str(i)+ ".phy", seqfmt = "phylip")
    print evolve.get_sequences()