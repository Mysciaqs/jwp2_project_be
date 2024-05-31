-- DropForeignKey
ALTER TABLE "Column" DROP CONSTRAINT "Column_userId_fkey";

-- DropForeignKey
ALTER TABLE "Task" DROP CONSTRAINT "Task_columnId_fkey";

-- AddForeignKey
ALTER TABLE "Column" ADD CONSTRAINT "Column_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Task" ADD CONSTRAINT "Task_columnId_fkey" FOREIGN KEY ("columnId") REFERENCES "Column"("id") ON DELETE CASCADE ON UPDATE CASCADE;
