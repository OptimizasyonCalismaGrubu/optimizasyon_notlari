#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import pandas as pd
import numpy as np


# %%


A=np.array([[1,1,2],[2,1,3]]);B=np.array([[1,1],[2,3],[1,2]]);A


# %%


W=A.dot(B);W


# %%


W.T


# %%


print("olley")


# %%


def matris_carpım(A,B):#fonsiyon tanımlama
    try:
        W=A.dot(B)
        return W
    except:print("olmadı kiii")


# %%


C=np.array([[3],[4]]) #Değişkenleri tanımlama
D=np.array([[1,2]])


# %%


matris_carpım(C,D) #fonksiyonu çağırıp değişkenlerimizi girdik.


# %%


W.T


# %%


matris_carpım(D,C)


# %%


E=np.array([[1,2],[3,4]]) 
F=np.array([[1,1],[0,1],[1,2]])


# %%


matris_carpım(E,F) #Vektörel çarpım için 1. matrisin sütun sayısının 2. matrisin satır sayısına eşit olması gerekmektedir. Aksi halde fonksiyon hata verir.


# Example 4

# %%


M=np.array([[3/4,2/3,1/4],[1/4,1/3,3/4]])#Katsayılarımız
N=np.array([[10],[6],[5]])#istediğimiz miktar


# %%


matris_carpım(M,N)#Çarpım sonucumuz gerekli crude oil miktarını veriyor.


# %%


pd.DataFrame(matris_carpım(M,N)) #pandas kütüphanesinin DataFrame modülü ile matrisimizi tablo haline getirdik.


# # Properties of Matrix Multiplication

# Çarpma işlemine 1. matrisin 1.satırı girerse çözümün 1. satırını elde ederiz.

# %%


A=np.array([[1,1,2],[2,1,3]])
B=np.array([[1,1],[2,3],[1,2]])


# %%


matris_carpım(A,B)


# %%


matris_carpım(A[0],B)


# %%


matris_carpım(A[0],B)==matris_carpım(A,B)[0]


# Çarpma işlemine 2. matrisin 1.sütünu girerse çözümün 1. sütununu elde ederiz.

# %%


B[:,0]


# %%


matris_carpım(A,B[:,0])==matris_carpım(A,B)[:,0]


# %%


B[1:,]


# <strong><u>Kural2:</u></strong>A(BC)=(AB)C

# %%


A=np.array([[1,2]])


# %%


B=np.array([[2,3],[4,5]])


# %%


C=np.array([[2],[1]])


# %%


(A.dot(B)).dot(C)==A.dot(B.dot(C))


# %%


matris_carpım((matris_carpım(A,B)),C)==matris_carpım(A,(matris_carpım(B,C)))

