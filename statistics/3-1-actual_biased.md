[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

'Brian  problem 3-1'
coding: utf-8

In[51]:from thinkstats2 import *
import thinkstats2
import thinkplot
import nsfg
import pandas


 In[ ]:


In[72]:


In[78]:
true data
nsfg.numkdhh = {7: 8, 12: 8, 17: 14, 22: 4,
                27: 6, 32: 12, 37: 8, 42: 3, 47: 2}

In[79]:

pmf = thinkstats2.Pmf(nsfg.numkdhh)

In[80]:

thinkplot.Pmf(pmf, label='numkdhh')
thinkplot.Show()


In[81]:
data from random child from each family

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

In[82]:

biased = BiasPmf(pmf, label='biased')

In[83]:

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()

In[84]:

pmf.Mean()

In[85]:

biased.Mean()


In[ ]:

