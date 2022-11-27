import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.linear_model import LinearRegression

df = pd.read_csv('cost_revenue_dirty.csv')

#challenge 1
#data exploration and data cleaning
df.shape
df.head()
df.tail()
df.info()
df.sample()

#checking for nan values
df.isna().values.any()

#duplicates
df.duplicated().values.any()

#challenge 2

removeChar = [',', '$']
cleanColumns = ['USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']

for col in cleanColumns:
    for char in removeChar:
        df[col] = df[col].astype(str).str.replace(char, "")

    df[col] = pd.to_numeric(df[col])

#challenge 3
df.Release_Date = pd.to_datetime(df.Release_Date)

### investigate films that had zero revenue

#challenge 1a
df[df.USD_Production_Budget == 1100.00]

#challenge 1b
df[df.USD_Production_Budget == 425000000.00]

#challenge 2
domestic = df[df.USD_Domestic_Gross == 0]
print(domestic)
domestic.sort_values('USD_Production_Budget', ascending=False)

#challenge 3
worldwide = df[df.USD_Worldwide_Gross == 0]
print(worldwide)
worldwide.sort_values('USD_Production_Budget', ascending=False)


##filter on multiple conditions

internationalReleases = df.loc[(df.USD_Domestic_Gross == 0) & (df.USD_Worldwide_Gross != 0)]
print(f"Number of international releases: {len(internationalReleases)}")
internationalReleases.head()

#challenge
international_releases = df.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')
international_releases.tail()

##unreleased films
scrape_date = pd.Timestamp('2018-5-1')
future_releases = df[df.Release_Date >= scrape_date]
cleanData = df.drop(future_releases.index)


###SEABORN

sns.scatterplot(data=cleanData, x='USD_Production_Budget', y='USD_Worldwide_Gross')
plt.figure(figsize=(8, 4), dpi=200)

#styling
with sns.axes_style('darkgrid'):
    ax = sns.scatterplot(data=cleanData,
                         x='USD_Production_Budget',
                         y='USD_Worldwide_Gross',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross',)

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')

plt.show()

#challennge
plt.figure(figsize=(8, 4), dpi=200)

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=cleanData,
                         x='Release_Date',
                         y='USD_Production_Budget',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross', )

    ax.set(ylim=(0, 450000000),
           xlim=(cleanData.Release_Date.min(), cleanData.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')

#converting years to decades
dateTimeIndex = pd.DatetimeIndex(cleanData.Release_Date)
years = dateTimeIndex.year

decades = years//10*10
cleanData['Decade'] = decades

#challenge 2
oldFilms = cleanData[cleanData.Decade <= 1960]
newFilms = cleanData[cleanData.Decade > 1960]


##linear regressions with seaborn
sns.regplot(data=oldFilms,
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross')

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
  sns.regplot(data=oldFilms,
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})

##challenge
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style('darkgrid'):
    ax = sns.regplot(data=newFilms,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     color='#2f4b7c',
                     scatter_kws={'alpha': 0.3},
                     line_kws={'color': '#ff7c43'})

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')


##using scikit-learn

regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(newFilms, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(newFilms, columns=['USD_Worldwide_Gross'])

# Find the best-fit line
regression.fit(X, y)

# R-squared
regression.score(X, y)

##challengee
X = pd.DataFrame(oldFilms, columns=['USD_Production_budget'])
y = pd.DataFrame(oldFilms, columns=['USD_Worldwide_Gross'])

regression.fit(X, y)

print(f"the slope coefficient is: {regression.coef_[0]}")
print(f"The intercept is: {regression.intercept_[0]}")
print(f"the r-squared is: {regression.score(X, y)}")


#challenge
budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')