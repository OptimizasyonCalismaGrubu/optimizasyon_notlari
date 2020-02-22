# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + pycharm={"is_executing": false}
import pandas as pd
import numpy as np

# + pycharm={"is_executing": false}
v1=[1,3]

# + pycharm={"is_executing": false}
v2=[2,4]

# + pycharm={"is_executing": false}
matrix=[v1,v2]

# + pycharm={"is_executing": false}
matrix

# + pycharm={"is_executing": false}
np.array(matrix).shape

# + pycharm={"is_executing": false}
pd.DataFrame(np.array(matrix) )
# -


# #  Matris ve Vektör
#

# + pycharm={"is_executing": false}
1 #Scalar

# + pycharm={"is_executing": false}
[1] # Vektör

# + pycharm={"is_executing": false}
[1,1] # Vektör 1,2

# + pycharm={"is_executing": false}
[[1,1],[1,1]] # Matris 2,2

# + pycharm={"is_executing": false}
a00=1;a01=0;a10=7;a11=3;a20=7;a21=3


# + pycharm={"is_executing": false}
A=np.array([[a00,a01],[a10,a11],[a20,a21]])

# + pycharm={"is_executing": false}
pd.DataFrame(A)

# + pycharm={"is_executing": false}
A.shape[1]

# + pycharm={"is_executing": false}
A[1][1]

# + pycharm={"is_executing": false}
A=np.array([1,2])

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
A.shape

# + pycharm={"is_executing": false}
Satır_Vektor=np.array([1,2,3,34,2])

# + pycharm={"is_executing": false}
u=np.array([1,2]);v=np.array([1,-3])
w=np.array([-1,-2])


# + pycharm={"is_executing": false}
u =np.array( [1, 2, 3] )

# + pycharm={"is_executing": false}
v=  np.array( [2,1,2] )

# + pycharm={"is_executing": false}
u.dot(v)

# + pycharm={"is_executing": false}
u.view

# + pycharm={"is_executing": false}
u+v #matris toplama

# + pycharm={"is_executing": false}
u=np.array([1,2]);v=np.array([2,1])
w=u+v;w

# + pycharm={"is_executing": false}



# + pycharm={"is_executing": false}
def doğru_parçası(c,u,v):
       return c*u + (1 - c)*v


# + pycharm={"is_executing": false}
c=0
doğru_parçası(c,u,v)


# + pycharm={"is_executing": false}
c=1
doğru_parçası(c,u,v)


# + pycharm={"is_executing": false}
c=0.5
doğru_parçası(c,u,v)

# + pycharm={"is_executing": false}
# Tranpozu, Devrik

# + pycharm={"is_executing": false}
A=np.array([[a00,a01],[a10,a11],[a20,a21]])

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
A.T

# + pycharm={"is_executing": false}
A.transpose().shape

# + pycharm={"is_executing": false}
A.shape

# + pycharm={"is_executing": false}
A.T.T

# + pycharm={"is_executing": false}
A=np.array([[1,1,2],[2,1,3]])
B=np.array([[1,1],[2,3],[1,2]])
A.dot(B)


# + pycharm={"is_executing": false}
def vektörel_çarpım(A,B):
    return A.dot(B)


# + pycharm={"is_executing": false}
A=np.array([[3],[4]]);B=np.array([[1, 2]]);

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B)

# + pycharm={"is_executing": false}
vektörel_çarpım(B,A)

 # LEBG
# -

# ![image.png](attachment:image.png)

# + active=""
# class insan(a,b):
#     adı=a
#     def gökhanfonksiyonu(c):
#         def gökhanfonksiyonu2(q):
#             return a+b
#     
#     

# + active=""
# sum()

# + active=""
# sum="akaka"

# + active=""
# sum([1,2,34])

# + pycharm={"is_executing": false}
A=np.array([[1,2],[3,4]]);B=np.array([[1,1],[0,1],[1,2]]);

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B) # Vektörel çarpımda ilk matrisin sütün sayısı ile ikinci matrisin satır sayısı aynı olmalı

# + pycharm={"is_executing": false}
vektörel_çarpım(B,A)

# + pycharm={"is_executing": false}
PremiumUnleaded=np.array([3/4,1/4])
RegularUnleaded=np.array([2/3,1/3])
RegularLeaded=np.array([1/4,3/4])

# + pycharm={"is_executing": false}
mainTable=np.array([PremiumUnleaded,RegularUnleaded,RegularLeaded])

# + pycharm={"is_executing": false}
mainDataFrame=pd.DataFrame(mainTable,columns=("crude1","crude2"))

# + pycharm={"is_executing": false}
mainDataFrame.index=["PremiumUnleaded","RegularUnleaded","RegularLeaded"]

# + pycharm={"is_executing": false}
mainDataFrame

# + pycharm={"is_executing": false}
Stock=np.array([10,6,5])

# + pycharm={"is_executing": false}
vektörel_çarpım(Stock,mainDataFrame)

# + pycharm={"is_executing": false}
# Kural 1 Satır

# + pycharm={"is_executing": false}
A=np.array([[1,1,2],[2,1,3]]);B=np.array([[1,1],[2,3],[1,2]])

# + pycharm={"is_executing": false}
A[1]

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B)

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B)[0]

# + pycharm={"is_executing": false}
vektörel_çarpım(A[0],B)

# + pycharm={"is_executing": false}
# Kural 2 Sütün

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B[:,0])

# + pycharm={"is_executing": false}
vektörel_çarpım(A,B)[:,0]

# + pycharm={"is_executing": false}
# Geçişkenlik Kuralı

# + pycharm={"is_executing": false}
A=np.array([1,2]) ; B=np.array([[2,3],[4,5]]);C=np.array([[2],[1]])

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
B

# + pycharm={"is_executing": false}
C

# + pycharm={"is_executing": false}
vektörel_çarpım(vektörel_çarpım(A,B),C)

# + pycharm={"is_executing": false}
vektörel_çarpım(A,vektörel_çarpım(B,C))

# + pycharm={"is_executing": false}
vektörel_çarpım(vektörel_çarpım(A,B),C)==vektörel_çarpım(A,vektörel_çarpım(B,C))
# -

# ## Problemler
#

#
# ### 1. Problem

# + pycharm={"is_executing": false}

A=np.array([[1,2,3],[4,5,6],[7,8,9]]);B=np.array([[1,2],[0,-1],[1,2]])

# + pycharm={"is_executing": false}

print("A :\n", A,"\n")



# + pycharm={"is_executing": false}
print("B :\n", B,"\n")


# + pycharm={"is_executing": false}
 
print("-A :\n", A*-1,"\n")



# + pycharm={"is_executing": false}
print("3A :\n", A*3,"\n")


# + pycharm={"is_executing": false}

print("A+2B : \n",A+2*B)


# + pycharm={"is_executing": false}

print("A transpose : \n" , A.T  )


# + pycharm={"is_executing": false}
      
print("B transpose : \n" , B.T  )

# + pycharm={"is_executing": false}
print("AB transpose : \n" , A.dot(B)  )

# + pycharm={"is_executing": false}
print("BA transpose : \n" , B.dot(A)  )
# -

# ### 2. Problem

# + pycharm={"is_executing": false}
Bira1=[.5,.3,.2]
Bira2=[0,.7,.3]
Bira3=[.1,.3,.6]
Bira_dict={"Bira1":Bira1
          ,"Bira2":Bira2,
          "Bira3":Bira3}

# + pycharm={"is_executing": false}
Bira_df=pd.DataFrame(Bira_dict,index=["Bira1","Bira2","Bira3"])

# + pycharm={"is_executing": false}
Bira_df

# + pycharm={"is_executing": false}
x1=pd.DataFrame({"t1":[0,10,90]},index=["Bira1","Bira2","Bira3"])

# + pycharm={"is_executing": false}
x1

# + pycharm={"is_executing": false}
Bira_df.shape

# + pycharm={"is_executing": false}
x1.shape

# + pycharm={"is_executing": false}
y1=Bira_df.dot(x1)

# + pycharm={"is_executing": false}
y1
# -

# ### 3.Problem

# + pycharm={"is_executing": false}
A=np.array([1,2]) ; B=np.array([[2,3],[4,5]]);C=np.array([[2],[1]])
vektörel_çarpım(vektörel_çarpım(A,B),C)==vektörel_çarpım(A,vektörel_çarpım(B,C))
# -

# ### 4.Problem

# + pycharm={"is_executing": false}
A=np.array([1,2]) ; B=np.array([[2,3],[4,5]])
print(" (AB)T :\n", vektörel_çarpım(A,B).T)
print(" BT*AT :\n",vektörel_çarpım(B.T,A.T))
vektörel_çarpım(A,B).T==vektörel_çarpım(B.T,A.T)
# -

# ### 5.Problem

# + pycharm={"is_executing": false}
A=np.array([[1,2],[2,1]]);
print(" A : \n",A)
print(" A.T : \n",A.T)

print(" A==A.T : \n",A==A.T  )

# + pycharm={"is_executing": false}
# a 
print("A*A.T simetrik \n" , A.dot(A.T)==A.dot(A.T).T)

# + pycharm={"is_executing": false}
# b 
print("A+A.T simetrik \n" , (A+A.T)==(A+A.T).T)
# -

# ### 6.Problem

# + pycharm={"is_executing": false}
A=np.array([[1,1],[1,1]]);
B=np.array([[2,1],[1,2]]);

# + pycharm={"is_executing": false}
A.shape

# + pycharm={"is_executing": false}
B.shape

# + pycharm={"is_executing": false}
n=A.shape[0]

# + pycharm={"is_executing": false}
n**3 # Gereken çarpma sayısı

# + pycharm={"is_executing": false}
n**3-n**2 # Gereken toplama sayısı


# -

# ### 7.Problem

# + pycharm={"is_executing": false}
def matriks_izi(A):
    return np.array([A[i][i] for i in range(len(A))])


# + pycharm={"is_executing": false}
# a
matriks_izi(A+B)==(matriks_izi(A)+matriks_izi(B))

# + pycharm={"is_executing": false}
# b
matriks_izi(vektörel_çarpım(A,B))  == matriks_izi(vektörel_çarpım(B,A))
# -

# ## Lineer Denklemlerin Matrisleri

# + pycharm={"is_executing": false}
a11=None;a12=None;a13=None;a21=None;a22=None;a23=None; a31=None;a32=None;a33=None;

A=np.array([[a11,a12,a13],
[a21,a22,a23],
[a31,a32,a33]])


# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
x11=None;x12=None;x13=None;x21=None;x22=None;x23=None; x31=None;x32=None;x33=None;

X=np.array([[x11,x12,x13],
[x21,x22,x23],
[x31,x32,x33]])

# + pycharm={"is_executing": false}
b1=None;b2=None;b3=None;
B=np.array([b1,b2,b3])

# + pycharm={"is_executing": false}
B

# + pycharm={"is_executing": false}
A.dot(X)==B
# -

# <b><i> X değişken , A ve B sabittir. A*X=B </b></i> 

# <b> Örnek Olarak : </b>  

# + pycharm={"is_executing": false}
A=np.array([[1,2],[2,-1]])
B=np.array([[5],[0]])

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
B

# + pycharm={"is_executing": false}
X=np.array([[1],[2]])

# + pycharm={"is_executing": false}
A.dot(X)==B

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
B

# + pycharm={"is_executing": false}
# A|b
np.concatenate((A,B), axis=1)

# + pycharm={"is_executing": false}
# Problem 

A=np.array([[1,-1],[2,1],[1,3]])
B=np.array([[4],[6],[8]])

np.concatenate((A,B), axis=1)
# -

# ## Gauss-Jordan Metodu ile Lineer Denklem Çözümü

# + pycharm={"is_executing": false}
# Durum 1 : Sistemin çözümü yoktur.
# Durum 2 : Sistemin tek bir çözümü vardır.
# Durum 3 : Sistemin sonsuz çözümü vardır.
# -

# #### Satır Operasyonları (ERO)

# + pycharm={"is_executing": false}
# ERO 1  : herhangi bir satırı bir sabit ile çarpmak 
A=np.array([[11,-1],[12,1],[1,37]])

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false}
A[0]=A[0]*33

# + pycharm={"is_executing": false}
A

# + pycharm={"is_executing": false, "name": "#%%\n"}
# ERO 2  : herhangi  diğer satıra eklemek
A=np.array([[11,-1],[12,1],[1,37]])
A[2]=A[2]+A[0]*5
A

# + pycharm={"name": "#%%\n", "is_executing": false}
# ERO 3 : İki satırın yerlerini değiştirmek 
A=np.array([[11,-1],[12,1],[1,37]])
Geçici_Değişken=A[0].copy() # .copy() yapmazsak aynı yere kaydediyor.
A[0]=A[2]
A[2]=Geçici_Değişken
A



# + pycharm={"name": "#%%\n", "is_executing": false}
# x1+x2 = 2  ve 2x1 + 4x2 =7 denklemini bu öğrendiklerimiz ile çözelim.

A=np.array([[1,1,2],[2,4,7.0]],float)
A




# + pycharm={"name": "#%%\n", "is_executing": false}
A[1]=A[1]/2  # ERO1
A

# + pycharm={"name": "#%%\n", "is_executing": false}
A[1]=A[1]-A[0]  # ERO2
A



# + pycharm={"name": "#%%\n", "is_executing": false}
A[0]=A[0]-A[1]  # ERO2
A


# + pycharm={"name": "#%%\n", "is_executing": false}
[x1,x2]=A[:,2]
print("x1 : {x1} ve x2: {x2}".format(x1=x1,x2=x2))



# -

# ### Gauss Jordan İle Çözüm 

# + pycharm={"name": "#%%\n", "is_executing": false}
A=np.array([[2,2,1],[2,-1,2],[1,-1,2]],float) # Katsayı
b=np.array([[9],[6],[5]],float) # y 

Ab=np.concatenate((A,b),axis=1) # matrisleri birleştirdik

Ab 



# +
Ab1=Ab.copy() # ilk işlem olarak birinci satırın ilk elemanı 1 olacak şekilde ERO işlemi yaptık
Ab1[0]=Ab1[0]/2

Ab1

# + pycharm={"name": "#%%\n", "is_executing": false}
Ab2=Ab1.copy() # Sonrasında 2 ve 3. satırların ilk sütünlarını 0 olacak şekilde ERO işlemleri yapıyoruz.
Ab2[1]=Ab2[1]-2*Ab1[0]
Ab2

# + pycharm={"name": "#%%\n", "is_executing": false}
Ab3=Ab2.copy()
Ab3[2]=Ab2[2]-Ab2[0]

Ab3


# + pycharm={"name": "#%%\n", "is_executing": false}
Ab3[1]=Ab3[1]*(-1/3) # Yukarıda birinci satır için yaptığımız işlemleri 2. ve 3 satırlar için de yapıyoruz.

Ab3[0]=Ab3[0]-Ab3[1]

Ab3[2]=Ab3[2]+2*Ab3[1]
Ab3

# + pycharm={"name": "#%%\n", "is_executing": false}
Ab4=Ab3.copy()

Ab4[2]=Ab4[2]*(6/5)

Ab4[0]=Ab4[0]-Ab4[2]*(5/6)

Ab4[1]=Ab4[1]+Ab4[2]*(1/3)


# -

np.round(Ab4,6) 

[x1,x2,x3]=Ab4[:,3]

print("x1 : {x1} , x2: {x2} ve x3: {x3} olarak bulunmuştur.".format(x1=x1,x2=x2,x3=x3))

# +
## Çözümsüz veya Sonsuz Çözümlü Denklemler
# -

# Örnek 6
A=np.array([[1,2],[2,4]]);b=np.array([[3],[4]])
Ab=np.concatenate((A,b),axis=1)

Ab

Ab[1]=Ab[1]-2*Ab[0]

Ab

Ab[1] # x1 ve x2 ye ne verirsek verelim sonuç -2 olmaz. Bu yüzden ÇÖZÜMSÜZDÜR.

# +
# Eğer A nın bir satırı tamamen 0 oluyor ve buna karşılık b nin o satıra ait değeri 0 olmuyorsa bu sistemin çözümü yoktur.

# +
# Örnek 7
# -
A=np.array([[1,1,0],[0,1,1],[1,2,1]]);b=np.array([[1],[3],[4]]);
Ab=np.concatenate((A,b),axis=1)


Ab[2]=Ab[2]-Ab[0]

Ab

Ab[0]=Ab[0]-Ab[1]

Ab[2]=Ab[2]-Ab[1]

Ab

a=[i for i in range(4)];a.pop(1);a


# +
# Gauss Jordan Metodu 

def GaussJordan(A,b):
    
    # Adım 1 : A|b matrisini oluştur. 
    
    Ab=np.concatenate((A,b),axis=1)
    
    # Adım 2a :  İlk satır ilk kolon ile başla 0 a eşit değilse ERO değişimi yaparak ilk sütünü 1 0 0 0 ... 0 haline getir.
    
    satır_sayısı=Ab.shape[0]
    sutun_sayısı=Ab.shape[1]
    
    for i in range(satır_sayısı):
        if not Ab[i][i]==0:
            Ab[i]=Ab[i]/Ab[i][i]    
            satır_indisleri=[a for a in range(satır_sayısı)]
            satır_indisleri.pop(i)
            for j in satır_indisleri:
                Ab[j]=Ab[j]-Ab[i]*Ab[j][i]
                
    # Adım 2b : Eğer ilk kolon ve sütün 0 ise diğer bir sütünla ilk sütünü değiştir.  
    
        elif Ab[i][i]==0:
            Geçici=Ab[i].copy()
            satır_indisleri=[a for a in range(satır_sayısı)]
            satır_indisleri.pop(i)
            a=0
            for j in satır_indisleri:
                if a==0:
                    Ab[i]=Ab[j].copy()
                    Ab[j]=Geçici
                

    return Ab
# -





# + code_folding=[]
class DoğrusalDenklem():
    
    def __init__(self,A,b):
        self.denklem=np.concatenate((A,b),axis=1)
        self.satır_sayısı=self.denklem.shape[0]
        self.sütün_sayısı=self.denklem.shape[1]
        print("{n} bilinmeyenli doğrusal denklem sistemi oluşturulmuştur.".format(n=A.shape[1],Ab=self.denklem))
    
    def __str__(self):
        return "Denklem sistemi ----> \n {Ab}".format(Ab=self.denklem)
    
    def __len__(self):
        return self.denklem.shape[0]

    def __del__(self):
        return  "Doğrusal denklem silinmiştir." 
    
    def GaussJordan(self):
        Ab=self.denklem.copy()
        satır_sayısı=self.satır_sayısı
        sutun_sayısı= self.sütün_sayısı

        for i in range(satır_sayısı):
            
            if not Ab[i][i]==0:
                Ab[i]=Ab[i]/Ab[i][i]    
                satır_indisleri=[a for a in range(satır_sayısı)]
                satır_indisleri.pop(i)
                for j in satır_indisleri:
                    Ab[j]=Ab[j]-Ab[i]*Ab[j][i]

        # Adım 2b : Eğer ilk kolon ve sütün 0 ise diğer bir sütünla ilk sütünü değiştir.  

            elif Ab[i][i]==0:
                Geçici=Ab[i].copy()
                satır_indisleri=[a for a in range(satır_sayısı)]
                satır_indisleri.pop(i)
                a=0
                for j in satır_indisleri:
                    if a==0:
                        Ab[i]=Ab[j].copy()
                        Ab[j]=Geçici
        
        return Ab
        
    
    def çözüm_durumu(self):
        çözüm=self.GaussJordan()
        satır_sayısı=self.satır_sayısı
        sutun_sayısı= self.sütün_sayısı
        tekÇözüm=False
        
        for i in range(satır_sayısı):
            if sum(çözüm[i,:sutun_sayısı-1])==0 and çözüm[i,sutun_sayısı-1]!=0:
                print("Denklem Kümesi Çözümsüzdür.")
                return "çözümsüz"
            
            
        tek_çözüm=0    
        for i in range(satır_sayısı):    
            if sum(çözüm[i,:sutun_sayısı-1])==1:
                tek_çözüm+=1
                if tek_çözüm==satır_sayısı:
                    tekÇözüm=True
                    print("Denklem Kümesinin Tek Çözümü mevcuttur.")
                    return "tek"

        for i in range(satır):
            if sum(örnek_denklem_çözümü[i,:sütün])==0:
                sonsuz_çözüm=True
                print("Denklem Kümesinin Sonsuz Çözümü mevcuttur.")
                return "sonsuz"
            elif tekÇözüm==False:
                print("Denklem Kümesinin Sonsuz Çözümü mevcuttur.")
                return "sonsuz"


# -

# ### Ana Değişkenler ve Doğrusal Denklemlerde Çözümleri 

# <i> Doğrusal denklem sistemlerini çözdükten sonra eğer bir satırda sadece bir sütünda 1 katsayısı var ve diğer sütünların katsayıları 0 ise bu değişkene <b> esas değişken (BV) </b>  denir.   </i>  <i> Aksi durumdaki değişkenler <b>  esas olmayan  (NBV)</b>  değişkenlerdir  .   </i>

def çözüm_durumu(örnek_denklem_çözümü):
        çözümsüz=False
        sonsuz_çözüm=False
        tek_çözüm=0
        tekÇözüm=False
        for i in range(satır):
            if sum(örnek_denklem_çözümü[i,:sütün-1])==0 and örnek_denklem_çözümü[i,sütün-1]!=0:
                çözümsüz=True
                print("Denklem Kümesi Çözümsüzdür.")
                return "çözümsüz"
              
        for i in range(satır):    
            if sum(örnek_denklem_çözümü[i,:sütün-1])==1:
                tek_çözüm+=1
                if tek_çözüm==satır:
                    print("Denklem Kümesinin Tek Çözümü mevcuttur.")
                    tekÇözüm=True
                    return "tek"

        for i in range(satır):
            if sum(örnek_denklem_çözümü[i,:sütün])==0:
                sonsuz_çözüm=True
                print("Denklem Kümesinin Sonsuz Çözümü mevcuttur.")
                return "sonsuz"
            elif tekÇözüm==False:
                print("Denklem Kümesinin Sonsuz Çözümü mevcuttur.")
                return "sonsuz"
            


# +
## Durum 1 

A=np.array([[1,0,0,1],[0,1,0,2],[0,0,1,3],[0,0,0,0],[0,0,0,0]],float)
b=np.array([[1],[1],[-1],[0],[2]],float)
# -

örnek_denklem_1=DoğrusalDenklem(A,b)

örnek_denklem_1.GaussJordan()

sonuç=örnek_denklem_1.çözüm_durumu()

print(sonuç)

# +
# Durum 2

A=np.array([[2,2, 1],[2,-1,2],[1,-1,2]],float)
b=np.array([[9],[6],[5]],float)

# -

örnek_denklem_2=DoğrusalDenklem(A,b)

örnek_denklem_2.GaussJordan()

sonuç=örnek_denklem_2.çözüm_durumu();

print(sonuç)

# Durum 3 
A=np.array([[1,0,0,1,1],[0,1,0,2,0],[0,0,1,0,1],[0,0,0,0,0]],float)
b=np.array([[3],[2],[1],[0]],float)


örnek_denklem_3=DoğrusalDenklem(A,b)

örnek_denklem_3.denklem

örnek_denklem_3.GaussJordan()

sonuç=örnek_denklem_3.çözüm_durumu()

sonuç


# ### Problemler 
#
#
#

# #### 1-8  Problemler

def problem_çözer(A,b):
    denklem=DoğrusalDenklem(A,b)
    print("Çözüm: \n",denklem.GaussJordan(),"\n")
    print("Çözüm durumu : ",denklem.çözüm_durumu(),"\n")


# 1 
A=np.array([[1,1,0,1],[0,1,1,0],[1,2,1,1]],float)
b=np.array([[3],[4],[8]],float)
problem_çözer(A,b)

# 2 
A=np.array([[1,1,1],[1,2,0]],float)
b=np.array([[4],[6]],float)
problem_çözer(A,b)

# 3 
A=np.array([[1,1],[2,1],[3,2]],float)
b=np.array([[1],[3],[4]],float)
problem_çözer(A,b)

# 4 
A=np.array([[2,-1,1,1],[1,1,1,0]],float)
b=np.array([[6],[4]],float)
problem_çözer(A,b)

# 5 
A=np.array([[1,0,0,1],[0,1,0,2],[0,0,1,.5],[0,0,2,1]],float)
b=np.array([[5],[5],[1],[3]],float)
problem_çözer(A,b)

# 6
A=np.array([[0,2,2 ],[1,2,1 ],[0,1,-1 ]],float)
b=np.array([[4],[4],[0]],float)
problem_çözer(A,b)

# 7
A=np.array([[1,1,0 ],[0,-1,2 ],[0,1,1 ]],float)
b=np.array([[2],[3],[3]],float)
problem_çözer(A,b)

# 8
A=np.array([[1,1,1 ,0],[0,1,2,1 ],[0,0,0,1 ]],float)
b=np.array([[1],[2],[3]],float)
problem_çözer(A,b)

# +
# 9 

A=np.array([[1,1,1 ,0],[0,1,2,1 ],[0,0,0,1 ]],float)
b=np.array([[1],[2],[3]],float)

değişken_sayısı=A.shape[1]
# -

bulunabilecek_değişken_sayısı=b.shape[0]

bulunabilecek_değişken_sayısı

değişken_sayısı

if bulunabilecek_değişken_sayısı>değişken_sayısı:
    print("Tek bir çözüm olma şansı mevcuttur.")
else:
    print("Tek bir çözüm olma şansı mevcut değildir.")


