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


