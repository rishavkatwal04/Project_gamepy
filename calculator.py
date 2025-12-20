from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)
last_result = 0

def preprocess_expression(expression, last_result):
    expression = expression.lower().replace("ans", str(last_result))
    expression = expression.replace(" ", "")
    expression = re.sub(r'(\d)(\()', r'\1*\2', expression)
    expression = re.sub(r'(\))(\d)', r'\1*\2', expression)
    expression = re.sub(r'(\))(\()', r'\1*\2', expression)
    expression = expression.replace("^", "**")

    return expression

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    global last_result
    data = request.json
    expr = data.get("expression", "")
    try:
        clean_expr = preprocess_expression(expr, last_result)
        if not set(clean_expr).issubset(set("0123456789+-*/().")):
            return jsonify({"error": "Invalid characters"})
        last_result = eval(clean_expr)
        if isinstance(last_result, float) and last_result.is_integer():
            last_result = int(last_result)
        return jsonify({"result": last_result})
    except ZeroDivisionError:
        return jsonify({"error": "Division by zero"})
    except:
        return jsonify({"error": "Invalid expression"})

if __name__ == "__main__":
    app.run(debug=True)
