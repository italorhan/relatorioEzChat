class CategoriaInfo:
    def __init__(self, categoria, total_chats, user_messages, agent_messages, oficial):
        self.categoria = categoria
        self.total_chats = total_chats
        self.user_messages = user_messages
        self.agent_messages = agent_messages
        self.total_mensagens = user_messages + agent_messages
        self.oficial = oficial

    def __str__(self):
        tipo = "Oficial" if self.oficial else "Não Oficial"
        return (f"[{tipo}] Categoria: {self.categoria}, "
                f"Chats: {self.total_chats}, "
                f"Mensagens (Usuário): {self.user_messages}, "
                f"Mensagens (Agente): {self.agent_messages}, "
                f"Mensagens (Total): {self.total_mensagens}")