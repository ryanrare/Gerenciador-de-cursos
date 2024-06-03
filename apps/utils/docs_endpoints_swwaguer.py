get_user_response = {
    'responses': {
        200: {
            'description': 'A user object',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'username': {'type': 'string'},
                    'email': {'type': 'string'},
                    'created_at': {'type': 'string', 'format': 'date-time'},
                    'is_deleted': {'type': 'boolean'},
                    'comentarios': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'descricao': {'type': 'string'}
                            }
                        }
                    },
                    'avaliacoes': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'valor': {'type': 'integer'}
                            }
                        }
                    },
                    'trilhas': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'nome': {'type': 'string'},
                                'descricao': {'type': 'string'}
                            }
                        }
                    },
                    'cursos': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'titulo': {'type': 'string'},
                                'descricao': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        },
        404: {'description': 'User not found'}
    }
}

update_user_response = {
    'parameters': [
        {
            'name': 'username',
            'in': 'body',
            'type': 'string',
            'required': False,
            'description': 'New username of the user'
        },
        {
            'name': 'email',
            'in': 'body',
            'type': 'string',
            'required': False,
            'description': 'New email of the user'
        },
        {
            'name': 'password',
            'in': 'body',
            'type': 'string',
            'required': False,
            'description': 'New password of the user'
        }
    ],
    'responses': {
        200: {
            'description': 'User updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'username': {'type': 'string'},
                    'email': {'type': 'string'},
                    'created_at': {'type': 'string', 'format': 'date-time'},
                    'is_deleted': {'type': 'boolean'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        },
        404: {
            'description': 'User not found'
        }
    }
}

delete_user_response = {
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the user to be deleted'
        }
    ],
    'responses': {
        200: {
            'description': 'User deleted successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        },
        404: {
            'description': 'User not found'
        }
    }
}

login_response = {
    'parameters': [
        {
            'name': 'username',
            'in': 'body',
            'type': 'string',
            'required': True,
            'description': 'Username of the user'
        },
        {
            'name': 'password',
            'in': 'body',
            'type': 'string',
            'required': True,
            'description': 'Password of the user'
        }
    ],
    'responses': {
        200: {
            'description': 'User logged in successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'access_token': {'type': 'string'}
                }
            }
        },
        401: {
            'description': 'Invalid credentials'
        }
    }
}

home_response = {
    'responses': {
        200: {
            'description': 'A list of users',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'username': {'type': 'string'},
                        'email': {'type': 'string'},
                        'created_at': {'type': 'string', 'format': 'date-time'},
                        'is_deleted': {'type': 'boolean'}
                    }
                }
            }
        }
    }
}

register_response = {
    'parameters': [
        {
            'name': 'username',
            'in': 'body',
            'type': 'string',
            'required': True,
            'description': 'Username of the user'
        },
        {
            'name': 'email',
            'in': 'body',
            'type': 'string',
            'required': True,
            'description': 'Email of the user'
        },
        {
            'name': 'password',
            'in': 'body',
            'type': 'string',
            'required': True,
            'description': 'Password of the user'
        }
    ],
    'responses': {
        201: {
            'description': 'User created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'username': {'type': 'string'},
                    'email': {'type': 'string'},
                    'created_at': {'type': 'string', 'format': 'date-time'},
                    'is_deleted': {'type': 'boolean'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        }
    }
}

get_all_trilhas_response = {
    'responses': {
        200: {
            'description': 'A list of trilhas',
            'schema': {
                'type': 'object',
                'properties': {
                    'trilhas': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'titulo': {'type': 'string'},
                                'descricao': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized'
        }
    }
}

create_trilha_response = {
    'parameters': [
        {
            'name': 'data',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'titulo': {'type': 'string'},
                    'descricao': {'type': 'string'}
                },
                'required': ['titulo', 'descricao']
            },
            'required': True,
            'description': 'Data for creating a new trilha'
        }
    ],
    'responses': {
        201: {
            'description': 'Trilha created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'titulo': {'type': 'string'},
                    'descricao': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Missing data'
        }
    }
}

get_trilha_response = {
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the trilha'
        }
    ],
    'responses': {
        200: {
            'description': 'Trilha found',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'titulo': {'type': 'string'},
                    'descricao': {'type': 'string'}
                }
            }
        },
        404: {
            'description': 'Trilha not found'
        }
    }
}

update_trilha_response = {
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the trilha to be updated'
        },
        {
            'name': 'data',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'titulo': {'type': 'string'},
                    'descricao': {'type': 'string'}
                },
                'required': ['titulo', 'descricao']
            },
            'required': True,
            'description': 'Updated data for the trilha'
        }
    ],
    'responses': {
        200: {
            'description': 'Trilha updated successfully'
        },
        400: {
            'description': 'Missing data'
        },
        404: {
            'description': 'Trilha not found'
        }
    }
}

delete_trilha_response = {
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the trilha to be deleted'
        }
    ],
    'responses': {
        200: {
            'description': 'Trilha deleted successfully'
        },
        404: {
            'description': 'Trilha not found'
        }
    }
}

get_trilha_comentarios_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha para buscar os comentários'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de comentários da trilha',
            'schema': {
                'type': 'object',
                'properties': {
                    'comentarios': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'descricao': {'type': 'string'},
                                'id_user': {'type': 'integer'}
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Trilha não encontrada'
        }
    }
}

create_trilha_comentario_response = {
    'parameters': [
        {
            'name': 'trilha_id e user_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Já são pegos da url e sessão Jwt'
        },
        {
            'name': 'descricao',
            'in': 'body',
            'type': 'string',
            'required': True,
            'description': 'Descrição do comentário'
        }
    ],
    'responses': {
        201: {
            'description': 'Comentário adicionado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'comentario': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'descricao': {'type': 'string'},
                            'id_user': {'type': 'integer'}
                        }
                    }
                }
            }
        },
        400: {
            'description': 'Dados do comentário ausentes'
        },
        404: {
            'description': 'Trilha não encontrada'
        },
        500: {
            'description': 'Erro interno do servidor ao criar o comentário'
        }
    }
}

delete_trilha_comentario_response = {
    'parameters': [
        {
            'name': 'comentario_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do comentário a ser deletado ja vem pela a url'
        }
    ],
    'responses': {
        200: {
            'description': 'Comentário deletado com sucesso'
        },
        404: {
            'description': 'Trilha não encontrada ou Comentário não encontrado nesta trilha'
        },
        500: {
            'description': 'Erro interno do servidor ao deletar o comentário'
        }
    }
}

create_trilha_avaliacao_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha para a qual a avaliação será criada'
        },
        {
            'name': 'valor',
            'in': 'body',
            'type': 'integer',
            'required': True,
            'description': 'Valor da avaliação'
        },
        {
            'name': 'descricao',
            'in': 'body',
            'type': 'string',
            'required': False,
            'description': 'Descrição da avaliação'
        }
    ],
    'responses': {
        201: {
            'description': 'Avaliação criada com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'avaliacao': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'valor': {'type': 'integer'},
                            'descricao': {'type': 'string'},
                            'id_user': {'type': 'integer'}
                        }
                    }
                }
            }
        },
        400: {
            'description': 'Dados da avaliação ausentes'
        },
        404: {
            'description': 'Trilha não encontrada'
        },
        500: {
            'description': 'Erro interno do servidor ao criar a avaliação'
        }
    }
}

get_trilha_avaliacoes_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha para buscar as avaliações'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de avaliações da trilha',
            'schema': {
                'type': 'object',
                'properties': {
                    'avaliacoes': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'valor': {'type': 'integer'},
                                'descricao': {'type': 'string'},
                                'id_user': {'type': 'integer'}
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Trilha não encontrada'
        }
    }
}

delete_trilha_avaliacao_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha para a qual a avaliação pertence pela a url'
        },
        {
            'name': 'avaliacao_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da avaliação a ser deletada pela a url'
        }
    ],
    'responses': {
        200: {
            'description': 'Avaliação deletada com sucesso'
        },
        404: {
            'description': 'Trilha não encontrada ou Avaliação não encontrada nesta trilha'
        },
        500: {
            'description': 'Erro interno do servidor ao deletar a avaliação'
        }
    }
}


create_trilha_curso_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha à qual o curso será associado'
        },
        {
            'name': 'curso_id',
            'in': 'body',
            'type': 'integer',
            'required': True,
            'description': 'ID do curso a ser associado à trilha'
        }
    ],
    'responses': {
        201: {
            'description': 'Curso associado à trilha com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'curso': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'titulo': {'type': 'string'},
                            'descricao': {'type': 'string'}
                        }
                    }
                }
            }
        },
        400: {
            'description': 'ID do curso ausente'
        },
        404: {
            'description': 'Trilha não encontrada ou Curso não encontrado'
        },
        409: {
            'description': 'Curso já associado a esta Trilha'
        },
        500: {
            'description': 'Erro interno do servidor ao associar o curso à trilha'
        }
    }
}

get_trilha_cursos_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha para buscar os cursos associados'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de cursos associados à trilha',
            'schema': {
                'type': 'object',
                'properties': {
                    'cursos': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'titulo': {'type': 'string'},
                                'descricao': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Trilha não encontrada'
        }
    }
}

delete_trilha_curso_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha à qual o curso está associado'
        },
        {
            'name': 'curso_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do curso a ser removido da trilha'
        }
    ],
    'responses': {
        200: {
            'description': 'Curso removido da trilha com sucesso'
        },
        404: {
            'description': 'Trilha não encontrada ou Curso não encontrado nesta trilha'
        },
        500: {
            'description': 'Erro interno do servidor ao remover o curso da trilha'
        }
    }
}

create_trilha_aula_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha à qual a aula será associada'
        },
        {
            'name': 'aula_id',
            'in': 'body',
            'type': 'integer',
            'required': True,
            'description': 'ID da aula a ser associada à trilha'
        }
    ],
    'responses': {
        201: {
            'description': 'Aula associada à trilha com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'aula': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'titulo': {'type': 'string'},
                            'descricao': {'type': 'string'}
                        }
                    }
                }
            }
        },
        400: {
            'description': 'ID da aula ausente'
        },
        404: {
            'description': 'Trilha não encontrada ou Aula não encontrada'
        },
        409: {
            'description': 'Aula já associada a esta Trilha'
        },
        500: {
            'description': 'Erro interno do servidor ao associar a aula à trilha'
        }
    }
}

get_trilha_aulas_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha para buscar as aulas associadas'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de aulas associadas à trilha',
            'schema': {
                'type': 'object',
                'properties': {
                    'aulas': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'titulo': {'type': 'string'},
                                'descricao': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Trilha não encontrada'
        }
    }
}

delete_trilha_aula_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha à qual a aula está associada'
        },
        {
            'name': 'aula_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da aula a ser removida da trilha'
        }
    ],
    'responses': {
        200: {
            'description': 'Aula removida da trilha com sucesso'
        },
        404: {
            'description': 'Trilha não encontrada ou Aula não encontrada nesta trilha'
        },
        500: {
            'description': 'Erro interno do servidor ao remover a aula da trilha'
        }
    }
}

add_trilha_user_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha à qual o usuário será adicionado'
        }
    ],
    'responses': {
        201: {
            'description': 'Usuário adicionado à trilha com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'user': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'username': {'type': 'string'}
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Trilha não encontrada ou Usuário não encontrado'
        },
        409: {
            'description': 'Usuário já matriculado nesta Trilha'
        },
        500: {
            'description': 'Erro interno do servidor ao adicionar o usuário à trilha'
        }
    }
}

get_trilha_users_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha para buscar os usuários matriculados'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de usuários matriculados na trilha',
            'schema': {
                'type': 'object',
                'properties': {
                    'users': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'username': {'type': 'string'},
                                'email': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Trilha não encontrada'
        }
    }
}

remove_trilha_user_response = {
    'parameters': [
        {
            'name': 'trilha_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da trilha da qual o usuário será removido'
        },
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do usuário a ser removido da trilha'
        }
    ],
    'responses': {
        200: {
            'description': 'Usuário removido da trilha com sucesso'
        },
        404: {
            'description': 'Trilha não encontrada ou Usuário não encontrado nesta trilha'
        },
        500: {
            'description': 'Erro interno do servidor ao remover o usuário da trilha'
        }
    }
}


get_cursos_response = {
    'responses': {
        200: {
            'description': 'Lista de todos os cursos',
            'schema': {
                'type': 'object',
                'properties': {
                    'cursos': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'titulo': {'type': 'string'},
                                'descricao': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        }
    }
}

create_curso_response = {
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'titulo': {'type': 'string'},
                    'descricao': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Curso criado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'curso': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer'},
                            'titulo': {'type': 'string'},
                            'descricao': {'type': 'string'}
                        }
                    }
                }
            }
        },
        400: {
            'description': 'Dados ausentes'
        }
    }
}

get_curso_response = {
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do curso a ser recuperado'
        }
    ],
    'responses': {
        200: {
            'description': 'Detalhes do curso',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'titulo': {'type': 'string'},
                    'descricao': {'type': 'string'}
                }
            }
        },
        404: {
            'description': 'Curso não encontrado'
        }
    }
}

update_curso_response = {
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do curso a ser atualizado'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'titulo': {'type': 'string'},
                    'descricao': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Curso atualizado com sucesso'
        },
        400: {
            'description': 'Dados ausentes'
        },
        404: {
            'description': 'Curso não encontrado'
        }
    }
}

delete_curso_response = {
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do curso a ser excluído'
        }
    ],
    'responses': {
        200: {
            'description': 'Curso excluído com sucesso'
        },
        404: {
            'description': 'Curso não encontrado'
        }
    }
}

get_curso_comentarios_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'}
    ],
    'responses': {
        200: {'description': 'Lista de comentários do curso'},
        404: {'description': 'Curso não encontrado'}
    }
}

create_curso_comentario_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'}
    ],
    'responses': {
        201: {'description': 'Comentário criado com sucesso'},
        400: {'description': 'Dados ausentes'},
        404: {'description': 'Curso não encontrado'}
    }
}

delete_curso_comentario_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'},
        {'name': 'comentario_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do comentário'}
    ],
    'responses': {
        200: {'description': 'Comentário excluído com sucesso'},
        404: {'description': 'Curso ou comentário não encontrado'}
    }
}

get_curso_avaliacoes_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'}
    ],
    'responses': {
        200: {'description': 'Lista de avaliações do curso'},
        404: {'description': 'Curso não encontrado'}
    }
}

add_curso_avaliacao_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'}
    ],
    'responses': {
        201: {'description': 'Avaliação adicionada com sucesso'},
        400: {'description': 'Dados ausentes'},
        404: {'description': 'Curso não encontrado'}
    }
}

remove_curso_avaliacao_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'},
        {'name': 'avaliacao_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID da avaliação'}
    ],
    'responses': {
        200: {'description': 'Avaliação removida com sucesso'},
        404: {'description': 'Curso ou avaliação não encontrado'}
    }
}

get_curso_aulas_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'}
    ],
    'responses': {
        200: {'description': 'Lista de aulas do curso'},
        404: {'description': 'Curso não encontrado'}
    }
}

add_curso_aula_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'}
    ],
    'responses': {
        201: {'description': 'Aula adicionada com sucesso'},
        400: {'description': 'Dados ausentes'},
        404: {'description': 'Curso não encontrado'}
    }
}

remove_curso_aula_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'},
        {'name': 'aula_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID da aula'}
    ],
    'responses': {
        200: {'description': 'Aula removida com sucesso'},
        404: {'description': 'Curso ou aula não encontrado'}
    }
}

get_curso_trilhas_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'}
    ],
    'responses': {
        200: {'description': 'Lista de trilhas associadas ao curso'},
        404: {'description': 'Curso não encontrado'}
    }
}

create_curso_trilha_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'titulo': {'type': 'string', 'description': 'Título da trilha'},
                        'descricao': {'type': 'string', 'description': 'Descrição da trilha'}
                    },
                    'required': ['titulo']
                }
            }
        }
    },
    'responses': {
        201: {'description': 'Trilha criada com sucesso'},
        400: {'description': 'Dados inválidos'},
        404: {'description': 'Curso não encontrado'},
        500: {'description': 'Erro interno do servidor'}
    }
}

delete_curso_trilha_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'},
        {'name': 'trilha_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID da trilha'}
    ],
    'responses': {
        200: {'description': 'Trilha deletada com sucesso'},
        404: {'description': 'Curso ou trilha não encontrados'},
        500: {'description': 'Erro interno do servidor'}
    }
}

get_curso_users_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'}
    ],
    'responses': {
        200: {'description': 'Lista de usuários inscritos no curso'},
        404: {'description': 'Curso não encontrado'}
    }
}

add_logged_in_user_to_curso_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'}
    ],
    'responses': {
        201: {'description': 'Usuário adicionado ao curso com sucesso'},
        404: {'description': 'Curso ou usuário não encontrado'},
        409: {'description': 'Usuário já está inscrito neste curso'},
        500: {'description': 'Erro interno do servidor'}
    }
}

remove_user_from_curso_response = {
    'parameters': [
        {'name': 'curso_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do curso'},
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do usuário'}
    ],
    'responses': {
        200: {'description': 'Usuário removido do curso com sucesso'},
        404: {'description': 'Curso ou usuário não encontrado'},
        500: {'description': 'Erro interno do servidor'}
    }
}