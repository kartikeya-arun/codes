guest_name=input()
residence_host_name=input()
letter_pile=input()

sorted_LHS=sorted(list(guest_name)+list(residence_host_name))

if(sorted_LHS==sorted(list(letter_pile))):
    print('YES')
else:
    print('NO')


# ONE LINER

# print('YES') if sorted(list(input())+list(input()))==sorted(list(input())) else print ('NO')