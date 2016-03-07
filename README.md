# Factors and Multiples with Caching

### Using this Script
This program will take integers from the command line as parameters and will then print two different mappings. The first one will print each value of the input and the corresponding numbers (also from the input) that are a factor of it. The second one will print each value of the input and corresponding numbers (also from the input) of which it is a factor of.

Run the script with:
```
python3 factors.py 10 5 2 30
```
This will produce the following output:
```
Factors: {2: [], 10: [2, 5], 30: [2, 5, 10], 5: []}
Multiples: {2: [10, 30], 10: [30], 30: [], 5: [10, 30]}
```

### Notes
1.  The cache is a mapping of input arrays to the corresponding output array
    The keys are the input arrays sorted in ascending order and the values are 
    the maps of each value in the input to its factors which are in the input
2.  N is the number of elements in the input array
    The sorting of the input list takes N*logN time
    If the input is in the cache then the operation is done, this takes constant time
    Otherwise it enters the nested for loop which takes N(N+1)/2 time which is equivalent to N^2
    The time it takes to cache a result is constant locally
    Therefore in the worst case in which the input isn't in the cache it would be O(N^2)
        in the best case the input would be cached the run time would be O(N*logN)
3.  To reverse the functionality the caching algorithm would be the same, in the map
    the input array would be the key and the corresponding output would be in a different
    but would still be the value. You would however need to change how you calculated the
    output.