# interplanetary-rover
## Navigation
The below table is the essentially the base implementation of the calculation of the new position vector of the rover.

|                	| EAST  	| WEST  	| NORTH 	| SOUTH 	|
|----------------	|-------	|-------	|-------	|-------	|
| MOVE FORWARDS  	| x+1   	| x-1   	| y+1   	| y-1   	|
| MOVE BACKWARDS 	| x-1   	| x+1   	| y-1   	| y+1   	|
| TURN LEFT      	| NORTH 	| SOUTH 	| WEST  	| EAST  	|
| TURN RIGHT     	| SOUTH 	| NORTH 	| EAST  	| WEST  	|


## Round planet
As the Earth is not flat (although some people disagree with this statement), we need to wrap around the edges, and thus if |grid| = (m, n), then

- (m + 1, y) -> (0, y)
- (-1, y) -> (m, y)
- (x, -1) -> (x, n)
- (x, n + 1) -> (x, 0)

There might be other better ways of achieving this but this was the first thing
that popped in my head as it's the simplest and most rudimentary way of solving
this.

## Potential improvements
- Split and perhaps simplify `Navigation.calc_new_pos_vec()`. Not particularly pleased with this implementation.
- Review the boundary conditions and make sure no conditions were missed as I'm sure there were things I missed.
- Better error handling by writing custom Exceptions

## Secondary objectives
4. It is indeed inefficient to store the commands in a list of strings as apparently
the size of a one letter string is 50 bytes, whereas if we put the one letter string
in a list, the size of that object increases to 64 bytes, as can be seen below.

```python
>>> import sys
>>> sys.getsizeof('F')
50
>>> sys.getsizeof(['F'])
64
```

As an example, the size of the following list of commands is 152 bytes.

```python
>>> commands = ['F', 'F', 'L', 'F', 'R', 'F', 'B', 'L', 'F', 'F', 'F', 'F']
>>> sys.getsizeof(commands)
152
```

The size of a single integer in Python is 28 bytes.

```python
>>> sys.getsizeof(1)
28
```

Size of tuples are less than that of lists:

```python
>>> sys.getsizeof((1))
28
>>> sys.getsizeof([1])
64
```

Just replacing the list with a tuple, we get a slight improvement:

```python
>>> sys.getsizeof(('F', 'F', 'L', 'F', 'R', 'F', 'B', 'L', 'F', 'F', 'F', 'F'))
136
```

5. If the rover has intermittent power issues and storing current state and
commands in memory only is unreliable, then we can persist the data to the local
disk and in case of failure, i.e. the signals cannot arrive to the rover in time
for them to be processed, then we can get the rover's current state and continue from that state reading from the persisted data. Another method is to send
the commands in chunks to the rover and persist them to the disk and therefore,
when the signal to the rover doesn't arrive in time, the rover can continue
its trajectory by reading the commands from the local disk.