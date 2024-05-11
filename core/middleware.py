from django.utils.translation import activate

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obter o idioma preferido do navegador do usuário
        language = request.headers.get('Accept-Language', 'en')

        # Mapear idiomas suportados para os códigos correspondentes
        supported_languages = {
            'en': 'en',  # Inglês
            'pt': 'pt',  # Português            
        }

        # Ativar o idioma correspondente se estiver entre os idiomas suportados
        if language.split('-')[0] in supported_languages:
            activate(supported_languages[language.split('-')[0]])
        else:
            # Caso contrário, ativar o inglês como idioma padrão
            activate('en')

        response = self.get_response(request)
        return response
