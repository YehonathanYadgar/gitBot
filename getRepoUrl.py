import requests

def search_github_repo(query):
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 1  # We only need the top result
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['items']:
            return data['items'][0]  # Return the entire repository data
        else:
            return None
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

def display_repo_info(repo):
    print(f"Name: {repo['name']}")
    print(f"Full Name: {repo['full_name']}")
    print(f"URL: {repo['html_url']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}")

def main():
    query = input("Enter a search term for GitHub repositories: ")
    top_repo = search_github_repo(query)

    if top_repo:
        print("Top repository by stars:")
        display_repo_info(top_repo)
        return top_repo['html_url']  # Return the URL
    else:
        print("No repositories found.")
        return None


