import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils import add_subreddit, add_post, add_proxy
from datetime import datetime


def main():
    while True:
        print("\n1. Add Subreddit")
        print("2. Add Post")
        print("3. Add Proxy")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter subreddit name: ")
            add_subreddit(name)
        elif choice == '2':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            subreddit_name = input("Enter subreddit name: ")
            scheduled_time_str = input("Enter scheduled time (YYYY-MM-DD HH:MM): ")
            scheduled_time = datetime.strptime(scheduled_time_str, "%Y-%m-%d %H:%M")
            is_self_str = input("Is this a self post? (y/n): ")
            is_self = is_self_str.lower() == 'y'
            add_post(title, content, subreddit_name, scheduled_time, is_self)
        elif choice == '3':
            address = input("Enter proxy address: ")
            port = int(input("Enter proxy port: "))
            protocol = input("Enter proxy protocol (http/https): ")
            add_proxy(address, port, protocol)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()