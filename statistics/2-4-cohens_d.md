[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

'Brian Maimone problem 2-4'

import thinkplot
import thinkstats2
import nsfg


preg = nsfg.ReadFemPreg()

boolean_index = (preg.pregordr == 1)

firsts = preg[boolean_index]

boolean_index2 = (preg.pregordr != 1)

others = preg[boolean_index2]

print "First born size: {}".format(len(firsts))

print "Others size: {}".format(len(others))

print ("do we have the total weight column? {}".format("totalwgt_lb" in preg.columns))

first_hist = thinkstats2.Hist(firsts.totalwgt_lb)

other_hist = thinkstats2.Hist(others.totalwgt_lb)

width = 0.45
thinkplot.PrePlot(2)

thinkplot.Hist(other_hist, align='left', width=width, alpha=0.3, color="yellow", label="other")

thinkplot.Hist(first_hist, align='right', width=width, alpha=0.3, color="red", label="first born")

thinkplot.Show(xlabel='total wgt lbs', ylabel='frequency')

'Cohens d function'

import math

def CohenEffectSize(group1, group2):

diff = group1.mean() - group2.mean()

print group1.mean()

    print group2.mean()
    
    var1 = group1.var()
    
    var2 = group2.var()
    
    n1, n2 = len(group1), len(group2)
    
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
    d = diff / math.sqrt(pooled_var)
    
    return d

cohen_effect = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

print("Cohen effect for baby weight (between firstborn and non firstborn): {}".format(cohen_effect))

cohen_effect = CohenEffectSize(firsts.prglngth, others.prglngth)

print("Cohen effect for pregnacy length (between firstborn and non firstborn): {}".format(cohen_effect))
