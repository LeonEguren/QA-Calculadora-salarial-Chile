from typing import Literal
from playwright.sync_api import Page
import pyodbc
import pytest
from playwright.sync_api import expect
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv

from database import eliminar_registro_CL

from playwright.sync_api import sync_playwright
import datetime
import allure
# Cargar las variables de entorno desde el archivo .env
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright
import random
screenshot_dir = r"C:\Users\leguren\Desktop\Automatizacion\Calculadora salarial Chile\Utilities\Evidencia"

load_dotenv()
Url_Calculadora_test_Cl = os.getenv("Url_Calculadora_test_Cl")
correo_empresa_nueva_CL = os.getenv("correo_empresa_nueva_CL")
nombre_empresa_nueva = os.getenv("nombre_empresa_nueva")
buzon_correo=os.getenv("buzon_correo")
especialidad_CL = os.getenv("especialidad_CL")
posicion_CL = os.getenv("posicion_CL")
localidad_RM_CL = os.getenv("localidad_RM_CL")
experiencia_CL = os.getenv("experiencia_CL")
salario_a_ingresar = os.getenv("salario_a_ingresar")
localidad_ZonaSur_CL = os.getenv("localidad_ZonaSur_CL")
nombre_empresa_registrada=os.getenv("nombre_empresa_registrada")
correo_empresa_registrada_CL=os.getenv("correo_empresa_registrada_CL")
url_professional_CL=os.getenv("url_professional_CL")
url_digital_CL=os.getenv("url_digital_CL")
url_enterprise_CL=os.getenv("url_enterprise_CL")
url_operational_CL=os.getenv("url_operational_CL")

def test_empresa_no_registrada_CL(playwright: Playwright):
    
   
    eliminar_registro_CL(correo_empresa_nueva_CL)
    # browser = playwright.chromium.launch(headless=True)
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Url_Calculadora_test_Cl)
    page.get_by_role("button", name="soy empresa").click()
    page.get_by_placeholder("ingresa tu nombre").click()
    page.get_by_placeholder("ingresa tu nombre").fill(nombre_empresa_nueva)
    page.get_by_placeholder("ingresa tu email").click()
    page.get_by_placeholder("ingresa tu email").fill(correo_empresa_nueva_CL)
    page.get_by_text("He leído y acepto las").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="continuar").click()
    page.get_by_text("reenviar email.").click()
    page.goto(buzon_correo)
    page.get_by_placeholder("Ingrese una dirección aquí").click()
    page.get_by_placeholder("Ingrese una dirección aquí").fill(correo_empresa_nueva_CL)
    page.get_by_placeholder("Ingrese una dirección aquí").press("Enter")
    with page.expect_popup() as page2_info:
        page.frame_locator("iframe[name=\"ifmail\"]").get_by_role("link", name="confirmar correo electrónico").click()
    page = page2_info.value
    page.locator("#selSubEspecialidad").select_option(especialidad_CL )
    page.locator("#selPosicion").select_option(posicion_CL)
    expect(page.locator("label:has-text('industria')")).to_have_count(0) 
    page.get_by_role("button", name="continuar").click()
    page.select_option('select[id="selLocalidad"]', label=localidad_RM_CL)
    page.select_option('select[id="selExperiencia"]', value=experiencia_CL)
    page.get_by_role("button", name="continuar").click()
    page.get_by_placeholder("ingresa tu salario").click()
    page.get_by_placeholder("ingresa tu salario").fill(salario_a_ingresar)
    page.get_by_role("button", name="calcular").click()
    page.get_by_role("tab", name="otras zonas").locator("div").nth(1).click()
    page.locator("#selOtraLocalidad").select_option(localidad_ZonaSur_CL)
    with page.expect_popup() as page1_info:
        page.get_by_label("1comparador").locator("div").filter(has_text="¿ya viste nuestro último").nth(1).click()
    page1 = page1_info.value
    page.locator("#cdk-step-label-0-2").get_by_text("nuestras soluciones").click()
    screenshot_path = os.path.join(screenshot_dir, "screenshot_nuestras_soluciones.png")
    page.screenshot(path=screenshot_path)
    with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name="screenshot_nuestras_soluciones", attachment_type=allure.attachment_type.PNG)
    with page.expect_popup() as page2_info:
        page.get_by_text("descubre más").first.click()
    page2 = page2_info.value
    screenshot_path = os.path.join(screenshot_dir, "screenshot_nuestras_soluciones01.png")
    page.screenshot(path=screenshot_path)
    with page.expect_popup() as page3_info:
        page.get_by_text("descubre más").nth(1).click()
    page3 = page3_info.value
    screenshot_path = os.path.join(screenshot_dir, "screenshot_nuestras_soluciones02.png")
    page.screenshot(path=screenshot_path)
    with page.expect_popup() as page4_info:
        page.get_by_text("descubre más").nth(2).click()
    page4 = page4_info.value
    with page.expect_popup() as page5_info:
        page.get_by_text("descubre más").nth(3).click()
    page5 = page5_info.value

    # ---------------------
    context.close()

    browser.close()



def test_empresa_registrada_CL(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Url_Calculadora_test_Cl)
    page.get_by_role("button", name="soy empresa").click()
    page.get_by_placeholder("ingresa tu nombre").click()
    page.get_by_placeholder("ingresa tu nombre").fill(nombre_empresa_registrada)
    page.get_by_placeholder("ingresa tu email").click()
    page.get_by_placeholder("ingresa tu email").fill(correo_empresa_registrada_CL)
    page.get_by_text("He leído y acepto las").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="continuar").click()
    page.locator("#selSubEspecialidad").select_option(especialidad_CL)
    page.locator("#selPosicion").select_option(posicion_CL)
    expect(page.locator("label:has-text('industria')")).to_have_count(0) 
    page.get_by_role("button", name="continuar").click()
    page.select_option('select[id="selLocalidad"]', label=localidad_RM_CL)
    page.select_option('select[id="selExperiencia"]', value=experiencia_CL)
    page.get_by_role("button", name="continuar").click()
    page.get_by_placeholder("ingresa tu salario").click()
    page.get_by_placeholder("ingresa tu salario").fill(salario_a_ingresar)
    page.get_by_role("button", name="calcular").click()
    page.get_by_role("tab", name="otras zonas").locator("div").nth(1).click()
    page.locator("#selOtraLocalidad").select_option("Zona sur")
    with page.expect_popup() as page1_info:
        page.get_by_label("1comparador").locator("div").filter(has_text="¿ya viste nuestro último").nth(1).click()
    page1 = page1_info.value
    page.locator("#cdk-step-label-0-2").get_by_text("nuestras soluciones").click()
    screenshot_path = os.path.join(screenshot_dir, "screenshot_nuestras_soluciones03.png")
    page.screenshot(path=screenshot_path)
    with page.expect_popup() as page2_info:
        page.get_by_text("descubre más").first.click()
    page2 = page2_info.value
    with page.expect_popup() as page3_info:
        page.get_by_text("descubre más").nth(1).click()
    page3 = page3_info.value
    with page.expect_popup() as page4_info:
        page.get_by_text("descubre más").nth(2).click()
    page4 = page4_info.value
    with page.expect_popup() as page5_info:
        page.get_by_text("descubre más").nth(3).click()
    page5 = page5_info.value

    # ---------------------
    context.close()

    browser.close()
def test_validar_servicios_CL(playwright: Playwright):
    # browser = playwright.chromium.launch(headless=True)
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Url_Calculadora_test_Cl)
    page.get_by_role("button", name="soy empresa").click()
    page.get_by_placeholder("ingresa tu nombre").click()
    page.get_by_placeholder("ingresa tu nombre").fill(nombre_empresa_registrada)
    page.get_by_placeholder("ingresa tu email").click()
    page.get_by_placeholder("ingresa tu email").fill(correo_empresa_registrada_CL)
    page.get_by_text("He leído y acepto las").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="continuar").click()
    page.locator("#selSubEspecialidad").select_option(especialidad_CL)
    page.locator("#selPosicion").select_option(posicion_CL)
    expect(page.locator("label:has-text('industria')")).to_have_count(0) 
    page.get_by_role("button", name="continuar").click()
    page.select_option('select[id="selLocalidad"]', label=localidad_RM_CL)
    page.select_option('select[id="selExperiencia"]', value=experiencia_CL)
    page.get_by_role("button", name="continuar").click()
    page.get_by_placeholder("ingresa tu salario").click()
    page.get_by_placeholder("ingresa tu salario").fill(salario_a_ingresar)
    page.get_by_role("button", name="calcular").click()
    page.locator("#cdk-step-label-0-2").get_by_text("nuestras soluciones").click()

    # Abrir múltiples pestañas y regresar a la pestaña original después de cada una
    with page.expect_popup() as page1_info:
        page.get_by_text("descubre más").first.click()  # Clic en "operational talent solutions"
    page1 = page1_info.value
    expect(page1).to_have_url(url_operational_CL)
    screenshot_path = os.path.join(screenshot_dir, "screenshot_operational.png")
    page.screenshot(path=screenshot_path)

    page1.bring_to_front()  # Regresar a la pestaña original
    page1.close()  # Cerrar la pestaña después de revisarla (opcional)

    with page.expect_popup() as page2_info:
        page.get_by_text("descubre más").nth(1).click()  # Clic en "professional talent solutions"
    page2 = page2_info.value
    expect(page2).to_have_url(url_professional_CL)
    screenshot_path = os.path.join(screenshot_dir, "screenshot_professional.png")
    page.screenshot(path=screenshot_path)
    page2.bring_to_front()  # Regresar a la pestaña original
    page2.close()  # Cerrar la pestaña después de revisarla (opcional)

    with page.expect_popup() as page3_info:
        page.get_by_text("descubre más").nth(2).click()  # Clic en "digital talent solutions"
    page3 = page3_info.value
    expect(page3).to_have_url(url_digital_CL)
    screenshot_path = os.path.join(screenshot_dir, "screenshot_digital.png")
    page.screenshot(path=screenshot_path)
    page3.bring_to_front()  # Regresar a la pestaña original
    page3.close()  # Cerrar la pestaña después de revisarla (opcional)

    with page.expect_popup() as page4_info:
        page.get_by_text("descubre más").nth(3).click()  # Clic en "enterprise solutions"
    page4 = page4_info.value
    expect(page4).to_have_url(url_enterprise_CL)
    screenshot_path = os.path.join(screenshot_dir, "screenshot_enterprise.png")
    page.screenshot(path=screenshot_path)
    page4.bring_to_front()  # Regresar a la pestaña original
    page4.close()  # Cerrar la pestaña después de revisarla (opcional)Cerrar la pestaña después de revisarla (opcional)
    browser.close()
   