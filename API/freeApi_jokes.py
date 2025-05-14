import requests

def fetchFreeAPI_comment():
    url = "https://api.freeapi.app/api/v1/public/youtube/comments/cv-6bAeYsOY"
    response = requests.get(url)
    data = response.json()
    
    
    if data.get('success') and 'data' in data:
        user_data = data["data"]
        
        # if not isinstance(user_data,list):
        #     raise Exception("Expected a list of comments, but got something else")
        
        
    for user_data1 in user_data:
        videoId = user_data1.get("videoId","videoId")
        comment_id = user_data1.get("comment_id","comment_id")
        snippet = user_data1.get("snippet","snippet")
        LikeCount = user_data1.get("likeCount","likeCount")
        publishedAt = user_data1.get("publishedAt","publishedAt")
        totalReplyCount = user_data1.get("totalreplyCount","totalreplyCount")
        
        print(f"Video ID: {videoId} \n CommentID: {comment_id} \nSnippet: {snippet}")
        print(f"Likes: {LikeCount} \n PublishedDate: {publishedAt} \n Replies: {totalReplyCount}")
    
    
    else:
        raise Exception("Failed to fetch")
    

def main():
    try:
        video_id, comment_id, snippet, like_count, published_at, total_reply_count = fetchFreeAPI_comment()
        print(f"Video ID: {video_id}\n \n Comment ID: {comment_id}\n \n Snippet: {snippet}\n")
        print(f"Likes: {like_count}\nPublished At: {published_at}\nReplies: {total_reply_count}")
    except Exception as err:
        print("Some error occurred:", err)
        # 
if __name__ == "__main__":
    main()
