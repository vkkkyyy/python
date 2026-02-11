# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)

def simple_interst(principal ,rate ,time):
    si= (principal * rate* time)/100
    print(f"simple interestis {si}")
simple_interst(45000,7,8)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.
interest =[
    (3000,7,6)
    (53279,7,4)
]
for p,r,t in interest:
    simple_interst(p,r,t)