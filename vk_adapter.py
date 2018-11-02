import requests

'''
    Описание констант для работы с VK API
'''
class VK:
    #https://api.vk.com/method/wall.get?owner_id=-165878204&v=5.87
    #'750749131600d4b82e17b9477898644403a85f89547b9ea21c7d791dc03b557a49cbe4b9c3e4aa335c41c'

    token = '750749131600d4b82e17b9477898644403a85f89547b9ea21c7d791dc03b557a49cbe4b9c3e4aa335c41c'
    version = '5.87'
    count_read_posts = 20

    '''
        получить все посты до указанной даты 
        group_id - id группы
        last_date - дата размещения постов до которой их нужно просматривать
        вощвращается массив из словарей
    '''
    def get_all_posts_in_group(self, group_id, last_date, offset = 0):
        all_posts = []
        group_id = '-' + group_id
        while True:
            print('\33[32m'+str(int(offset/self.count_read_posts//1)+1) + ' request........done'+ '\x1b[0m')
            r = requests.get('https://api.vk.com/method/wall.get',
                             params={'owner_id': group_id, 'count': self.count_read_posts,
                                     'offset': offset, 'access_token': self.token, 'v': self.version})

            if 'response' in r.json().keys():
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
            if 'error' in r.json().keys():
                print( '\33[31m'+'Error: ' + r.json()['error']['error_msg']+ '\x1b[0m')
                break
        return all_posts

    '''
    возвращает список групп пользователя
    id_user - id пользователя
    '''
    def get_all_user_group(self, id_user):
        print('Getting all groups')

        r = requests.get('https://api.vk.com/method/groups.get',
                         params={'user_id': id_user, 'extended': 1, 'count': 120,
                                 'access_token': self.token,
                                 'v': self.version})
        groups = []
        for group in r.json()['response']['items']:
            groups.append(str(group['id']))

        print('Finish getting all groups')
        return groups