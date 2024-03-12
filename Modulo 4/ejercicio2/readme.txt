Este código define una jerarquía de clases para representar personas (Persona),
estudiantes (Estudiante), profesores (Profesor) y asignaturas (Asignatura).

** Clase Persona: **
Define una clase base llamada Persona que tiene atributos de nombre y edad.
Tiene métodos para establecer y obtener el nombre y la edad.
Hay dos métodos llamados set_nombre y set_edad, que muestran sobrecarga de
métodos. El método set_nombre tiene una versión que toma dos argumentos
(nombre y apellido), mientras que el método set_edad tiene una versión que también
toma un parámetro adicional (unidad) para indicar la unidad de la edad.

** Clase Estudiante (Subclase de Persona): **
Hereda de la clase Persona.
Agrega un nuevo atributo llamado grado.
Define métodos para establecer y obtener el grado.
Tiene un método adicional llamado estudiar_asignatura, que toma uno o más objetos
de asignatura como argumentos y muestra las asignaturas que el estudiante está
estudiando.

** Clase Profesor (Subclase de Persona): **
Hereda de la clase Persona.
Agrega un nuevo atributo llamado asignatura.
Define métodos para establecer y obtener la asignatura.
Tiene un método adicional llamado ensenar_asignatura, que imprime el nombre de la
asignatura que el profesor está enseñando.

** Clase Asignatura: **
Define una clase llamada Asignatura que tiene atributos de materia y código.
Tiene métodos para establecer y obtener la materia.

** Instancias y Uso: **
Se crean instancias de la clase Asignatura para representar diferentes asignaturas.
Se crean instancias de las clases Estudiante y Profesor con datos específicos.
Se llama a varios métodos para obtener información sobre los estudiantes y las asignaturas
que están estudiando.
Se muestra en la salida estándar información sobre los estudiantes y las asignaturas que
están estudiando.
Este código es un ejemplo básico de modelado de objetos en Python, utilizando herencia y
encapsulamiento para definir diferentes tipos de personas y su relación con las asignaturas.
La sobrecarga de métodos se utiliza para manejar diferentes formas de establecer la edad y
el nombre en la clase Persona.