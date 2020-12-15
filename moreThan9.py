#dictionary for words of main numbers
number_dict= dict()
number_dict = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight',
'9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen',
'17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty','30':'thirty','40':'fourty','50':'fifty','60':'sixty',
'70':'seventy','80':'eighty','90':'ninety','100':'one hundred'}

def number_to_word(pos,number='0',list=None,add_zero=False,string=''):
    if number[pos]!='0': #getting words only if the number is non-zero
        if add_zero:
            num=number[pos]+'0'
        else:
            num=number[pos]
        num_words=number_dict[num] + string
        list.append(num_words)

def teen_check(pos2,pos1,number='0',list=None,string=''):
        num=number[pos2]+number[pos1]
        num_words=number_dict[num] + string
        list.append(num_words)

while True:
    number = input('\nWrite the number:')

    #for numbers with commas
    if ',' in number:
        number=number.replace(',','')

    #sanity check
    try:
        int(number)
    except:
        print('Put a valid number!')
        continue

    #checks for an input with starting value 0,
    number=number.lstrip('0')

    if len(number) >13:
        print('Put a valid number!')
        continue

    #checks for an input with multiple 0s like 0000 or 00 or 00

    if len(number)<1:
        print('zero')
        continue
    else:
         pass

    words=list()
    number_len=len(number)

    #checks if the number is already present in our dictionary otherwise passes on for more processing
    try:
        words.append(number_dict[number])
        found=True
    except:
        found=False
        pass

    #word assigning code block
    if not found:
        while True:
            # print(len(number))
            try: #checks if the tens and ones place is a teen number
                teen_check(-2,-1,number,words)
                if number_len == 2:break
            except:
                number_to_word(-1,number,words)
                number_to_word(-2,number,words,True)
                if number_len ==2:break #for two digit number

            number_to_word(-3,number,words,False,' hundred')
            if number_len ==3:break#for three digit number

            try: #checks if the  ten-thousandth and thousandth place is a teen number
                teen_check(-5,-4,number,words,' thousand')
                if number_len == 5:break

            except:
                number_to_word(-4,number,words,False,' thousand')
                if number_len ==4:break #for four digit number
                number_to_word(-5,number,words,True)
                if number_len ==5:break #for five digit number

            try: #checks if the  ten-lakhth and lakhth place is a teen number
                teen_check(-7,-6,number,words,' lakh')
                if number_len == 7:break

            except:
                number_to_word(-6,number,words,False,' lakh')
                if number_len ==6: break #for six digit number
                number_to_word(-7,number,words,True)
                if number_len ==7: break #for seven digit number


            try: #checks if the  ten-croreth and croreth place is a teen number
                teen_check(-9,-8,number,words,' crore')
                if number_len == 9:break

            except:
                number_to_word(-8,number,words,False,' crore')
                if number_len ==8: break #for eight digit number
                number_to_word(-9,number,words,True)
                if number_len ==9: break #for nine digit number

            try:
                teen_check(-11,-10,number,words,' arab')
                if number_len == 11 : break
            except:
                number_to_word(-10,number,words,False,' arab')
                if number_len== 10: break
                number_to_word(-11,number,words,True)
                if number_len== 11: break

            try:
                teen_check(-13,-12,number,words,' kharab')
                if number_len==13:break
            except:
                number_to_word(-12,number,words,False,' kharab')
                if number_len==12:break
                number_to_word(-13,number,words,True)
                if number_len == 13:break


    pos=-1
    # print(words)
    for times in range(len(words)):
        print(words[pos],end=' ')

        pos=pos-1
    print('')
