import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def pandas_test():
    df = pd.read_csv('box_since_2000_simple.csv', sep=';')
    print(df)
    print(df.keys())

    keys = [key for key in df.std().index]
    print(keys)

    weights = df['Weight']
    print(weights)

    bmi = df['Weight'] / (df['Height'] / 100) ** 2
    print(df[bmi < 20])
    # print(bmi.dropna())


def pandas_plotly():
    df = pd.read_csv('athlete_events_since_2000.csv', sep=';')

    df = df[df['Year'] > 2000]
    df_ski_results = df[df['Event'].str.contains("Ski Jumping Men's")].dropna()

    team_labels = df_ski_results['Team'].unique()

    medal_labels = df_ski_results['Medal'].unique()

    team_dict = {}
    for team in team_labels:
        team_dict[team] = [
            {"Count": df_ski_results[df_ski_results['Team'] == team].shape[0],
             "Bronze": df_ski_results[(df_ski_results['Team'] == team) & (df_ski_results['Medal'] == 'Bronze')].shape[
                 0],
             "Silver": df_ski_results[(df_ski_results['Team'] == team) & (df_ski_results['Medal'] == 'Silver')].shape[
                 0],
             "Gold": df_ski_results[(df_ski_results['Team'] == team) & (df_ski_results['Medal'] == 'Gold')].shape[0]}
        ]

    print(team_dict)
    values = [team_dict[team][0]['Count'] for team in team_labels]

    print(values)

    fig = go.Figure(data=[
        go.Pie(labels=team_labels,
               values=values)])

    sunburst_labels = []
    labels = []
    parent = []
    values = []
    for team in team_labels:
        labels.append(str(team))
        sunburst_labels.append(str(team))
        parent.append('')
        values.append(team_dict[team][0]['Count'])
        for medal in medal_labels:
            if team_dict[team][0][medal] != 0:
                sunburst_labels.append(str(team) + '_' + str(medal))
                values.append(team_dict[team][0][medal])
                parent.append(str(team))
                labels.append(str(medal))

    trace = go.Sunburst(
        ids=sunburst_labels,
        labels=labels,
        parents=parent,
        values=values,
        branchvalues="total",
        outsidetextfont={"size": 20, "color": "#377eb8"},
        marker={"line": {"width": 2}},
    )

    layout = go.Layout(
        margin=go.layout.Margin(t=0, l=0, r=0, b=0)
    )

    plot(fig, auto_open=True, filename='ski_jump.html')

    plot(go.Figure([trace], layout), auto_open=True, filename='ski_jump_sun.html')


if __name__ == '__main__':
    pandas_plotly()
