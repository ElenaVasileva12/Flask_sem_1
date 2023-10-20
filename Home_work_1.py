# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), 
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. 
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.get('/main/') #это корневой(по ip)
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)



clothes = [
    {'title_clothes':'Кофта','colour':'красный','size':36,'price':47.5},
    {'title_clothes':'Юбка','colour':'синий','size':42,'price':64.2},
    {'title_clothes':'Джинсы','colour':'зеленый','size':34,'price':25.7},
    {'title_clothes':'Даша','colour':'желтый','size':32,'price':74.6},
    {'title_clothes':'Виктор','colour':'голубой','size':53,'price':9.9},
    {'title_clothes':'Майне','colour':'черный','size':48,'price':114.6},
]

@app.get('/clothes/')
def get_clothes():
    return render_template('clothes.html', clothes=clothes)

jacket=[
    {'title_jacket':'ветровка','colour':'синий','size':34,'price':198.0},
    {'title_jacket':'пуховик','colour':'красный','size':46,'price':554.2},
    {'title_jacket':'косуха','colour':'зеленый','size':54,'price':256.7},
]

@app.route('/jacket/')
def get_jacket():
    return render_template('jacket.html', jacket=jacket)


shoes=[
    {'title_shoes':'кроссовки','colour':'голубой','size':[34,35,36,37,38,39,40,41,42],'price':78.3},
    {'title_shoes':'калоши','colour':'желтый','size':[34,36,37,39,40,41,42],'price':58.9},
    {'title_shoes':'босоножки','colour':'черный','size':[34,35,36,37,38,39,40],'price':185.9},
]

@app.route('/shoes/')
def get_shoes():
    return render_template('shoes.html', shoes=shoes)




if __name__=='__main__':
    app.run(debug==True)