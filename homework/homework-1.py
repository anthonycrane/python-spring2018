
# coding: utf-8

# In[2]:


# Load required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


# Data were taken from fivethirthyeight's repository and contain
# the number of births in the U.S. on a given day from 1994-2003
birth_data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_1994-2003_CDC_NCHS.csv')

# Here, I replace the numeric coded day of the week with the actual day of week
birth_data['day_of_week'].replace(to_replace={1:'Monday',
                                              2:'Tuesday',
                                              3:'Wednesday',
                                              4:'Thursday',
                                              5:'Friday',
                                              6:'Saturday',
                                              7:'Sunday'},
                                  inplace=True)


# In[4]:


# Now I make a boxplot of the number of births on each day of the week
# between 1994 and 2003. 
daily_birth_boxplot = sns.boxplot(x="day_of_week", y="births", color=sns.xkcd_rgb["pale red"], data=birth_data)
daily_birth_boxplot.set(xlabel="Day of week", ylabel="Number of births")
# This rotates the xaxis labels to be more readable
daily_birth_boxplot.set_xticklabels(daily_birth_boxplot.get_xticklabels(), rotation=30)
daily_birth_boxplot.set_title("Daily number of US births from 1994 to 2003")
plt.show()

