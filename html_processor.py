from jinja2 import Template
import json_processor

'''
запись всех постов из переменной all_post
в html документ 
с именем file_name
'''
def write_posts(all_posts, file_name = 'best_post.html'):

    #создать папку если ее еще нет
    path = json_processor.ensure_dir('res\\'+file_name)

    #
    html_template = open('templates\\templ.html','r').read()
    template = Template(html_template)
    render = template.render(posts=all_posts)[3:]

    with open(path,'w',encoding='utf-8') as file:
        file.write(render)
        print('Success')

