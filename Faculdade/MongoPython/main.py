#pip install pymongo
from pymongo import MongoClient
# Conectar ao MongoDB (localhost na porta padrão 27017)
client = MongoClient("mongodb://localhost:27017/")
# Selecionar o banco de dados e a coleção
db = client['meu_banco_de_dados']
colecao = db['minha_colecao']

# Exemplo de documento
documento = {
"nome": "Roberto Cândido",
"idade": 30,
"profissao": "Desenvolvedor"
}
# Inserir um único documento
resultado = colecao.insert_one(documento)
print("Documento inserido com o ID:", resultado.inserted_id)

documentos = [
    {
        "nome": "Ana",
        "idade" : 23,
        "profissao":"Professora"
    }
]

resultado = colecao.insert_many(documentos)
print("IDs dos documentos inseridos", resultado.inserted_ids)

# Buscar um único documento
# Buscar um único documento
documento = colecao.find_one({"nome": "Roberto Cândido"})
print("Documento encontrado:", documento)
# Buscar múltiplos documentos
documentos = colecao.find({"idade": {"$gt": 20}})
for doc in documentos:
    print(doc)
resultado = colecao.delete_one({ "nome": "José Roberto",})
print("Número de documentos deletados:", resultado.deleted_count)
resultado = colecao.delete_many({"idade": {"$lt": 30}})
print("Número de documentos deletados:", resultado.deleted_count)

projecao = {"_id": 0, "nome": 1, "idade": 1} 
resultados = colecao.find({}, projection=projecao)
for doc in resultados:
    print(doc)