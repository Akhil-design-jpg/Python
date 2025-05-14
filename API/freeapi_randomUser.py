import requests


def fetch_freeApi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Falid to fetch user data")
    
    # 
def main():
    try:
        username, country = fetch_freeApi()
        print(f"Username{username} \n Country{country}")
    except Exception as err:
            print("Some error occured", str(err))
            
            
if __name__ == "__main__":
    main()
