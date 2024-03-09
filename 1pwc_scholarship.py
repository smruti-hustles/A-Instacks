'''
pwc ccr-py micro certification question
input - two strings first string takes ids of students separated by commas. second string takes ids of students who got scholarships separated by commas. 
output - student ids who do not have scholarship
'''
'''
You are tasked with implementing a function called "scholarship" that takes two comma-separated strings as input. The first string contains all student IDs, and the second string contains the IDs of students who have received scholarships. The function should return a comma-separated string of student IDs who do not have scholarships. If all students have scholarships or the input data is invalid, appropriate messages should be returned.

Write the check_scholarships function and a main function to demonstrate its usage by taking user input.

Input Format:

The main function prompts the user to input two comma-separated strings.
The first string contains all student IDs.
The second string contains the IDs of students who have received scholarships.
Output Format:

The main function prints the result, which is a comma-separated string of student IDs who do not have scholarships.
input
Enter all student IDs separated by commas: 1,2,3,4,5
Enter scholarship recipient IDs separated by commas: 2,4

output
Students without scholarships: 1,3,5
'''
def scholarship(s1,s2):
    p=s1.split(",")
    q=s2.split(",")
    if(len(p)<len(q)):
        return "Invalid Input"
    result=[i for i in p if i not in q]
    if not result:
        return "All students have scholaship"
    return f"Students without scholarships: {','.join(result)}"
def main():
    l1=input()
    l2=input()
    sc=scholarship(l1,l2)
    print(sc)
if __name__ == "__main__":
    main() 
