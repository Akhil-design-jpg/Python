import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
        ) ''')


def list_videos():
    cursor.execute("Select * from videos")
    result = cursor.fetchall()
    if not result:
        print("\n")
        print("*" * 70)
        print("Empty for now ")
        print("\n")
        
    else:
        for row in result:
            print("*" * 70)
            print(row)
            print("\n")
            
def add_video(name,time):
    cursor.execute("Insert into videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos set name = ?, time = ? where id = ?",(new_name,new_time,video_id))
    conn.commit()
    
def delete_video(video_id):
    
    cursor.execute("Delete from videos where id = ?",(video_id,)) # will go to tupple after using (,) and only tupple gets accepted
    conn.commit()
    
def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        choice = input('Enter your choice: ')

        if choice == '1':
            list_videos()
        elif choice == '2':
           name = input("Enter the video name: ")
           time = input("Enter the video time: ")
           add_video(name,time)
        elif choice == '3':
           videoID = input('Enter Video ID to update: ')
           name = input("Enter the video name: ")
           time = input("Enter the video time: ")
           update_video(videoID,name,time)
        elif choice == '4':
           videoID = input('Enter Video ID to delete: ')   
           delete_video(videoID)     
        elif choice == '5':
            print("App exited")
            break
        else:
            print('Invalid choice')
       
    conn.close()     

if __name__ == "__main__":
    main()