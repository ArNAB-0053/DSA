### basic intuition - 
- initialize an empty stack
- loop through the tokens
- if encounter an number add to stack
- if it is an operator
	- pop two element
	- perform the operation
	- append that into stack
- follow the same steps until you get end of the tokens
- return the last element of stack