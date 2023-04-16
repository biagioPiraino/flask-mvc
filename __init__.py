from flask import Flask, render_template
from controllers.user_controller import user_bp
from controllers.action_controller import action_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(action_bp)
  
@app.route('/')
def index():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)