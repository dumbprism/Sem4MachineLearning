### NAME : KOTAMRAJU ARHANT
### ROLL NUMBER : AIE22123

### ASSIGNMENT REPORT

---
do check out my teammates github accounts
1. Naveen(AIE221115) : [https://github.com/GanganapalliNaveen]
2. Aashritha(AIE22144) : [https://github.com/aasritha22144]

####  SET A: QUESTION 01

###### Pseudo Code

```plaintext
Input : target
function Pairs(List,pairs)

for i  = 0 to len(list)
    for j = i+1 to len(list)
        if List[i] + List[j] == target then
            found_pair -> List[i] + List[j]
            append found_pair to list pairs
        End if
        for k = i+2 to len(list)
            if List[i] + List[j] + List[k] == target:
                found_pair -> List[i] + List[j] + List[k]
                append found pair to list pairs
        End for
    End for
End for

user_list -> create empty list()
Input :  n -> size of the list
Print enter the values of the list

for a = 0 to n 
    values -> Input : entering the values
    append the values in the user_list list
Print user_list
pairs -> create empty list()
Pairs(user_list,pairs)
```

**Code Explanation :** 

The main objective of the question is to find pairs that give us a specified target sum. In this case it is 10. To attain that, the approach that I have used is that, I shall first be finding pairs that produce the the sum as 10 when two numbers are added. to do that I have implemented 2 `for` loops. The ranges are set set as per the length of the list for the outer loop 'i' and `i+1` to `length-1` for the inner loop 'j'. So basically, the elements shall be stored in the list. Here is the pictorial representation of what will happen : 
![[Pasted image 20240203092303.png]]

'i' shall iterate the `if` conditions help in finding if the sum is 10 or not. But since we are considering the complete list, we must also see if there are pair of three that form a sum of 10 and indeed there are. Thus, I have used another `for` loop, from range `i+2` to `length of the list` to find pair of three.

Overall, to not be bound to only one list as per the question, I have made sure that the user inputs the elements inside the list and they themselves set a target value by which the complete code shall work.


### SET A: QUESTION 02

###### Pseudo Code

```plaintext

function findingrange(List):
    for i = 0 to length(List):
        for j = i+1 to length(List):
            if List[i]  > List[j] : 
                temp = List[i]
                List[i] = List[j]
                List[j] = temp
            End if
        End for
    End for

    computed_range -> List[n-1] - List[0]
    if computed_range < 0 then
        print("Error : the range cannot be computed...")
    print(f"the range of the List is {computed_range}")

    userList = empty List
    n -> Input : Enter the size of the list
    for a = 0 to n do 
        value -> Input : enterin the ath value of the list
        append value to userList
    
    findingRange(userList)

```

**Code Explanation**

The main objective of the question is to find the range of a user input list. To do so we first understand how range works. The working of range is quite simple where the maximum and the minimum value are subtracted, thus we obtain the range. To attain the range now, we first take in elements in the list and we sort them in ascending order. The sorting is done through the method of `bubble sort` technique, where two consecutive elements are compared and if one element is greater than the other they swap positions. After few iterations of swapping we come up with a ordered list. This makes it easy for us to now compute the range. The minimum value element will be in the first position of the list and the maximum value element will be in the last position of the list. Thus we we pick only those two elements and come up with the final range of the list.


### SET A: QUESTION 03


###### Pseudo Code

```
plaintext
function matrix_mult(A, B):
    result -> empty list
    for i from 0 to length(A) - 1 do 
        rows -> empty list
        for j from 0 to length(B[0]) - 1 do 
            mul_value = 0
            for k from 0 to length(B) - 1 do
                mul_value = mul_value + A[i][k] * B[k][j]
            append sum_value to rows
        append rows to result
    return result

function power_mult(A, m):
    result = copy of A
    for l from 0 to m - 2:
        result = matrix_mult(result, A)
    return result

function Matrix():
    rows = input("Enter the rows of the matrix = ")
    columns = input("Enter the columns of the matrix = ")
    A = empty list

    print("Enter the values inside the matrix:")
    for a from 0 to rows - 1:
        row = empty list
        for b from 0 to columns - 1:
            value = input()
            append value to row
        append row to A

    print(A)

    for row in A:
        print(row)

    m = input("Enter the power to be applied to the matrix: ")

    output = power_mult(A, m)

    print(output)
```

**Code Explanation**

The question's main objective is to find A^m. Where A is a matrix and m is the power given to it. To attain that, we have split our question into three functionalities. WE first have to understand how matrix multiplication works between two Lists in python. Thus, we have created a function that finds the multiplicative form of two lists. we first create an empty list `result` that shall store all the values attained after multiplication in row-wise order. The implementation of 3 `for` loops is mandatory since that shall help us give the right answer. We use a temporary list `row` that stores the row wise multiplicative values and then appends it inside the `result` list. We also take a temporary `mul_value` variable that multiplies the elements inside the list. THe inner most `for` loop is responsible for the multiplication of of the elements where the ith and the kth elements of a list are multiplied by the jth and the kth element of the other list. 


### SET A: QUESTION 04

###### Pseudo Code

```plaintext
  Get user input for a word and store it in the variable 'word'.
 Initialize variables: 
   count = 0
   max_count = 0
   frequent_letter = ''
   letters_list = empty list

 Iterate through each character (a) in the input word:
   Append the character 'a' to the 'letters_list'.

  Display the 'letters_list'.

Iterate over the range of the length of 'letters_list' using variable 'i':
   Set 'count' to 1.

   Iterate over the range (j) from (i + 1) to the length of 'letters_list':
       Check if 'letters_list[i]' is equal to 'letters_list[j]':
           Increment 'count' by 1.
           If 'count' is greater than 'max_count':
               Update 'max_count' to 'count'.
               Update 'frequent_letter' to 'letters_list[i]'.

Display the most occurring letter and its count:
   Display "The most occurring letter is: " followed by 'frequent_letter'.
   Display the occurrence count of the most occurring letter.

```

**Code Explanation**

The question's main objective is the find the most repetitive letter in a word. The approach was quite straightforward where I tried to break down the word and store it inside as an individual element each. To check for the maximum count I initialized a variable `max_count` . I also have implemented a count variable that resets to the value of 1 after every iteration and updates the `max_count` also. if the the `count` variable is greater than the `max_count` variable, the max_count's value changes to the count's value. to display the most occurring letter I have also implemented a `frequent_letter` variable that initially is an empty string but in the later period switches based on the most occurring letter. 
