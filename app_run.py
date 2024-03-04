from myapp import MyApp
from database import SentenceDatabase


if __name__ == "__main__":
    db = SentenceDatabase('sentences.db')
    my_app = MyApp(db)
    my_app.run()