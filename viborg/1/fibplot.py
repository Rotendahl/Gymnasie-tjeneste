from plotly.offline import iplot, init_notebook_mode

def fibplot(xsr,ysr,xsi,ysi):
    frames = []
    for i in range(len(xsr)+2):
        frames.append({'data': [{'x': xsr[:i], 'y': ysr[:i]}, {'x':xsi[:i], 'y':ysi[:i]}]})

    figure = {
        'data': [
            {
                'x': xsr,
                'y': ysr,
                'mode':'lines',
                'name': 'Recursive Fib'
            }, {
                'x': xsi,
                'y': ysi,
                'mode':'lines',
                'name': 'Imperative Fib'
            }
        ],
        'layout': {'title': 'Fibonacci',
                   'updatemenus': [{
                       'buttons': [
                           {'args': [None],
                            'label': 'Play',
                            'method': 'animate'}
                   ],
                   'pad': {'r': 10, 't': 87},
                   'showactive': False,
                   'type': 'buttons'
                    }]},
        'frames': frames,
    }

    iplot(figure, filename='Fibonacci')
