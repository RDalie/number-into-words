
#dictionary for words of main numbers
number_dict= dict()
number_dict = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight',
'9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen',
'17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty','30':'thirty','40':'fourty','50':'fifty','60':'sixty',
'70':'seventy','80':'eighty','90':'ninety','100':'hundred'}

while True:
    number = input('Write the number:')
    number=number.lstrip('0')
    if len(number)<1:
        print('zero')
        continue
    words=list()
    

    try:
        print(number_dict[number])
        continue
    except:
        pass

    number_len=len(number)

    if number[1:] == '0'*(number_len-1):
        if number_len==3:
            print(number_dict[number[0]] + ' hundred')
            continue
        elif number_len==4:
            print(number_dict[number[0]]+' thousand')
            continue
        elif number_len==5:
            print(number_dict[number[0]+'0']+' thousand')
            continue
        elif number_len==6:
            print(number_dict[number[0]]+' lakh')
            continue
        elif number_len==7:
            print(number_dict[number[0]+'0']+' lakh')
            continue
        elif number_len==8:
            print(number_dict[number[0]] + ' crore')
            continue
        elif number_len==9:
            print(number_dict[number[0]+'0']+' crore')
            continue



    while True:
        if number[-1]!='0':
            ones=number[-1]
            ones_words=number_dict[ones]
            words.append(ones_words)

        if number[-2]!='0':
            tens=number[-2]+'0'
            tens_words=number_dict[tens]
            words.append(tens_words)
            if number_len ==2:break #for two digit number
            # print(tens_words,ones_words)
        if number[-3]!='0':
            hundreds=number[-3]
            hundreds_words=number_dict[hundreds]+' hundred'
            words.append(hundreds_words)
            if number_len ==3:break#for three digit number
            # print(hundreds_words,tens_words,ones_words)
        try:
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
                # print(thousands_words,hundreds_words,tens_words,ones_words)
            if number[-5]!='0':
                ten_thousands=number[-5] + '0'
                ten_thousands_words=number_dict[ten_thousands]
                words.append(ten_thousands_words)
                if number_len ==5:break #for five digit number
            # print(ten_thousands,thousands_words,hundreds_words,tens_words,ones_words)
        try:
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
                # print(lakhs_words,ten_thousands,thousands_words,hundreds_words,tens_words,ones_words)
            if number[-7]!='0':
                ten_lakhs=number[-7]+'0'
                ten_lakhs_words=number_dict[ten_lakhs]
                words.append(ten_lakhs_words)
                if number_len ==7: break

        try:
            ten_crores=number[-9]+number[-8]
            ten_crores_words=number_dict[ten_crores] + ' crore'
            words.append(ten_crores_words)
            if number_len == 9:break

        except:
            if number[-8]!='0':
                crores=number[-8]
                crore_words=number_dict[crores] + ' crore'
                words.append(crore_words)
                if number_len ==8: break #for six digit number
                # print(lakhs_words,ten_thousands,thousands_words,hundreds_words,tens_words,ones_words)
            if number[-9]!='0':
                ten_crores=number[-9]+'0'
                ten_crores_words=number_dict[ten_crores]
                words.append(ten_crores_words)
                if number_len ==9: break

    pos=-1

    for times in range(len(words)):
        print(words[pos],end=' ')
        pos=pos-1

    # words=list()
    print('\n')
    # if len(number)<= 2 AND int(number)<=20:
    #     print(number_dict[number])
    #     break
    #
    # if len(number)>1 AND number[-1]=='0':
    #     break
    #     words.append(number_dict[number[-1]])
    #
    # number_len= len(number)
    #
    # for num in range(number_len):
    #     words.append(number_dict(number[num]))
