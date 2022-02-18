import random
import requests
from faker import Faker
import asyncio
from conf import (
    MAX_LIKES,
    MAX_POSTS,
    MAX_USERS,
    CREATE_USER_URL,
    CREATE_POST_URL,
    LIKE_POST_URL,
    GET_TOKEN_URL
)


class Bot:
    user_list = []
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
            print('user was created')
            await self.sign_in(username, password)

    async def create_multiple_users(self):
        for i in range(MAX_USERS):
            await self.create_user()

    async def sign_in(self, username, password):
        data = {'username': username, 'password': password}
        req = requests.post(GET_TOKEN_URL, data=data)
        header = self.set_headers(req.json()['access'])
        data['header'] = header
        self.user_list.append(data)
        await self.create_multiple_posts(header)
        # await self.like_multiple_post(header)

    async def create_post(self, header):
        data = {'title': self.faker.sentence(),
                'text': self.faker.paragraph(10),
                }
        req = requests.post(CREATE_POST_URL, data=data, headers=header)
        print('post was created')

    async def create_multiple_posts(self, header):
        for i in range(MAX_POSTS):
            await self.create_post(header)

    async def like_post(self, header):
        id = random.randrange(1, MAX_POSTS*MAX_USERS)
        choice = [True, False, None]
        status = random.choice(choice)
        data = {'post':id,
                'status': status}
        req = requests.post(LIKE_POST_URL, data=data, headers=header)
        print('like was created')

    async def like_multiple_post(self):
        for user in self.user_list:
            for i in range(MAX_LIKES):
                await self.like_post(user['header'])


async def main():
    bot = Bot()
    await bot.create_multiple_users()
    await bot.like_multiple_post()

if __name__ == '__main__':
    # main()
    asyncio.run(main())
