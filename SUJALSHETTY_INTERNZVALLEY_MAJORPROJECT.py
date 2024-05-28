#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
td=pd.read_excel("heart-disease.xlsx")
df=pd.DataFrame(td)
df


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.head(10)


# In[6]:


df.tail(20)


# In[7]:


df.shape


# In[8]:


df["age"].describe()


# In[9]:


import matplotlib.pyplot as plt
plt.hist(df["age"],bins=[0,10,20,30,40,50,60,70,80,90,100],edgecolor="red")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# In[10]:


df["age"].describe()


# In[11]:


df.isnull().sum()


# In[12]:


plt.hist(df["sex"],label="0:Female 1:Male")
plt.xlabel("sex")
plt.ylabel("Frequency")
plt.legend()
plt.show()


# In[13]:


df["target"].value_counts()


# In[42]:


import seaborn as sns
plt.hist(df["target"],label="0:NOT DIAGNOSED,1:DIAGNOSED")
plt.xlabel("Target")
plt.ylabel("Count of target")
plt.title("Target variable count plot")
plt.legend()
plt.show()


# In[26]:


X=df.iloc[:,:-1]
Y=df.iloc[:,-1]



# In[27]:


X.shape


# In[28]:


Y.shape


# In[29]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=99)


# In[30]:


from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(criterion="gini",
                          max_depth=8,
                          min_samples_split=10,
                           random_state=5)


# In[31]:


clf.fit(X_train,Y_train)


# In[32]:


clf.feature_importances_


# In[33]:


df.columns


# In[34]:


Y_pred=clf.predict(X_test)
Y_pred


# In[35]:


from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,Y_pred)


# In[36]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_test,Y_pred)


# In[37]:


from sklearn.model_selection import cross_val_score
cross_val_score(clf,X_train,Y_train,cv=10)


# In[38]:


from sklearn.metrics import classification_report
print(classification_report(Y_pred,Y_test))


# In[40]:


import numpy as np
features=df.columns
importances=clf.feature_importances_
indices=np.argsort(importances)

plt.title("Feature Importance")
plt.barh(range(len(indices)),importances[indices],color="b",align="center")
plt.yticks(range(len(indices)),[features[i] for i in indices])
plt.xlabel("Relative Importance")
plt.show()


# In[ ]:




