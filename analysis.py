import pandas as pd
import numpy as np


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


if __name__ == '__main__':
    votes_per_person('Data/FullData.csv')
