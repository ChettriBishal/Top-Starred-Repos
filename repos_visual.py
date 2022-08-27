import requests

from plotly.graph_objs import Bar
from plotly import offline

#make an api call and store the response

tech = input("Enter the technology or language to see its most starred respositories: ")
url = f'https://api.github.com/search/repositories?q={tech}&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers = headers)
print(f"Status code: {r.status_code}")


# processing the results
response_dict = r.json()
repo_dicts = response_dict['items']

repo_links , stars, labels = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']

    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name} </a>" #clickable url 
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br>{description}"
    labels.append(label)


#make visualization
data = [{
    'type': 'bar', #type of chart
    'x': repo_links, # x axis
    'y': stars, #y axis
    'hovertext': labels,
    'marker':{
        # 'color': 'rgb(60,100,150)',
        'color': 'rgb(255,160,0)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
        # 'line': {'width': 1.5, 'color': 'rgb(255, 165, 0)'}
    },
    'opacity': 0.6,
}]

graph_layout = {
    'title': f'Most Starred {tech} Repositories on GitHub',
    'titlefont': {'size': 28},
    # 'plot_bgcolor' : 'rgb(0,0,0,0)',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': graph_layout}
offline.plot(fig,filename='repos.html')

