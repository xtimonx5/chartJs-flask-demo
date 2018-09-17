from flask import Flask, url_for
from flask import render_template
from flask import request
from file_parser import FileParser

app = Flask(__name__)


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def file_upload(show_error=False):
    return render_template('file_upload.html', show_error=show_error)


@app.route('/upload', methods=['POST', ])
def upload_file():
    if request.method == 'POST':
        f = request.files['file_to_parse']
        file_path = 'uploads/{}'.format(f.name)
        f.save(file_path)
        file_parser = FileParser(file_path)
        if file_parser.is_valid():
            context = {
                'petl_table': file_parser.get_petl_table(),
                'points_json': file_parser.get_points_json()
            }
            return render_template('result.html', context=context)
        else:
            return file_upload(show_error=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
