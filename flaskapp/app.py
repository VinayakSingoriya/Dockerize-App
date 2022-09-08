from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database local connection
# db = pymysql.connect(host='localhost',user='root',password='vinayak',database='todo',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

# Database remote connection
db = pymysql.connect(
            host='database-1.cmjf6xf1uo4z.us-east-1.rds.amazonaws.com',
            user='admin',
            port=3306,
            password='vinayak123',
            database='TodoApp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

# Routing

# db = pymysql.connect(host='52.2.189.87',user='admin',password='vinayak123',database='TodoApp',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

#Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404
 
#Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'),500

@app.errorhandler(502)
def bad_gateway(error):
    return render_template('502.html'),502



@app.route("/")
def home():
    try:
        sql_select_Query = "select * from record"
        cursor = db.cursor()
        cursor.execute(sql_select_Query )
        todo_list =  cursor.fetchall()  
        return render_template("base.html", todo_list=todo_list)
    except Exception as e : 
        return render_template("custom_error.html", error=e)

# DONE
@app.route("/add", methods=["POST"])
def add():
    try:
        cursor = db.cursor()
        title = request.form.get("title")
        sql = """INSERT INTO record(title, complete) VALUES(%s, %s)"""
        data = (title, False)
        cursor.execute(sql, data)
        db.commit()
        return redirect(url_for("home"))
    except Exception as e : 
        return render_template("custom_error.html", error=e)
    


@app.route("/update/<int:todo_id>")
def update(todo_id):
    try:
        cursor = db.cursor()
        select_query = "select * from record where id = %s"
        cursor.execute(select_query, todo_id)
        record = cursor.fetchone()
        val = not(record["complete"])
        update_query = """update record set complete = %s where id = %s"""
        data = (val, todo_id)
        cursor.execute(update_query, data)
        db.commit()
        return redirect(url_for("home"))
    except Exception as e : 
        return render_template("custom_error.html", error=e)


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    try:
        cursor = db.cursor()
        Delete_query = """Delete from record where id = %s"""
        cursor.execute(Delete_query, todo_id)
        db.commit()
        return redirect(url_for("home"))
    except Exception as e : 
        return render_template("custom_error.html", error=e)

@app.route("/reset")
def reset():
    try:
        cursor = db.cursor()
        cursor.execute("TRUNCATE TABLE record")
        db.commit()
        return redirect(url_for("home"))
    except Exception as e : 
        return render_template("custom_error.html", error=e)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
 