# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, escape
from vsearch import search4letters

# mysql user-login: vsearch, password: passwd

app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Добро пожаловать!!')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(search4letters(phrase, letters))
    log_request(request, result)
    return render_template('results.html',
                           the_title='Результаты поиска',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=result)


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for row in log:
            contents.append([])
            for item in row.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote Address', 'User Agent', 'Results',)
    return render_template('viewlog.html',
                           the_title='Просмотр логов',
                           the_row_titles=titles,
                           the_data=contents,)


def log_request(req: 'flask_request', res: str) -> None:
    # with open('vsearch.log', 'a') as log:
    #     print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'passwd',
                'database': 'vsearchlog',
                'charset': 'utf8'}
    import mysql.connector

    my_connection = mysql.connector.connect(**dbconfig)
    cursor = my_connection.cursor()

    _SQL = """INSERT INTO log 
              (phrase, letters, ip, browser_string, results) 
              VALUES (%s, %s, %s, %s, %s)"""

    cursor.execute('SET NAMES utf8;')
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))

    my_connection.commit()

    _SQL = """SELECT * FROM log"""
    cursor.execute(_SQL)
    for row in cursor.fetchall():
        print(str(row).encode('utf8'))

    cursor.close()
    my_connection.close()


if __name__ == '__main__':
    app.run(debug=True)