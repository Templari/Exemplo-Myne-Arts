from django.shortcuts import render
from MyneArts.models import Usuario, LoginUsuario, Endereco, Produto

logado = False

def index(request):
	return render(request, 'index.html', {})
	
def sobre(request):
	return render(request, 'sobre.html', {})
	
def cadastro(request):
	usuario  = Usuario()
	login    = LoginUsuario()
	endereco = Endereco()

	if(request.method == 'POST'):
		usuario.setNome(request.POST.get('tNome'))
		usuario.setCPF(request.POST.get('tCPF'))
		usuario.setFone(request.POST.get('tFone'))
		usuario.setEmail(request.POST.get('tMail'))
		usuario.save()

		login.setUsuario(request.POST.get('tUsuario'))
		login.setSenha(request.POST.get('tSenha'))
		login.setIdUsuario(usuario.id)
		login.save()

		endereco.setCidade(request.POST.get('tCidade'))
		endereco.setRua(request.POST.get('tRua'))
		endereco.setNumero(request.POST.get('tNumero'))
		endereco.setBairro(request.POST.get('tBairro'))
		endereco.setComplemento(request.POST.get('tComplemento'))
		endereco.setIdUsuario(usuario.id)
		endereco.save()
		
		return render(request, 'index.html', {})
	
	return render(request, 'cadastro.html', {})

def cadastro2(request):
	usuario  = Usuario()
	login    = LoginUsuario()
	endereco = Endereco()

	if(request.method == 'POST'):
		usuario.setNome(request.POST.get('tNome'))
		usuario.setCPF(request.POST.get('tCPF'))
		usuario.setFone(request.POST.get('tFone'))
		usuario.setEmail(request.POST.get('tMail'))
		usuario.save()

		login.setUsuario(request.POST.get('tUsuario'))
		login.setSenha(request.POST.get('tSenha'))
		login.setIdUsuario(usuario.id)
		login.save()

		endereco.setCidade(request.POST.get('tCidade'))
		endereco.setRua(request.POST.get('tRua'))
		endereco.setNumero(request.POST.get('tNumero'))
		endereco.setBairro(request.POST.get('tBairro'))
		endereco.setComplemento(request.POST.get('tComplemento'))
		endereco.setIdUsuario(usuario.id)
		endereco.save()
		
		return render(request, 'index.html', {})
	
	return render(request, 'cadastro2.html', {})

def login(request):
	if(request.method == 'POST'):
		users = LoginUsuario.objects.all()
		usuario = request.POST.get('usuario')
		senha   = request.POST.get('senha')

		for user in users:
			if(user.getUsuario() == usuario and user.getSenha() == senha):
				return render(request, 'index.html', {})

	return render(request, 'login.html', {})


def produto(request):
	produto = Produto()
	if(request.method == 'POST'):
		p = request.POST.get('nome')
		print(p)

	produto = Produto.objects.all()
	STATIC_URL = '/static/'
	return render(request, 'produto.html', {"produto" : produto})