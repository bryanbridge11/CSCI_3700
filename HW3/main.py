from flask import Flask, render_template
import util

app = Flask(__name__)

username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/api/update_basket_a')
def update_basket_a():
	success_message = "No update performed"
	cursor, connection = util.connect_to_db(username,password,host, port, database)
	try:
		record = util.insert_into_basket_a(cursor,"INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
	
		if record:
			print('Successfully Updated')
	
		else:
			print('Error, Something Wrong with SQL Command')
	except Exception as error:
        	return f"Error: {error}"
	
	util.disconnect_from_db(connection,cursor)
	
	if record:
		success_message = "Basket A Updated Successfully"
	
	return render_template('update.html', success_message=success_message)
	
	
@app.route('/api/unique')
def unique():
	cursor, connection = util.connect_to_db(username, password, host, port, database)
	record_a = util.run_and_fetch_sql(cursor,"SELECT DISTINCT fruit_a FROM basket_a;")
	if record_a == -1:
		print('Basket A Not Retrieved')
	else:
		print('Basket A Retrieved.')
		a_col_names = [desc[0] for desc in cursor.description]
		a_log = record_a[:5]
	
	record_b = util.run_and_fetch_sql(cursor,"SELECT DISTINCT fruit_b FROM basket_b;")
	if record_b == -1:
		print('Basket B Not Retrieved')
	else:
		print('Basket B Retrieved')
		b_col_names = [desc[0] for desc in cursor.description]
		b_log = record_b[:5]
		
	record_uni = util.run_and_fetch_sql(cursor, "SELECT DISTINCT fruit FROM (SELECT fruit_a AS fruit FROM basket_a UNION ALL SELECT fruit_b AS fruit FROM basket_b) AS unique_fruits;")
	if record_uni == -1:
		print('Unique Basket Not Found')
	else: 
		print('Basket Unique Retrieved')
		uni_col_names = [desc[0] for desc in cursor.description]
		uni_log = record_uni[:7]
	
	util.disconnect_from_db(connection, cursor)
	return render_template('index.html', sql_table_a = a_log, table_title_a=a_col_names, sql_table_b = b_log, table_title_b=b_col_names, sql_table_uni = uni_log, table_title_uni=uni_col_names)


if __name__ == '__main__':
	app.debug = True
	ip = '127.0.0.1'
	app.run(host=ip)
		
