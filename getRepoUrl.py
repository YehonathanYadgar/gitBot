import requests

def search_github_repo(query):
    url = "https://api.github.com/search/repositories"

    # defining seqrch params.
    params = {
        "q": query, # name you want to search
        "sort": "stars", # sort by git hub stars
        "order": "desc", # order by descending
        "per_page": 1  # We only need the top result
    }

    # fetching data with the params
    response = requests.get(url, params=params)

    # checking if the request was successful
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            return data['items'][0] 
        else:
            return None
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None
    
# function to display repo info
def display_repo_info(repo):
    print(f"Name: {repo['name']}")
    print(f"Full Name: {repo['full_name']}")
    print(f"URL: {repo['html_url']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}")

# putting it all together
def main():

    # getting user input
    query = input("Enter a search term for GitHub repositories: ")

    # getting the top repo by stars
    top_repo = search_github_repo(query)

    # checking if the repo is found, and if it is displaying the info.
    if top_repo:
        print("Top repository by stars:")
        display_repo_info(top_repo)
        return top_repo['html_url']  # Return the URL
    else:
        print("No repositories found.")
        return None


