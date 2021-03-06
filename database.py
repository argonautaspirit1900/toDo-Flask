import sqlite3
import bcrypt

def createDatabase(path):
	conn = sqlite3.connect(path)
	conn.close()
	print("Database created or already existed")


def createUserModel(path):
	table = "User"
	columns = """
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		username TEXT UNIQUE,
		password TEXT
			 """
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS {}({});".format(table,columns))
	conn.commit()
	conn.close()
	print("User table created or already existed")

def createToDoModel(path):
	table = "toDo"
	columns = """
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		user_id INTEGER,
		description TEXT
			 """
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS {}({});".format(table,columns))
	conn.commit()
	conn.close()
	print("toDo table created or already existed")


def loginUser(username,password,path):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	users = c.execute("SELECT * FROM User")
	users = c.fetchall()
	conn.close()
	for user in users:
		if user[1] == username:
			if bcrypt.checkpw(password.encode('utf8'),user[2]):
				return user
			break
	return False

def createUser(username,password,path):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	user = c.execute("""INSERT INTO User(username,password)
						 VALUES (?,?);""",(username,password))
	conn.commit()
	conn.close()

def usernameExists(username,path):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	users = c.execute("SELECT * FROM User")
	users = c.fetchall()
	conn.close()
	for user in users:
		if user[1] == username:
			return True
	return False	

def createToDo(user_id,description,path):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("""INSERT INTO toDo(user_id,description) 
							VALUES(?,?)""",(user_id,description,))
	print("""INSERT INTO toDo(user_id,description) 
							VALUES({},{})""".format(user_id,description))
	conn.commit()
	conn.close()

def deleteToDo(user_id,todo_id,path):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("DELETE FROM toDo WHERE user_id=? and id=?",(user_id,todo_id,))
	conn.commit()
	conn.close()

def getToDos(user_id,path):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("SELECT * FROM toDo WHERE user_id=?",(user_id,))
	toDos = c.fetchall()
	conn.close()
	return toDos
#createUser("DSADddA","DSADdsaAS","db.sqlite3")
#getToDos(1,"db.sqlite3")
#createToDo(1,"dasdsa","db.sqlite3")