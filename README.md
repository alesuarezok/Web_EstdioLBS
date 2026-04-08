# Plantilla de Página Web para LBC y Asociados

Esta es una plantilla básica de página web para el estudio jurídico LBC y Asociados, construida con Flask (Python). Incluye secciones como inicio, nosotros, cómo trabajamos, servicios, equipo y contacto.

## Estructura del Proyecto

- `app.py`: Aplicación Flask principal
- `templates/index.html`: Plantilla HTML principal
- `static/css/style.css`: Estilos CSS
- `static/images/`: Carpeta para imágenes (logo, fotos de abogados, fondo, etc.)

## Cómo Usar

1. Clona o descarga este proyecto.
2. Asegúrate de tener Python instalado.
3. Instala las dependencias: `pip install -r requirements.txt`
4. Personaliza el contenido en `templates/index.html` con la información de tu estudio jurídico.
5. Reemplaza las imágenes en la carpeta `static/images/` con tus propias imágenes.
6. Modifica los estilos en `static/css/style.css` según tus preferencias.
7. Ejecuta la aplicación: `python app.py`
8. Abre http://localhost:5000 en tu navegador.

## Personalización

- **Contenido**: Edita el texto en `templates/index.html` para reflejar la información de tu estudio.
- **Estilos**: Modifica `static/css/style.css` para cambiar colores, fuentes, etc.
- **Funcionalidades**: Agrega más rutas y lógica en `app.py` si necesitas funcionalidades adicionales.
- **Imágenes**: Asegúrate de que las imágenes tengan los nombres correctos o actualiza las rutas en la plantilla.

## Servidor Local

Para ejecutar la aplicación:

```bash
python app.py
```

La aplicación se ejecutará en http://localhost:5000 por defecto.

## Notas

- La plantilla es responsive y se adapta a dispositivos móviles.
- Incluye navegación suave con CSS y un formulario de contacto manejado por Flask.
- Personaliza los colores y fuentes para que coincidan con la identidad de tu marca.
- El formulario de contacto actualmente muestra un mensaje flash; puedes extenderlo para enviar emails.

## Licencia

Esta plantilla es de uso libre. Modifícala según tus necesidades.