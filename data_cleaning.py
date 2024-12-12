import pandas as pd
import locale


def state_populations_adults(dfFull = None):
    dfNew = dfFull
    if not dfFull:
        dfNew = pd.read_csv('Data/states-agegroup-2020.csv')

        locale.setlocale(locale.LC_NUMERIC, '')
        'en_GB.UTF-8'

    suffix = ' - Population - April 1, 2020'
    groups = ['18 to 24 years', '25 to 34 years', '35 to 44 years', '45 to 64 years',
              '65 to 84 years', '85 to 99 years', '100 years and over', 'All ages']
    groups = [g + suffix for g in groups]
    dfNew = dfNew.loc[:, ['State'] + groups]

    # Removes comma from columns and forces to numeric
    for col in groups:
        numeric_col = []
        for val in list(dfNew.loc[:, col]):
            val = val.replace(",", "")
            numeric_col.append(int(val))

        dfNew[col] = numeric_col

    return dfNew


def electoral_college(dfFull):
    dfNew = pd.read_csv('Data/electoral_college_votes.csv')
    dfFull = dfFull.merge(dfNew, left_on='State', right_on='State')
    return dfFull


if __name__ == '__main__':
    df = state_populations_adults()
    df = electoral_college(df)

    df.to_csv('Data/FullData.csv', index=False)
