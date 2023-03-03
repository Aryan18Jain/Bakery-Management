import mysql.connector
mydb = mysql.connector.connect(host="bpbljahtfbqi1aj1tvbu-mysql.services.clever-cloud.com", user="uyzr5pngla0ksreu", password="1sMKq9ozmlnQy5aiSmYM", database="bpbljahtfbqi1aj1tvbu")
cur = mydb.cursor()
print('WELCOME TO CAKE BAKE SHAKE')
print('DO YOU HAVE LOGIN ID')
print('IF YES THEN Y OTHER WISE N')
ask = str(input('ENTER:'))
abc = 1
while abc == 1:
    if ask == 'y' or ask == 'Y':
        a = 0
        id = str(input('ENTER YOUR ID:'))
        while a == 0:
            if len(id) == 10:
                a = 1
            else:
                print('INVALID ID')
                a = 0
                id = str(input('ENTER YOUR ID:'))
        password = str(input('ENTER YOUR PASSWORD:'))
        abc = 0
    elif ask == 'N' or ask == 'n':
        print('ENTER THE FOLLOWING DETAILS TO GET REGISTER')
        name = str(input('ENTER YOUR NAME:'))
        mob = str(input('ENTER YOUR MOBILE NUMBER:'))
        a = 0
        while a == 0:
            if len(mob) == 10:
                a = 1
                pass
            else:
                a = 0
                print('INVALID MOBILE NUMBER')
                mob = str(input('ENTER YOUR MOBILE NUMBER:'))
        password = str(input('CREATE YOUR PASSWORD:'))
        s = 'insert into register (name,mob,pass) values(%s,%s,%s)'
        d = (name, mob, password)
        cur.execute(s, d)
        mydb.commit()
        print('REGISTERED SUCCESSFULLY')
        print('YOUR ID IS:', mob)
        print('YOUR PASSWORD IS:', password)
        print('NOW LOGIN')
        id = str(input('ENTER YOUR ID:'))
        b = 0
        while b == 0:
            if len(id) == 10:
                password = str(input('ENTER YOUR PASSWORD:'))
                b = 1
            else:
                print('INVALID ID')
                id = str(input('ENTER YOUR ID:'))
                b = 0
        abc = 0
    else:
        print('ENTER Y OR N ')
        ask = str(input('ENTER:'))
        abc = 1
m = 'select * from register'
cur.execute(m)
result = cur.fetchall()
list_of_mob = [lis[1] for lis in result]
mann = 1
while mann == 1:
    if id in list_of_mob:
        mann = 0
    else:
        print('INVALID ID')
        id = str(input('ENTER YOUR ID:'))
        b = 0
        while b == 0:
            if len(id) == 10:
                b = 1
            else:
                print('INVALID ID')
                print('ENTER ID OF 10 DIGIT')
                id = str(input('ENTER YOUR ID:'))
                b = 0
        mann = 1
a = list_of_mob.index(id)
list_of_pass = [lis[2] for lis in result]
c = 0
while c == 0:
    if list_of_mob[a] == id and list_of_pass[a] == password:
        c = 1
        print("Login Succesfull")
    else:
        print('INCORRECT PASSWORD')
        password = str(input('ENTER YOUR PASSWORD:'))
        C = 0
print('DO YOU WANT TO SEE YOUR PROFILE')
print('IF YES THEN Y OTHER WISE N')
enter = str(input('ENTER:'))
bcd = 1
while bcd == 1:
    if enter == 'Y' or enter == 'y':
        s = 'select * from register where mob = %s'
        c = (id,)
        cur.execute(s, c)
        result = cur.fetchall()
        show_name = [lis[0] for lis in result]
        show_mob = [lis[1] for lis in result]
        show_pass = [lis[2] for lis in result]
        print('YOUR NAME:', show_name[0])
        print('YOUR ID:', show_mob[0])
        print('YOUR PASSWORD:', show_pass[0])
        bcd = 0
    elif enter == 'n' or enter == 'N':
        bcd = 0
    else:
        print('ENTER Y OR N')
        enter = str(input('ENTER:'))
        bcd = 1
print('DO YOU WANT TO CHANGE YOUR PASSWORD')
print('IF YES THEN Y OTHERWISE N')
yes = str(input('ENTER:'))
cd = 1
while cd == 1:
    if yes == 'y' or yes == 'Y':
        old_pass = str(input('ENTER THE OLD PASSWORD:'))
        lo = 1
        while lo == 1:
            if list_of_pass[a] == old_pass:
                lo = 0
                new_pass = str(input('ENTER THE NEW PASSWORD YOU WANT TO CREATE:'))
                re_new_pass = str(input('RETYPE YOUR NEW PASSWORD:'))
                ma = 1
                while ma == 1:
                    if new_pass == re_new_pass:
                        s = 'update register set pass = %s where mob = %s'
                        b = (new_pass, id)
                        cur.execute(s, b)
                        mydb.commit()
                        print('PASSWORD CHANGED SUCCESSFULLY')
                        print('YOUR NEW PASSWORD IS :', new_pass)
                        ma = 0
                    else:
                        print('ENTERED PASSWORD DOES NOT MATCH WITH NEW PASSWORD')
                        print('PLEASE ENTER WRITE PASSWORD')
                        re_new_pass = str(input('RETYPE YOUR NEW PASSWORD:'))
                        ma = 1
            else:
                print('ENTERED OLD PASSWORD IS WRONG')
                print('ENTER AGAIN YOUR OLD PASSWORD:')
                old_pass = str(input('ENTER THE OLD PASSWORD:'))
                lo = 1
        cd = 0
    elif yes == 'n' or yes == 'N':
        cd = 0
    else:
        print('ENTER Y OR N')
        yes = str(input('ENTER:'))
        cd = 1
if id == '6265857466':
    b = 0
    while b == 0:
        print(
            'ENTER THE OPTION\n''1. ADD NEW PRODUCT\n''2. EDIT EXIXSTING PRODUCTS\n''3. DELETE THE EXISTING PRODUCT\n''4. VIEW THE LIST OF PRODUCTS\n''5. END')
        ask = str(input('ENTER:'))
        a = 0
        while a == 0:
            if ask == '1':
                cur.execute('select max(product_id) from details')
                result = cur.fetchall()
                m = int(result[0][0])
                ma = m + 1
                print('TO INSERT ENTERIES PROVIDE FOLLOWING DETAILS')
                name_of_product = str(input('ENTER THE NAME OF PRODUCT:'))
                category = str(input('ENTER THE CATEGORY OF PRODUCT:'))
                price = str(input('ENTER THE PRICE:'))
                shape = str(input('ENTER THE SHAPE OF PRODUCT:'))
                flavour = str(input('ENTER THE FLAVOUR OF PRODUCT:'))
                size = str(input('ENTER THE SIZE OF PRODUCT:'))
                eggless = str(input('WHETHER EGG IN PRODUCT: YES/NO'))
                s = 'insert into details (product_id,name,category,price,shape,flavour,size,eggless) values (%s,%s,%s,%s,%s,%s,%s,%s)'
                b = (ma, name_of_product, category, price, shape, flavour, size, eggless)
                cur.execute(s, b)
                mydb.commit()
                print('SUCCESFULLY ENTERED')
                a = 1
                b = 0
            elif ask == '2':
                print('WHAT YOU WANT TO UPDATE')
                c = 0
                while c == 0:
                    print(
                        'ENTER THE OPTION\n''1. NAME OF PRODUCT\n''2. CATEGORY OF PRODUCT\n''3. PRICE OF PRODUCT\n''4. SHAPE OF PRODUCT\n''5. FLAVOUR OF PRODUCT\n''6. SIZE OF PRODUCT\n''7. EGGLESS\n''8. END')
                    ask = str(input('ENTER:'))
                    d = 0
                    while d == 0:
                        if ask == '1':
                            print('TO UPDATE ENTERIES PROVIDE FOLLOWING DETAILS')
                            name_of_product = str(input('ENTER THE NAME OF PRODUCT TO BE UPDATE:'))
                            product_id = str(input('ENTER THE ID OF PRODUCT CORRESPONDED:'))
                            s = 'update details set name = %s where product_id = %s'
                            b = (name_of_product, product_id)
                            cur.execute(s, b)
                            mydb.commit()
                            print('SUCCESFULLY UPDATED')
                            d = 1
                            c = 0
                        elif ask == '2':
                            print('TO UPDATE ENTERIES PROVIDE FOLLOWING DETAILS')
                            category = str(input('ENTER THE CATEGORY OF PRODUCT TO BE UPDATE:'))
                            product_id = str(input('ENTER THE ID OF PRODUCT CORRESPONDED:'))
                            s = 'update details set category = %s where product_id = %s'
                            b = (category, product_id)
                            cur.execute(s, b)
                            mydb.commit()
                            print('SUCCESFULLY UPDATED')
                            d = 1
                            c = 0
                        elif ask == '3':
                            print('TO UPDATE ENTERIES PROVIDE FOLLOWING DETAILS')
                            price = str(input('ENTER THE PRICE TO BE UPDATE:'))
                            product_id = str(input('ENTER THE ID OF PRODUCT CORRESPONDED:'))
                            s = 'update details set price = %s where product_id = %s'
                            b = (price, product_id)
                            cur.execute(s, b)
                            mydb.commit()
                            print('SUCCESFULLY UPDATED')
                            d = 1
                            c = 0
                        elif ask == '4':
                            print('TO UPDATE ENTERIES PROVIDE FOLLOWING DETAILS')
                            shape = str(input('ENTER THE SHAPE OF PRODUCT TO BE UPDATE:'))
                            product_id = str(input('ENTER THE ID OF PRODUCT CORRESPONDED:'))
                            s = 'update details set shape = %s where product_id = %s'
                            b = (shape, product_id)
                            cur.execute(s, b)
                            mydb.commit()
                            print('SUCCESFULLY UPDATED')
                            d = 1
                            c = 0
                        elif ask == '5':
                            print('TO UPDATE ENTERIES PROVIDE FOLLOWING DETAILS')
                            flavour = str(input('ENTER THE FLAVOUR OF PRODUCT TO BE UPDATE:'))
                            product_id = str(input('ENTER THE ID OF PRODUCT CORRESPONDED:'))
                            s = 'update details set flavour = %s where product_id = %s'
                            b = (flavour, product_id)
                            cur.execute(s, b)
                            mydb.commit()
                            print('SUCCESFULLY UPDATED')
                            d = 1
                            c = 0
                        elif ask == '6':
                            print('TO UPDATE ENTERIES PROVIDE FOLLOWING DETAILS')
                            size = str(input('ENTER THE SIZE OF PRODUCT TO BE UPDATE:'))
                            product_id = str(input('ENTER THE ID OF PRODUCT CORRESPONDED:'))
                            s = 'update details set size = %s where product_id = %s'
                            b = (size, product_id)
                            cur.execute(s, b)
                            mydb.commit()
                            print('SUCCESFULLY UPDATED')
                            d = 1
                            c = 0
                        elif ask == '7':
                            print('TO UPDATE ENTERIES PROVIDE FOLLOWING DETAILS')
                            eggless = str(input('WHETHER EGG IN PRODUCT: YES/NO'))
                            product_id = str(input('ENTER THE ID OF PRODUCT CORRESPONDED:'))
                            s = 'update details set eggless = %s where product_id = %s'
                            b = (eggless, product_id)
                            cur.execute(s, b)
                            mydb.commit()
                            print('SUCCESFULLY UPDATED')
                            d = 1
                            c = 0
                        elif ask == '8':
                            a, b, c, d, = 1, 0, 1, 1
                        else:
                            print('ENTER ONLY 1/2/3/4/5/6/7/8')
                            ask = str(input('ENTER:'))
                            c = 0
            elif ask == '3':
                print('TO DELETE ENTERIES PROVIDE FOLLOWING DETAILS')
                product_id = str(input('ENTER THE ID OF PRODUCT TO BE DELETED:'))
                s = 'delete from details where product_id = %s'
                b = (product_id,)
                cur.execute(s, b)
                mydb.commit()
                print('SUCCESFULLY DELETED')
                a = 1
                b = 0
            elif ask == '4':
                cur.execute('select * from details')
                result = cur.fetchall()
                print(
                    ': ''PRODUCT ID'' : ''NAME OF PRODUCT'' : ''CATEGORY'' : ''PRICE  '' : ''   SHAPE   '' : ''  FLAVOUR  '' : ''  SIZE  '' : ''EGGLESS'' : ')
                for i in result:
                    product_id = str(i[0])
                    name_of_product = str(i[1])
                    category = str(i[2])
                    price = str(i[3])
                    shape = str(i[4])
                    flavour = str(i[5])
                    size = str(i[6])
                    eggless = str(i[7])
                    print(":", product_id, ' ' * (9 - len(product_id)), ':', name_of_product,
                          ' ' * (14 - len(name_of_product)), ':', category, ' ' * (7 - len(category)), ":", price,
                          ' ' * (6 - len(price)), ':', shape, ' ' * (10 - len(shape)), ':', flavour,
                          ' ' * (10 - len(flavour)), ':', size, ' ' * (7 - len(size)), ':', eggless,
                          ' ' * (6 - len(eggless)), ":")
                a = 1
                b = 0
            elif ask == '5':
                a = 1
                b = 1
            else:
                print('ENTER ONLY 1/2/3/4')
                ask = str(input('ENTER:'))
                a = 0
else:
    print('DO YOU WANT TO SEE THE ITEMS AVAILABLE AMOUNT WISE OR CATEGORY WISE OR ALL ITEMS')
    print('ENTER THE OPTION\n''1. AMOUNT WISE\n''2. CATEGORY WISE\n''3. ALL ITEMS')
    ask = str(input('ENTER:'))
    a = 0
    while a == 0:
        ab = 0
        while ab == 0:
            if ask == '1':
                s = 'select * from details where price <= %s order by price'
                d = str(input('ENTER THE MAXIMUM AMOUNT YOU LOOKING FOR:'))
                b = (d,)
                cur.execute(s, b)
                result = cur.fetchall()
                if result == []:
                    print('NO ITEM AVAILABLE LESS THAN PRICE:', d)
                    print('ENTER ANOTHER PRICE:')
                    ab = 0
                else:
                    print(
                        ': ''PRODUCT ID'' : ''NAME OF PRODUCT'' : ''CATEGORY'' : ''PRICE  '' : ''   SHAPE   '' : ''  FLAVOUR  '' : ''  SIZE  '' : ''EGGLESS'' : ')
                    for i in result:
                        product_id = str(i[0])
                        name_of_product = str(i[1])
                        category = str(i[2])
                        price = str(i[3])
                        shape = str(i[4])
                        flavour = str(i[5])
                        size = str(i[6])
                        eggless = str(i[7])
                        print(":", product_id, ' ' * (9 - len(product_id)), ':', name_of_product,
                              ' ' * (14 - len(name_of_product)), ':', category, ' ' * (7 - len(category)), ":", price,
                              ' ' * (6 - len(price)), ':', shape, ' ' * (10 - len(shape)), ':', flavour,
                              ' ' * (10 - len(flavour)), ':', size, ' ' * (7 - len(size)), ':', eggless,
                              ' ' * (6 - len(eggless)), ":")
                        ab = 1
                a = 1
            elif ask == '2':
                cur.execute('select distinct(category) from details')
                result = cur.fetchall()
                cate = [i[0] for i in result]
                print('AVAILABLE CATEGORY')
                d = 1
                for i in cate:
                    print(d, i)
                    d = d + 1
                s = 'select * from details where category = %s order by name'
                d = str(input('ENTER THE CATEGORY YOU LOOKING FOR:'))
                b = (d,)
                cur.execute(s, b)
                result = cur.fetchall()
                if result == []:
                    print('NO ITEM AVAILABLE IN CATEGORY:', d)
                    print('ENTER ANOTHER CATEGORY:')
                    ab = 0
                else:
                    print(
                        ': ''PRODUCT ID'' : ''NAME OF PRODUCT'' : ''CATEGORY'' : ''PRICE  '' : ''   SHAPE   '' : ''  FLAVOUR  '' : ''  SIZE  '' : ''EGGLESS'' : ')
                    for i in result:
                        product_id = str(i[0])
                        name_of_product = str(i[1])
                        category = str(i[2])
                        price = str(i[3])
                        shape = str(i[4])
                        flavour = str(i[5])
                        size = str(i[6])
                        eggless = str(i[7])
                        print(":", product_id, ' ' * (9 - len(product_id)), ':', name_of_product,
                              ' ' * (14 - len(name_of_product)), ':', category, ' ' * (7 - len(category)), ":", price,
                              ' ' * (6 - len(price)), ':', shape, ' ' * (10 - len(shape)), ':', flavour,
                              ' ' * (10 - len(flavour)), ':', size, ' ' * (7 - len(size)), ':', eggless,
                              ' ' * (6 - len(eggless)), ":")
                        ab = 1
                a = 1
            elif ask == '3':
                cur.execute('select * from details')
                result = cur.fetchall()
                print(
                    ': ''PRODUCT ID'' : ''NAME OF PRODUCT'' : ''CATEGORY'' : ''PRICE  '' : ''   SHAPE   '' : ''  FLAVOUR  '' : ''  SIZE  '' : ''EGGLESS'' : ')
                for i in result:
                    product_id = str(i[0])
                    name_of_product = str(i[1])
                    category = str(i[2])
                    price = str(i[3])
                    shape = str(i[4])
                    flavour = str(i[5])
                    size = str(i[6])
                    eggless = str(i[7])
                    print(":", product_id, ' ' * (9 - len(product_id)), ':', name_of_product,
                          ' ' * (14 - len(name_of_product)), ':', category, ' ' * (7 - len(category)), ":", price,
                          ' ' * (6 - len(price)), ':', shape, ' ' * (10 - len(shape)), ':', flavour,
                          ' ' * (10 - len(flavour)), ':', size, ' ' * (7 - len(size)), ':', eggless,
                          ' ' * (6 - len(eggless)), ":")
                    ab = 1
                    a = 1
            else:
                print('ENTER ONLY 1/2/3')
                ask = str(input('ENTER:'))
                a = 0
    cur.execute('truncate cart')
    cur.execute('truncate customer')
    print('SELECT THE ITEMS TO ADD IN CART')
    if ask == '3':
        s = 'select product_id from details'
        cur.execute(s)
        result = cur.fetchall()
        list_of_all_product_id = [i[0] for i in result]
    if ask == '1':
        s = 'select product_id from details where price <= %s order by price '
        d = (d,)
        cur.execute(s, d)
        result = cur.fetchall()
        list_of_price_product_id = [i[0] for i in result]
    if ask == '2':
        s = 'select product_id from details where category = %s order by name'
        d = (d,)
        cur.execute(s, d)
        result = cur.fetchall()
        list_of_category_product_id = [i[0] for i in result]
    while a == 1:
        c = 0
        while c == 0:
            pid = int(input('ENTER THE PRODUCT ID:'))
            if ask == '1':
                if pid in list_of_price_product_id:
                    quan = str(input('ENTER THE QUANTITY:'))
                    s = 'insert into cart values (%s,%s)'
                    d = (pid, quan)
                    cur.execute(s, d)
                    mydb.commit()
                    c = 1
                else:
                    print('WRONG ID')
                    print('ENTER VALID PRODUCT ID:')
                    c = 0
            elif ask == '2':
                if pid in list_of_category_product_id:
                    quan = str(input('ENTER THE QUANTITY:'))
                    s = 'insert into cart values (%s,%s)'
                    d = (pid, quan)
                    cur.execute(s, d)
                    mydb.commit()
                    c = 1
                else:
                    print('WRONG ID')
                    print('ENTER VALID PRODUCT ID:')
                    c = 0
            else:
                if pid in list_of_all_product_id:
                    quan = str(input('ENTER THE QUANTITY:'))
                    s = 'insert into cart values (%s,%s)'
                    d = (pid, quan)
                    cur.execute(s, d)
                    mydb.commit()
                    c = 1
                else:
                    print('WRONG ID')
                    print('ENTER VALID PRODUCT ID:')
                    c = 0
        print('SUCCESFULLY ADDED IN CART')
        print('DO YOU WANT TO BOOK MORE ITEMS')
        print('ENTER Y FOR YES OR N FOR NO')
        b = 1
        while b == 1:
            ak = str(input('ENTER:'))
            if ak == 'y' or ak == 'Y':
                a = 1
                b = 0
            elif ak == 'n' or ak == 'N':
                a = 0
                b = 0
            else:
                print('ENTER ONLY Y OR N')
                b = 1
    s = 'select distinct (selected_id) from cart'
    cur.execute(s)
    result = cur.fetchall()
    selected_id = [i[0] for i in result]
    print('YOUR SELECTED ITEMS ARE')
    print(': ''PRODUCT ID'' : ''NAME OF PRODUCT'' : ''RATE   '' : ''quantity'' : ')
    for i in selected_id:
        s = 'select selected_id , sum(quantity) from cart where selected_id=%s'
        d = (i,)
        cur.execute(s, d)
        result = cur.fetchall()
        selected_id = [i[0] for i in result]
        quantity = [i[1] for i in result]
        for i in selected_id:
            for j in quantity:
                s = 'insert into customer values (%s,%s)'
                d = (i, j)
                cur.execute(s, d)
                mydb.commit()
    cur.execute('select a.product_id,a.name,a.price,b.quantity,a.price*b.quantity as rate from details a , customer b where a.product_id=b.selected_id;')
    result = cur.fetchall()
    for i in result:
        product_id = str(i[0])
        name_of_product = str(i[1])
        rate = str(i[2])
        quantity = str(i[3])
        price = str(i[4])
        print(":", product_id, ' ' * (9 - len(product_id)), ':', name_of_product, ' ' * (14 - len(name_of_product)),
              ':', rate, ' ' * (6 - len(rate)), ':', quantity, ' ' * (7 - len(quantity)), ':')
    print('ENTER THE ADDRESS WHERE TO DELIVER')
    address = str(input('ENTER YOUR ADDRESS'))
    cur.execute('select max(bill_no) from bill')
    result = cur.fetchall()
    ma = [i[0] for i in result]
    for i in ma:
        m = i
        k=str(m)
    s = 'insert into bill values(%s)'
    n = m + 1
    d = (n,)
    cur.execute(s, d)
    mydb.commit()
    print('YOUR BILL')
    import datetime
    dtr = datetime.datetime.now()
    print('-' * 71)
    print('\t\t\t\t INVOICE')
    print('-' * 71)
    print('\t\t\t     CAKE BAKE SHAKE')
    print('Adr.13, MAKRONIA SAGAR(M.P.)', end='')
    print('\t\t\tTel.{0:>s}'.format('07582-244676,403067'))
    print('-' * 71)
    s = 'select name from register where mob=%s'
    d = (id,)
    cur.execute(s, d)
    result = cur.fetchall()
    for i in result:
        name = str(i[0])
    print('NAME:', name, end='')
    print(' ' * (32 - len(name)), 'DATE:', dtr)
    print('Mob.:', id, end='')
    print(' ' * (44-len(k)), 'BILL NO.:', m)
    print('adr.:', address)
    print('-' * 71)
    print('S.NO.\tPRODUCT ID\tNAME OF PRODUCT\t\tRATE\tQTY.\t AMOUNT')
    sno = 0
    total = 0
    cur.execute(
        'select a.product_id,a.name,a.price,b.quantity,a.price*b.quantity as rate from details a , customer b where a.product_id=b.selected_id;')
    result = cur.fetchall()
    for i in result:
        product_id = int(i[0])
        name_of_product = str(i[1])
        rate = float(i[2])
        quantity = int(i[3])
        price = str(i[4])
        amount = float(price)
        total = amount + total
        sno = sno + 1
        print('{0:>3d}'.format(sno), end='')
        print('{0:>10d}'.format(product_id), end='')
        print('{0:>25s}'.format(name_of_product), end='')
        print('{0:>15.2f}'.format(rate), end='')
        print('{0:>6d}'.format(quantity), end='')
        print('{0:>12.2f}'.format(amount))
    pay = total + total * 18 / 100
    print('-' * 71)
    print('\t\t\t\t\t\t\tTOTAL:{0:>9.2f}'.format(total))
    print('-' * 71)
    print('TAX(CGST + SGST): 18%', end='')
    print('\t\t\t\t   TAX AMOUNT:{0:>9.2f}'.format(total * 18 / 100))
    print('\t\t\t\t\t       AMOUND PAYABLE:{0:>9.2f}'.format(pay))
    print('-' * 71)
    print('ENTER THE OPTION OF PAYMENT')
    print('1. BY CREDIT / DEBIT / ATM CARD\n''2. UPI\n''3. CASH ON DELIVERY')
    b = 0
    while b == 0:
        ask = str(input('ENTER:'))
        if ask == '1':
            a = 0
            while a == 0:
                card_no = str(input('ENTER THE CARD NUMBER:'))
                if len(card_no) == 16:
                    a = 1
                else:
                    print('ENTER VALID CARD NUMBER OF 16 DIGIT')
                    a = 0
            month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
            print('ENTER THE MONTH VALID THRU')
            print(
                '1. JAN\n''2. FEB\n''3. MAR\n''4. APR\n''5. MAY\n''6. JUN\n''7. JUL\n''8. AUG\n''9. SEP\n''10. OCT\n''11. NOV\n''12. DEC')
            a = 0
            while a == 0:
                m = str(input('ENTER:'))
                if m in month:
                    a = 1
                else:
                    print('ENTER VALID OPTION OF MONTH')
                    a = 0
            a = 0
            while a == 0:
                year = str(input('ENTER THE YEAR VALID THRU:'))
                if len(year) == 2 and int(year) >= 20:
                    a = 1
                else:
                    print('ENTER VALID YEAR OF 2 DIGIT AND FROM YEAR 2020 OR ABOVE')
                    a = 0
            a = 0
            while a == 0:
                cvv = str(input('ENTER THE CVV NUMBER:'))
                if len(cvv) == 3:
                    a = 1
                else:
                    print('ENTER VALID CVV NUMBER OF 3 DIGIT')
                    a = 0
            b = 1
            print('ORDER WIL BE DELIVERED IN 1 HOUR TO YOUR ADDRESS:', address)
            print('PAYMENT SUCCESSFULLY OF RS.', round(pay, 2))
        elif ask == '2':
            upi = str(input('ENTER THE BHIM ID '))
            print('ORDER WIL BE DELIVERED IN 1 HOUR TO YOUR ADDRESS:', address)
            print('PAYMENT SUCCESSFULLY OF RS.', round(pay, 2))
            b = 1
        elif ask == '3':
            print('ORDER WIL BE DELIVERED IN 1 HOUR TO YOUR ADDRESS:', address)
            print('PAY RS.', round(pay, 2), 'AT YOUR DOOR STEP')
            b = 1
        else:
            print('ENTER 1/2/3')
            b = 0
