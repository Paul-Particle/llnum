# mypy utils.py

# Code snippets for common tasks

# --------------------------------------------------------

import plotly.graph_objects as go
import plotly.express as px
import kaleido # required for saveFig
import datetime
from pathlib import Path

# --------------------------------------------------------

# Saving figures
OUTPUTPATH = Path('./output/')
DATAPATH = Path('./data/')

def get_timestamp(date=True,time=True):
    dt = datetime.datetime.now()
    if date and time:
        return dt.strftime('%Y-%m-%d_%H-%M-%S')
    elif date:
        return dt.strftime('%Y-%m-%d')
    else:
        return dt.strftime('%H-%M-%S')

def save_fig(fig, filename='untitled', path=OUTPUTPATH, add_time=True, html=True, png=True, svg=False, json=False, scale=2, save_condition=True):
    if not save_condition:
        return
    if add_time:
        filename = f'{get_timestamp()}_{filename}'
    if html:
        fig.write_html(path / (filename + '.html'))
    if png:
        fig.write_image(path / (filename + '.png'), scale=scale)
    if svg:
        fig.write_image(path / (filename + '.svg'))
    if json:
        fig.write_json(path / (filename + '.json'), pretty=True)

# --------------------------------------------------------

# Colors
PLOTLY_BLUE, PLOTLY_RED = ['#636EFA', '#EF553B']
PLOTLY_CONFIG = {
    'displaylogo': False,
    # 'scrollZoom': True
    }

def get_colorscale(points, cmap='viridis', normalize=False):
    if normalize:
        points = (points - min(points)) / (max(points) - min(points))
    # map n points to n colors
    return px.colors.sample_colorscale(cmap, points)

# --------------------------------------------------------

# f-strings 
# See also: https://fstring.help/cheat/
number = 4125.6
percent = 0.3738
examples = (
    f'{number:.2f}',
    f'{number:,.2f}',
    f'{number:08.2f}',
    f'{number: 9,.2f}',
    f'{number:.2g}',
    f'{number:.3g}',
    f'{percent:.0%}'
)
#print(examples)
# > print(examples)
# ('4125.60', '4,125.60', '04125.60', ' 4125.60', '4.1e+03', '4125.6', '37%')"

# --------------------------------------------------------

def example():
    # EXAMPLE FIGURE
    
    figname='example_figure'
    
    # Two x-axes is not natively supported for some reason in plotly, but can be relatively easily achieved with this. Interaction with the html version makes the plot inconsistent though.
    
    from plotly.subplots import make_subplots
    
    # initial subplot with two traces 
    # (can be just normal plot or just one row & col)
    fig = make_subplots(rows=1, cols=2)
    
    fig.add_trace(
        go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
        row=1, col=2
    )
    
    fig.update_layout(height=600, width=800,
                      title_text="Subplots with shared x-axes")
    
    # extra data where xaxis3 is shared with subplot 1
    fig.add_trace(go.Scatter(
        x=[11, 12, 13],
        y=[6, 5, 4],
        name="xaxis3 data",
        xaxis="x3" # key part
    ))
    
    # some adjustmentns for xaxis3 
    # Don't know exatly how ('x3' and 'xaxis3' are connected)
    fig.update_layout(xaxis3=dict(
            title="xaxis3 title",
            titlefont=dict(
                color="#9467bd"
            ),
            tickfont=dict(
                color="#9467bd"
            ),
            anchor="free", # key part
            overlaying="x1", 
            side="right",
            position=0.0
        ))
    
    # extra data where xaxis4 is shared with subplot 2
    fig.add_trace(go.Scatter(
        x=[50, 60, 70],
        y=[60, 60, 60],
        name="xaxis4 data",
        xaxis="x4",
        yaxis = 'y2'
    ))
    
    # some adjustments for xaxis4
    fig.update_layout(xaxis4=dict(
            title="xaxis4 title",
            titlefont=dict(
                color="#9467bd"
            ),
            tickfont=dict(
                color="#9467bd"
            ),
            anchor="free",
            overlaying="x2",
            side="right",
            position=0.0
        ))
    
    # make room to display double x-axes
    fig.update_layout(yaxis1=dict(domain=[0.1, 1]),
                      yaxis2=dict(domain=[0.1, 1]),
                     )
    
    # not critical, but just to put a little air in there
    fig.update_layout(xaxis1=dict(domain=[0.0, 0.4]),
                      xaxis2=dict(domain=[0.6, 1]),
                     )
    
    fig.update_layout(
        title={
            'text': "Plot Title",
            'y':0.88,
            'x':0.42,
            'xanchor': 'left',
            'yanchor': 'top'},
        template="plotly_dark",
        # hovermode=False, # good for figures with many traces
        # plot_bgcolor= 'rgba(0, 0, 0, 0)', # transparent
        #paper_bgcolor= 'rgba(0, 0, 0, 0)',
        # yaxis1=dict(
        #     visible=False,  # Makes the y-axis invisible
        #     showgrid=False  # Removes the grid lines on the y-axis
        # )
    )
    
    fig.show(config=PLOTLY_CONFIG)
    save_fig(fig, figname, add_time=False)


if __name__ == '__main__':
    example()