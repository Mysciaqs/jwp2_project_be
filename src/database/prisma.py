from prisma import Prisma, models

prisma = Prisma(auto_register=True)

User = models.User
