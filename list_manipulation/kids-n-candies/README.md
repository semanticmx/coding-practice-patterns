# Kids with Candies

Given a list of children candies, verify whether adding
extra candies results in a child having most or equal candies
than any other child.

## Challenges

1. Loop over children list
2. Loop every child's candies over every other children's candies.
3. Get max candies

## Edge Cases


## Approach


## Optimized approach

1. On already calculated values, reuse (cache)
2. Reduce time complexity

## Take Away

1. Traverse for-loop using two opposite indices
2. max() allows to set the maximum value between a set
   3. max_value = 0
   4. max_value = max(max_value, ....)
5. Init a set of default values
   6. defaults = [1] * 10 