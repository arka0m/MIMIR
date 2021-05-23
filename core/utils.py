import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

def format_graph():
    ''' Function to format graph '''
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def func(pct, allvals):
    absolute = int(round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)

def get_pieGraph(labels, x_series):
    colors = []
    for label in labels:
        if label == "Compromised":
            colors.append('#dc1e1e') # red
        elif label == "Unknown":
            colors.append('#ff8b00') # orange
        elif label == "Healthy":
            colors.append('#33a21d') # green
        else:
            colors.append('blue')
    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(aspect="equal"))
    wedges, texts, autotexts = ax.pie(x_series, colors=colors, autopct=lambda pct: func(pct, x_series), shadow=False)
    ax.legend(wedges, labels,  loc="upper right", bbox_to_anchor=(0.6, 0, 0.5, 1))
    plt.setp(autotexts, size=10, weight="heavy")
    ax.set_title("endpoints status", fontsize=16, weight="bold")
    graph = format_graph()
    return graph

def get_lineGraph(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('test')
    plt.plot(x,y)
    plt.xlabel=('item')
    plt.ylabel=('price')
    plt.tight_layout()
    graph = format_graph()
    return graph