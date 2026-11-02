A=[3,2,1]
B=[]
C=[]
def hanoi(n,s,t,h):
  if n==0:
    return
  hanoi(n-1,s,h,t)
  t.append(s.pop())
  print("A:",A,"B:",B,"C:",C)
  hanoi(n-1,h,t,s)

print("Initial:",A,B,C)
hanoi(3,A,C,B)
