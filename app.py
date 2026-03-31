from flask import render_template, Flask, request
from conversion import convert_now
from search import *

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])

def index():
    error = None

    if request.method == "POST":
        from_input = request.form.get("from_currency")
        to_input = request.form.get("to_currency")
        amount_input = request.form.get("amount")

        try:
            amount = float(amount_input)
            if amount <=0:
                raise ValueError
        except:
            error = "Invalid Amount"
            return render_template("index.html", error=error)

        currencies = get_currencies()

        from_currency = find_currency(from_input, currencies)
        to_currency = find_currency(to_input, currencies)
        if not from_currency or not to_currency:
            error = "Invalid currency"
            return render_template("index.html", error=error)

        result = convert_now(from_currency, to_currency, amount)

        return render_template(
            "result.html",
            result=result,
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount
        )

    return render_template("index.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)