##===============PERSONAL NOTES================================
import os,math
##-------All-Special chaecters and digits------------
special_char,digits="!#$%&'()*+,-""./:;<{=?@''[>\]^_`~}|","0123456789"
#----creating data storing folder if not present--------
def change_path(x):
    s=""
    for i in x:
        if(i=="/"):
            s=s+"/"
        else:
            s=s+i
    return s
p=os.getcwd()
path,f=change_path(p),1
for path,folder,file in os.walk(path):
    if(f==1):
        if ("NOTES(Database)"  in folder ):
            dta_path=path+"/NOTES(Database)"
            dta=dta_path+"/database.txt"
            act_path=dta_path+"/Accounts"
        else:
            dta_path=path+"/NOTES(Database)"  
            os.makedirs("NOTES(Database)")
            dta=dta_path+"/database.txt"
            f5=open(dta,"a")
            f5.close
            act_path=dta_path+"/Accounts"
            os.makedirs(act_path)
    else:
        break
    f+=1
##--------Creating file1------------------------
def file_name(a,b):
    l=[a,b]
    fn,c="",1
    for i in l:
        if (len(i)%2!=0 and c==1):
            h1=int(math.ceil((len(i)/2)))
            f1=a[:h1]
            fn=fn+f1
        elif (len(i)%2!=0 and c==2):
            h1=int(math.ceil((len(i)/2))*(-1))
            f1=b[h1:]
            fn=fn+f1
        elif (len(i)%2==0 and c==1):
            h1=int(len(i)/2)
            f1=a[:h1]
            fn=fn+f1
        elif (len(i)%2==0 and c==2):
            h1=int(len(i)/2)*(-1)
            f1=b[h1:]
            fn=fn+f1
        c+=1
    fi=fn+".txt"
    return fi
##-----storing data in file1------------------------
def add_data(file1,*l):
    f5=open(file1,"a")
    for j in l:
        nl=""
        for i in j:
            a1,b=(ord(i))**2,""
            while a1>0:
                x=a1%2
                b=str(x)+b
                a1=a1//2
            if (nl==""):
                nl=b
            else:
                nl=b+" "+nl
        f5.write(nl+"\n")
    f5.close()
##-------Changing data to Binary form--------
def to_Binary(j):
    nl=""
    for i in j:
        a1,b=(ord(i))**2,""
        while a1>0:
            x=a1%2
            b=str(x)+b
            a1=a1//2
        if (nl==""):
            nl=b
        else:
            nl=b+" "+nl
    nl=nl+"\n"
    return nl
##---------Decoding data---------------------
def de_code(f):
    nl=f.split()
    s,x="",(len(nl)-1)
    for i in range(x,-1,-1):
        i=int(nl[i])
        sum,p=0,0
        while (i>0):
            y=i%10
            d=(y)*(2)**p
            sum+=d
            p+=1
            i=i//10         
        s=s+chr(int(math.sqrt(sum)))
    return s
##---------Username & School --valid or not --finder-----------------
def check_valid(n,c):
    while (len(n)<3 or len(n)==0 or n[0]==" " or (len(n)>=3 and ((n[0] or n[1] or n[2]) in special_char) or n[0].isupper())
            or (len(n)>=3 and ((n[0] or n[1] or n[2]) in digits))):
        if(len(n)==0):
            print(">>> You not entered",c,"\n")
        elif(n[0]==" "):
            print(">>> ",c,"not start with space","\n")
            print()
        elif(len(n)<3 and (n!="  ")):
            print(">>> ",c,"contains at lest of 3 letters","\n")
        elif(n[0].isupper()):
            print(">>> ",c,"not start with capital letter","\n")
        elif(len(n)>=3 and ((n[0] or n[1] or n[2]) in special_char)):
            print(">>> ",c,"not start with special charecters","\n")
        elif(len(n)>=3 and ((n[0] or n[1] or n[2]) in digits)):
            print(">>> ",c,"not start with digit","\n")
        n=input("Enter "+c+"    :") 
    return n
##---------Password --valid or not --finder-----------------
def valid_check(p):
    while( len(p)<4 or len(p)==0 or p[0]==" "):
        if(len(p)==0):
            print(">>> You not entered password","\n")
        elif(p[0]==" "):
            print(">>> Password not start with space","\n")
        elif(len(p)<4):
            print(">>> Password must be at least of length 4","\n")
        p=input("Enter password:")
    return p
##---------reading-Chapter_content-----------------
def chapter_data(file1,title):
    with open(file1,"r") as f7:
        c=0
        f=f7.readline()
        while f:
            c+=1
            f=f7.readline()
    if (title[-1]==":"):
        tit=title
    else:
        tit=title+":"
    data,title_check,ncl=[],False,3
    f5=open(file1,"r")
    f=f5.readline()
    while(ncl>0 and title_check==False):
        i=1
        while i<=c:
            t1=de_code(f)
            if(t1.lower()==(tit.lower())):
                title_check=True
                data.append(t1)
                f=f5.readline()
                t1=de_code(f)
                while t1!=70*"-":
                    data.append(t1)
                    f=f5.readline()
                    t1=de_code(f)
            else:
                f=f5.readline()
            i+=1
        i=1
        if (title_check==False):
            ncl=ncl-1
        if(title_check==False and ncl>0):
            print("\n",">>> Chapetr (or) Title name not found re-try",sep="")
            print(">>> You have",ncl,"chances left to enter correct Title","\n")
            title=input("Enter chapter (or) Title name:")
            print()
            if (title.endswith(":")):
                tit=title
            else:
                tit=title+":"
            f5.seek(0)
            f=f5.readline()
    if(ncl==0 and title_check==False):
        print("\n",">>> Your chances are completed re-try")
    if(title_check==True):
        return data
def all_chapters(file1):
    with open(file1,"r") as uf:
        f,chap,l=uf.readline(),[],1
        while f:
            if(l==1):
                chap.append(de_code(f))
            elif(de_code(f)==70*"-"):
                f=uf.readline()
                if(f!=""):
                    chap.append(de_code(f))
            f=uf.readline()
            l+=1
    return chap
def above_chapter(file1,t):
    x=chapter_data(file1,t)
    new,fl,cl,vl=[],0,0,0
    if(x!=None):
        for i in x:
            cl+=1
    if (t.endswith(":")):
        tit=t
    else:
        tit=t+":"
    t=tit.title()
    with open(file1,"r") as uf:
        for line in uf:
            fl+=1
    with open(file1,"r") as u:
        for line in u:
            if (de_code(line)==t):
                break
            else:
                new.append(line)
            vl+=1
    vl=vl+cl
    v=new,vl
    return v
def below_chapter(file1,t):
    d=above_chapter(file1,t)
    vl,bl,vl2=d[1],[],0
    with open(file1,"r") as f:
        for line in f:
            if (vl2 > vl):
                bl.append(line)
            vl2+=1
    return bl
def del_chapter(file1,t):
    a=above_chapter(file1,t)
    b=below_chapter(file1,t)
    c=a[0]+b
    f= open(file1,"w")
    f.close()
    with open(file1,"a") as e:
        e.writelines(c)
def display_chapter(x):
    for i in range(len(x)):
        if(i>=1):
            print(x[i])
            print("--(",str(i),")--",sep="")
        else:
            print(x[i])
def display_lines(x):
    for i in range(len(x)):
        if(i>=2):
            z="line("+str(i-1)+"):"
            print(z,x[i])
        else:
            print(x[i])
def insert_chap(file1,t,x):
    new,en=[],70*"-"
    a=above_chapter(file1,t)
    b=below_chapter(file1,t)
    for i in x:
        new.append(to_Binary(i))
    new.append(to_Binary(en))
    c=a[0]+new+b
    f= open(file1,"w")
    f.close()
    with open(file1,"a") as e:
        e.writelines(c)
def sort_del_lines(l):
    m,nl=l.split(","),[]
    for i in range(len(m)-1):
        for j in range(i,len(m)):
            if(("-" not in m[i]) and ("-" not in m[j])):
                if(int(m[i])> int(m[j])):
                    m[i],m[j]=m[j],m[i]
            elif(len(m[i])>=3):
                k=m[i].split("-")
                l=k[0]
                if(len(m[j])>=3):
                    n=m[j].split("-")
                    o=n[0]
                    if(int(l) > int(o)):
                        m[i],m[j]=m[j],m[i]
                else:
                    if(int(l)> int(m[j])):
                        m[i],m[j]=m[j],m[i]
    for i in m:
        if(len(i)>=3):
            k=i.split("-")
            for t in range (int(k[0]),int(k[1])+1):
                nl.append(t+1)
        else: 
            nl.append(int(i)+1)
    return nl
def log_in():
    ##-----finding length of dtabase file1---------
    c=0
    f5=open(dta,"r")
    a=f5.readline()
    while a:
        c+=1
        a=f5.readline()
    f5.close()
    ##--------index:user name line 
    m,dict,i=[i for i in range(1,c+1,3)],{},0
    for j in m:
        dict[i]=j
        i+=1
    ##-------storing alll user_names--------------
    f5=open(dta,"r")
    a=f5.readline()
    k,ru=1,[]        
    while a:
        if (k in m):
            u1=de_code(a)
            ru.append(u1)      
        a=f5.readline()
        k+=1
    ##----------cheking user name Found or not-------------
    ncl,c=3,False
    while( ncl>0 and c==False):
        n=input("Enter user name :")   
        for i in range(len(ru)):
            if (ru[i]==n):
                ul=int(dict[i])
                pl=int(dict[i])+1
                user_verify,ncl,c=True,0,True
                break
        if (ncl>0 and c!=True):
            c=False
            ncl-=1
            print("\n",">>> Username not found",sep="")
            if (ncl>0):
                print(">>>",ncl,"Chances are left to enter correct Username","\n")
    if(ncl==0 and c==False):
        print(">>> User name not found & your chances are completed")
        print(">>> Log-in secisssion is closed re-login ")
        user_verify=False
    #--------knowing  password of a user--------------
    if(c==True):
        f5=open(dta,"r")
        a=f5.readline()
        k=1      
        while a:
            if (k == pl):
                p1=de_code(a)
            a=f5.readline()
            k+=1
        ##-----checking password is correct or not ------------------------------
        p=input("Enter password :")
        ncl=3
        if(p!=p1):
            ncl-=1
            while(p!=p1 and ncl>0):
                print("\n",">>> Password is incorrect please re-enter",sep="")
                print(">>>",ncl,"Chances are left to enter correct password","\n")
                p=input("Enter password :")
                if(p==p1):
                    pass_verify=True
                    break
                ncl-=1
            if ncl==0:
                pass_verify=False
                print("\n",">>> Password is incorrect & your chances are completed",sep="")
                print(">>> Log-in secisssion is closed re-login ")
        else:
            pass_verify=True
    if(user_verify==True and pass_verify==True):
        x=[n,p,user_verify,pass_verify]
    elif(user_verify==True and pass_verify==False):
        x=[n,"",user_verify,pass_verify] 
    elif(user_verify==False):
        x=["","",user_verify,"False"]
    return x
def line_to_word(x):
    w,ns1,ns,nl,l="","",[],[],len(x)
    for i in range(l):
        if (x[i]!=" " and i==l-1):
            w=w+x[i]
            ns.append(w)
        elif(x[i]!=" "):
            w=w+x[i]
        else:
            ns.append(w)
            w=""
    for i in range(len(ns)):
        if(i<=(len(ns)-2)):
            x=i+1
            nl.append(x)
            n="("+str(x)+")"
            ns1=ns1+n+" "+ns[i]+" "
        else:
            x=i+1
            n="("+str(x)+")"
            n1="("+str(x+1)+")"
            nl=nl+[x,x+1]
            ns1=ns1+n+" "+ns[i]+" "+n1
    y=ns,ns1,nl
    return y
def word_number(x):
    w,ns1,ns,l="","",[],len(x)
    for i in range(l):
        if (x[i]!=" " and i==l-1):
            w=w+x[i]
            ns.append(w)
        elif(x[i]!=" "):
            w=w+x[i]
        else:
            ns.append(w)
            w=""
    for i in range(len(ns)):
        x=i+1
        n="("+str(x)+")"
        ns1=ns1+ns[i]+n+" "
    n=ns,ns1
    return n
def main_menu():
    print("_"*40)
    print("|")
    print("| 1 : Create account")
    print("|")
    print("| 2 : Login ")
    print("|")
    print("|       i. Add new Chapter")
    print("|")
    print("|      ii. Add text between chapter")
    print("|")
    print("|     iii. Edit chapter")
    print("|")
    print("|      vi. Delete  chapter")
    print("|")
    print("|       v. Display chapter")
    print("|")
    print("|      vi. Display all chapter")
    print("|")
    print("| 3: Manage account")
    print("|")
    print("|       i. Forgott Password")
    print("|")
    print("|      ii. Change Password")
    print("|")
    print("|     iii. Delete account")
    print("|")
    print("| 4: Help")
    print("|")
    print("| 4: Exit")
    print("|","_"*40,sep="")
    print()
def log_menu():
    print("-"*15,"LOG-IN MENU","-"*15)
    print("1: Add Chapter","\n")
    print("2: Add text in a chapter","\n")
    print("3: Edit chapter","\n")
    print("4: Delet chapter","\n")
    print("5: Display chapter")
    print("6: Display all chapters","\n")
    print("7: Exit")
    print("-"*43)
def edit_menu():
    print("-"*7,"Edit Menu","-"*7)
    print("1: Replace words in a line","\n")
    print("2: Remove words in a line","\n")
    print("3: Remove line","\n")
    print("4: Exit")
    print("-"*23)
def account_menu():
    print("-"*7,"Manage account","-"*7)
    print("1: Forgott Password","\n")
    print("2: Change Password","\n")
    print("3: Delete account","\n")
    print("4: Exit")
    print("-"*28)
def text_menu():
    print("-"*8,"Add menu","-"*8)
    print("1: Add text in a line","\n")
    print("2: Add new line ","\n")
    print("3: Exit")
    print("-"*24)
def help_menu():
    print("-"*50)
    print("I.Creating account:-")
    print("     1.Enter user name")
    print("     2.Enter password")
    print("     3.Enter your childhood school name")
    print("-"*50)
    print("II.Log-in menu:","\n")
    print("    * Add chapter:-")
    print("         1.Enter Chapter (or) Title name")
    print("         2.Enter lines of concept","\n")
    print("         Example for chapter")
    print("         India:","\n")
    print("         India is still devoloping country.India is second")
    print("         largest country in population.India got indipence")
    print("         after strugling of 150 years in 15th august 1947.","\n")
    print("    * Add text in a chapter:-")
    print("           1.Enter chapter name in which you want to add text")
    print("              ---Text menu---")
    print("              1: add text in aline")
    print("              2: add new line")
    print("           2.Enter corresponding number of text menu")
    print("           3.Add text","\n")
    print("    * Edit chapter:-")
    print("           1.Enter chapter name in which you want to edit")
    print("              ---Edit menu---")
    print("                1: Replace words in a line")
    print("                2: Remove words in a line")
    print("                3: Remove line")
    print("           2.Enter corresponding number of edit menu")
    print("           3. Enter corresponding numbers or words or line","\n")
    print("    * Delete Chapter:-")
    print("           1.Enter chapter name in which you want to Delete")
    print("           2.confirm to delete Chapter yes (or) no","\n")
    print("    * Display chapter:-")
    print("           1.Enter chapter name which you want to Display","\n")
    print("-"*50)
    print("III.Manage account:","\n")
    print("    * Forgott password:-")
    print("         1.Enter your user name")
    print("         2.Enter your childhood schoool name")
    print("         3.Enter new-password","\n")
    print("    * Change password:-")
    print("         1.Enter user name")
    print("         2.Enter old-password")
    print("         3.Enter new password","\n")
    print("    * Delete account:-")
    print("         1.Enter user name")
    print("         2.Enter password")
    print("         3.confirm to delete account yes (or) no","\n")
    print("-"*50)
##-----------------------------------------
main_menu()
print("Enter numer of above data as you want: 2  #For Log-in")
print("<"*27,end="")
print(">"*30,"\n")
i,mm,lm,em,am,tm=int(input("Enter numer of above data as you want:")),0,0,0,0,0
print()
while (i>=1 and i<=4):
    ##---------Creating account-------------------
    if (i==1):
        ##----asking username---------------
        c,user="Username",True
        a=input("Enter "+c+"    :")
        n=check_valid(a,c)
        ##----Cheking user exist or not-------------
        f5=open(dta,"r")
        a,c=f5.readline(),0
        while a:
            c+=1
            a=f5.readline()
        f5.close()
        m=[i for i in range(1,c+1,3)]
        f5=open(dta,"r")
        a=f5.readline()
        k,ru=1,[]
        while a:
            if (k in m):
                s=de_code(a)
                ru.append(s)
                if(s==n or n in ru):
                    print("\n",">>> User name alredy exist","\n")
                    user=False
                    break
            a=f5.readline()
            k+=1
        else:
            n=n
        if(user!=False):
            ##----asking password---------------
            q=input("Enter new Password:")
            while (q==n):
                print("\n",">>> Invalid password")
                print(">>> You should not take user name as password","\n")
                q=input("Enter new Password:")
            p=valid_check(q)
            p1=input("Confirm password  :")
            while(p1!=p ):
                print("\n",">>> Confirmation password is wrong","\n")
                q=input("Enter new Password re-again:")
                while (q==n):
                    print(">>> Invalid password")
                    print(">>> You should not take user name as password","\n")
                    q=input("Enter new Password:")
                p=valid_check(q)
                p1=input("Confirm password  :")
            print()
            ##-------asking shool name--------
            m=input("In which school your child hood education was done:")
            print()
            c="School name"
            rq=check_valid(m,c)
            while (p==rq):
                print("\n",">>> Invalid School name")
                print(">>> You should not take password as School name","\n")
                m=input("In which school your child hood education was done:")
                c="School name"
                rq=check_valid(m,c)
            rq=rq.lower()
            ##------creating user file----------
            file=file_name(n,p)
            file1=act_path+"/"+file
            f=open(file1,"a")
            f.close()
            ##---------Storing user details in database------------
            add_data(dta,n,p,rq)
            print("---Your account is successfully created---","\n")
        else:
            pass
    ##-----LOG IN----------
    elif(i==2):
        l=log_in()
        n,p,user_verify,pass_verify=l[0],l[1],l[2],l[3]
        ##-----------Login features-----------
        if (user_verify==True and pass_verify==True):
            print("\n","---Your Successfully Logged in----","\n")
            log_menu()
            print("Enter numer of above login menu as you want: 1  # To add Chapter")
            print("::"*25)
            j=int(input("Enter login menu number  as you want:"))
            file,e=file_name(n,p),0
            file1=act_path+"/"+file
            chap=all_chapters(file1)
            while (j>=1 and j<=6):
                ##-----adding chapter------------
                if (j==1):
                    print()
                    t=input("Enter Title name :")
                    if (t.endswith(":")):
                        tit=t
                    else:
                        tit=t+":"
                    t=tit.title()
                    if (t in chap):
                        print("\n",">>> Title name alredy used","\n")
                        chapter=False
                    if(chapter!=False):
                        while( len(t)==0 or t[0]==" "):
                            if(len(t)==0):
                                print(">>> You not entered Title name")
                                print()
                            elif(t[0]==" "):
                                print(">>> Title not start with space","\n")
                            t=input("Enter Title:")
                        print("NOTE: If you want stop enteing data ")
                        print("      Press Enter key with out entering data ","\n")
                        n,i=input("Enter a "+ str(1)+"st"+" line:").capitalize(),1
                        while n:
                            if(i==1):
                                add_data(file1,t)
                                add_data(file1," ")    
                            add_data(file1,n)
                            i+=1
                            if (i==2):
                                n=input("Enter a "+ str(i)+"nd"+" line:")
                            elif(i==3):
                                n=input("Enter a "+ str(i)+"rd"+" line:")
                            else:
                                n=input("Enter a "+ str(i)+"th"+" line:")
                        x=70*"-"
                        add_data(file1,x)
                    else:
                        pass
                ##-----adding text in a content----------
                elif(j==2):
                    ti=input("Enter Title (or) Chapter in which you want to add text:")
                    print()
                    x,num_list=chapter_data(file1,ti),[]
                    if(x!=None):
                        for i in range(len(x)):
                            print(x[i])
                            num_list.append(str(i+1))
                    print()
                    if(x!=None):
                        text_menu()
                        print("Enter numer of above text menu as you want: 2  # To add new line")
                        print("-"*25)
                        w=int(input("Enter numer of above text menu as you want:"))
                        while (w==1 or w==2):
                            ##-------- Add text in a line------------
                            if(w==1):
                                display_lines(x)
                                print("\n","NOTE: If you want stop addiing text (or) new line  ")
                                print("      Press Enter key with out entering data ","\n")
                                l=input("Enter corresponding line number in which you want to add text:")
                                if(l in num_list):
                                    line=x[int(l)+1]
                                    li=line_to_word(line)
                                    w,w1,list,new,fl,new_chap,c=li[0],li[1],li[2],"","",[],0
                                    print("\n",w1,"\n")
                                    n=input("Enter a number at which you want to add text:")
                                    while (n!=""):
                                        if( (int(n) in list)):
                                            if(int(n)==(len(w)+1)):
                                                w.append(" ")
                                                print(w)
                                            for i in range(len(w)):
                                                if(i+1==int(n)):
                                                    t=input("Enter text:")
                                                    if(new==""):
                                                        new=t+" "+w[i]
                                                    elif(i==(len(w)-1)):
                                                         new=new+" "+t
                                                    else:
                                                        new=new+" "+t+" "+w[i]
                                                    c+=1
                                                else:
                                                    if(new==""):
                                                       new=w[i]
                                                    else:
                                                        new=new+" "+w[i]
                                            print(new)
                                            li=line_to_word(new)
                                            w,w1,list,new=li[0],li[1],li[2],""
                                            print(w1,"\n")
                                            n=input("Enter a number at which you want to add text:")
                                    for i in w:
                                        if(fl==""):
                                            fl=i
                                        else:
                                            fl=fl+" "+i
                                    print("new",fl.capitalize())
                                    print(int(l) in range(len(x)))
                                    for i in range(len(x)):
                                        if(int(l)+1==i):
                                            new_chap.append(fl.capitalize())
                                        else:
                                            new_chap.append(x[i])
                                        
                                    if(c>0):
                                        t=x[0]
                                        insert_chap(file1,t,new_chap)
                            ##-------add new line------------
                            elif(w==2):
                                x=chapter_data(file1,ti)
                                display_chapter(x)
                                print("\n","NOTE: If you want stop addiing text (or) new line  ")
                                print("      Press Enter key with out entering line number ","\n")
                                l,c,nc,y=input("Enter a number where you want to add new line:"),0,x,[]
                                while (l!="" and (int(l) in range(1,len(nc)+1))):
                                    t=input("Enter new line text:")
                                    if(t!=""):
                                        for i in range(len(nc)):
                                            y.append(nc[i])
                                            if(i==int(l)):
                                                y.append(t.capitalize())
                                        display_chapter(y)
                                        nc,y=y,[]
                                        l=input("Enter a number where you want to add new line:")
                                        c+=1
                                if(c>0):
                                    t=x[0]
                                    insert_chap(file1,t,nc)
                            print("-"*25)
                            tm+=1
                            if(tm==2):
                                text_menu()
                                tm=0
                            w=int(input("Enter numer of above text menu as you want:"))
                ##--------Edit Chapter-----------------
                elif(j==3):
                    ti=input("Enter Title (or) Chapter  name you want to edit:")
                    print()
                    x,num_list=chapter_data(file1,ti),[]
                    if(x!=None):
                        for i in range(len(x)):
                            print(x[i])
                            num_list.append(str(i+1))
                    if(x!=None):
                        print()
                        c=input("Doy want to edit "+ti+" Chapter  yes (or) no:").lower()
                        if(c=="yes"):
                            edit_menu()
                            print("Eter menu numbers of above data as you like to edit : 3 #remove line" )
                            print("."*40)
                            e=int(input("Enter menu numbers of edit  data as you like to edit :"))
                            print()
                            while(e>=1 and e<=3):
                                ##--------Replace words in a line------------
                                if(e==1):
                                    display_lines(x)
                                    print("\n","NOTE: If you want stop removing (or) replacing  ")
                                    print("      Press Enter key with out entering data ","\n")
                                    l=input("Enter corresponding line number in which you want to replace words :")
                                    if(l in num_list):
                                        line=x[int(l)+1]
                                        z=word_number(line)
                                        wl,wn,new,new_chap,count,fl=z[0],z[1],"",[],0,""
                                        print("\n",wn,"\n")
                                        n=input("Enter a word number which you want to replace:")
                                        while (n!=""):
                                            for i in range(len(wl)):
                                                if(i+1==int(n)):
                                                    t=input("Enter new word:")
                                                    if(new==""):
                                                        new=t
                                                    else:
                                                        new=new+" "+t
                                                    count+=1
                                                else:
                                                    if(new==""):
                                                       new=wl[i]
                                                    else:
                                                        new=new+" "+wl[i]
                                            print(new)
                                            z=word_number(new)
                                            wl,wn,new=z[0],z[1],""
                                            print(wn,"\n")
                                            n=input("Enter a number at which you want to replace:")                                   
                                        for i in wl:
                                            if(fl==""):
                                                fl=i
                                            else:
                                                fl=fl+" "+i
                                        for i in range(len(x)):
                                            if(i==int(l)+1):
                                                print("fl",fl)
                                                new_chap.append(fl.capitalize())
                                            else:
                                                new_chap.append(x[i])
                                        print(new_chap)
                                        if(count>0):
                                            t=x[0]
                                            insert_chap(file1,t,new_chap)
                                ##--------Remove words in a line------------
                                elif(e==2):
                                    display_lines(x)
                                    print("\n","NOTE: If you want stop removing (or) replacing  ")
                                    print("      Press Enter key with out entering data ","\n")
                                    l=input("Enter corresponding line number in which you want to replace words :")
                                    if(l in num_list):
                                        line=x[int(l)+1]
                                        z=word_number(line)
                                        wl,wn,new,new_chap,count,fl=z[0],z[1],"",[],0,""
                                        print("\n",wn,"\n")
                                        n=input("Enter a word number which you want to remove:")
                                        while (n!=""):
                                            for i in range(len(wl)):
                                                if(i+1!=int(n)):
                                                    if(new==""):
                                                       new=wl[i]
                                                    else:
                                                        new=new+" "+wl[i]
                                            print(new)
                                            z=word_number(new)
                                            wl,wn,new=z[0],z[1],""
                                            print(wn,"\n")
                                            n=input("Enter a number at which you want to remove:")                                   
                                        for i in wl:
                                            if(fl==""):
                                                fl=i
                                            else:
                                                fl=fl+" "+i
                                        for i in range(len(x)):
                                            if(i==int(l)+1):
                                                print("fl",fl)
                                                new_chap.append(fl.capitalize())
                                            else:
                                                new_chap.append(x[i])
                                        print(new_chap)
                                        if(count>0):
                                            t=x[0]
                                            insert_chap(file1,t,new_chap)
                                ##-----------remove line-----------
                                elif(e==3):
                                    display_lines(x)
                                    print("\n","Enter corresponding line number you want to delete")
                                    print("ex:2,4,5-6,")
                                    print("\n","NOTE: If you want stop deleting line ")
                                    print("      Press Enter key with out entering line number ","\n")
                                    l=input("Enter corresponding line number you want to delete:")
                                    delete,nc=False,x
                                    while l and l!=" ":
                                        m,x,nc=sort_del_lines(l),nc,[]
                                        for i in range(len(x)):
                                            if(i not in m):
                                                nc.append(x[i])
                                                delete=True
                                        display_lines(nc)
                                        print()
                                        l=input("Enter corresponding line number you want to delete:")
                                    if(delete==True):
                                        t=x[0]
                                        insert_chap(file1,t,nc)
                                edit_menu()
                                e=int(input("Enter menu numbers of edit  data as you like to edit :"))
                elif(j==4):
                    ##--------Deleting chapter------------
                    t=input("Enter Title (or) Chapter  name you want to Delete:")
                    print()
                    x=chapter_data(file1,t)
                    if(x!=None):
                        for i in x:
                            print(i)
                        if(x!=None):
                            title=True
                        else:
                            title=False
                        if (title==True):
                            print()
                            c=input("Are you sure to delete "+t.title()+" Chapter yes (or) no :").lower()
                            if (t.endswith(":")):
                                tit=t
                            else:
                                tit=t+":"
                            t=tit.title()
                            t1=t[:-1]
                            if(c=="yes"):
                                del_chapter(file1,t)
                                print("\n","---",t1.title(),"chapter is deleted-----","\n")
                elif(j==5):
                    ##--------Displaying chapter-----------
                    t=input("Enter chapter (or) Title name:")
                    print()
                    x=chapter_data(file1,t)
                    if(x!=None):
                        for i in x:
                            print(i)
                elif(j==6):
                    ##------Display alll chapters----------
                    print()
                    print("_"*25)
                    with open(file1,"r") as uf:
                        l,j1=0,1
                        for line in uf:
                            l+=1
                        uf.seek(0)
                        for line in uf:
                            if(j1<l):
                                if(de_code(line)!=70*"-"):
                                    print(de_code(line))
                                else:
                                    print("_"*25)
                            j1+=1
                print("::"*25)
                lm+=1
                if (j!=4 and j!=5 and j!=6 and j!=7):
                    log_menu()
                    lm=0
                j=int(input("Enter login menu number  as you want:"))
    ##----------Manage account------------
    elif(i==3):
        account_menu()
        print("ex: Eter menu numbers of Manage acoount data as you want: 2 #Change password","\n")
        e=int(input("Enter menu numbers of above  Manage acoount data as you want:"))
        print()
        while(e>=1 and e<=3):
            ##----------forgot password----------------
            if(e==1):
                ##.....finding length of database....
                f5=open(dta,"r")
                a,le=f5.readline(),0
                while a:
                    le+=1
                    a=f5.readline()
                f5.close()
                ##.....knowing user name line.....
                m=[i for i in range(1,le+1,3)]
                ##...storing alll user names.....
                f5=open(dta,"r")
                a=f5.readline()
                k,ru=1,[]
                while a:
                    if (k in m):
                        s=de_code(a)
                        ru.append(s)
                    a=f5.readline()
                    k+=1
                ##.....Cheking user found or not.....
                nc=3
                n=input("Eter user name:")
                if(n not in ru):
                    nc=nc-1
                    while ((n not in ru) and nc>0):
                        print("\n",">>> Username not fount re-try",sep="")
                        print(">>>",nc,"Chances left to enter correct user name ","\n")
                        n=input("Eter user name:")
                        if(n in ru):
                            break
                        nc=nc-1
                    else:
                        print("\n",">>> Username not fount re-try")
                        print(">>> Your Chances are over try_again")
                        print("<"*30,end="")
                        print(">"*35)
                        i=int(input("Enter menu number of above data as you want:"))
                        continue
                else:
                    n=n
                ##........Knowing user school & password name ..........
                with open(dta,"r") as d:
                    a=d.readline()
                    l,k=[],1
                    while a:
                        if(de_code(a)==n):
                            l.append(a)
                            x=d.readline()
                            p1=de_code(x)
                            y=d.readline()
                            sc1=de_code(y)
                            k+=1
                            break
                        else:
                            l.append(a)
                        a=d.readline()
                        k+=1
                ##....knowing user file name......
                file=file_name(n,p1)
                file1=act_path+"/"+file
                ##.........if schoool name correct then asking new password......
                sc=input("Enter your school name:").lower()
                ncl=3
                if sc!=sc1:
                    ncl=ncl-1
                    while(sc!=sc1 and ncl>0):
                        print("\n",">>> School name is in correct re-enter")
                        print(">>>",ncl,"Chances left to enter correct school name","\n")
                        sc=input("Enter your school name:").lower()
                        if (sc==sc1):
                            print()
                            q=input("Enter new password:")
                            while (q==n):
                                print(">>> Invalid password")
                                print(">>> You should not take user name as password","\n")
                                q=input("Enter new Password:")
                            p=valid_check(q)
                            p1=input("Confirm password:")
                            while(p1!=p ):
                                print("\n","Confirmation password is wrong","\n")
                                q=input("Enter new Password re-again:")
                                while (q==n):
                                    print("Invalid password")
                                    print("You should not take user name as password","\n")
                                    q=input("Enter new Password:")
                                p=valid_check(q)
                                p1=input("Confirm password:")
                            break
                        ncl=ncl-1
                    else:
                        print(">>> Your Chances are over try_again")
                        i=int(input("Enter menu number of above data as you want:"))
                        continue
                else:
                    print()
                    q=input("Enter new password:")
                    while (q==n):
                        print(">>> Invalid password")
                        print(">>> You should not take user name as password","\n")
                        q=input("Enter new Password:")
                    p=valid_check(q)
                    p1=input("Confirm password:")
                    while(p1!=p):
                        print("\n",">>>Confirmation password is wrong","\n")
                        q=input("Enter new Password re-again:")
                        while (q==n):
                            print(">>> Invalid password")
                            print(">>> You should not take user name as password","\n")
                            q=input("Enter new Password:")
                        p=valid_check(q)
                        p1=input("Confirm password:")
                    l.append(to_Binary(p))
                ##......if  user entered school name is match exactly.....Creating new pasword....
                if (sc==sc1):
                    with open(dta,"r") as d2:
                        a=d2.readline()
                        j=1
                        while a:
                            if (j>k):
                                l.append(a)
                            a=d2.readline()
                            j+=1
                    f=open(dta,"w")
                    f.close()
                    with open(dta,"a") as d3:
                        d3.writelines(l)
                    ##.....copying data of a user....
                    with open(file1,"r") as f5:
                        l=f5.readlines()
                    ##...removing old file....
                    os.remove(file1)
                    ##.... creatig file with new password....
                    file=file_name(n,p)
                    file1=act_path+"/"+file
                    ##....writing user copied data to knew file....
                    with open(file1,"a") as f3:
                        f3.writelines(l)
                    print("\n","--Your password is changed successfully---")
                    print("Your new password is:-",q,"\n")
            ##----------Changing password------------------
            elif(e==2):
                with open(dta,"r") as f5:
                    le=0
                    a=f5.readline()
                    while a:
                        le+=1
                        a=f5.readline()
                l=log_in()
                n,p,user_verify,pass_verify=l[0],l[1],l[2],l[3]
                if (user_verify==True and pass_verify==True):
                    file=file_name(n,p)
                    file1=act_path+"/"+file
                    c=input("Are you sure to Change your Password yes (or) no :").lower()
                    if(c=="yes"):
                        print()
                        np=input("Enter new password:")
                        cp=input("Confirm password again:")
                        while (np!=cp):
                            print("\n",">>> Confirmation password is wrong","\n")
                            np=input("Enter new password:")
                            cp=input("Confirm password again:")
                        l,k,m=[],1,[i for i in range(1,le+1,3)]
                        print(m)
                        with open(dta,"r") as f:
                            for line in f:
                                if(k in m and (n==de_code(line))):
                                    l.append(line)
                                    break
                                else:
                                    l.append(line)
                                k+=1
                        l.append(to_Binary(np))
                        j,i=k+1,1
                        with open(dta,"r") as f1:
                            for line in f1:
                                if(i>j):
                                    l.append(line)
                                i+=1
                        f=open(dta,"w")
                        f.close()
                        with open(dta,"a") as f2:
                            for i in l:
                                f2.write(i)
                        print()
                        with open(file1,"r") as f5:
                            l=f5.readlines()
                        os.remove(file1)
                        file=file_name(n,np)
                        file1=act_path+"/"+file
                        with open(file1,"a") as f3:
                            f3.writelines(l)
                        print("---Your password is successsfully changed--- ","\n")
                        print("::"*25)
            ##-------Delete acccount------------------
            elif(e==3):
                with open(dta,"r") as f5:
                    le=0
                    a=f5.readline()
                    while a:
                        le+=1
                        a=f5.readline()
                l=log_in()
                n,p,user_verify,pass_verify=l[0],l[1],l[2],l[3]
                if (user_verify==True and pass_verify==True):
                    print()
                    print("Hellow ,",n)
                    re_ver=input("Are you sure to delete your account (yes or no):").lower()
                    if (re_ver=="yes"):
                        l,k,m=[],1,[i for i in range(1,le+1,3)]
                        with open(dta,"r") as f:
                            for line in f:
                                if(k in m and (n==de_code(line))):
                                        break
                                else:
                                    l.append(line)
                                k+=1
                        j,i=k+2,1
                        with open(dta,"r") as f1:
                            for line in f1:
                                if(i>j):
                                    l.append(line)
                                i+=1
                        f=open(dta,"w")
                        f.close()
                        with open(dta,"a") as f2:
                            for i in l:
                                f2.write(i)
                        file=file_name(n,p)
                        file1=act_path+"/"+file
                        os.remove(file1)
                        print("\n","---Your account is deleted Successfully----","\n")
            am+=1
            if(am==2):
                account_menu()
                am=0
                print()
            
            break
    elif(i==4):
        help_menu()    
    print("<"*27,end="")
    print(">"*30,"\n")
    mm+=1
    if(mm==2 and (i==1 and user!=False)):
        main_menu()
        mm=0
    i=int(input("Enter menu number of above data as you want:"))
    print()