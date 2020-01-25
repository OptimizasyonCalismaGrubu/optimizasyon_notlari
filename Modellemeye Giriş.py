#!/usr/bin/env python
# coding: utf-8

# # Modellemeye Giriş

# #### <em>İA<em/>

# Matematiksel modellerin amacı temel olarak gerçek dünyayı açıklamaktır.

# ### Tanımlayıcı Modeller/Optimizasyon Modelleri

# Tanımlayıcı modeller, bir organizasyonun amacı/amaçlarıyla buluşabilmesi için davranışlarını "tanımlayan" modellerdir

# Descriptive (Açıklayıcı) Modellerde sistemin yapısını anlamak için genellikle İstatistik alanından yararlanılır fakat sistemin anlaşılmasında çok faydalı olmaz. 

#  Predictive modellerde ise geleceğin tahmin edilebilmesi bakımından Machine Learning'e başvurulur. Contraints'ler (kısıtlarımız) belli olmadığında verileri belirlemekte yardımcı olabilir.

# Prescriptive (Tanımlayıcı) Modeller ise optimizasyon modelleridir. Sistemin amacı doğrultusunda kısıtları kullanır.

# ### Amaç Fonksiyonu

# Feasible Region (Fizibil Bölge), elimizdeki kısıtları ele aldığımızda bu kısıtları karşılayan bölgedir. Optimal nokta ise bu bölgede amaç fonksiyonunu maksimize edecek noktadır.

# ### 1.1 Örnek Model (Daisy Firması Wozac Ürünü)

# In[ ]:


"""
T-Temperature
P-Pressure
V-Volume
A,B,C-Mixtures

"""


# In[17]:


def objfunc1(V,T,P,A,B,C):
    return 300+0.8*V+0.01*P+0.06*T+0.001*T*P-0.01*T*T-0.001*P*P+11.7*A+9.4*B+16.4*C+19*A*B+11.4*A*C-9.6*B*C


# In[23]:


def checkFeasible(V,T,P,A,B,C):
    meets_constraints = (
                         V <= 5 and 
                         V>=1 and 
                         P<=400 and 
                         P>=200 and 
                         T<=200 and 
                         T>=100 and 
                         A>=0 and 
                         B>=0 and 
                         C>=0 and 
                         (A+B+C == 1) and 
                         A<=5
                        )
    
    return meets_constraints


# In[19]:


print("Fizibil :",checkFeasible(5,100,200,0.294,0,0.706))


# In[20]:


print("Amaç Fonksiyonu = ",objfunc1(5,100,200,0.294,0,0.706))


# ### Statik ve Dinamik Modeller

# Statik modeller belirli periyodlarda karar verilmesini gerektirmez, bir kez model çözüldüyse tekrar çözülmesine genellikle gerek olmaz

# ### Lineer ve Lineer Olmayan Modeller

# Karar değişkenleri kendi aralarında veya sabit katsayılarla çarpıldığında <u>Lineer Modeller</u> elde edilir. Lineer olmayan modellerde türev ve integralden yararlanılır, iki ve ikiden fazla dereceye sahip denklemlerdir.

# ### Tam Sayı ve Tam Sayı Olmayan Modeller

# Tam sayı olan modeller tam sayı olmayan modellere göre çözülmesi daha zordur. Çünkü kısıt sayısı daha fazladır.

# <u>Çözülmesi zor modeller</u> : Dinamik, lineer olmayan ve tam sayı modeller

# ### Örnek 1.2

# Starbucks'ta sabah 08.00 ile akşam 18.00 arasında kaç kişinin çalışması gerektiğini Beşiktaş şubesi için hesaplarsak, oluşturacağımız modeli nasıl sınıflandırırız?

# #### Çalışan Sayısını Etkileyebilecek Faktörler (Değişkenler)
# 1.Çalışılan alanın büyüklüğü<br>
# 2.Müşterilerin içeride geçirdikleri süre<br>
# 3.Çalışanlara yapılacak olan ödeme miktarı<br>
# 4.Çalışanların part-time/full-time çalışması<br>
# 5.Müşteri Sayısı

# <u><i>Sistem, değişkenleri düzenli olarak değiştiği için Dinamik Model sınıfına girer</i></u>

# <strong>Amaçlar :  </strong><br>A) Çalışan sayısını minimize etmek<br>B) Satış miktarını maksimize etmek<br><br>
# <strong>Amaç <i>(MAKS)</i> = </strong> - Ödeme * Çalışan Sayısı + kar * müşteri
# 
# <u><i>Amaç fonksiyonunun bu şekilde olduğunu varsayarsak modelin lineer olduğunu söyleyebiliriz </i></u>

# #### İlişkiler:
# 1.Müşteri sayısı arttıkça çalışan sayısı artar.
# 
# Örneğin, 
# (çalışan sayısı) - (müşteri sayısı) * kar = 0
# 
# 
# 
# 

# <i><u>Müşteri sayısı kontrol edilemeyen bir değişkendir. Bu yüzden kullanacağımız model predictive (öngörülebilen) bir modeldir.</u></i>

# <i><u>Müşteri sayısı sabitse deterministik, bir dağılıma sahipse stokastik bir modeldir.</u><i>

# <u><i>Müşteri sayısı ve çalışan sayısı tam sayı cinsinden elde edildiğinden tam sayı modelidir.</i></u>

# #### Modellemenin 7 Adımı
# 

# 1. Problemin Formülasyonu
# 2. Sistemin Gözlemlenmesi
# 3. Problemin Matematiksel Model olarak Formülasyonu
# 4. Modelin Doğrulanması ve Tahmin Amaçlı Kullanımı
# 5. Uygun Alternatifin Seçimi
# 6. Sonuçların Sunulması ve Organizasyon Çalışmasının Sonucu
# 7. Yerleştirme ve Önerilerin Değerlendirilmesi

# In[ ]:




