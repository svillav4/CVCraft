import os, json
from openai import OpenAI
from dotenv import load_dotenv
from formulario.models import Profile

class recomendacionesIA():
    load_dotenv(".env")
    def __init__(self, request):
        self.profile = Profile.objects.filter(user=request.user).first()
        api_key = os.getenv("openai_apikey")
        self.client = OpenAI(api_key=api_key)

    def generateSubprofile(self, idx):
        promt = f"""
        Imagina que eres un consultor de empleo con la tarea de crear un currículum personalizado y llamativo basado en las ofertas actuales para la ocupación de '{self.profile.occupation_list[idx]}'. 
        
        Este currículum debe contener información personal del aspirante, como su nombre: '{self.profile.name}', su numero de telofono: {self.profile.PhoneNumber} e email: {self.profile.Email}, y debe resaltar las siguientes secciones clave:

        1. **Habilidades Técnicas**: Incluye las habilidades más relevantes que requiere la ocupación y destaca las proporcionadas por el usuario: {self.profile.tecnical_information}. 
        Además, sugiere las habilidades más demandadas actualmente en la industria para esta ocupación.
        2. **Habilidades Blandas**: Selecciona habilidades blandas que se ajusten mejor a la ocupación, algunas sugeridas son: {self.profile.soft_skills}.
        3. **Idiomas**: Los idiomas que domina el aspirante: {self.profile.languages}.
        4. **Hobbies**: Incluye los pasatiempos del usuario: {self.profile.hobbies}.
        5. **Experiencia Laboral**: Resalta la experiencia laboral del aspirante, si la tiene: {self.profile.work_experience}.
        6. **Educación**: Incluye títulos y certificaciones relevantes: {self.profile.education}.
        7. **Referencias**: Menciona las referencias proporcionadas: {self.profile.references}.

        Asegurate que la respuesta la des en un formato json de la siguiente forma:
        'curriculum': - 'informacion_personal': 'nombre': '', 'telefono': '', 'email': '', 
                      - 'secciones' -'habilidades_tecnicas': [], 
                                    -'habilidades_blandas': [],
                                    -'idiomas': ['idioma(nivel)', ...],
                                    -'hobbies': [], 
                                    -'experiencia_laboral': ['empresa': '', 'cargo': '', 'duracion': '', ...],
                                    -'educacion': ['titulo': '', 'institucion': '', 'ano': ,...],
                                    -'referencias': ['nombre': '', 'relacion': '', 'contacto': , ...]
        """

        msg = [
            {"role": "user", "content": promt}
        ]
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=msg,
            response_format={"type": "json_object"},
            max_tokens=2000
        )
        return json.loads(response.choices[0].message.content) # Returns JSON formmated response.