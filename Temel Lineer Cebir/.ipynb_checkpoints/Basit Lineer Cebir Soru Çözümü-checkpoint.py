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

# # 2. Hafta Soruları

import pandas as pd
import numpy as np

# ### 1.

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[1,2],[0,-1],[1,2]])

# <strong>a. -A</strong>

-A

# <strong>b. 3A</strong>

3*A

# <strong>c. A + 2B</strong>

A+ 2*B #Toplama işlemi yapabilmemiz için matris boyutlarının birbirine eşit olması gerekmektedir. A=(3,3) iken B=(2,3) olduğundan toplama işlemini gerçekleştiremeyiz.

# <strong>d. A^T</strong>

A.T

# <strong>e. B^T</strong>

B.T

# <strong>f. AB</strong> (Vektörel Çarpım)

A.dot(B)

# <strong>g. BA</strong> (Vektörel Çarpım)

B.dot(A) # Vektörel çarpım için 1. matrisin sütun sayısının 2. matrisin satır sayısına eşit olması gerekmektedir. Bu eşitlik sağlanmadığı için çarpma işlemi gerçekleştirilememiştir.

# ### 3.

# A=np.array([[1,2,3],[4,5,6],[7,8,9]])
# B=np.array([[1,2],[0,-1],[1,2]])      Bu değerleri tekrardan kullanacağız.
C=np.array([[4,9,7],[1,8,3]])

(A.dot(B)).dot(C) #(AB)

A.dot(B.dot(C))  #A(BC)

# Matris çarpımının birleşme özelliği vardır. A(BC)=(AB)C

(A.dot(B)).dot(C)==(A.dot(B)).dot(C) #karşılıklı tüm değerler/matrisler birbirine eşittir.

# ### 5.

# Eğer matrisin devriği kendisine eşit ise matris simetriktir. A=A^T

#Önceki örnekteki A matrisini ele alalım
A

# <strong>a. Her n*n matrisin devriği ile çarpımı simetrik matris verir.</strong>

A.dot(A.T)

A.dot(A.T)==(A.dot(A.T)) # AA^T= (AA^T)^T

# <strong>b. Her n*n matrisin devriği ile toplamı simetrik matris verir.</strong>

A+A.T

A+A.T==(A+A.T).T #(A+A^T)=(A+A^T)^T

# ### 7.

# Matrisin izi köşeğeni üzerindeki sayıların toplamıdır.
A # 1+5+9=15

np.trace(A)

# <strong>a. Herhangi iki A ve B matrisinin toplamının izi iki matrisin izinin toplamına eşittir.</strong>

#A matrisimizle toplayabilmek için 3*3 boyutlarında bir matris tanımlayalım.
D=np.array([[4,8,2],[5,3,4],[4,5,2]])

np.trace(D)

np.trace(A)+np.trace(D)

np.trace(A+D)

np.trace(A)+np.trace(D)==np.trace(A+D) # iz(A+B)=iz(A)+iz(B)

# <strong>a. BA ve AB çarpımı tanımlı herhangi iki A ve B matrisinin AB ve BA matrislerinin izleri birbirine eşittir.</strong>

A.dot(D)

np.trace(A.dot(D))

D.dot(A)

np.trace(D.dot(A))

np.trace(A.dot(D))==np.trace(D.dot(A)) # iz(AD)=iz(DA)
