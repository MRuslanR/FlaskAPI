from app import models

db = models.Database("localhost", "postgres", "postgres", "password")
db.connect()