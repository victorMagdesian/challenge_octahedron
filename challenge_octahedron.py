def fact(n):
    fact = 1
  
    for i in range(1,n+1): 
        fact = fact * i 
    
    return fact

def unique_combination(n,k):
    return fact(n)/fact(k)*fact(n-k)

def calculate_num_of_tetra_formed_with_octa_vert():
    print(unique_combination(6,5))

def calculate_num_of_tetra_formed_with_octa_vert_plus_centers():
    print(unique_combination(14,5))

print("Select one:\n")
print("for the number of tetrahedrons constructed with only octahedron vertices input 1.\n")
print("for the number of tetrahedrons constructed with octahedron vertices + shapes center input 2.")

inputVar = input()

if(inputVar == "1"):
    calculate_num_of_tetra_formed_with_octa_vert()
elif(inputVar == "2"):
    calculate_num_of_tetra_formed_with_octa_vert_plus_centers()
else:
    print("invalid input")