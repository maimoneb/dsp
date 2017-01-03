[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)


#get_ipython().magic(u'reset -f')
import numpy as np
from scipy.stats import norm
import brfss


mean_men = 178
sd_men = 7.7

def convert_to_cms(fts, inches):
    return  (fts * 12 + inches) * 2.54

lb = convert_to_cms(5,10)
ub = convert_to_cms(6,1)
print(lb, ub)

male_percent = (norm.cdf(ub, mean_men, sd_men) - norm.cdf(lb, mean_men, sd_men)) * 100
print(male_percent)

