import json
import os

'''
    Запись json данных в файл file_name
    data - переменная типа json
    file_name - название файла в которй будут записаны данные
    по умолчанию запись происходит в файл post.json
'''
def write_json(data, file_name= 'post.json'):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

'''
    запись списка постов в файл
    posts - массив с постами
    file_name - имя файла
    по умолчанию post.json
'''
def write_posts(posts, file_name = 'post.json'):

    #создаем папку res если ее еще нет
    path = ensure_dir('res\\'+file_name)
    with open(path,'w',encoding='cp1251') as file:
        for post in posts:
            keys = post.keys()
            for key in keys:
                s = ('{} : {}\n'.format(key,post[key])).encode('cp1251', errors='ignore').decode('cp1251')
                file.write(s)

            file.write('\n\n\n')


'''
    получение выбранных полей из объекта json
    post - один пост из ВК
    data - словарь в котором храниться
    'id' - id поста,
    'likes' - количество лайков,
    'comment' - количество комментариев,
    'repost':  - количество репостов
    'views':  - количество просмотров
    'text': - текст поста
'''
def get_data(post):
    try:
        post_id = post['id']
    except:
        post_id = 0
    try:
        likes = int(post['likes']['count'])
    except:
        likes = 0
    try:
        comment = int(post['comments']['count'])
    except:
        comment = 0
    try:
        repost = post['reposts']['count']
    except:
        repost = 0
    try:
        views = post['views']['count']
    except:
        views = 0
    try:
        text = str(post['text'])
    except:
        text = '***'
    try:
        attach_photos = '-'
        if 'photo' in (post['attachments'][0]).keys():
            attach_photos = post['attachments'][0]['photo']['sizes'][-1]['url']
        if 'video' in (post['attachments'][0]).keys():
            attach_photos = post['attachments'][0]['video']['description']
    except:
        attach_photos = '-'
    try:
        group_id =  post['owner_id']
        link = 'https://vk.com/wall'+str(group_id)+'_'+str(post_id)
    except:
        link = '-'
    data = {
        'id': post_id,
        'likes': likes,
        'comment': comment,
        'repost': repost,
        'views': views,
        'text': text,
        'attachments':attach_photos,
        'link': link
    }

    return  data


'''
    сортировка постов из групп вк
    по убыванию популярности
'''
def sort_post(posts):
    return sorted(posts,key = lambda x: x['likes'],reverse=True)

'''
создание новой папки если она еще не существует
path - путь к новой папке
filename - имя файла
'''
def ensure_dir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path