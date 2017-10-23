from django.db import models

#model Usuario
class Usuario(models.Model):
	nome  = models.CharField(max_length=255, null=False)
	cpf   = models.CharField(max_length=11,  null=False)
	fone  = models.CharField(max_length=11,  null=False)
	email = models.CharField(max_length=255, null=False)

	def setNome(self, nome=''):
		self.nome = nome

	def setCPF(self, cpf=''):
		self.cpf = cpf

	def setFone(self, fone=''):
		self.fone = fone

	def setEmail(self, email=''):
		self.email = email

#model Administrador
class Administrador(models.Model):
	nome  = models.CharField(max_length=255, null=False)
	cpf   = models.CharField(max_length=11,  null=False)
	fone  = models.CharField(max_length=11,  null=False)
	email = models.CharField(max_length=255, null=False)

#model LoginUsuario
class LoginUsuario(models.Model):
	usuario    = models.CharField(max_length=45, null=False)
	senha      = models.CharField(max_length=16, null=False)
	id_usuario = models.IntegerField(null = False)

	def setUsuario(self, usuario=''):
		self.usuario = usuario

	def getUsuario(self):
		return self.usuario

	def setSenha(self, senha=''):
		self.senha = senha

	def getSenha(self):
		return self.senha

	def setIdUsuario(self, id_usuario=''):
		self.id_usuario = id_usuario


class Produto (models.Model):
	imagem = models.FileField(null=True,blank=True)
	nome = models.CharField(max_length=255, null=False)
	preco = models.FloatField()
	descricao = models.CharField(max_length=255,null=False)
	quantidade = models.IntegerField()

class Encomenda(models.Model):
	iduser = models.IntegerField(null=False)
	descricao = models.CharField(max_length=300, null=False)
	quantidade = models.IntegerField(null=False)
	estado = models.CharField(max_length=20,null=False)

class Venda(models.Model):
	idprod = models.IntegerField(null=False)
	iduser = models.IntegerField(null=False)

class Endereco(models.Model):
	cidade = models.CharField(max_length=100, null=False)
	rua = models.CharField(max_length=100, null=False)
	numero = models.IntegerField(null=False)
	bairro = models.CharField(max_length=100, null=False)
	complemento = models.CharField(max_length=100, null=False)
	id_usuario = models.IntegerField(null = False)

	def setCidade(self, cidade=''):
		self.cidade = cidade

	def setRua(self, rua=''):
		self.rua = rua

	def setNumero(self, numero=''):
		self.numero = numero

	def setBairro(self, bairro=''):
		self.bairro = bairro

	def setComplemento(self, complemento=''):
		self.complemento = complemento

	def setIdUsuario(self, id_usuario=''):
		self.id_usuario = id_usuario

class Comentario(models.Model):
	iduser = models.IntegerField(null=False)
	texto = models.CharField(max_length=300,null=False)

class Usuario_has_Endereco(models.Model):
	iduser = models.IntegerField(null=False)
	idend = models.IntegerField(null=False)

class login_Administrador(models.Model):
	idAdm = models.IntegerField(null=False)
	user = models.CharField(max_length=45,null=False)
	senha = models.CharField(max_length=45,null=False)

class Administrador_has_Endereco(models.Model):
	idAdm = models.IntegerField(null=False)
	idEnd = models.IntegerField(null=False)	