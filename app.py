from flask import *
from pickle import *

f = open("model.pkl", "rb")
model = load(f)
f.close()


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
	if request.method == "POST":
		app_income = int(request.form["inc"])
		coapp_income = int(request.form["coinc"])
		dependents = int(request.form["dep"])
		loan_amt = int(request.form["amt"])
		loan_amt_term = int(request.form["loanamt"])
		credit_history = int(request.form["cre"])

		gender = int(request.form["gender"])
		married = int(request.form["married"])
		edu = int(request.form["edu"])
		self_emp = int(request.form["se"])
		pro_area = int(request.form["area"])

		d = [gender, married, dependents, edu, self_emp, app_income, coapp_income, loan_amt, loan_amt_term, credit_history, pro_area]

		res = model.predict([d])
		if res[0] == 0:
			msg = "Don't Approve the Applicant Loan"
			return render_template("home.html", msg = msg)
		else:
			msg = "Approve the Applicant Loan"
			return render_template("home.html", msg = msg)

	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(use_reloader = True, debug = True)








