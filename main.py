import argparse
from datetime import datetime
import os

from dotenv import load_dotenv
import requests


def reduce_url(input_url, TOKEN):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
    'Authorization': TOKEN
    }
    post_url = {
    'long_url' : input_url
    }

    response = requests.post(url, headers = headers, json = post_url)

    if response.ok:
        redused_link = response.json()['id']
        return redused_link
    return None
    

def count_clicks(input_url, TOKEN):
    date_clicks = []
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{input_url}/clicks'
    headers = {
    'Authorization': TOKEN
    }
    params = {
    'units' : -1
    }

    response = requests.get(url, headers = headers, params = params)

    if not response.ok:
      return None
    for day in response.json()['link_clicks']:
            date_dt = datetime.strptime(day['date'][:10], '%Y-%m-%d')
            date_clicks.append(f"{date_dt.strftime('%d.%m.%Y')} - {day['clicks']} clicks")
    return date_clicks


def check_input_link(input_url, TOKEN):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{input_url}'
    headers = {
    'Authorization': TOKEN
    }
  
    response = requests.get(url, headers = headers)
    return response.ok


def create_parser():
    parser = argparse.ArgumentParser(description='Программа сокращает ссылку, либо выдает статистику по сокращенной ссылке')
    parser.add_argument('link')
    return parser


def main():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    parser = create_parser()
    args = parser.parse_args()
    input_url = args.link

    if check_input_link(input_url, TOKEN):
        date_clicks = count_clicks(input_url, TOKEN)
        if date_clicks is None:
            print('Something went wrong, repeat the request again')
            return
        for day in date_clicks:
            print(day, end = '\n')         
    else:
        reduced_link = reduce_url(input_url, TOKEN)
        if reduced_link is None:
            print('Incorrect link')
            return
        print(reduced_link)
            

if __name__ == '__main__':
    main()

   
    
