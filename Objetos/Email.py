class Email():
    def init(self):
        self.nome = 'joao'
        self.email = 'joao@gmail.com'
    def pegar_servidor(self):
        return self.email[4:]
    
email = Email()
email.init()
print(email.nome)
print(email.email)
print(email.pegar_servidor())
