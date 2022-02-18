import random

import requests
from faker import Faker
import asyncio

CREATE_USER_URL = 'http://127.0.0.1:8000/users/'
CREATE_POST_URL = 'http://127.0.0.1:8000/posts/'
GET_TOKEN_URL = 'http://127.0.0.1:8000/token/'
LIKE_POST_URL = 'http://127.0.0.1:8000/likes/'
MAX_USERS = 10
MAX_POSTS = 10
MAX_LIKES = 10


class Bot:

    faker = Faker()

    def set_headers(self, jwt):
        header = {'Authorization': f'Bearer {jwt}'}
        return header

    async def create_user(self):
        password = self.faker.pystr(min_chars=10, max_chars=20)
        username = self.faker.user_name()
        user_json = {'email': self.faker.email(),
                     'password': password,
                     'username': username}

        req = requests.post(CREATE_USER_URL, data=user_json)
        if req.status_code == 201:
            await self.sign_in(username, password)

    async def create_multiple_users(self):
        for i in range(MAX_USERS):
            await self.create_user()

    async def sign_in(self, username, password):
        data = {'username': username, 'password': password}
        req = requests.post(GET_TOKEN_URL, data=data)
        await self.create_multiple_posts(req.json()['access'])

    async def create_post(self, jwt):
        data = {'title': self.faker.sentence(),
                'text': self.faker.paragraph(10),
                }
        req = requests.post(CREATE_POST_URL, data=data, headers=self.set_headers(jwt))
        await self.like_multiple_post(self.set_headers(jwt))

    async def create_multiple_posts(self, jwt):
        for i in range(MAX_POSTS):
            await self.create_post(jwt)

    async def like_post(self, jwt):
        id = random.randrange(1, MAX_POSTS*MAX_USERS)
        choice = [True, False, None]
        status = random.choice(choice)
        data = {'post':id,
                'status': status}
        req = requests.post(LIKE_POST_URL, data=data, headers=jwt)

    async def like_multiple_post(self, jwt):
        for i in range(MAX_LIKES):
            await self.like_post(jwt)


async def main():
    bot = Bot()
    await bot.create_multiple_users()


if __name__ == '__main__':
    # main()
    asyncio.run(main())
