import database

class User:

	def __init__(self):
		self.db = database.Database()
	
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
		self.db.cursor.execute("INSERT INTO user (username, email, passwordHash, passwordSalt) VALUES (?, ?, ?, ?)", params)
		self.db.conn.commit()
		return "user added";
