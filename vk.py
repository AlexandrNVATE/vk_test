import datetime
import vk_adapter
import json_adapter
import requests



def main():
    print('Start')
    #инициализация класса
    vk = vk_adapter.VK()
    last_date = int((datetime.datetime.now()- datetime.timedelta(days=vk.shift_last_day)).timestamp()//1)

    # загрузка объектов json с ВК
    '''выбор 10 самых популярных постов из каждой группы
        и добавление их в конец файла 
    '''
    all_posts=[]
    groups_id = vk.get_all_user_group('113930716')
    print(groups_id)

    for group_id in groups_id:
        all_group_posts = vk.get_all_posts_in_group(group_id, last_date)
        data_posts = [json_adapter.get_data(post) for post in all_group_posts]
        data_posts = sorted(data_posts, key=lambda x: x['likes'], reverse=True)
        data_posts = data_posts[:10]
        all_posts.extend(data_posts)
    #запись 10 самых популярных постов тз каждой группы в файл, без сортировки
    json_adapter.write_posts(all_posts, 'ali_post.txt')

    # запись самых популярных постов в файл, отсортировав
    #и выбрав самые популярные из всех груп
    all_sort_post = sorted(all_posts,key=lambda x: x['likes'], reverse=True)
    json_adapter.write_posts(all_posts, 'ali_post_sort.txt')
    print('Finish')




if __name__ == '__main__':
    main()