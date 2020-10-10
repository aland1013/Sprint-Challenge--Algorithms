#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The runtime of this is O(n) because the number of operations increases directly in proportion to the size of n. Although the loop involves an upper limit of n^3, it increments by n^2, and n^3/n^2 = n. For example, with n = 2, teh while loop runs twice. If we double n to n = 4, the number of times the loop runs doubles to 4, also. If we again double n to n = 8, the loop runs 8 times. This shows O(n) runtime.

b) The runtime of this is O(n^2) because the big O notation for the outer loop is O(n), and the big O notation for the inner loop is O(n). When loops are nested, we multiply their big O notations together, which gives us O(n) \* O(n) = O(n^2)

c) The runtime of this is O(n), because the number of operations performed for the base case is a constant (1), and the number of recursive calls made will be n - 1. The big O for a constant is O(1) and the big O for the recursive calls is O(n - 1) => O(n). We can disregard the O(1) runtime because it is overwhelmed by O(n).

## Exercise II

This problem is well suited for a binary search algorithm, which has a runtime of O(log n):

To find floor f, start by calculating the floor halfway between the ground floor and the highest floor (n). Set this equal to middle.

Go to floor middle and drop an egg. If the egg breaks, descend one floor and drop another egg. If it does not break, then we know that f is equal to middle. If it does break, then we know that f must be somewhere between the floor we are on (middle - 1) and the ground floor. We can consider the floor we are on the new n, calculate a new middle, descend to it, and drop another egg, repeating the process desribed here. If the first egg we dropped did not break, we know that f must be somewhere between the floor above the one we are on and n. We can consider the floor above us the new ground floor, calculate a new middle, ascend to it, and drop another egg, repeating the process described here. Eventually we will reach a floor where the egg dropped from it breaks, and the egg dropped from the floor below it does not, revealing floor f.

Each time we repeat this process of climbing or descending to middle and dropping an egg, we can eliminate half of the floors in the building, just like with a binary search we can eliminate half of the remaining list with each iteration. This results in a runtime of O(log n).
