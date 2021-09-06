### data storage

i think ideally, because of the tree-like nature of chess games, we should use JSON to store things.

of course, this means that i have to figure out how to cleanly convert to JSON. 

### starting from nothing

we have a list of starting FENs for fischerrandom. when we're starting as white, we want to calculate the best move for starting. when we're starting as black, we want the ten most common moves for each opening. of course, this implies... 960 times 10 moves. 9600 moves, just in the opening!

of course, this was the purpose of fischerrandom: making opening theory not worth studying!

however, there's a problem with this idea: i don't think anyone ever really calculated the benefit from 

1) doing what i proposed above, vs.
2) studying a certain amount of tactics moves using the same amount of time and energy

it might turn out that (1) increases ones' rating more than (2)!
i'm assuming, of course, that memorizing 960 best moves for white, 1 for each unique position, is easy because most of those will be the same!