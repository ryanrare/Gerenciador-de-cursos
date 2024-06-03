from sqlalchemy import text

trilhas_query = text("""
    SELECT t.id, t.titulo, t.descricao
    FROM trilha AS t
    JOIN trilha_user AS tu ON t.id = tu.trilha_id
    WHERE tu.user_id = :user_id
""")

cursos_query = text("""
    SELECT c.id, c.titulo, c.descricao
    FROM curso AS c
    JOIN curso_user AS cu ON c.id = cu.curso_id
    WHERE cu.user_id = :user_id
""")