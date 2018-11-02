import datetime
import vk_adapter
import json_adapter



def main():
    print('Start')
    groups_id = ['101436686','36941068','96457590','93943373','113590406']
    # groups_id = ['125704690']
    #инициализация класса
    vk = vk_adapter.VK()
    last_date = int((datetime.datetime.now() - datetime.timedelta(days=vk.shift_last_day)).timestamp()//1)

    # загрузка объектов json с ВК
    '''выбор 10 самых популярных постов из каждой группы
        и добавление их в конец файла 
    '''
    all_posts=[]
    for group_id in groups_id:
        all_group_posts = vk.get_all_posts_in_group(group_id, last_date)
        data_posts = [json_adapter.get_data(post) for post in all_group_posts]
        data_posts = json_adapter.sort_post(data_posts)
        data_posts = data_posts[:10]
        all_posts.extend(data_posts)

    # запись самых популярных постов в файл, отсортировав
    #и выбрав самые популярные из всех груп
    all_sort_post = json_adapter.sort_post(all_posts)
    json_adapter.write_posts(all_sort_post, 'popular_post_sort.txt')
    print('Finish')


def most_popular_posts_in_user_group():
    '''
    Настроечаная информация
    id пользователя
    shift_last_day - за сколько дней просматривать посты
    '''
    vk = vk_adapter.VK()
    id_user = '113930716'
    shift_last_day = 1
    groups = vk.get_all_user_group(id_user)
    last_date = int((datetime.datetime.now() - datetime.timedelta(days=shift_last_day)).timestamp() // 1)
    all_posts = []

    for group_id in groups:
        all_post_in_group = vk.get_all_posts_in_group(group_id,last_date)
        if all_post_in_group:
            '''
                получение data_post из json
                сортировка постов по убываю популярности
                и добавление первых 10 в общий список популярных постов пользователя
            '''
            data_posts = json_adapter.sort_post([json_adapter.get_data(post) for post in all_post_in_group])[:10]
            all_posts.extend(data_posts)

    most_popular_posts = json_adapter.sort_post(all_posts)[:100]
    json_adapter.write_posts(most_popular_posts,'my_best_days_posts.txt')




if __name__ == '__main__':
    # main()
    most_popular_posts_in_user_group()