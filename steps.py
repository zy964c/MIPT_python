import sys
num_steps = int(sys.argv[1])
num_steps_init = num_steps
while(num_steps > 0):
    spaces = num_steps - 1
    hashes = num_steps_init - spaces
    print(' '*spaces + '#'*hashes)
    num_steps -= 1
