card_no=int(input("card no. "))
empty=''
if card_no>=1000000000000000 and card_no<=9999999999999999:
    cal=str(card_no)
    # empty=''
    i=0
    while i<len(cal):
        if i%2==0:
            digit=int(cal[i])*2
            if digit>9:
                sum=0
                while digit>0:
                    last=digit%10
                    sum+=last
                    digit=digit//10
                empty+=str(sum)
            else:
                empty+=str(digit)
        else:
            empty+=cal[i]
        i+=1
else:
    print("not valid")
if empty!='':
    total=0
    i=0
    while i<len(empty):
        total+=int(empty[i])
        i+=1
    if total%10==0:
        print("valid card no.")
    else:
        print("not valid")
# print(empty)
# print(total)