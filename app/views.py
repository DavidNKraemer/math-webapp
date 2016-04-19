import markdown
from flask import Markup, render_template, request
from app.derivative_problem import derivative_string, evaluate_derivative
from app import app
from app.derivative_problem import latex, parse_expr 
from app.derivative_problem import transformations

def str_to_latex(string):
    return latex(parse_expr(string, transformations=transformations))

@app.route("/")
def index():
    return render_template('index.html', **locals()) 


problem = {'new': None, 'old': None}
answer = {'new': None, 'old': None}
@app.route("/derivatives", methods=['GET', 'POST'])
def derivatives():
    if request.method == 'POST':
        input_text = request.form['text']
        problem['old'] = problem['new']
        answer['old'] = answer['new']

        correct = evaluate_derivative(input_text, answer['old'])
        input_text = str_to_latex(input_text)
    else:
        input_text = None
        correct = None


    problem['new'], answer['new'] = derivative_string()
    return render_template("derivatives.html",
            problem=problem,
            correct=correct,
            input_text=input_text)


@app.route("/pi")
def pi():
    return "{:1.100f}".format(np.pi)
