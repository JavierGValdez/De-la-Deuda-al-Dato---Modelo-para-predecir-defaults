# 💳 De la Deuda al Dato: ML para Predecir Defaults
Modelo predictivo a partir de datos de clientes de una entidad crediticia dentro del contexto de una crisis en Taiwán (año 2005) bajo el marco del <u><strong>Trabajo Práctico Final</strong></u>

# Contexto 
En 2005, Taiwán enfrentó una crisis crediticia que expuso la necesidad crítica de detectar tempranamente los impagos por parte de los clientes de los bancos. Las causas pueden deberse
a que el cliente no puede afrontar las condiciones necesarias de pago por la coyuntura económica del país en ese entonces, o por la deficiente identificación a la hora de evaluar potenciales clientes.

Por entonces, nos surge la pregunta: <u><strong>¿Cómo pudieron haberse anticipado ante la situación crítica de avasallante número de clientes en deudas con la mayor anterioridad posible?</strong></u>

# 🎯 Definición del problema
El impago de las tarjetas de crédito resulta ser un problema de causa mayor para las entidades bancarias, por lo cual, se generan diversos inconvenientes para estas mismas, como principalmente:
💸 Pérdidas financieras significativas,
📉 Deterioro de la cartera crediticia, 
⚠️ Riesgo sistémico acumulativo 
y entre otros, impacto en el flujo de caja que afecta y acorta directamente la capacidad de otorgar nuevas líneas de crédito, y además consecuente de infringir la reputación del banco, deteriorando la gestión del mismo.

Y por las mismas razones, es necesario y esencial para los bancos detectar con anticipación el segmento de clientes con probabilidades de entrar en mora. Con estos patrones de identificación, se logra direccionar las nuevas medidas de prevención para este grupo fervientemente, siendo así mejorando la cota de decisión a la hora de brindar un nuevo crédito al cliente. 

# 🔍 Solución Propuesta
Exploramos distintos algoritmos de Machine Learning para buscar a los potenciales clientes que no se encuentran ocasionalmente al día con su deuda, utilizando datos demográficos y de comportamiento financiero para el aprendizaje de los modelos.
Teniendo en cuenta que el no identificar un deudor correctamente es más costoso que el hecho de confundir un deudor con un cliente que mantiene al día su deuda, desarrollaremos un modelo de Machine Learning enfocado en <u><strong>maximizar el recall</strong></u>: preferimos alertar sobre posibles defaults aunque generemos algunas falsas alarmas, porque el costo de perder un default real es mucho mayor.


# 📁 Estructura del Proyecto
├── 📓 notebooks/          # Análisis exploratorio y modelos
├── 📊 data/              # Dataset original y procesado
├── 🎨 visualizations/    # Gráficos y matriz de confusión
└── 📋 docs/              # Presentación y documentación

# Datos utilizados
Los datos provienen desde UCI Irvine Machine Learning Repository. La recolección fue hecha por los autores (Yeh y Lien, 2009) con el objetivo de evaluar la precisión predictiva de la probabilidad de default a través de distintos métodos de minería de datos.

Este conjunto contiene observaciones acerca del pago de clientes de un banco Taiwanés en el año 2005, incluyendo variables demográficas (género, estado civil, edad, nivel educativo), variables categóricas que describen el estado de pago de un mes dado para el periodo Abril- Septiembre y variables numéricas que describen tanto el monto de la factura a pagar como el pago realizado por la persona en dicho mes.
También se incluye la línea de crédito de la persona y un estado binario para el mes de octubre que indica si la persona pagó su resumen en ese mes.

# 👥 Equipo

Javier Gonzalo Valdez - jgvaldez@unsam-bue.edu.ar
Bruno Inguanzo - brunoinguanzo14@gmail.com
Matías Alejandro Vergara Vicencio - mavergaravicencio@estudiantes.unsam.edu.ar


