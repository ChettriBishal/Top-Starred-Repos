import requests

from plotly.graph_objs import Bar
from plotly import offline

#make an api call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers = headers)
print(f"Status code: {r.status_code}")


# processing the results
response_dict = r.json()
repo_dicts = response_dict['items']

repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


#make visualization
data = [{
    'type': 'bar', #type of chart
    'x': repo_names, # x axis
    'y': stars, #y axis
}]

graph_layout = {
    'title': 'Most Starred Python Repositories on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': graph_layout}
offline.plot(fig,filename='python_repos.html')

