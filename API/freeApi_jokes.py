import requests

def fetch_jokeApi():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()
    
    
    if ["success"] and "data" in data:
        user_data = data["data"]
        message = user_data.get("message",["message"])
        content = user_data.get("content",["content"])
        
        return message, content
    
    else:
        raise Exception("failed to fetch the data")
    # 
    
    
def main():
    
    try:
        message, content = fetch_jokeApi()
        print(f"Message: {message} \n Content: {content}")
    except Exception as err:
        print(str(err))
        print(err)
        
if __name__ == "__main__":
    main()
    
