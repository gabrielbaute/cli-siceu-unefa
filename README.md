# CLI para cálculo de notas formato SICEU

En su estado actual, el archivo cuenta con una interfaz por línea de comando (CLI por sus siglas en inglés) construída mediante el package Click de Python. Cuenta con cuatro comandos:

* hello
* calcular-notas
* equivalente
* registrar-corte

Cada uno de ellos tiene su correspondiente sintaxis, sin embargo las descripciones aún no están del todo terminadas.

Actualmente, las notas se registran en un archivo .txt definido de manera predeterminada, pero el usuario puede escoger el nombre del archivo, sin embargo aún no se incorpora un módulo para leer las notas del archivo, por lo que la CRUD está incompleta.

Agregada integración con JSON.

El archivo es originalmente elaborado por @MisaVnz, estudiante de la institución.

## Roadmap

Estado actual y futuros desarrollos:

- [x] Construcción de la app de cálculos
- [x] Interfaz CLI
- [x] Registro de los datos en .txt
- [x] Registro de los datos en JSON
- [x] Docsting
- [ ] Completar el proceso CRUD
- [ ] Desarrollo de una GUI (Interfaz Gráfica de Usuario)
- [ ] Integración mediante BDD
- [ ] Desarrollo de interfaz web (mediante reflex)
- [ ] Desarrollo de un sistema de sesiones de usuario


## Recursos:
* [Documentación oficial de Click](https://click.palletsprojects.com/en/8.1.x/)