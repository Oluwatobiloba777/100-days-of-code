import pandas as pd
import matplotlib.pyplot as plt
import px as px
import numpy as np
import seaborn as sns

#challenge 1
df_data = pd.read_csv('nobel_prize_data.csv')

df_data.shape
df_data.tail()
df_data.head()

#challenge 2

print(df_data.duplicated().values.any())

##nan values
print(df_data.isna().values.any())

col_subset = ['year','category', 'laureate_type',
              'birth_date','full_name', 'organization_name']
df_data.loc[df_data.organization_name.isna()][col_subset]

#challenge 3

df_data.birth_date = pd.to_datetime(df_data.birth_date)

separatedValues = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separatedValues[0])
denomenator = pd.to_numeric(separatedValues[1])
df_data['share_pct'] = numerator / denomenator

#plotly bar and donuts charts
#challenge 1

gender = df_data.sex.value_counts()
fig = px.pie(labels=gender.index,
             values=gender.values,
             title="Percentage of Male vs. Female Winners",
             names=gender.index,
             hole=0.4, )

fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')

fig.show()

#challenge 2

df_data[df_data.sex == 'Female'].sort_values('year', ascending=True)[:3]

#challenge 3

winner = df_data.duplicated(subset=['full_name'], keep=False)
multipleWinners = df_data[winner]
print(f'There are {multipleWinners.full_name.nunique()}' \
      ' winners who were awarded the prize more than once.')
col_subset = ['year', 'category', 'laureate_type', 'full_name']
multipleWinners[col_subset]

#challenge 4

df_data.category.nunique()

prizesByCategory = df_data.category.value_counts()
vBar = px.bar(
    x=prizesByCategory.index,
    y=prizesByCategory.values,
    color=prizesByCategory.values,
    color_continuous_scale='Aggrnyl',
    title='Number of Prizes Awarded per Category')

vBar.update_layout(xaxis_title='Nobel Prize Category',
                    coloraxis_showscale=False,
                    yaxis_title='Number of Prizes')
vBar.show()

#challenge 5

df_data[df_data.category == 'Economics'].sort_values('year')[:3]

#challenge 6

menAndWomen = df_data.groupby(['category', 'sex'],
                               as_index=False).agg({'prize': pd.Series.count})
menAndWomen.sort_values('prize', ascending=False, inplace=True)

v_bar_split = px.bar(x=menAndWomen.category,
                     y=menAndWomen.prize,
                     color=menAndWomen.sex,
                     title='Number of Prizes Awarded per Category split by Men and Women')

v_bar_split.update_layout(xaxis_title='Nobel Prize Category',
                          yaxis_title='Number of Prizes')
v_bar_split.show()


##using matplotlib to visualize trends

#challenge 1

prizeByYear = df_data.groupby(by='year').count().prize
average = prizeByYear.rolling(window=5).mean()
# plt.scatter(x=prizeByYear.index,
#             y=prizeByYear.values,
#             c='dodgerblue',
#             alpha=0.7,
#             s=100, )
#
# plt.plot(prizeByYear.index,
#          average.values,
#          c='crimson',
#          linewidth=3, )
#
# plt.show()

np.arange(1900, 2021, step=5)

plt.figure(figsize=(16, 8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax = plt.gca()
ax.set_xlim(1900, 2020)

ax.scatter(x=prizeByYear.index,
           y=prizeByYear.values,
           c='dodgerblue',
           alpha=0.7,
           s=100, )

ax.plot(prizeByYear.index,
        average.values,
        c='crimson',
        linewidth=3, )

plt.show()

#challenge 2

yearlyAverage = df_data.groupby(by='year').agg({'share_pct': pd.Series.mean})
movingAverage = yearlyAverage.rolling(window=5).mean()
plt.figure(figsize=(16, 8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900, 2020)

# Can invert axis
ax2.invert_yaxis()

ax1.scatter(x=prizeByYear.index,
            y=prizeByYear.values,
            c='dodgerblue',
            alpha=0.7,
            s=100, )

ax1.plot(prizeByYear.index,
         average.values,
         c='crimson',
         linewidth=3, )

ax2.plot(prizeByYear.index,
         movingAverage.values,
         c='grey',
         linewidth=3, )

plt.show()

#a choropleth map

#challenge 1
top_countries = df_data.groupby(['birth_country_current'],
                                as_index=False).agg({'prize': pd.Series.count})

top_countries.sort_values(by='prize', inplace=True)
top20_countries = top_countries[-20:]

h_bar = px.bar(x=top20_countries.prize,
               y=top20_countries.birth_country_current,
               orientation='h',
               color=top20_countries.prize,
               color_continuous_scale='Viridis',
               title='Top 20 Countries by Number of Prizes')

h_bar.update_layout(xaxis_title='Number of Prizes',
                    yaxis_title='Country',
                    coloraxis_showscale=False)
h_bar.show()

#challenge 2

df_countries = df_data.groupby(['birth_country_current', 'ISO'],
                               as_index=False).agg({'prize': pd.Series.count})
df_countries.sort_values('prize', ascending=False)

world_map = px.choropleth(df_countries,
                          locations='ISO',
                          color='prize',
                          hover_name='birth_country_current',
                          color_continuous_scale=px.colors.sequential.matter)

world_map.update_layout(coloraxis_showscale=True, )

world_map.show()

#challenge 3

cat_country = df_data.groupby(['birth_country_current', 'category'],
                               as_index=False).agg({'prize': pd.Series.count})
cat_country.sort_values(by='prize', ascending=False, inplace=True)

merged_df = pd.merge(cat_country, top20_countries, on='birth_country_current')
# change column names
merged_df.columns = ['birth_country_current', 'category', 'cat_prize', 'total_prize']
merged_df.sort_values(by='total_prize', inplace=True)
cat_cntry_bar = px.bar(x=merged_df.cat_prize,
                       y=merged_df.birth_country_current,
                       color=merged_df.category,
                       orientation='h',
                       title='Top 20 Countries by Number of Prizes and Category')

cat_cntry_bar.update_layout(xaxis_title='Number of Prizes',
                            yaxis_title='Country')
cat_cntry_bar.show()

##challenge 4

prize_by_year = df_data.groupby(by=['birth_country_current', 'year'], as_index=False).count()
prize_by_year = prize_by_year.sort_values('year')[['year', 'birth_country_current', 'prize']]

cumulative_prizes = prize_by_year.groupby(by=['birth_country_current',
                                              'year']).sum().groupby(level=[0]).cumsum()
cumulative_prizes.reset_index(inplace=True)

l_chart = px.line(cumulative_prizes,
                  x='year',
                  y='prize',
                  color='birth_country_current',
                  hover_name='birth_country_current')

l_chart.update_layout(xaxis_title='Year',
                      yaxis_title='Number of Prizes')

l_chart.show()

##create sunburst charts

#challenge 1

top20_orgs = df_data.organization_name.value_counts()[:20]
top20_orgs.sort_values(ascending=True, inplace=True)

org_bar = px.bar(x=top20_orgs.values,
                 y=top20_orgs.index,
                 orientation='h',
                 color=top20_orgs.values,
                 color_continuous_scale=px.colors.sequential.haline,
                 title='Top 20 Research Institutions by Number of Prizes')

org_bar.update_layout(xaxis_title='Number of Prizes',
                      yaxis_title='Institution',
                      coloraxis_showscale=False)
org_bar.show()

#challenge 2

top20_org_cities = df_data.organization_city.value_counts()[:20]
top20_org_cities.sort_values(ascending=True, inplace=True)
city_bar2 = px.bar(x=top20_org_cities.values,
                   y=top20_org_cities.index,
                   orientation='h',
                   color=top20_org_cities.values,
                   color_continuous_scale=px.colors.sequential.Plasma,
                   title='Which Cities Do the Most Research?')

city_bar2.update_layout(xaxis_title='Number of Prizes',
                        yaxis_title='City',
                        coloraxis_showscale=False)
city_bar2.show()

#challenge 3
top20_cities = df_data.birth_city.value_counts()[:20]
top20_cities.sort_values(ascending=True, inplace=True)
city_bar = px.bar(x=top20_cities.values,
                  y=top20_cities.index,
                  orientation='h',
                  color=top20_cities.values,
                  color_continuous_scale=px.colors.sequential.Plasma,
                  title='Where were the Nobel Laureates Born?')

city_bar.update_layout(xaxis_title='Number of Prizes',
                       yaxis_title='City of Birth',
                       coloraxis_showscale=False)
city_bar.show()

#challenge 4

country_city_org = df_data.groupby(by=['organization_country',
                                       'organization_city',
                                       'organization_name'], as_index=False).agg({'prize': pd.Series.count})

country_city_org = country_city_org.sort_values('prize', ascending=False)

burst = px.sunburst(country_city_org,
                    path=['organization_country', 'organization_city', 'organization_name'],
                    values='prize',
                    title='Where do Discoveries Take Place?',
                    )

burst.update_layout(xaxis_title='Number of Prizes',
                    yaxis_title='City',
                    coloraxis_showscale=False)

burst.show()

##laureate age at the time of the award

#challenge 1

birthYear = df_data.birth_date.dt.year
df_data['winning_age'] = df_data.year - birthYear

#challenge 2
display(df_data.nlargest(n=1, columns='winning_age'))
display(df_data.nsmallest(n=1, columns='winning_age'))

#challenge 3

plt.figure(figsize=(8, 4), dpi=200)
sns.histplot(data=df_data,
             x=df_data.winning_age,
             bins=30)
plt.xlabel('Age')
plt.title('Distribution of Age on Receipt of Prize')
plt.show()

#challenge 4
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.regplot(data=df_data,
                x='year',
                y='winning_age',
                lowess=True,
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'black'})

plt.show()

#challenge 5
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.boxplot(data=df_data,
                x='category',
                y='winning_age')

plt.show()


#challenge 6

with sns.axes_style("whitegrid"):
    sns.lmplot(data=df_data,
               x='year',
               y='winning_age',
               hue='category',
               lowess=True,
               aspect=2,
               scatter_kws={'alpha': 0.5},
               line_kws={'linewidth': 5})

plt.show()

