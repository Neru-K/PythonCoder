S=list(input())
if S[0]==S[1]==S[2] or S[1]==S[2]==S[3] or S[2]==S[3]==S[4] :
  if S[2]=='o':
    print('o')
  else:
    print('x')
else:
  print('draw')