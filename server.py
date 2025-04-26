from flask import Flask, render_template, request
# Import the Maths package here
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = summation(num1, num2)
        return f"The result of summation is: {result}"
    except (ValueError, TypeError):
        return "Error: Please provide valid numerical inputs for num1 and num2."

@app.route("/sub")
def sub_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = subtraction(num1, num2)
        return f"The result of subtraction is: {result}"
    except (ValueError, TypeError):
        return "Error: Please provide valid numerical inputs for num1 and num2."

@app.route("/mul")
def mul_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = multiplication(num1, num2)
        return f"The result of multiplication is: {result}"
    except (ValueError, TypeError):
        return "Error: Please provide valid numerical inputs for num1 and num2."

@app.route("/")
def render_index_page():
    # Write your code here
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
