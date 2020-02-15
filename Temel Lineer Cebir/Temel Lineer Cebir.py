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

import pandas as pd
import numpy as np

v1=[1,3]

v2=[2,4]

matrix=[v1,v2]

matrix

np.array(matrix).shape

pd.DataFrame(np.array(matrix) )


# #  Matris ve Vektör
#

1 #Scalar

[1] # Vektör

[1,1] # Vektör 1,2

[[1,1],[1,1]] # Matris 2,2

a00=1;a01=0;a10=7;a11=3;a20=7;a21=3


A=np.array([[a00,a01],[a10,a11],[a20,a21]])

pd.DataFrame(A)

A.shape[1]

A[1][1]

A=np.array([1,2])

A

A.shape

Satır_Vektor=np.array([1,2,3,34,2])

u=np.array([1,2]);v=np.array([1,-3])
w=np.array([-1,-2])


u =np.array( [1, 2, 3] )

v=  np.array( [2,1,2] )

u.dot(v)

u.view

u+v #matris toplama

u=np.array([1,2]);v=np.array([2,1])
w=u+v;w



def doğru_parçası(c,u,v):
       return c*u + (1 - c)*v


c=0
doğru_parçası(c,u,v)


c=1
doğru_parçası(c,u,v)


c=0.5
doğru_parçası(c,u,v)

# +
# Tranpozu, Devrik
# -

A=np.array([[a00,a01],[a10,a11],[a20,a21]])

A

A.T

A.transpose().shape

A.shape

A.T.T

A=np.array([[1,1,2],[2,1,3]])
B=np.array([[1,1],[2,3],[1,2]])
A.dot(B)


def vektörel_çarpım(A,B):
    return A.dot(B)


A=np.array([[3],[4]]);B=np.array([[1, 2]]);

vektörel_çarpım(A,B)

vektörel_çarpım(B,A)

 # LEBG

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
# -

A=np.array([[1,2],[3,4]]);B=np.array([[1,1],[0,1],[1,2]]);

vektörel_çarpım(A,B) # Vektörel çarpımda ilk matrisin sütün sayısı ile ikinci matrisin satır sayısı aynı olmalı

vektörel_çarpım(B,A)

PremiumUnleaded=np.array([3/4,1/4])
RegularUnleaded=np.array([2/3,1/3])
RegularLeaded=np.array([1/4,3/4])

mainTable=np.array([PremiumUnleaded,RegularUnleaded,RegularLeaded])

mainDataFrame=pd.DataFrame(mainTable,columns=("crude1","crude2"))

mainDataFrame.index=["PremiumUnleaded","RegularUnleaded","RegularLeaded"]

mainDataFrame

Stock=np.array([10,6,5])

vektörel_çarpım(Stock,mainDataFrame)

# +
# Kural 1 Satır
# -

A=np.array([[1,1,2],[2,1,3]]);B=np.array([[1,1],[2,3],[1,2]])

A[1]

vektörel_çarpım(A,B)

vektörel_çarpım(A,B)[0]

vektörel_çarpım(A[0],B)

# +
# Kural 2 Sütün
# -

vektörel_çarpım(A,B[:,0])

vektörel_çarpım(A,B)[:,0]

# +
# Geçişkenlik Kuralı
# -

A=np.array([1,2]) ; B=np.array([[2,3],[4,5]]);C=np.array([[2],[1]])

A

B

C

vektörel_çarpım(vektörel_çarpım(A,B),C)

vektörel_çarpım(A,vektörel_çarpım(B,C))

vektörel_çarpım(vektörel_çarpım(A,B),C)==vektörel_çarpım(A,vektörel_çarpım(B,C))

# ## Problemler
#

#
# ### 1. Problem

# +

A=np.array([[1,2,3],[4,5,6],[7,8,9]]);B=np.array([[1,2],[0,-1],[1,2]])

# +

print("A :\n", A,"\n")


# -

print("B :\n", B,"\n")


# +
 
print("-A :\n", A*-1,"\n")


# -

print("3A :\n", A*3,"\n")


# +

print("A+2B : \n",A+2*B)


# +

print("A transpose : \n" , A.T  )


# +
      
print("B transpose : \n" , B.T  )
# -

print("AB transpose : \n" , A.dot(B)  )

print("BA transpose : \n" , B.dot(A)  )

# ### 2. Problem

Bira1=[.5,.3,.2]
Bira2=[0,.7,.3]
Bira3=[.1,.3,.6]
Bira_dict={"Bira1":Bira1
          ,"Bira2":Bira2,
          "Bira3":Bira3}

Bira_df=pd.DataFrame(Bira_dict,index=["Bira1","Bira2","Bira3"])

Bira_df

x1=pd.DataFrame({"t1":[0,10,90]},index=["Bira1","Bira2","Bira3"])

x1

Bira_df.shape

x1.shape

y1=Bira_df.dot(x1)

y1

# ### 3.Problem

A=np.array([1,2]) ; B=np.array([[2,3],[4,5]]);C=np.array([[2],[1]])
vektörel_çarpım(vektörel_çarpım(A,B),C)==vektörel_çarpım(A,vektörel_çarpım(B,C))

# ### 4.Problem

A=np.array([1,2]) ; B=np.array([[2,3],[4,5]])
print(" (AB)T :\n", vektörel_çarpım(A,B).T)
print(" BT*AT :\n",vektörel_çarpım(B.T,A.T))
vektörel_çarpım(A,B).T==vektörel_çarpım(B.T,A.T)

# ### 5.Problem

# +
A=np.array([[1,2],[2,1]]);
print(" A : \n",A)
print(" A.T : \n",A.T)

print(" A==A.T : \n",A==A.T  )
# -

# a 
print("A*A.T simetrik \n" , A.dot(A.T)==A.dot(A.T).T)

# b 
print("A+A.T simetrik \n" , (A+A.T)==(A+A.T).T)

# ### 6.Problem

A=np.array([[1,1],[1,1]]);
B=np.array([[2,1],[1,2]]);

A.shape

B.shape

n=A.shape[0]

n**3 # Gereken çarpma sayısı

n**3-n**2 # Gereken toplama sayısı


# ### 7.Problem

def matriks_izi(A):
    return np.array([A[i][i] for i in range(len(A))])


# a
matriks_izi(A+B)==(matriks_izi(A)+matriks_izi(B))

# b
matriks_izi(vektörel_çarpım(A,B))  == matriks_izi(vektörel_çarpım(B,A))

# ## Lineer Denklemlerin Matrisleri

# +
a11=None;a12=None;a13=None;a21=None;a22=None;a23=None; a31=None;a32=None;a33=None;

A=np.array([[a11,a12,a13],
[a21,a22,a23],
[a31,a32,a33]])

# -

A

# +
x11=None;x12=None;x13=None;x21=None;x22=None;x23=None; x31=None;x32=None;x33=None;

X=np.array([[x11,x12,x13],
[x21,x22,x23],
[x31,x32,x33]])
# -

b1=None;b2=None;b3=None;
B=np.array([b1,b2,b3])

B

A.dot(X)==B

# <b> X değişken , A ve B sabittir. A*X=B <b>


