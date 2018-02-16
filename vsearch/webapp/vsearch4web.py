from flask import Flask, render_template, request, escape
from vsearch import search4letters

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
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


if __name__ == '__main__':
    app.run(debug=True)