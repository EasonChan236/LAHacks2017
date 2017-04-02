import requests

def search(searchText):
    headers={"Ocp-Apim-Subscription-Key":"498f4c1486bb4411b7f801c114442a4d"}
    response = requests.get("https://api.cognitive.microsoft.com/bing/v5.0/search", headers=headers, params={"q":searchText})
    json = response.json()


    pages = json["webPages"]["value"]

    return [(page["name"], page["url"] )for page in pages]

if __name__ == "__main__":
    print search("Hello, World!!!")

