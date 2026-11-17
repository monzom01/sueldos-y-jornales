import os
from google import genai

# Inicializar el cliente de Gemini usando la variable de entorno configurada
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def procesar_calculo_salarial(prompt_contexto):
    """
    Envía los datos de jornales o novedades a Gemini para su análisis y cálculo.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt_contexto,
        )
        return response.text
    except Exception as e:
        return f"Error en el procesamiento con AI Studio: {e}"

if __name__ == "__main__":
    print("--- Motor de Sueldos y Jornales (AI Studio conectado) ---")
    # Ejemplo de prueba rápida
    prueba = "Simula el cálculo de un jornal con 18 presentismo y 2 horas al 50%."
    resultado = procesar_calculo_salarial(prueba)
    print(resultado)