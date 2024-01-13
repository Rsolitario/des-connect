# Des-Connect
Des-Connect es un chatbot desarrollado en Python que utiliza la biblioteca Spacy para calcular la similitud entre textos y proporcionar respuestas basadas en aproximidad. El chatbot está diseñado con una interfaz personalizada utilizando Flask, HTML y AJAX.

## Requisitos
Python (versión 3.11.7)
Las siguientes bibliotecas de Python deben estar instaladas:
- re
- spacy
- flask
- es_core_news_lg

## Instalación
Clona este repositorio:
Copiar
git clone https://github.com/Rsolitario/des-connect.git
Navega al directorio del proyecto:
Copiar
cd des-connect
Instala las dependencias requeridas:

```python
pip install -r requirements.txt
python -m spacy download es_core_news_lg
```

## Uso
Ejecuta la aplicación Flask:
Copiar
python main.py
Abre tu navegador web y visita http://localhost:5000.

Interactúa con el chatbot y prueba diferentes conversaciones.

Personalización
Puedes personalizar las respuestas del chatbot modificando la conversación preestablecida en el archivo formateador.py. Añade o elimina preguntas y respuestas según tus necesidades.

Ejemplos
Enlace al video de demostración
<video src="concepto.mp4" controls></video>

¡Disfruta usando Des-Connect y experimenta con diferentes conversaciones!


