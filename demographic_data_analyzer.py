import pandas as pd

def calculate_demographic_data(print_data=True):
      # Read data from file
      df = pd.read_csv('csv/adult.data.csv')

      # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
      race_count = df.pivot_table(index = ['race'], aggfunc = 'size').values.tolist()
      race_count.sort(reverse = True)
     
      # What is the average age of men?
      average_age_men = round(df.loc[df['sex']=='Male','age'].mean(),1)

      # What is the percentage of people who have a Bachelor's degree?
      percentage_bachelors = round(((df[df['education'] == 'Bachelors']['education'].count())/len(df)) * 100, 1)

      # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K? 
      
      # What percentage of people without advanced education make more than 50K?

      # with and without `Bachelors`, `Masters`, or `Doctorate`
      higher_education = df[(df.education == 'Bachelors')|(df.education == 'Masters') | (df.education == 'Doctorate')]
      lower_education = df[(df.education != 'Bachelors') & (df.education != 'Masters') & (df.education != 'Doctorate')]

      # percentage with salary >50K
      higher_education_rich = round((higher_education[((higher_education['salary'] == '>=50K')|(higher_education['salary'] == '>50K'))]['salary'].count()/len(higher_education))*100,1)

      lower_education_rich = round((lower_education[((lower_education['salary'] == '>=50K')|(lower_education['salary'] == '>50K'))]['salary'].count()/len(lower_education))*100,1)

      # What is the minimum number of hours a person works per week (hours-per-week feature)?
      min_work_hours = df['hours-per-week'].min()

      # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

      num_min_workers = df[(df['hours-per-week'] == min_work_hours)]
      rich_percentage = round((num_min_workers[(num_min_workers['salary'] == '>50K')|(num_min_workers['salary'] == '>=50K')]['salary'].count()/len(num_min_workers))*100,1)

      # What country has the highest percentage of people that earn >50K?
      # iran_salary = df[(df['native-country'] == 'Iran')][['native-country','salary']]
      # print(round((iran_salary[iran_salary.salary == '>50K'].count()/len(iran_salary))*100,1))

      # us_salary = df[(df['native-country'] == 'United-States')][['native-country','salary']]
      # print(round((us_salary[us_salary.salary == '>50K'].count()/len(us_salary))*100,1))

      # df[df['Courses'].duplicated() == True]

      df_country = df.drop_duplicates('native-country', keep='first')
      list_country = df_country['native-country'].values.tolist()
      list_rich_percentage = list()
      dist_highest_earning_country = {}

      for c in list_country:
            temp_salary = df[(df['native-country'] == c)][['native-country','salary']]
            list_rich_percentage.append(round((temp_salary[temp_salary.salary == '>50K']['salary'].count()/len(temp_salary))*100,1))

      for key in list_country:
            for value in list_rich_percentage:
                  dist_highest_earning_country[key] = value
                  list_rich_percentage.remove(value)
                  break
      
      highest_earning_country = max(dist_highest_earning_country, key=dist_highest_earning_country.get)

      highest_earning_country_percentage = dist_highest_earning_country[highest_earning_country]

      # Identify the most popular occupation for those who earn >50K in India.
      # Country India and Salary >50K, occupation
      test_df = df[(df['native-country'] == 'India')&(df['salary'] == '>50K')]
      df_occupation = test_df.pivot_table(columns=['occupation'], aggfunc='size').to_frame(name='top')
      series_occupation = test_df.pivot_table(columns=['occupation'], aggfunc='size')
      sortedSeries = series_occupation.sort_values(ascending=False)

      # print(list(sortedSeries.index)[0])
      # for i in sortedSeries.index:
      #       print(i)
      
      top_IN_occupation = list(sortedSeries.index)[0]

      # DO NOT MODIFY BELOW THIS LINE

      if print_data:
            print("Number of each race:", race_count) 
            print("Average age of men:", average_age_men)
            print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
            print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
            print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
            print(f"Min work time: {min_work_hours} hours/week")
            print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
            print("Country with highest percentage of rich:", highest_earning_country)
            print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
            print("Top occupations in India:", top_IN_occupation)

      return {
            'race_count': race_count,
            'average_age_men': average_age_men,
            'percentage_bachelors': percentage_bachelors,
            'higher_education_rich': higher_education_rich,
            'lower_education_rich': lower_education_rich,
            'min_work_hours': min_work_hours,
            'rich_percentage': rich_percentage,
            'highest_earning_country': highest_earning_country,
            'highest_earning_country_percentage':
            highest_earning_country_percentage,
            'top_IN_occupation': top_IN_occupation
      }

calculate_demographic_data()