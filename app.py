# app.py
from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    prompt = f"""
    Yo soy un ingeniero en tecnologías computacionales que comenzo su carrera desde los 16 años,
    mi primer trabajo fue a los 19 años en un negocio local que se llamaba "Servicio Computacional y electrónico NIBLE",
    dure 3 años en donde mi primer logro profesional fue el aprender a reparar célulares y mejorar en la reparación de computadoras y laptops.

    Después de eso me fui a trabajar a Renova, dure 11 meses en donde obtuve otro logro profesional fue el conocer el soporte técnico en redes y servidores.
    Durante este tiempo me di cuenta de que necesitaba aprender más así decidí estudiar la carrera de ingeniería en tecnologías computacionales en la universidad CNCI.
    😵 si te preguntas porque tengo tantos huecos de tiempo es porque entraba en empresas como CTDI,CNS que trabajaban por proyecto y podian durar 1 mes a 6 meses.Dependiendo de que también
    se hiciera el proyecto dependía mi estancia en esas empresas, lo mejor de estás oportunidades es que a nivel profesional entendi el concepto de lidrazgo y administración de equipos multidisciplinarios.
    Por otra parte, en SLM estuve 3 meses pero ya como programador jr en donde aprendí como realizar un proyecto desde cero con PHP y JavaScript.

    Al termino de ese contrato, llego la pandemia y estuve estudiando mi carrera hasta que llego mi oportunidad en Softtek estuve 1 años y 8 meses en está
    consultoria aquí fue donde comence a desarrollarme más por sus cursos internos y por la oportunidad de trabajar con Coppel en el area de remediaciones, mi mayor logro
    fue el cumplir en tiempo y forma con los cursos de Udemy y los cursos internos de Softtek. Gracias a eso fui lider de célula antes de finalizar mi estancia en Softtek termine un
    curso impartido por Google en Gestión de proyectos y manejo de equipos de trabajo en donde comprendí mejor el rol de project manager y scrum master.
    Si quieres saber más me puedes encontrar en las siguientes redes sociales:
    LinkedIn: https://www.linkedin.com/in/jorge-alexis-rosales-morales
    Twitter: https://twitter.com/proyectonible
    Youtube: https://www.youtube.com/@ProyectoNible/featured 👈 Aquí hago directos de programación y hablo de temas de ciberseguridad y más detalles.
    {user_text}
    """
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=100
    )
    translated_response = openai.Translation.create(
      engine="text-davinci-002",
      prompt=response.choices[0].text.strip(),
      model="translation",
      source_lang="es",
      target_lang="en"
    )
    return translated_response.choices[0].text.strip()

if __name__ == "__main__":
    app.run()