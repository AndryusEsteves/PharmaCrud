import pprint
from ..data.database import medicamentos as db

def listar_remedios_por_id (remedios, id_remedio):
    return [remedio for remedio in remedios if remedio['id'] == id_remedio]

def listar_todos_remedios(remedios):
    return remedios

pprint.pprint(listar_todos_remedios(db))