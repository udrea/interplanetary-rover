# interplanetary-rover
## Navigation
The below table is the essentially the base implementation of the calculation of the new position vector of the rover.

|                	| EAST  	| WEST  	| NORTH 	| SOUTH 	|
|----------------	|-------	|-------	|-------	|-------	|
| MOVE FORWARDS  	| x+1   	| x-1   	| y+1   	| y-1   	|
| MOVE BACKWARDS 	| x-1   	| x+1   	| y-1   	| y+1   	|
| TURN LEFT      	| NORTH 	| SOUTH 	| WEST  	| EAST  	|
| TURN RIGHT     	| SOUTH 	| NORTH 	| EAST  	| WEST  	|
