from werkzeug.security import generate_password_hash, check_password_hash

from app.models.auth.DatabaseFactory import DatabaseFactory

class Help():
    def __init__(self, code=0, user=None, skills="", topics=[], title="", description=""):
        self.code = code
        self.user = user
        self.skills = skills
        self.topics = topics
        self.title = title
        self.description = description
        self.connection = DatabaseFactory().getConnection()

    def create(self, help=""):
        try:
            self.connection.helps.insert({
                "user": help.user,
                "topics": help.topics,
                "title": help.title,
                "description": help.description
                })

            return True
        except:
            print("Houve um problema ao tentar criar uma ajuda.")
            return False

    def update(self, help=""):
        try:
            self.connection.helps.update({"user.email": help.user.email}, {
                "user": help.user,
                "topics": help.topics,
                "title": help.title,
                "description": help.description
                })

            return True
        except:
            print("Houve um problema ao tentar atualizar uma ajuda.")
            return False

    def delete(self, code=""):
        try:
            self.connection.helps.remove({
                "_id": ObjectId(code)
                })

            return True
        except:
            print("Houve um problema ao tentar deletar uma ajuda.")
            return False

    def getHelpsByUser(self, email=""):
        try:
            helps = self.connection.helps.find({
                "email": email
                })

            return helps
        except:
            print("Houve um problema ao tentar obter ajudas por email.")
            return None

    def getHelpsByTopics(self, topics=[]):
        try:
            helps = self.connection.helps.find({"topics": { "$all" : topics}})

            return helps
        except:
            print("Houve um problema ao tentar obter ajudas por tópicos.")
            return None