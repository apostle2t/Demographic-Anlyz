import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round((df[df['sex'] == 'Male']['age'].mean()),1)

    # What is the percentage of people who have a Bachelor's degree?
    edu_count = df[df["education"] == "Bachelors"].shape[0]
    total_count = len(df)
    percentage_bachelors = round((edu_count/total_count * 100),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    adv_list = ["Bachelors","Masters","Doctorate"]
    adv_deg_count = df[(df["education"].isin(adv_list)) & (df["salary"] == ">50K")].shape[0]
    ppl_total_count = df[(df["education"].isin(adv_list))].shape[0]
    high_edu_percent = round((adv_deg_count/ppl_total_count * 100),1)


    # What percentage of people without advanced education make more than 50K?
    ex_list = ["Bachelors","Masters","Doctorate"]
    ex_adv = df[(~df["education"].isin(ex_list)) & ((df["salary"] == ">50K"))].shape[0]
    total_ex = df[(~df["education"].isin(ex_list))].shape[0]
    ex_percent = round((ex_adv/total_ex * 100),1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df["education"].isin(adv_list))]
    lower_education = df[(~df["education"].isin(adv_list))]

    # percentage with salary >50K
    higher_education_rich = high_edu_percent
    lower_education_rich = ex_percent

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

   # Country with highest percentage of people that earn >50K
    rich_by_country = df[df["salary"] == ">50K"]["native-country"].value_counts()
    total_by_country = df["native-country"].value_counts()
    country_percent = (rich_by_country / total_by_country * 100).round(1)
    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = country_percent.max()

    # Percentage of rich among those who work fewest hours
    num_min_workers = df[df["hours-per-week"] == min_work_hours].shape[0]
    num_min_workers_rich = df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")].shape[0]
    rich_percentage = round((num_min_workers_rich / num_min_workers * 100), 1) if num_min_workers > 0 else 0

    # Identify the most popular occupation for those who earn >50K in India.
    earn_india = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()

    top_IN_occupation = earn_india


    if print_data:
        print("Number of each race:\n", race_count) 
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

