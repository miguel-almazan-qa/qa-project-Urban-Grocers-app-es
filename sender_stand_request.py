import configuration
import requests
import data

# Función para crear un nuevo usuario
def post_new_user(body):
    return requests.post(
    configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
    json=body,
    headers=data.headers
)

# Función para obtener el authToken del usuario creado
def get_new_user_token():
    user_response = post_new_user(data.user_body)
    return user_response.json()["authToken"]

# Función para crear un kit vinculado al usuario mediante Authorization Bearer
def post_new_client_kit(kit_body, auth_token):
    # Copiar encabezados e incluir el token de autorización
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )

