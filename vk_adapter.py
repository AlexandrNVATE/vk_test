import requests

'''
    Описание констант для работы с VK API
'''
class VK:
    #https://api.vk.com/method/wall.get?owner_id=-165878204&v=5.87
    #'750749131600d4b82e17b9477898644403a85f89547b9ea21c7d791dc03b557a49cbe4b9c3e4aa335c41c'

    token = '750749131600d4b82e17b9477898644403a85f89547b9ea21c7d791dc03b557a49cbe4b9c3e4aa335c41c'
    version = '5.87'
    # groups_id = ['-141332590','-150111598','-118304034','-54947048','-154465696','-144654434','-99436205']
    count_read_posts = 20
    shift_last_day = 10

    '''
        получить все посты до указанной даты 
        group_id - id группы
        last_date - дата размещения постов до которой их нужно просматривать
        вощвращается массив из словарей
    '''
    def get_all_posts_in_group(self, group_id, last_date, offset = 0):
        all_posts = []

        while True:
            print(str(int(offset/self.count_read_posts//1)+1) + ' request........done')
            group_id = str('-' + str(group_id))
            r = requests.get('https://api.vk.com/method/wall.get',
                             params={'owner_id': group_id, 'count': self.count_read_posts,
                                     'offset': offset, 'access_token': self.token, 'v': self.version})
            print(r.json())

            if r.json()['response']['items']:
                posts = r.json()['response']['items']
                all_posts.extend(posts)
                oldest_post_date = posts[-1]['date']
                # если дата позднее заданной то остановить цикл или постов больше нет
                if (oldest_post_date < last_date):
                    print('Записи получены')
                    break
                offset += self.count_read_posts
            else:
                print('Записи закончены')
                break
        return all_posts

    def get_all_user_group(self,id_user):
        print('Getting all groups')
        r = requests.get('https://api.vk.com/method/groups.get',
                         params={'user_id': id_user, 'extended': 1, 'count': 120,
                                 'access_token': self.token,
                                 'v': '5.87'})
        groups = []
        for group in r.json()['response']['items']:
            groups.append(group['id'])

        print('Finish getting all groups')
        return groups