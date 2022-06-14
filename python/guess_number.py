import random as rd
# def guess_number(x):
#     name =input("Whats ur name :")
#     greeting=f"Well,{name},I am thinking of a number between 1 and {x}"
#     print(greeting)
#     computer_num=rd.randint(1,x)
#     guess_num=0
#     while computer_num != guess_num:
#         guess_num=int(input("Take a guess:"))
#         if guess_num>computer_num:
#             print(f"{guess_num} is too high!! Try again")
#         elif guess_num < computer_num:
#             print(f"{guess_num} is too low!! Try again")
#         else :
#             print(f"{guess_num} is right answer")
#             break
# guess_number(10)

def computer_guess(x):
    lowwer=1
    higher=x
    feedback=''
    while feedback != 'c' and lowwer !=higher:
        if lowwer != higher:
            guess_num=rd.randint(lowwer,higher)
        else:
            guess_num=lowwer    
        feedback=input(f'Is{guess_num} too high(H),too low(L),or correct(c)')
        if feedback== 'h':
           higher=guess_num-1
        elif feedback =='l':
           lowwer=guess_num+1
        else :
            print(f"{guess_num} is right answer")
            break
computer_guess(10)
