bd = [
    {"nome": "luiz", 'cpf': "07123121123", 'grupos': [{'materia':"artes", 'link': "https://chat.whatsapp.com/CHuObirQ1iw7ZSBdBE558"},{'materia':"algo", 'link': "https://chat.whatsapp.com/CHuObirQ1iw7ZSBdBE558"}, {'materia':"nem ideia", 'link': "https://chat.whatsapp.com/CHuObirQ1iw7ZSBdBE558"}]},
    {'nome': "sebas", 'cpf': "07165384154", 'grupos': [{'materia':"artes", 'link': "https://chat.whatsapp.com/CHuObirQ1iw7ZSBdBE558"},{'materia':"algo", 'link': "https://chat.whatsapp.com/CHuObirQ1iw7ZSBdBE558"}, {'materia':"nem ideia", 'link': "https://chat.whatsapp.com/CHuObirQ1iw7ZSBdBE558"}]},
    {'nome': "miguel", 'cpf': "071212899812", 'grupos': [{'materia':"artes", 'link': "https://chat.whatsapp.com/CHuObirQ1iw7ZSBdBE558"},{'materia':"algo", 'link': "https://chat.whatsapp.com/CHuObirQ1iw7ZSBdBE558"}, {'materia':"nem ideia", 'link': "https://chat.whatsapp.com/CHuObirQ1iw7ZSBdBE558"}]}
    ]

def buscar_alunos_no_bd(cpf: str):
    for aluno in bd:
        if aluno['cpf'] == cpf:
            return aluno
    return "não encontrado"