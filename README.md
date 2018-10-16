# Compression Algorithms With Julia 1.0
Several Compression Algorithms Implemented Using Julia 1.0

## Features
- [x] Move-To-Front
- [ ] Burrows–Wheeler Transform
- [ ] Time Stamp

## Results

### Move-TO-Front

This Algorithm Increased Temporal Locality by decaoding the common showed up letters to the front.

_-> Original string: 
Man is the only creature that consumes without producing. He does not give milk, he does not lay eggs, he is too weak to pull the plough, he cannot run fast enough to catch rabbits. Yet he is lord of all the animals. He sets them to work, he gives back to them the bare minimum that will prevent them from starving, and the rest he keeps for himself.
-> Decoded seq: 
Man is the only creature that consumes without producing. He does not give milk, he does not lay eggs, he is too weak to pull the plough, he cannot run fast enough to catch rabbits. Yet he is lord of all the animals. He sets them to work, he gives back to them the bare minimum that will prevent them from starving, and the rest he keeps for himself._

_Look Up Cost
Total Cost Using MTF Algorithm: 4688
Total Cost Using Original Access: 16438
Total Look up cost saved 71.481%_
