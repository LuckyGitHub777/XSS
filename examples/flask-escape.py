"""
Defensive Flask example using Jinja2 escaping.

This file demonstrates safe server-side rendering of user input.
It is for local educational use only.
"""

from flask import Flask, render_template_string, request

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Safe Server Example</title>
</head>
<body>
  <h1>User comment</h1>

  <form method="post">
    <label for="comment">Comment:</label>
    <input id="comment" name="comment">
    <button type="submit">Submit</button>
  </form>

  <p>{{ comment }}</p>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    comment = ""

    if request.method == "POST":
        comment = request.form.get("comment", "")

    return render_template_string(TEMPLATE, comment=comment)


if __name__ == "__main__":
    app.run(debug=True)
