# 1. Create two matrices of the same layout and test if addition and subtraction of the matrix works as expected: C = A + B
x = [1 2 0 5; 0 6 7 -9]
y = [5 -7 3 8; 2 1 3 4]
print(x-y)
print(x+y)

# 2. Now compare matrix multiplication either this way A * B and this way A .* B. Whats the difference?!
print(x.*y) # works as expected
print(x*y) # multiplis array and int, but not two multidimensional elements

# 3. What about matrix division with "/" or "\"?!
print(x/y) # works as expected, divides the first operand by the second
print(x\y) # Division (Inverse), divides the second operand by the first

# 4. Create a 3x3 integer matrix A with useful numbers. Now try A+1, A-1, A*2, A/2.
A = [1 2 3;0 2 9; 7 5 6]
print(A.+1) # needs fixing + -> .+
print(A.-1) # needs fixing - -> .-
print(A*2) # same result for * and .*
print(A/2) # same result for * and .*

# 5. Now multiply a 3x4 matrix with a suitable (4)vector.
x = [1 2 3;0 2 9; 7 5 6; 2 8 4]
y = (0, 3, 8, 3)
print(x.*y) # .* can multiply a matrix and vector of suitable dimensions, * can not