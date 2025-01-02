import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def votes_per_person(data_file):
    df = pd.read_csv(data_file)
    states = df.loc[:, 'State']
    adult_pop = df.loc[:, 'Adults - Population - April 1, 2020']
    ec_votes = df.loc[:, 'Electoral College Votes']
    ec_votes_per_adult = ec_votes/adult_pop
    ec_votes_per_adult_standardized = []

    median_vote = np.median(ec_votes_per_adult)
    for i in ec_votes_per_adult:
        ec_votes_per_adult_standardized.append(i/median_vote)

    data = {'State': states,
            'Adults - Population - April 1, 2020': adult_pop,
            'Electoral College Votes': ec_votes,
            'Electoral College Votes Per Adult': ec_votes_per_adult,
            'Standardized Electoral College Votes Per Adult': ec_votes_per_adult_standardized}

    pd.DataFrame(data).to_csv('Data/electoral_college_votes_per_adult.csv', index=False)


def tax_vs_metrics(data_file, columns):
    df = pd.read_csv(data_file)

    dfNew = df.loc[:, columns]
    dfNew.to_csv('Data/Tax_vs_State_Metrics.csv', index=False)


if __name__ == '__main__':
    votes_per_person('Data/FullData.csv')
    tax_vs_metrics('Data/FullData.csv',
                   ['State-Local Effective Tax Rate Percentage',
                    'Air Quality',
                    'Public Drinking Water'])
