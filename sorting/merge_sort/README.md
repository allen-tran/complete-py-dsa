# Merge Sort

- Time complexity: O(Nlog(N))

This is a divide and conquer sorting algorithm that first divides all of the arrays into subararys of size 1. Once the length is of size one, we then use a three pointer approach where we make the i'th element in the array be the greater of the two subarrays at their respective pointers. Make sure to increment the pointers appopriately. At the end we need to make sure there is nothin left insider of the arrays so we another two seperate while loops that clears the rest of the subrarays.