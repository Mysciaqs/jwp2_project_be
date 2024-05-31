from prisma import Prisma, models

prisma = Prisma(auto_register=True)

User = models.User
Column = models.Column
Task = models.Task
