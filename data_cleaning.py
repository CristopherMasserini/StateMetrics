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

    dfNew[f'Adults{suffix}'] = dfNew[[g for g in groups if g != 'All ages']].sum(axis=1)

    return dfNew


def electoral_college():
    dfNew = pd.read_csv('Data/electoral_college_votes.csv')
    return dfNew


def air_water_metrics():
    dfNew = pd.read_csv('Data/air_water_quality.csv')
    return dfNew

def state_tax_burden(new_rank=False):
    dfNew = pd.read_csv('Data/state_tax_burden.csv')
    if new_rank:
        effectiveRate = dfNew.loc[:, 'State-Local Effective Tax Rate Percentage']
        erate_rank = effectiveRate.rank()
        dfNew['Rank'] = erate_rank
    else:
        dfNew = dfNew.drop('Rank', axis=1)

    return dfNew


def merge_dfs(dataframes, by='State'):
    dfFull = dataframes[0]

    if len(dataframes) == 2:
        dfFull = dfFull.merge(dataframes[1], left_on=by, right_on=by)
    else:
        for i in range(1, len(dataframes)):
            dfFull = dfFull.merge(dataframes[i], left_on=by, right_on=by)

    return dfFull


if __name__ == '__main__':
    dfPops = state_populations_adults()
    dfEC = electoral_college()
    dfBurden = state_tax_burden()
    dfAirWater = air_water_metrics()

    df = merge_dfs([dfPops, dfEC, dfBurden, dfAirWater])
    df.to_csv('Data/FullData.csv', index=False)
