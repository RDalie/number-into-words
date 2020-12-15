#dictionary for words of main numbers
number_dict= dict()
number_dict = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight',
'9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen',
'17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty','30':'thirty','40':'fourty','50':'fifty','60':'sixty',
'70':'seventy','80':'eighty','90':'ninety','100':'one hundred'}

while True:
    number_input = input('\nWrite the number:')

    #checks for an input with starting value 0,multiple 0s like 0000 or 00 or 00
    number_input=number_input.lstrip('0')
    if len(number_input)<1:
        print('zero')
        continue
    else:
         pass

    #dividing a number into two parts if greater than 9 digits
    parts=list()
    if len(number_input)>9:
        number_part1=number_input[-7:]
        parts.append(number_part1)
        number_part2=number_input[:-7]
        parts.append(number_part2)
    else:
        parts.append(number_input)
    # print(number_part1,number_part2)

    words=list()
    number_len=len(number_input)
    times=1
    # print(parts)
    #looping through 1 or 2 parts
    for number in parts:
        # print(number)
        #checking if a divided number consists of zeroes only
        number=number.lstrip('0')
        if len(number)<1:
            times=times+1
            continue
        else:
             pass

        #word check for the 2nd part of the number
        if times==2:
            words.append('crore')

        #checks if the number is already present in our dictionary otherwise passes on for more processing
        try:
            words.append(number_dict[number])
            found=True
            continue
        except:
            found=False
            pass


        number_len=len(number)
        #word assigning code block
        if not found:
            while True:
                # print(len(number))
                try: #checks if the tens and ones place is a teen number
                    ones=number[-2]+number[-1]
                    ones_words=number_dict[ones]
                    words.append(ones_words)
                    if number_len == 2:break
                except:
                    if number[-1]!='0': #getting words only if the number is non-zero
                        ones=number[-1]
                        ones_words=number_dict[ones]
                        words.append(ones_words)

                    if number[-2]!='0':
                        tens=number[-2]+'0'
                        tens_words=number_dict[tens]
                        words.append(tens_words)
                        if number_len ==2:break #for two digit number

                if number[-3]!='0':
                    hundreds=number[-3]
                    hundreds_words=number_dict[hundreds]+' hundred'
                    words.append(hundreds_words)
                    if number_len ==3:break#for three digit number

                try: #checks if the  ten-thousandth and thousandth place is a teen number
                    ten_thousands=number[-5]+number[-4]
                    ten_thousands_words=number_dict[ten_thousands] + ' thousand'
                    words.append(ten_thousands_words)
                    if number_len == 5:break

                except:
                    if number[-4]!='0':
                        thousands=number[-4]
                        thousands_words=number_dict[thousands]  + ' thousand'
                        words.append(thousands_words)
                        if number_len ==4:break #for four digit number

                    if number[-5]!='0':
                        ten_thousands=number[-5] + '0'
                        ten_thousands_words=number_dict[ten_thousands]
                        words.append(ten_thousands_words)
                        if number_len ==5:break #for five digit number

                try: #checks if the  ten-lakhth and lakhth place is a teen number
                    ten_lakhs=number[-7]+number[-6]
                    ten_lakhs_words=number_dict[ten_lakhs] + ' lakh'
                    words.append(ten_lakhs_words)
                    if number_len == 7:break

                except:
                    if number[-6]!='0':
                        lakhs=number[-6]
                        lakhs_words=number_dict[lakhs] + ' lakh'
                        words.append(lakhs_words)
                        if number_len ==6: break #for six digit number
                        
                    if number[-7]!='0':
                        ten_lakhs=number[-7]+'0'
                        ten_lakhs_words=number_dict[ten_lakhs]
                        words.append(ten_lakhs_words)
                        if number_len ==7: break #for seven digit number



                try: #checks if the  ten-croreth and croreth place is a teen number
                    ten_crores=number[-9]+number[-8]
                    ten_crores_words=number_dict[ten_crores] + ' crore'
                    words.append(ten_crores_words)
                    if number_len == 9:break

                except:
                    if number[-8]!='0':
                        crores=number[-8]
                        crore_words=number_dict[crores] + ' crore'
                        words.append(crore_words)
                        if number_len ==8: break #for eight digit number

                    if number[-9]!='0':
                        ten_crores=number[-9]+'0'
                        ten_crores_words=number_dict[ten_crores]
                        words.append(ten_crores_words)
                        if number_len ==9: break #for nine digit number

        times=times+1

    pos=-1
    for times in range(len(words)):
        print(words[pos],end=' ')

        pos=pos-1
    print('')
