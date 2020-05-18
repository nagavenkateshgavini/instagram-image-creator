import os

from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(PROJECT_ROOT, 'static', 'insta_photos')

app.config['DEBUG'] = True
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

@app.route("/home")
def hello():
    return render_template('index.html', message="Code Heist")

@app.route("/createmain")
def createmain():
    return render_template('createmain.html')

@app.route("/createcontent")
def createcontent():
    return render_template('createcontent.html')

@app.route("/about")
def about():
    return render_template('about.html')

def get_main_formdata(request):
    d = {
        'title': request.form['maintitle'],
        'subtitle': request.form['mainsubtitle']
    }

    return d

@app.route("/preview_imgs", methods=["POST", "GET"])
def preview_imgs():
    # Code to access the form data
    form_d = get_main_formdata(request)

    # Code for generating image and save it in the download folder
    out_file = 'out.png'

    return render_template('previewmain.html', main_image=out_file, form_d=form_d)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(
        app.config['DOWNLOAD_FOLDER'],
        filename,
        as_attachment=True)


if __name__ == '__main__':
    app.run()
