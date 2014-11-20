# coding=<UTF-8>
import sqlite3, json, random, hashlib

class Database:
	
	db_path = "songBook.db"
	
	conn = None
	cursor = None
	
	def __init__(self):
		self.conn = sqlite3.connect(self.db_path)
		self.cursor = self.conn.cursor()
	
	def hello(self):
		return "Hello!"
		
	def add_song(self, title, content, userid):
		params = [title, content, userid]
		self.cursor.execute("INSERT INTO song (title, content, userid) VALUES (?, ?, ?)", params)
		self.conn.commit()
		print ("added song with title %s" %title)
		
	def get_song(self, songId):
		self.cursor.execute("SELECT * FROM song WHERE id=?", [songId])
		result = self.cursor.fetchone()
		if result:
			return json.dumps(result)
		else:
			return False;
	
	def add_user(self, username, email, password):
		
		def generate_salt(length = 8):
			salt = ''
			for i in range(length):
				salt += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
			return salt
			
		salt = generate_salt()
		
		passwordAndSalt = password + salt
		
		hash_object = hashlib.sha256(passwordAndSalt.encode("utf-8"))
		passwordHash = hash_object.hexdigest()
		
		
		params = [username, email, passwordHash, salt]
		self.cursor.execute("INSERT INTO user (username, email, passwordHash, passwordSalt) VALUES (?, ?, ?, ?)", params)
		self.conn.commit()
		return "user added";
		
	def get_users(self):
		self.cursor.execute("SELECT * FROM user")
		return json.dumps(self.cursor.fetchall())
	
		
