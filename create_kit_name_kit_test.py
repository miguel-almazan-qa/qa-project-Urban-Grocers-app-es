#Este archivo contiene la lógica de automatización y las 9 pruebas de la lista de comprobación
import sender_stand_request
import data

# Genera una copia del kit\_body original modificando el campo 'name'
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Prueba positiva: Espera código de estado 201 y coincidencia del nombre
def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Prueba negativa: Espera código de estado 400
def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# Prueba 1: El número permitido de caracteres (1) - Código de respuesta: 201
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

# Prueba 2: El número permitido de caracteres (511) - Código de respuesta: 201
def test_create_kit_511_letter_in_name_get_success_response():
    name_511 = (
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    )
    kit_body = get_kit_body(name_511)
    positive_assert(kit_body)

# Prueba 3: El número de caracteres es menor que la cantidad permitida (0) - Código de respuesta: 400
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# Prueba 4: El número de caracteres es mayor que la cantidad permitida (512) - Código de respuesta: 400
def test_create_kit_512_letter_in_name_get_error_response():
    name_512 = (
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    )
    kit_body = get_kit_body(name_512)
    negative_assert_code_400(kit_body)

# Prueba 5: Se permiten caracteres especiales - Código de respuesta: 201
def test_create_kit_has_special_symbol_in_name_get_success_response():
    kit_body = get_kit_body('"№%@",')
    positive_assert(kit_body)

# Prueba 6: Se permiten espacios - Código de respuesta: 201
def test_create_kit_has_spaces_in_name_get_success_response():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

# Prueba 7: Se permiten números (como string) - Código de respuesta: 201
def test_create_kit_has_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

# Prueba 8: El parámetro no se pasa en la solicitud - Código de respuesta: 400
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

# Prueba 9: Se ha pasado un tipo de parámetro diferente (número en vez de string) - Código de respuesta: 400
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)




