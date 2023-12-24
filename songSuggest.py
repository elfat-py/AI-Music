from bs4 import BeautifulSoup
import requests


class SongSuggest:
    def __init__(self, song):
        self.song = song
        self.session = requests.Session()
        self.INITIAL_LINK = 'https://songslikex.com/'
        self.URL_SEARCH_VALUE = f"{self.INITIAL_LINK}?song={song}"
        self.list_suggestions = []
        self.link_header = ''

    def find_search_bar(self, user_input):
        html_home_page = requests.get(self.URL_SEARCH_VALUE).text
        soup = BeautifulSoup(html_home_page, 'lxml')

        full_body = soup.find_all('div', class_='full')
        for content in full_body:
            full_center = content.find_all('div', class_='m-b-m full center')
            for button in full_center:
                search_button = button.find(id='songSearchForm')
                if search_button:
                    search_place = search_button.find('div', class_='async-search')
                    if search_place:
                        input_element = search_place.find('input', id='songSearch')
                        input_element['value'] = user_input
                        if input_element['value'] == user_input:
                            for song_suggest in full_center:
                                song_suggestions_list = song_suggest.find_all('ul', class_='song-results left pad-m')
                                if song_suggestions_list:
                                    for song_list in song_suggestions_list:
                                        songs = song_list.find_all('li', class_='song')
                                        for song_element in songs:
                                            title_tag = song_element.find_all('a')
                                            for song_title_a in title_tag:
                                                title_tag = song_title_a.get('href')
                                                self.list_suggestions.append(title_tag)

    def get_first_suggestion(self):
        self.find_search_bar(self.song)
        first_suggestion = self.list_suggestions[0]
        self.link_header = self.INITIAL_LINK[:-1] + first_suggestion

    def results_from_response(self, response_link):
        songs_list = []
        html_text = self.session.get(response_link).text
        soup = BeautifulSoup(html_text, 'lxml')
        lists = soup.find_all('table', class_='trackList table full')

        for table in lists:
            tbody = table.find('tbody')

            if tbody:
                tr_elements = tbody.find_all('tr')

                for tr in tr_elements:
                    titles_td = tr.find('td').find('button')
                    if titles_td:
                        title = titles_td.get('title')
                        songs_list = title[15:]
                        print(title[15:])  # SHOULD BE REMOVED ONCE NOT NEEDED

        return songs_list

    def get_recommendations(self):
        self.get_first_suggestion()
        return self.results_from_response(self.link_header)


# Example usage:

