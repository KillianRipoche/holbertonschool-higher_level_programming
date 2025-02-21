import requests
import csv


def fetch_and_print_posts():

    url = "https://jsonplaceholder.typicode.com/posts"


    response = requests.get(url)


    if response.status_code == 200:
        print("Status Code: 200 - Success")


        posts = response.json()


        print("\nTitles of all posts:")
        for post in posts:
            print(post['title'])
    else:
        print(f"Failed to fetch posts. Status Code: {response.status_code}")


def fetch_and_save_posts():

    url = "https://jsonplaceholder.typicode.com/posts"


    response = requests.get(url)


    if response.status_code == 200:
        print("Status Code: 200 - Success")


        posts = response.json()


        post_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]


        with open('posts.csv', 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)


            writer.writeheader()


            writer.writerows(post_data)

        print("\nPosts have been saved to 'posts.csv'")
    else:
        print(f"Failed to fetch posts. Status Code: {response.status_code}")


fetch_and_print_posts()
fetch_and_save_posts()
