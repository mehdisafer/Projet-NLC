import openai
import config as config # with api key

def ai(request):
    """
    Cette fonction invoque ChatGPT et lui envoit une question en tant que programmer.
    avec :
        - request : comme question posée

    et retourne une string contenant la reponse
    --------------------------------------------------------------------------------
    TODO: rajouter la spécificité du langage dans le "system"
    """
    # initialisation de la clé
    openai.api_key = config.OPENAI_API_KEY

    # appel
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a programmer, and you can only write source code without any description."},
            {"role": "user", "content": request}]
    )

    # retour
    return completion.choices[0].message.content
