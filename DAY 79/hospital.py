import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import px as px
import seaborn as sns
import scipy.stats as stats

dfYearlyData = pd.read_csv('annual_deaths_by_clinic.csv')
dfMonthlyData = pd.read_csv('monthly_deaths.csv')

#challenge 1
dfYearlyData.shape
dfMonthlyData.shape

#challenge 2

chancesOfDeath = dfYearlyData.deaths.sum() / dfYearlyData.births.sum() * 100
print(f'Chances of dying in 1840s in Vienna: {chancesOfDeath:.3}%')

#challenge 3

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

plt.figure(figsize=(14, 8), dpi=200)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('Births', color='skyblue', fontsize=18)
ax2.set_ylabel('Deaths', color='crimson', fontsize=18)


ax1.set_xlim([dfMonthlyData.date.min(), dfMonthlyData.date.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.grid(color='grey', linestyle='--')

ax1.plot(dfMonthlyData.date,
         dfMonthlyData.births,
         color='skyblue',
         linewidth=3)

ax2.plot(dfMonthlyData.date,
         dfMonthlyData.deaths,
         color='crimson',
         linewidth=2,
         linestyle='--')

plt.show()


#analysing the yearly data split by clinic
#challenge 1

#births
line = px.line(dfYearlyData,
               x='year',
               y='births',
               color='clinic',
               title='Total Yearly Births by Clinic')

line.show()

#deaths

line = px.line(dfYearlyData,
               x='year',
               y='deaths',
               color='clinic',
               title='Total Yearly Deaths by Clinic')

line.show()

#challenge 2

dfYearlyData['pct_deaths'] = dfYearlyData.deaths / dfYearlyData.births
clinic1 = dfYearlyData[dfYearlyData.clinic == 'clinic 1']
avg_c1 = clinic1.deaths.sum() / clinic1.births.sum() * 100
print(f'Average death rate in clinic 1 is {avg_c1:.3}%.')

clinic_2 = dfYearlyData[dfYearlyData.clinic == 'clinic 2']
avg_c2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
print(f'Average death rate in clinic 2 is {avg_c2:.3}%.')

line = px.line(dfYearlyData,
               x='year',
               y='pct_deaths',
               color='clinic',
               title='Proportion of Yearly Deaths by Clinic')

line.show()

#effect of handwashing

#challenge 1

dfMonthlyData['pct_deaths'] = dfMonthlyData.deaths/dfMonthlyData.births

beforeWashing = dfMonthlyData[dfMonthlyData.date < handwashing_start]
afterWashing = dfMonthlyData[dfMonthlyData.date >= handwashing_start]

beforeWashingRate = beforeWashing.deaths.sum() / beforeWashing.births.sum() * 100
afterWashingwRate = afterWashing.deaths.sum() / afterWashing.births.sum() * 100
print(f'Average death rate before 1847 was {beforeWashingRate:.4}%')
print(f'Average death rate AFTER 1847 was {afterWashingwRate:.3}%')

#challenge 2

roll_df = beforeWashing.set_index('date')
roll_df = roll_df.rolling(window=6).mean()

#challenge 3
plt.figure(figsize=(14, 8), dpi=200)
plt.title('Percentage of Monthly Deaths over Time', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

plt.ylabel('Percentage of Deaths', color='crimson', fontsize=18)

ax = plt.gca()
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim([dfMonthlyData.date.min(), dfMonthlyData.date.max()])

plt.grid(color='grey', linestyle='--')

ma_line, = plt.plot(roll_df.index,
                    roll_df.pct_deaths,
                    color='crimson',
                    linewidth=3,
                    linestyle='--',
                    label='6m Moving Average')
bw_line, = plt.plot(beforeWashing.date,
                    beforeWashing.pct_deaths,
                    color='black',
                    linewidth=1,
                    linestyle='--',
                    label='Before Handwashing')
aw_line, = plt.plot(afterWashing.date,
                    afterWashing.pct_deaths,
                    color='skyblue',
                    linewidth=3,
                    marker='o',
                    label='After Handwashing')

plt.legend(handles=[ma_line, bw_line, aw_line],
           fontsize=18)

plt.show()


#visualizing distributions and testing for statistical


#challenge 1
avg_prob_before = beforeWashing.pct_deaths.mean() * 100
print(f'Chance of death during childbirth before handwashing: {avg_prob_before:.3}%.')

avg_prob_after = afterWashing.pct_deaths.mean() * 100
print(f'Chance of death during childbirth AFTER handwashing: {avg_prob_after:.3}%.')

mean_diff = avg_prob_before - avg_prob_after
print(f'Handwashing reduced the monthly proportion of deaths by {mean_diff:.3}%!')

times = avg_prob_before / avg_prob_after
print(f'This is a {times:.2}x improvement!')


#challenge 2
dfMonthlyData['washing_hands'] = np.where(dfMonthlyData.date < handwashing_start, 'No', 'Yes')

box = px.box(dfMonthlyData,
             x='washing_hands',
             y='pct_deaths',
             color='washing_hands',
             title='How Have the Stats Changed with Handwashing?')

box.update_layout(xaxis_title='Washing Hands?',
                  yaxis_title='Percentage of Monthly Deaths', )

box.show()

#challenge 3

hist = px.histogram(dfMonthlyData,
                    x='pct_deaths',
                    color='washing_hands',
                    nbins=30,
                    opacity=0.6,
                    barmode='overlay',
                    histnorm='percent',
                    marginal='box', )

hist.update_layout(xaxis_title='Proportion of Monthly Deaths',
                   yaxis_title='Count', )

hist.show()


#challenge 4

plt.figure(dpi=200)

sns.kdeplot(beforeWashing.pct_deaths, shade=True)
sns.kdeplot(afterWashing.pct_deaths, shade=True)
plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
plt.show()

plt.figure(dpi=200)
sns.kdeplot(beforeWashing.pct_deaths,
            shade=True,
            clip=(0,1))
sns.kdeplot(afterWashing.pct_deaths,
            shade=True,
            clip=(0,1))
plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
plt.xlim(0, 0.40)
plt.show()

#challenge 5
t_stat, p_value = stats.ttest_ind(a=beforeWashing.pct_deaths,
                                  b=afterWashing.pct_deaths)
print(f'p-palue is {p_value:.10f}')
print(f't-statstic is {t_stat:.4}')


