import requests

def get_random_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("fact")
    except requests.exceptions.RequestException as error:
        print("Error fetching cat fact:", error)
        return None

def main():
    fact = get_random_cat_fact()
    if fact:
        print("Random Cat Fact:")
        print(fact)
    else:
        print("Could not retrieve a cat fact at this time.")

if __name__ == "__main__":
    main()
