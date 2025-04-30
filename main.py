from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuración del navegador
driver = webdriver.Chrome()

try:
    # 1. Acceder a MercadoLibre
    driver.get("https://www.mercadolibre.com")
    time.sleep(2)

    # 2. Seleccionar México
    mexico_link = driver.find_element(By.CSS_SELECTOR, "a[href*='mercadolibre.com.mx']")
    mexico_link.click()
    time.sleep(2)

    # 3. Buscar "playstation 5"
    search_box = driver.find_element(By.NAME, "as_word")
    search_box.send_keys("playstation 5")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # 4. Filtrar por condición "Nuevo"
    nuevo_filter = driver.find_element(By.XPATH, "//span[text()='Nuevo']")
    nuevo_filter.click()
    time.sleep(2)

    # 5. Filtrar por ubicación "Estado de México"
    ubicacion_filter = driver.find_element(By.XPATH, "//span[text()='Estado De México']")
    ubicacion_filter.click()
    time.sleep(2)

    # 6. Ordenar por "Menor precio"
    ordenar_dropdown = driver.find_element(By.CLASS_NAME, "andes-dropdown__trigger")
    ordenar_dropdown.click()
    time.sleep(1)
    menor_precio_option = driver.find_element(By.XPATH, "//div[@class='andes-list__item']//span[text()='Menor precio']")
    menor_precio_option.click()
    time.sleep(2)

    # 7. Obtener nombre y precio de los primeros 5 productos
    productos = driver.find_elements(By.XPATH, "//li[@class='ui-search-layout__item']")[:5]
    for producto in productos:
        nombre = producto.find_element(By.XPATH, ".//h2").text
        precio = producto.find_element(By.XPATH, ".//span[@class='andes-money-amount__fraction']").text
        print(f"Producto: {nombre} - Precio: ${precio}")

finally:
    driver.quit()
