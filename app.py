from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    nama = request.form['nama']
    umur = request.form['umur']
    alamat = request.form['alamat']

    # Menjalankan perintah shell dengan menggunakan variabel
    command = f"bash script_shell.sh {nama} {umur} {alamat}"
    output = subprocess.check_output(command, shell=True, text=True)

    return render_template('result.html', output=output)

if __name__ == '__main__':
    app.run()
