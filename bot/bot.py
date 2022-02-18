import requests
from faker import Faker

CREATE_USER_URL = 'http://127.0.0.1:8000/users/'
CREATE_POST_URL = 'http://127.0.0.1:8000/posts/'
GET_TOKEN_URL = 'http://127.0.0.1:8000/token/'
LIKE_POST_URL = ''
MAX_USERS = 10
MAX_POSTS = 10
MAX_LIKES = 10


class Bot:

    faker = Faker()

    def set_headers(self, jwt):
        header = {'Authorization': f'Bearer {jwt}'}
        return header

    def create_user(self):
        password = self.faker.pystr(min_chars=10, max_chars=20)
        username = self.faker.user_name()
        user_json = {'email': self.faker.email(),
                     'password': password,
                     'username': username}

        req = requests.post(CREATE_USER_URL, data=user_json)
        if req.status_code == 201:
            self.sign_in(username, password)

    def create_multiple_users(self):
        pass

    def sign_in(self, username, password):
        data = {'username': username, 'password': password}
        req = requests.post(GET_TOKEN_URL, data=data)
        self.create_post(req.json()['access'])

    def create_post(self, jwt):
        data = {'title': self.faker.sentence(),
                'text': self.faker.paragraph(10),
                }
        req = requests.post(CREATE_POST_URL, data=data, headers=self.set_headers(jwt))

    def create_multiple_posts(self, jwt):
        pass

    def like_post(self):
        pass


def main():
    bot = Bot()
    bot.create_user()


if __name__ == '__main__':
    main()
