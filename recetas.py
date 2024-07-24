import re
import requests
import pdfkit
from urllib.parse import urlparse

# Función para extraer enlaces https, excluyendo Facebook y YouTube
def extract_links(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    links = re.findall(r'https://\S+', content)
    filtros = ["facebook", "fb.watch", "youtube", "youtu.be", "photos.app", "conlagente"]
    filtered_links = [link for link in links if not any(domain in link for domain in filtros)]
    return filtered_links

# Función para realizar scraping y guardar contenido en PDF
def save_page_as_pdf(url, pdf_filename):
    try:
        # Usar pdfkit para convertir HTML a PDF
        pdfkit.from_url(url, "recetas/" + pdf_filename)
    except Exception as e:
        print(f"Error al procesar {url}: {e}")

# Extraemos los enlaces del archivo de texto
filename = 'chats/Chat de WhatsApp con Claudia G.txt'
links = extract_links(filename)
links[17] = " "
print(f"La cantidad de links son:", len(links))

# Guardamos cada página como PDF
for i, link in enumerate(links):
    print("Procesando: ", link)
    domain = urlparse(link).netloc
    pdf_filename = f'recipe_{i}_{domain}.pdf'
    save_page_as_pdf(link, pdf_filename)
    print("Guardado como: ", pdf_filename)
