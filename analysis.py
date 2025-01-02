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


def tax_vs_metrics(data_file, plot=False):
    df = pd.read_csv(data_file)

    if plot:
        effective_tax = list(df.loc[:, 'State-Local Effective Tax Rate Percentage'])
        air = list(df.loc[:, 'Air Quality'])
        water = list(df.loc[:, 'Public Drinking Water'])

        fig, ax1 = plt.subplots()

        ax2 = ax1.twinx()
        ax1.scatter(effective_tax, air, color='g')
        ax2.scatter(effective_tax, water, color='b')

        ax1.set_xlabel('State-Local Effective Tax Rate Percentage')
        ax1.set_ylabel('Air Quality', color='g')
        ax2.set_ylabel('Public Drinking Water', color='b')

        plt.show()

    dfNew = df.loc[:, ['State-Local Effective Tax Rate Percentage', 'Air Quality', 'Public Drinking Water']]
    dfNew.to_csv('Data/Tax_vs_State_Metrics.csv', index=False)


if __name__ == '__main__':
    votes_per_person('Data/FullData.csv')
    tax_vs_metrics('Data/FullData.csv')
