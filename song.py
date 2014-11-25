import database

class Song:

	def __init__(self):
		self.db = database.Database()
			
	def get_song(self, songId):
		self.cursor.execute("SELECT * FROM song WHERE id=?", [songId])
		result = self.cursor.fetchone()
		if result:
			return json.dumps(result)
		else:
			return False;


