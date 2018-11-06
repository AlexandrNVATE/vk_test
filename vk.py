import datetime
import vk_adapter
import json_processor
import html_processor



def main():
    print('Start')
    # groups_id = ['101436686','36941068','96457590','93943373','113590406']
    groups_id = ['36941068']
    shift_last_day = 1
    #инициализация класса
    vk = vk_adapter.VK()
    last_date = int((datetime.datetime.now() - datetime.timedelta(days=shift_last_day)).timestamp()//1)

    # загрузка объектов json с ВК
    '''выбор 10 самых популярных постов из каждой группы
        и добавление их в конец файла 
    '''
    all_posts=[]
    for group_id in groups_id:
        all_group_posts = vk.get_all_posts_in_group(group_id, last_date)
        data_posts = [json_processor.get_data(post) for post in all_group_posts]
        data_posts = json_processor.sort_post(data_posts)
        data_posts = data_posts[:10]
        all_posts.extend(data_posts)

    # запись самых популярных постов в файл, отсортировав
    #и выбрав самые популярные из всех груп
    all_sort_post = sorted(all_posts,key=lambda x: x['likes'], reverse=True)
    html_processor.write_posts(all_posts, 'best_post.html')
    print('Finish')


def most_popular_posts_in_user_group():
    '''
    Настроечаная информация
    id пользователя
    shift_last_day - за сколько дней просматривать посты
    '''
    vk = vk_adapter.VK()
    #113930716
    #83656262
    id_user = '83656262'
    shift_last_day = 1
    groups = vk.get_all_user_group(id_user)
    last_date = int((datetime.datetime.now() - datetime.timedelta(days=shift_last_day)).timestamp() // 1)
    all_posts = []

    #данные о пользователе
    user = vk.get_user_by_id(id_user)
    print(user['last_name']+' '+user['last_name'])
    for group_id in groups:
        all_post_in_group = vk.get_all_posts_in_group(group_id,last_date)
        if all_post_in_group:
            '''
                получение data_post из json
                сортировка постов по убываю популярности
                и добавление первых 10 в общий список популярных постов пользователя
            '''
            data_posts = json_processor.sort_post([json_processor.get_data(post) for post in all_post_in_group])[:10]
            all_posts.extend(data_posts)

    most_popular_posts = json_processor.sort_post(all_posts)[:100]
    html_processor.write_posts(most_popular_posts, 'my_best_days_posts.html')



def temp():
    html_processor.write_posts([])


if __name__ == '__main__':
    # main()
    most_popular_posts_in_user_group()
    # temp()