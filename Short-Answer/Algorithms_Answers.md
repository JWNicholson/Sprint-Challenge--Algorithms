#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n) - it constantly grows depending on input size


b)O(n^2) - the two nested loops


c)O(n) - the time increases with the input number

## Exercise II

stories  = n
stories greater than or equal to f, egg = broken
stories less than f, egg = not broken

Starting on floor 0. Drop the egg and check if it is broken.

If it is NOT broken, move the egg to the next highest floor.

Drop the egg and see if it is broken.

Keep doing this until you reach a floor where the egg breaks.

return that floor number

Runtime - O(n), because only recurses n times (the number of floors)

