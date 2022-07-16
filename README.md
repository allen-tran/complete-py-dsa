# Complete Handbook for DSA Solutions in Python 🐍

A complete repository containing data structure implementations and LeetCode solutions. This can be used as a handbook to reference and learn these implementations in depth and a guide to study for interviews. Each python file follows the [pycodestyle](https://pypi.org/project/pycodestyle/) style guide.

Please feel free to reference and star to support this repo, thank you!

![image](https://user-images.githubusercontent.com/63386979/170837571-cc97bcc9-5faa-4c4a-b227-ea354f1b2160.png)

## LeetCode Solutions ✅

LeetCode is an online algorithm judging platform for engineers and mathmatcians to practice their problem solving abilities. Practicing LeetCode is known to help with passing technical interviews and can greatly increase algorithmic skills. Each solution is paired with a test file and README to understand the solution and overall problem. See below for an updated list of the solved problems in this repo.

![image](https://user-images.githubusercontent.com/63386979/170784722-7d7ce744-943a-41b1-9870-99deb5c4068a.png)

### Algorithm Table — [19] Solved

| No.| Title| Solution | Complexity  | Difficulty |
| :--: | :--------------------------------------------- | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------: | :--------: |
| 0001 | Two Sum| [Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0001.two_sum/two_sum.py) |    O(N)     |    Easy    |
| 0003 | Longest Substring without Repeating Characters | [Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0003.longest_substring_without_repeating_characters.py/longest_substring_without_repeating_characters.py) | O(N)     |   Medium   |
| 0004 | Median of two Sorted Arrays|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0004.median_of_two_sorted_arrays/median_of_two_sorted_arrays.py)| O(log(M+N)) |    Hard    |
| 0011 | Container with Most Water|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0011.container_with_most_water/container_with_most_water.py)|    O(N)     |   Medium   |
| 0014 | Longest Common Prefix|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0014.longest_common_prefix/longest_common_prefix.py)| O(Nlog(N))  |    Easy    |
| 0028 | Implement strStr()|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0028.implement_strStr/implement_strStr.py)|    O(N)     |    Easy    |
| 0049 | Group Anagrams|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0049.group_anagrams/group_anagrams.py)| O(Nlog(N))  |   Medium   |
| 0051 | N-Queens |[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0051.n_queens/n_queens.py) |   O(N^2)    |    Hard    |
| 0053 | Maximum Subarray|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0053.maximum_subarray/maximum_subarray.py)|    O(N)     |    Easy    |
| 0054 | Spiral Matrix|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0054.spiral_matrix/spiral_matrix.py)| O(M+N)     |    Medium    |
| 0056 | Merge Intervals |[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0056.merge_intervals/merge_intervals.py)|    O(Nlog(N))     |    Medium    |
| 0058 | Length of Last Word|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0058.length_of_last_word/length_of_last_word.py)|    O(N)     |    Easy    |
| 0094 | Binary Tree Inorder Traversal|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0094.binary_tree_inorder_traversal/binary_tree_inorder_traversal.py)|    O(N)     |    Easy    |
| 0125 | Valid Palindrome |[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0125.valid_palindrome/valid_palindrome.py)|    O(N)     |    Easy    |
| 0155 | Min Stack |[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0155.min_stack/min_stack.py)|    O(1)     |    Medium    |
| 0207 | Course Schedule|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0207.course_schedule/course_schedule.py)|    O(V+E)     |    Medium    |
| 0217 | Contains Duplicate|[Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0217.contains_duplicate/contains_duplicate.py)|    O(N)     |    Easy    |
| 0257 | Binary Tree Paths                              |                               [Py](https://github.com/allen-tran/complete-py-dsa/blob/main/leetcode/0257.binary_tree_paths/binary_tree_paths.py)                               |    O(N)     |    Easy    |

---

## Data Structures 🏛

Data Structures or `DS` are key to understanding the fundmentals of programming. They teach us how data is stored, retrieved, and updated. Each data structure implementation comes with a test file as well as a README to reinforce the learnings.

![image](https://user-images.githubusercontent.com/63386979/170795648-48bc2167-7dd7-4118-a8de-79b06f629ff5.png)

In this repository, the following data structures are implemented:

1. [Linked List](https://github.com/allen-tran/complete-py-dsa/blob/main/data%20structures/linked%20list/linked_list.py)
2. [Weighted Graph](https://github.com/allen-tran/complete-py-dsa/blob/main/data%20structures/graph/weighted_graph.py)
3. [Trie]()

---

## Operations

Python comes pack with various cool methods and operations that all time different amounts of time. Here is a list of all of the standard python method's and their respective time complexities. Refer to this to brush up on your knowledge of python's standard library.

### Lists

| Operation     | Example      | Class         | Notes |
--------------|--------------|---------------|-------------------------------
Index         | l[i]         | O(1)	         |
Store         | l[i] = 0     | O(1)	         |
Length        | len(l)       | O(1)	         |
Append        | l.append(5)  | O(1)	         | mostly: ICS-46 covers details
Pop	          | l.pop()      | O(1)	         | same as l.pop(-1), popping at end
Clear         | l.clear()    | O(1)	         | similar to l = []
Slice         | l[a:b]       | O(b-a)	       | l[1:5]:O(l)/l[:]:O(len(l)-0)=O(N)
Extend        | l.extend(...)| O(len(...))   | depends only on len of extension
Construction  | list(...)    | O(len(...))   | depends on length of ... iterable
check ==, !=  | l1 == l2     | O(N)          |
Insert        | l[a:b] = ... | O(N)	         | 
Delete        | del l[i]     | O(N)	         | depends on i; O(N) in worst case
Containment   | x in/not in l| O(N)	         | linearly searches list 
Copy          | l.copy()     | O(N)	         | Same as l[:] which is O(N)
Remove        | l.remove(...)| O(N)	         | 
Pop	          | l.pop(i)     | O(N)	         | O(N-i): l.pop(0):O(N) (see above)
Extreme value | min(l)/max(l)| O(N)	         | linearly searches list for value
Reverse	      | l.reverse()  | O(N)	         |
Iteration     | for v in l:  | O(N)          | Worst: no return/break in loop
Sort          | l.sort()     | O(N Log N)    | key/reverse mostly doesn't change
Multiply      | k*l          | O(k N)        | 5*l is O(N): len(l)*l is O(N**2)


### Sets

|Operation     | Example      | Class         | Notes|
--------------|--------------|---------------|-------------------------------
Length        | len(s)       | O(1)	     |
Add           | s.add(5)     | O(1)	     |
Containment   | x in/not in s| O(1)	     | compare to list/tuple - O(N)
Remove        | s.remove(..) | O(1)	     | compare to list/tuple - O(N)
Discard       | s.discard(..)| O(1)	     | 
Pop           | s.pop()      | O(1)	     | popped value "randomly" selected
Clear         | s.clear()    | O(1)	     | similar to s = set()
Construction  | set(...)     | O(len(...))   | depends on length of ... iterable
check ==, !=  | s != t       | O(len(s))     | same as len(t); False in O(1) if the lengths are different
| <=/<          | s <= t       | O(len(s))     | issubset |
| >=/>          | s >= t       | O(len(t))     | issuperset s <= t == t >= s |
| Union         | s | t        | O(len(s)+len(t)) |
Intersection  | s & t        | O(len(s)+len(t))
Difference    | s - t        | O(len(s)+len(t))
Symmetric Diff| s ^ t        | O(len(s)+len(t))
Iteration     | for v in s:  | O(N)          | Worst: no return/break in loop
Copy          | s.copy()     | O(N)	     |


### Dictionaries: Dict and Defaultdict

Operation     | Example      | Class         | Notes
--------------|--------------|---------------|-------------------------------
Index         | d[k]         | O(1)	     |
Store         | d[k] = v     | O(1)	     |
Length        | len(d)       | O(1)	     |
Delete        | del d[k]     | O(1)	     |
get/setdefault| d.get(k)     | O(1)	     |
Pop           | d.pop(k)     | O(1)	     | 
Pop item      | d.popitem()  | O(1)	     | popped item "randomly" selected
Clear         | d.clear()    | O(1)	     | similar to s = {} or = dict()
View          | d.keys()     | O(1)	     | same for d.values()
Construction  | dict(...)    | O(len(...))   | depends # (key,value) 2-tuples
Iteration     | for k in d:  | O(N)          | all forms: keys, values, items, Worst: no return/break in loop
                                 
---

## Helpful Resources

1. [Competitive Programming Handbook](https://cses.fi/book/book.pdf) 
2. [Grokking the Coding Interview](https://www.educative.io/courses/grokking-the-coding-interview?utm_term=grokking%20the%20coding%20interview&utm_campaign=%5BTest%5D+Dynamic+Verticals&utm_source=adwords&utm_medium=ppc&hsa_acc=5451446008&hsa_cam=14045073269&hsa_grp=135456430042&hsa_ad=584258867265&hsa_src=g&hsa_tgt=kwd-586801686237&hsa_kw=grokking%20the%20coding%20interview&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAjwtcCVBhA0EiwAT1fY7xaJyIJazvftqXqJyyMzJp7i3G2wzSYPb_Nj67kkPmJjaRsd0HBXNRoCm3EQAvD_BwE)
3. [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850/ref=sr_1_1?gclid=CjwKCAjwtcCVBhA0EiwAT1fY71Ez2P-ZkrUdleKX8FISOCjMPArC0tBchKPS4wR7WOAEv654sC0wMxoCTn0QAvD_BwE&hvadid=241871347365&hvdev=c&hvlocphy=9028770&hvnetw=g&hvqmt=b&hvrand=11460318510657825342&hvtargid=kwd-299613214513&hydadcr=16435_10305567&keywords=cracking+the+coding+interview+book&qid=1655785687&sr=8-1)
