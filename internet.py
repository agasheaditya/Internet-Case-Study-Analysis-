# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from datetime import timedelta
import seaborn as sn
from IPython.display import display
import statsmodels.api as sm
from statsmodels.formula.api import ols

'''-> to display all shrinked columns'''
pd.set_option('display.max_columns', 30)
df = pd.read_excel("InternetData.xlsx")
#display(df.head())
'''Understandig the data'''
# describe the structure of data
df.info()

#display the summary or descriptive statistics of the data
print(df.describe().transpose())
 #2: Do the unique page views depends on the visits?

mod_uniq_pg = ols('Uniquepageviews ~ Visits',
                data=df).fit()
                
aov_table = sm.stats.anova_lm(mod_uniq_pg, typ=2)
display(pd.DataFrame(aov_table))
#3: Exit page analysis

mod_exits = ols('Exits ~ Timeinpage+Continent+Sourcegroup+Bounces+Uniquepageviews+Visits',
                data=df).fit()
                
aov_table1 = sm.stats.anova_lm(mod_exits, typ=2)
display(pd.DataFrame(aov_table1))

#4: Time on page depends on?

mod_time = ols('Timeinpage ~ Exits+Continent+Sourcegroup+Bounces+Uniquepageviews+Visits',
                data=df).fit()
                
aov_table2 = sm.stats.anova_lm(mod_time, typ=2)
#display(pd.DataFrame(aov_table2))

#5: Bounce rate

'''-> Fitting a Linear Regression model '''
##X = df['Insured'].values.reshape(-1,1)
##y = df['Payment'].values.reshape(-1,1)
##reg = LinearRegression()
##reg.fit(X, y)
''' varience inflation factor'''
##vif1 = pd.DataFrame()
##vif1["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
##vif1["features"] = X.columns
##vif1.round(1)


y = df['Bounces']
X = np.column_stack((df['Visits'],df['Timeinpage'], df['Exits'],df['Uniquepageviews']))
X2 = sm.add_constant(X)

def regression(y,X2):
    est = sm.OLS(y, X2)
    est2 = est.fit()
    display(est2.summary())
    #df.plot()
    #plt.show()

regression(y,X2)

