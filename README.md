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