from typing import Literal
from playwright.sync_api import Page
import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv

from playwright.sync_api import Playwright, sync_playwright, expect
from database import obtener_rango_minimo_CL, eliminar_registro_CL, obtener_fecha_CL

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
# Definir las variables desde el archivo .env
Url_Calculadora_test_Cl = os.getenv("Url_Calculadora_test_Cl")
nombre_candidato_nuevo = os.getenv("nombre_candidato_nuevo")
nombre_candidato_registrado = os.getenv("nombre_candidato_registrado")
correo_candidato_nuevo_CL = os.getenv("correo_candidato_nuevo_CL")
correo_candidato_registrado_CL = os.getenv("correo_candidato_registrado_CL")
especialidad_CL = os.getenv("especialidad_CL")
posicion_CL = os.getenv("posicion_CL")
localidad_RM_CL = os.getenv("localidad_RM_CL")
localidad_ZonaSur_CL = os.getenv("localidad_ZonaSur_CL")
experiencia_CL = os.getenv("experiencia_CL")
buzon_correo = os.getenv("buzon_correo")
salario_a_ingresar = os.getenv("salario_a_ingresar")

# def variables_globales(playwright: Playwright):
      
#     global Url_Calculadora_test_Cl, nombre_candidato_nuevo,correo_candidato_nuevo_CL,especialidad_CL,posicion_CL,localidad_RM_CL,experiencia_CL,localidad_ZonaSur_CL,buzon_correo,salario_a_ingresar,nombre_candidato_registrado,correo_candidato_registrado_CL
def test_candidato_no_registrado_CL(playwright: Playwright):
    eliminar_registro_CL(correo_candidato_nuevo_CL)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Url_Calculadora_test_Cl)
    page.get_by_role("button", name="soy candidato").click()
    page.get_by_placeholder("ingresa tu nombre").click()
    page.get_by_placeholder("ingresa tu nombre").fill(nombre_candidato_nuevo)
    page.get_by_placeholder("ingresa tu email").click()
    page.get_by_placeholder("ingresa tu email").fill(correo_candidato_nuevo_CL)
    page.get_by_text("He leído y acepto las").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="continuar").click()
    page.get_by_text("reenviar email.").click()
    page.goto(buzon_correo)
    page.get_by_placeholder("Ingrese una dirección aquí").click()
    page.get_by_placeholder("Ingrese una dirección aquí").fill(correo_candidato_nuevo_CL)
    page.get_by_placeholder("Ingrese una dirección aquí").press("Enter")
    with page.expect_popup() as page2_info:
        page.frame_locator("iframe[name=\"ifmail\"]").get_by_role("link", name="confirmar correo electrónico").click()
    page = page2_info.value
    page.locator("#selSubEspecialidad").select_option(especialidad_CL)
    page.locator("#selPosicion").select_option(posicion_CL)
    page.get_by_role("button", name="continuar").click()
    page.select_option('select[id="selLocalidad"]', label=localidad_RM_CL)
    page.select_option('select[id="selExperiencia"]', value=experiencia_CL)
    page.get_by_role("button", name="continuar").click()
    page.get_by_placeholder("ingresa tu salario").click()
    page.get_by_placeholder("ingresa tu salario").fill(salario_a_ingresar)
    page.get_by_role("button", name="calcular").click()
    page.get_by_role("tab", name="otras zonas").locator("div").nth(1).click()
    page.locator("#selOtraLocalidad").select_option(localidad_ZonaSur_CL)
    page.get_by_role("tab", name="trabajos para ti").click()
    expect(page.locator('div.ol-banner-title')).to_have_text("¡Encuentra el trabajo que buscas!")

    browser.close()
def test_candidato_registrado_CL(playwright: Playwright):
 

    # browser = playwright.chromium.launch(headless=True)
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Url_Calculadora_test_Cl)
    page.get_by_role("button", name="soy candidato").click()
    page.get_by_placeholder("ingresa tu nombre").click()
    page.get_by_placeholder("ingresa tu nombre").fill(nombre_candidato_registrado)
    page.get_by_placeholder("ingresa tu email").click()
    page.get_by_placeholder("ingresa tu email").fill(correo_candidato_registrado_CL)
    page.get_by_text("He leído y acepto las").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="continuar").click()
    page.locator("#selSubEspecialidad").select_option(especialidad_CL)
    page.locator("#selPosicion").select_option(posicion_CL)
    page.get_by_role("button", name="continuar").click()
    page.select_option('select[id="selLocalidad"]', label=localidad_RM_CL)
    page.select_option('select[id="selExperiencia"]', value=experiencia_CL)
    page.get_by_role("button", name="continuar").click()
    page.get_by_placeholder("ingresa tu salario").click()
    page.get_by_placeholder("ingresa tu salario").fill(salario_a_ingresar)
    page.get_by_role("button", name="calcular").click()
    page.get_by_role("tab", name="otras zonas").locator("div").nth(1).click()
    page.locator("#selOtraLocalidad").select_option(localidad_ZonaSur_CL)
    page.get_by_role("tab", name="trabajos para ti").click()
    expect(page.locator('div.ol-banner-title')).to_have_text("¡Encuentra el trabajo que buscas!")

    browser.close()

def test_valido_sueldo_CL(playwright: Playwright):
    global experiencia_CL

    # mail = mail[0]

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page = context.new_page()
    page.goto(Url_Calculadora_test_Cl)
    page.get_by_role("button", name="soy candidato").click()
    page.get_by_placeholder("ingresa tu nombre").click()
    page.get_by_placeholder("ingresa tu nombre").fill(nombre_candidato_registrado)
    page.get_by_placeholder("ingresa tu nombre").press("Tab")
    page.get_by_placeholder("ingresa tu email").fill(correo_candidato_registrado_CL)
    page.get_by_text("He leído y acepto las").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="continuar").click()
    page.locator("#selSubEspecialidad").click()
    page.locator("#selSubEspecialidad").select_option(especialidad_CL)
    page.locator("#selPosicion").click()
    page.locator("#selPosicion").select_option(posicion_CL)
    page.get_by_role("button", name="continuar").click()

    page.select_option('select[id="selLocalidad"]', label=localidad_RM_CL)
    page.select_option('select[id="selExperiencia"]', value=experiencia_CL)
    page.get_by_role("button", name="continuar").click()
    page.get_by_placeholder("ingresa tu salario").click()
    page.get_by_placeholder("ingresa tu salario").fill(salario_a_ingresar)
    page.get_by_role("button", name="calcular").click()
    page.wait_for_selector('xpath=//*[@id="rb1"]/span[2]')
    page.wait_for_timeout(5000) 
    # Paso 2: Capturar el valor del sueldo desde el HTML
    valor_sueldo_text = page.locator('xpath=//*[@id="rb1"]/span[2]').inner_text()

    # Limpiar el texto obtenido para extraer el valor numérico
    valor_sueldo_text = valor_sueldo_text.replace('$', '').replace('.', '').replace(',', '').strip()
    valor_sueldo = float(valor_sueldo_text)
    valor_sueldo = valor_sueldo / 100

 
    # Paso 3: Obtener el rango mínimo desde la base de datos
    rango_minimo = obtener_rango_minimo_CL()
   


    # Paso 4: Comparar el valor del HTML con el valor de la base de datos
    if rango_minimo is not None:
        print("Valor del sueldo en la página: {}".format(valor_sueldo))
        print("Rango mínimo obtenido de la base de datos: {}".format(rango_minimo))
        # Comparar los valores y hacer una aserción
        assert valor_sueldo == rango_minimo, f"El valor del sueldo en la página ({valor_sueldo}) es menor que el rango mínimo ({rango_minimo})"
    else:
        pytest.fail("No se pudo obtener el rango mínimo de la base de datos.")


def test_valido_fecha_salario(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(Url_Calculadora_test_Cl)
    page.get_by_role("button", name="soy candidato").click()
    page.get_by_placeholder("ingresa tu nombre").fill(nombre_candidato_nuevo)
    page.get_by_placeholder("ingresa tu email").fill(correo_candidato_registrado_CL)
    page.get_by_text("He leído y acepto las").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="continuar").click()

    # Seleccionar especialidad y posición
    page.locator("#selSubEspecialidad").select_option(especialidad_CL)
    page.locator("#selPosicion").select_option(posicion_CL)
    page.get_by_role("button", name="continuar").click()
    page.select_option('select[id="selLocalidad"]', label=localidad_RM_CL)
    page.select_option('select[id="selExperiencia"]', value=experiencia_CL)
    page.get_by_role("button", name="continuar").click()

    # Llenar el salario y calcular
    page.get_by_placeholder("ingresa tu salario").fill(salario_a_ingresar)
    page.get_by_role("button", name="calcular").click()

    # Obtener el año desde el elemento <a>
    elemento_a = page.locator("a").get_by_text("2024")
    expect(elemento_a).to_be_visible()  # Asegúrate de que el elemento es visible
    anio_front = elemento_a.inner_text()  # Obtener el texto del elemento

    # Obtener el año desde la base de datos y extraer solo el año
    anio_db = obtener_fecha_CL()
    if anio_db is not None:
        anio_db_str = str(anio_db)[:4]  # Extraer solo el año como una cadena
    else:
        print("Error al obtener el año desde la base de datos.")
        browser.close()
        return

    # Imprimir para depuración
    print(f"Año en front: {anio_front}")
    print(f"Año desde la base de datos: {anio_db_str}")

    # Comparar si el año de la base de datos está contenido en el año del front-end
    assert anio_db_str in anio_front, f"Año {anio_db_str} no encontrado en el front: {anio_front}"

    # Cerrar el navegador
    browser.close()