# *Al seleccionar una tienda se mostrara:
# Una tabla con la información de dicha tienda. Y debajo de esa tabla:
# -total de facturación
# -total de gastos de personal
# -mes con mayor facturación

# *Al seleccionar un mes se mostrará:
# Una tabla con los datos de ese mes. Y debajo de esa tabla:
# -Media de facturación de todas las tiendas
# -Tienda con mayor gasto de personal

# import streamlit as st
# import tiendas_repository as tr
# import polars as pl
# import matplotlib.pyplot as plt 

# df = pl.read_csv("ventas_tiendas.csv")


# with st.sidebar:

#     st.header("Menú")

#     tienda = st.selectbox(
#         "Elige una tienda:",
#         df["nombre_tienda"].unique().to_list()
#     )

#     mes = st.selectbox(
#         "Elige un mes:",
#         df["mes"].unique().to_list()
#     )



# st.header(f"Información de {tienda}")

# datos_tienda = tr.informacion_tienda(tienda)

# st.dataframe(datos_tienda)

# st.subheader("Estadísticas de la tienda")

# st.write(
#     f"Total facturación: {tr.total_facturacion(tienda):,.2f} €"
# )

# st.write(
#     f"Total gastos de personal: {tr.total_gastos_personal(tienda):,.2f} €"
# )

# st.write(
#     f"Mes con mayor facturación: {tr.mes_mayor_facturacion(tienda)}"
# )


# st.divider()




# st.header(f"Información de {mes}")

# datos_mes = tr.informacion_mes(mes)

# st.dataframe(datos_mes)

# st.subheader("Estadísticas del mes")

# st.write(
#     f"Media de facturación de todas las tiendas: "
#     f"{tr.media_tiendas(mes):,.2f} €"
# )

# st.write(
#     f"Tienda con mayor gasto de personal: "
#     f"{tr.mayor_gasto_personal(mes)}"
# )
#  """
 
 
# """ import streamlit as st
# import tiendas_repository as repo

# tienda_sel=None
# mes_sel=None
# with st.sidebar:
#     st.subheader("Filtros")
#     curso_sel=st.selectbox("Curso",repo.tiendas(),index=None,key=1)
#     mes_sel=st.selectbox("Seleccione mes",repo.meses(),index=None,key=2)
    
# if tienda_sel!=None:
#     st.table(repo.datos_tabla_tienda(tienda_sel))
#     datos=repo.datos_tienda(tienda_sel)
#     tupla=repo.mes_mayor_facturacion(tienda_sel)
#     #st.write(f"Total facturacion {datos[0]["facturacion_total"]}, gastos totales {datos[0]["gastos_totales"]}, mes con mayor facturacion {tupla[1]}")
#     col1,col2,col=st.columns(3)
#     col1.metric("Total facturacion",datos[0]["facturacion_total"])
#     col2.metric("Gastos totales",datos[0]["gastos_totales"])
#     col.metric("Ms con mayor facturacion",repo.mes_mayor_facturacion(tienda_sel)[1])
# if mes_sel!=None:
#     st.table(repo.datos_tabla_mes(mes_sel))
    
    
import streamlit as st
import matplotlib.pyplot as plt

import formacion_repository as repo


st.set_page_config(
    page_title="Análisis académico",
    layout="wide"
)
#####################
##Funciones para gráficos#######
def grafico_notas_asignaturas(datos): #Recibe dataframe
    fig,gr=plt.subplots()
    gr.bar(
        datos["asignatura"].to_list(),
        datos["nota_media"].to_list()
    )

    gr.set_title("Nota media por asignatura")
    gr.set_xlabel("Asignatura")
    gr.set_ylabel("Nota media")
    gr.set_ylim(0,10)
    return fig

def grafico_evolucion_evaluaciones(datos):
    fig,gr=plt.subplots()
    gr.plot(
        datos["evaluacion"].to_list(),
        datos["nota_media"].to_list(),
        marker="o"
    )

    gr.set_title("Evolución de las notas")
    gr.set_xlabel("Evaluación")
    gr.set_ylabel("Nota media")

    gr.set_xticks(datos["evaluacion"].to_list())
    gr.set_ylim(0, 10)

    plt.grid(alpha=0.3)
    return fig

def grafico_distribucion_notas(datos):
    fig, gr = plt.subplots()
    gr.hist(
        datos["nota"].to_list(),
        bins=10,
        range=(0, 10),
        edgecolor="black"
    )

    gr.set_title("Distribución de calificaciones")
    gr.set_xlabel("Nota")
    gr.set_ylabel("Número de calificaciones")

    gr.set_xticks(range(0, 11))
    return fig



#########################




st.sidebar.title("Filtros")

curso = st.sidebar.selectbox("Curso",["Todos"] + repo.obtener_cursos())

asignatura = st.sidebar.selectbox("Asignatura",["Todas"] + repo.obtener_asignaturas())

grupo = st.sidebar.selectbox("Grupo",["Todos"] + repo.obtener_grupos())

evaluacion = st.sidebar.selectbox("Evaluación",["Todas"] + repo.obtener_evaluaciones())

#Dashboard
st.title("Dashboard de rendimiento académico")
#indicadores
indicadores = repo.obtener_indicadores(
    curso,
    asignatura,
    evaluacion,
    grupo
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Alumnos evaluados",
    indicadores["alumnos"]
)

col2.metric(
    "Nota media",
    f"{indicadores['media']:.2f}"
)

col3.metric(
    "Nota máxima",
    f"{indicadores['maxima']:.2f}"
)

col4.metric(
    "Nota mínima",
    f"{indicadores['minima']:.2f}"
)

col5.metric(
    "Aprobados",
    f"{indicadores['porcentaje_aprobados']:.1f}%"
)

#estadísticas por asignatura
st.subheader("Estadísticas por asignatura")

estadisticas_asignaturas = repo.obtener_estadisticas_asignaturas(
    curso,
    asignatura,
    evaluacion,
    grupo
)

st.dataframe(estadisticas_asignaturas)

#estadísticas por alumno
st.subheader("Rendimiento por alumno")

estadisticas_alumnos = repo.obtener_estadisticas_alumnos(
    curso,
    asignatura,
    evaluacion,
    grupo
)

st.dataframe(estadisticas_alumnos)


#graficos
st.subheader("Representación gráfica")

tab1, tab2, tab3 = st.tabs([
    "Notas por asignatura",
    "Evolución de evaluaciones",
    "Distribución de notas"
])
with tab1:
    fig=grafico_notas_asignaturas(estadisticas_asignaturas)
    st.pyplot(fig)
    plt.close(fig)
    

with tab2:
    evolucion=repo.obtener_evolucion_evaluaciones(curso,asignatura,grupo)
    fig=grafico_evolucion_evaluaciones(evolucion)
    st.pyplot(fig)
    plt.close(fig)

with tab3:

    fig = grafico_distribucion_notas(repo.obtener_datos_filtrados(curso,asignatura,evaluacion,grupo)) #función que devuelve todos los datos filtrados

    st.pyplot(fig)
    plt.close(fig)