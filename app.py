import os

from flask import Flask, send_from_directory, current_app
from flask import render_template
from flask import request

from file_parser import FileParser
from xlsx_writer import REPORTS_ROOT

app = Flask(__name__)


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
                'points_json': file_parser.get_points_json(),
                'xlsx_report': file_parser.get_xlsx_report(),
            }
            return render_template('result.html', context=context)
        else:
            return file_upload(show_error=True)


@app.route('/reports/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, REPORTS_ROOT)
    return send_from_directory(directory=uploads, filename=filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
