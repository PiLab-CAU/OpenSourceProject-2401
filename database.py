import sqlite3

class SentenceDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.initialize_database()

    def initialize_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sentences
                          (id INTEGER PRIMARY KEY, sentence TEXT, feedback TEXT)''')
        conn.commit()
        conn.close()

    def insert_sentence(self, sentence, feedback=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        print("{} saved.".format(sentence))
        if feedback is not None:
            cursor.execute("INSERT INTO sentences (sentence, feedback) VALUES (?, ?)", (sentence, feedback))
        # feedback 값이 제공되지 않은 경우
        else:
            cursor.execute("INSERT INTO sentences (sentence) VALUES (?)", (sentence,))
        conn.commit()
        conn.close()

    def form_checker(self, text):
        if text.endswith(':'):
                text = text[-1]
        return text

    def get_all_sentences(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sentences")
        sentences = cursor.fetchall()
        conn.close()
        return sentences

