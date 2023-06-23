from fastapi import APIRouter

router = APIRouter()

list_etudiant = []

@router.post("/etudiants")
async def add_etudiant(etudiant: dict)-> dict:
    list_etudiant.append(etudiant)


    return {"message": "Etudiant ajouté avec succès"}


@router.get("/etudiants")
async def get_etudiants():
    return {
        "data": list_etudiant
    }

@router.get("/etudiants/{id}")
async def get_etudiant(id: str) -> dict:
    for etudiant in list_etudiant:
        if etudiant["id"] == id:
            return etudiant["etudiant": etudiant]
        
    return {"message": "Etudiant non trouvé"}

