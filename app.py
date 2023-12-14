from flask import Flask,render_template,jsonify
app = Flask(__name__)

JOBS = [
  {'id': 1, 'title': 'Python Developer', 'location': 'Tema', 'salary': 'GHS120,000'},
  {'id': 2, 'title': 'Data Scientist', 'location': 'Ho', 'salary': 'GHS90,000'},
  {'id': 3, 'title': 'Software Engineer', 'location': 'Koforidua', 'salary': 'GHS90,000'},
  {'id': 4, 'title': 'Network Engineer', 'location': 'Accra', 'salary': 'GHS90,000'},
  {'id': 5, 'title': 'AI Developer', 'location': 'Kumasi', 'salary': 'GHS90,000'},
  {'id': 6, 'title': 'ML Developer', 'location': 'Kusi', 'salary': 'GHS980,000'},
  ]

  
@app.route('/')
def flex_dev():
    return render_template('home.html' ,job_offers = JOBS, com_name = 'Esteem')

@app.route('/api/jobs')
def job_list():
  return jsonify(JOBS)




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80)