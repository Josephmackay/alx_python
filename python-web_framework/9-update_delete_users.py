from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<db_username>:<db_password>@localhost/alx_flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

# Update a User
@app.route('/update_user/<int:user_id>', methods=['GET','POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        flash("User not found!", 'error')
        return redirect('/users')

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            flash("Name and Email are required fields.", 'error')
        else:
            try:
                user.name = name
                user.email = email
                db.session.commit()
                flash("User updated successfully!", 'success')
            except Exception as e:
                db.session.rollback()
                flash(f"Error: {str(e)}", 'error')

    return render_template('update_user.html', user=user)

# Delete a User
@app.route('/delete_user/<int:user_id>', methods=['GET','POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        flash("User not found!", 'error')
        return redirect('/users')

    if request.method == 'POST':
        try:
            db.session.delete(user)
            db.session.commit()
            flash("User deleted successfully!", 'success')
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", 'error')
        return redirect('/users')

    return render_template('delete_user.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
