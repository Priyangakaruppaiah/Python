# Linear search in python
def search(List, n):
    for i in range(len(List)):
        if List[i] == n:
            return True
    return False
list=['3','4','sun','7','87','sky']
n='sun'
if search(list,n):
    print("Found")
else:
    print("Not Found")
