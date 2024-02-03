<a name="br1"></a> 
Assignment Report

##### Assignment 01

### Name : Aasritha Reddy SG

#### Reg No : AIE22144

##### SET B : QUESTION 01

**Pseudo Code**

function VowelOrConsonant(word):
    vowel_count = 0
    consonant_count = 0
    letters = empty list
    
    for i in word:
        append i to letters
        if i is a vowel:
            increment vowel_count by 1
        else:
            increment consonant_count by 1
    
    print("the total number of vowels are:", vowel_count)
    print("the total number of consonants are:", consonant_count)

user_word = input("Enter any word of your choice: ")
VowelOrConsonant(user_word)

<a name="br2"></a> 

### Code Explanation :

The above Python code deﬁnes a funcꢀon, “count\_vowel\_consonants”, to count the number
of vowels and consonants in a given input string. It iterates through each character of the
string, checks if it's an alphabet, then determines whether it's a vowel or a consonant. The
`main` functonality prompts the user for an input string, calls `count\_vowel\_consonants`, and
prints the counts of vowels and consonants.

##### SET B : QUESTION 02


**Pseudo Code**

function matrixMultiplication(A, B):
    output = empty list
    for i in range(length of A):
        row = empty list
        for j in range(length of B[0]):
            multiplied_value = 0
            for k in range(length of B):
                multiplied_value += A[i][k] * B[k][j]
            append multiplied_value to row
        append row to output
    return output

matA = empty list
matB = empty list

rowA = input("Enter the number of rows of Matrix A: ")
columnA = input("Enter the number of columns of Matrix A: ")

print("Enter the values inside the matrix A:")
for a in range(rowA):
    temp_a = empty list
    for b in range(columnA):
        values = input()
        append values to temp_a
    append temp_a to matA

rowB = input("Enter the number of rows of Matrix B: ")
columnB = input("Enter the number of columns of Matrix B: ")

print("Enter the values inside the matrix B:")
for a in range(rowB):
    temp_b = empty list
    for b in range(columnB):
        values = input()
        append values to temp_b
    append temp_b to matB

if columnA != rowB:
    print("Error: The two matrices cannot be multiplied")
else:
    result = matrixMultiplication(matA, matB)
    print(f"The final product of the two matrices is: {result}")


Code Explanation :
The code deﬁnes a function “multiplymatrices” to compute the product of two matrices. It
checks if the matrices for mulꢀplicaꢀon, iniꢀalizes the product matrix, and performs matrix
multiplication using nested loops. The code takes user input to create two
matrices, computes their product, and prints the result. Finally, it ensures that the `main`
functionality is executed only when the script is run directly.

#### SET B : QUESTION 03

**Pseudo Code**
function CommonElements(A, B):
    common_elements = empty list
    for i in A:
        for j in B:
            if i is equal to j:
                append i to common_elements
    
    return common_elements

listA = empty list
listB = empty list

sizeA = input("Enter the size of listA: ")
sizeB = input("Enter the size of listB: ")

print("Enter the values in list A:")
for a in range(0, sizeA):
    valuesA = input()
    append valuesA to listA

print(f"List A elements: {listA}")

print("Enter the values in list B:")
for b in range(0, sizeB):
    valuesB = input()
    append valuesB to listB

print(f"List B elements: {listB}")

common_elements_result = CommonElements(listA, listB)
print(f"The common elements are: {common_elements_result}")


<a name="br4"></a> 

### Code Explanation :

the main objective is to find the common elements between two lists. To do that I have used a functions in which two `for` loops iterate over the elements of the lists and if any similiarty found it appends it into a `common_lists` list. Thus giving us a collection of common lists.

### SET B : QUESTION 04

**Pseudo Code**
Deﬁne a funcꢀon named transpose\_matrix which takes a matrix as input
Get the number of rows and columns in the matrix
Intilialize a matrix to store the transposed matrix
Iterate through each element of the matrix and transpose it
Return the transposed matrix
Deﬁne a funcꢀon named main
Prompt the user to input the dimensions of the matrix
Prompt the user to input elements for the matrix
Compute the transpose of the matrix using the transpose\_matrix funcꢀon
Print the original matrix
Print the transpose of the matrix
Check if the '\_\_name\_\_' is equal to '\_\_main\_\_'
If it is equal, call the main funcꢀon

### Code Explanation :
The above code deﬁnes a funcꢀon “transpose\_matrix”to compute the transpose of a given
matrix. It iterates through each element of the matrix and transposes it. The `main` funcꢀon
prompts the user to input the dimensions and elements of the matrix, computes its
transpose using “transpose\_matrix”, then prints both the original and transposed matrices.
Finally, it ensures that the `main` funcꢀon is executed only when the script is run directly.

<a name="br5"></a> 


