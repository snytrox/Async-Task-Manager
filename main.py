from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import models, schemas, database

app= FastAPI()
# Uygulama başladığında tabloları otomatik oluşturur
@app.on_event("startup")
async def startup():
#begin= "Veritabanında güvenli bir oturum aç,
#işim bitince (hata yoksa) her şeyi onayla (commit)" demektir.
    async with database.engine.begin() as conn:
# 'run_sync' asenkron motor üzerinde senkron bir fonksiyonu (create_all) 
# bloklama (blocking) yapmadan güvenle çalıştırmak için kullanılan bir köprüdür.
        await conn.run_sync(models.Base.metadata.create_all)
@app.get("/")
def check_status():
    return {"status": "çalıştı"}

@app.post("/tasks/", response_model=schemas.TaskResponse)
async def create_task(
    task:schemas.TaskCreate,
    db:AsyncSession = Depends(database.get_db)):
#Pydantic nesnesini (task) Python sözlüğüne (dict) çeviriyoruz (model_dump).
#'**' (Unpacking) operatörü ile bu sözlüğü parçalayıp models.Task'ın içine dağıtıyoruz.
#Yani: title=task.title, priority=task.priority gibi tek tek yazma zahmetinden kurtuluyoruz.
        new_task = models.Task(**task.model_dump())
        db.add(new_task)
# 'await' kullanıyoruz çünkü veritabanına yazma işlemi bir I/O (giriş-çıkış) işlemidir.
# Bu işlem sürerken programın diğer istekleri karşılamaya devam etmesini sağlıyoruz (Asenkron yapı).
        await db.commit()
        await db.refresh(new_task) 
        return new_task
    
