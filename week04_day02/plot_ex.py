import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot


def test_scatter():
    x = np.linspace(0, 3 * np.pi, 100)
    y = np.sin(x)

    trace1 = go.Scatter(  # linia wykresu
        x=x,
        y=y,
        mode='markers+lines',
        line=dict(width=5),
        name='sinus'
    )

    y2 = np.cos(x)

    trace2 = go.Scatter(
        x=x,
        y=y2,
        name='cosinus',
        line=dict(color='#123455')
    )

    layout = go.Layout(title='Plots using plotly',
                       height=1080,
                       width=1920)  # okno wykresu
    figure = go.Figure(data=[trace1, trace2], layout=layout)
    plot(figure, auto_open=True, filename='test.html')


def test_3D_plot():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)

    X, Y = np.meshgrid(x, y)

    print(X, Y)

    a = 1
    # b = 5

    Z = (X ** 2 + Y ** 2) / (a ** 2)

    paraboloid = go.Scatter(
        x=x,
        y=y,

        name='cosinus',
        line=dict(color='#123455')
    )

    # heat_map(x, y, Z)
    plot_mesh(x, y, Z)
    # Scatter_3D(x,y,Z)


def heat_map(x, y, Z):
    trace1 = go.Heatmapgl(
        x=x,
        y=y,
        z=Z
    )
    layout = go.Layout(title='HeatMap')  # okno wykresu
    figure = go.Figure(data=[trace1], layout=layout)
    plot(figure, auto_open=True, filename='heatmap.html')


def plot_mesh(x, y, Z):
    trace1 = go.Surface(
        x=x,
        y=y,
        z=Z
    )
    layout = go.Layout(title='HeatMap')  # okno wykresu
    figure = go.Figure(data=[trace1], layout=layout)
    plot(figure, auto_open=True, filename='heatmap.html')


def Scatter_3D(x, y, z):
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                       mode='markers')])
    plot(fig, auto_open=True, filename='heatmap.html')


def plot_circle():
    x = np.linspace(0, 2)
    y = np.linspace(0, 2)

    a = 1
    b = 1

    r = (x - a) ** 2 + (y - b) ** 2

    trace = go.Scatter(  # linia wykresu
        x=x,
        y=r,
        mode='markers+lines',
        line=dict(width=5),
        name='sinus'
    )

    layout = go.Layout(title='Plots using plotly')  # okno wykresu
    figure = go.Figure(data=[trace], layout=layout)
    plot(figure, auto_open=True, filename='kolo.html')


if __name__ == '__main__':
    # test_scatter()
    plot_circle()
    # test_3D_plot()
