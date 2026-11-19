
""" import polars as pl

df = pl.read_csv("ventas_tiendas.csv")


def informacion_tienda(tienda):
    resultado = df.filter(pl.col("nombre_tienda") == tienda)
    return resultado


def total_facturacion(tienda):
    resultado = df.filter(pl.col("nombre_tienda") == tienda).select(pl.col("facturacion").sum())
    return resultado.item()

def total_gastos_personal(tienda):
    resultado = df.filter(pl.col("nombre_tienda") == tienda).select(pl.col("gastos_personal").sum())
    return resultado.item()

def mes_mayor_facturacion(tienda):
    resultado = df.filter(pl.col("nombre_tienda") == tienda).sort("facturacion", descending=True)
    return resultado["mes"][0]


############

def informacion_mes(mes):
    resultado = df.filter(pl.col("mes") == mes)
    return resultado

def media_tiendas(mes):
    resultado = df.filter(pl.col("mes") == mes).select(pl.col("facturacion").mean())
    return resultado.item()

def mayor_gasto_personal(mes):
    resultado = df.filter(pl.col("mes") == mes).sort("gastos_personal", descending=True)
    return resultado["nombre_tienda"][0]
 """
 
""" import polars as pl
import matplotlib.pyplot as plt 

df = pl.read_csv("ventas_tiendas.csv")

def tiendas():
    return df["nombre_tienda"].unique().to_list()

def meses():
    return df["mes"].unique().to_list()

#----# funciones relacionadas al 1er cuadro #----#
def datos_tabla_tienda(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).to_dicts()

def datos_tienda(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).select(pl.col("facturacion").sum().alias("facturacion_total"),
                                                               pl.col("gastos_personal").sum().alias("gastos_totales")).to_dicts()
def mes_mayor_facturacion(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).sort(by="gastos_personal", descending=True).row(0)

#----# funciones relacionadas al 2do cuadro #----#
def datos_tabla_mes(mes):
    return df.filter(pl.col("mes") == mes).to_dicts()

def media_facturacion(mes):
    return df.filter(pl.col("mes") == mes).select(pl.col("facturacion").mean().alias("facturacion_media")).to_dicts()

def mayor_gasto_personal(mes):
    return df.filter(pl.col("mes") == mes).sort(by="gastos_personal", descending=True).row(0) 


#####
 
def facturacion_total_tiendas():
    return df.group_by("nombre_tienda").agg(pl.col("facturacion").sum().alias("facturacion_total")).to_dicts() """
    

import polars as pl
import streamlit as st


def cargar_datos():

    alumnos = pl.read_csv("alumnos.csv")
    notas = pl.read_csv("notas.csv")

    datos = notas.join(
        alumnos,
        on="id_alumno",
        how="inner"
    )

    return datos


def obtener_cursos():

    datos = cargar_datos()

    return sorted(datos["curso"].unique().to_list())


def obtener_asignaturas():

    datos = cargar_datos()

    return sorted(datos["asignatura"].unique().to_list())


def obtener_grupos():

    datos = cargar_datos()

    return sorted(datos["grupo"].unique().to_list())


def obtener_evaluaciones():

    datos = cargar_datos()

    return sorted(datos["evaluacion"].unique().to_list())
#a partir de los filtros recibidos, filtramos el dataframe global
#eta función será llamada por las demás
def obtener_datos_filtrados(curso, asignatura, evaluacion, grupo):

    resultado =  cargar_datos()

    if curso != "Todos":
        resultado = resultado.filter(
            pl.col("curso") == curso
        )

    if asignatura != "Todas":
        resultado = resultado.filter(
            pl.col("asignatura") == asignatura
        )

    if evaluacion != "Todas":
        resultado = resultado.filter(
            pl.col("evaluacion") == evaluacion
        )

    if grupo != "Todos":
        resultado = resultado.filter(
            pl.col("grupo") == grupo
        )

    return resultado

def obtener_indicadores(curso, asignatura, evaluacion, grupo):

    datos = obtener_datos_filtrados(curso, asignatura, evaluacion, grupo)

    indicadores = datos.select(
        pl.col("id_alumno").unique().count().alias("alumnos"),
        pl.col("nota").mean().alias("media"),
        pl.col("nota").max().alias("maxima"),
        pl.col("nota").min().alias("minima"),
        (
            (pl.col("nota") >= 5).mean() * 100
        ).alias("porcentaje_aprobados")
    )
    return indicadores.row(0,named=True) ##devuelve los indicadores en un diccionario
def obtener_estadisticas_asignaturas(curso, asignatura, evaluacion, grupo):
    datos = obtener_datos_filtrados(curso, asignatura, evaluacion, grupo)
    resultado = datos.group_by("asignatura").agg(
        pl.col("id_alumno").unique().count().alias("alumnos_evaluados"),

        pl.col("nota").mean().round(2).alias("nota_media"),

        pl.col("nota").max().alias("nota_maxima"),

        ((pl.col("nota") >= 5).mean() * 100).round(2).alias("porcentaje_aprobados")
    )

    return resultado.sort("nota_media",descending=True)

def obtener_estadisticas_alumnos(curso, asignatura, evaluacion, grupo):
    datos = obtener_datos_filtrados(curso, asignatura, evaluacion, grupo)
    print(datos)
    por_asignatura = datos.group_by(["id_alumno", "nombre", "curso", "grupo", "asignatura"]).agg(
        pl.col("nota").mean().alias("media_asignatura")
    )
    resultado = por_asignatura.group_by(["id_alumno", "nombre", "curso", "grupo"]).agg(
        pl.col("media_asignatura").mean().round(2).alias("nota_media"),

        pl.col("media_asignatura").count().alias("asignaturas_evaluadas"),

        ((pl.col("media_asignatura") >= 5).sum()).alias("asignaturas_aprobadas")
    )

    return resultado.sort(
        "nota_media",
        descending=True
    )

def obtener_evolucion_evaluaciones(curso, asignatura, grupo):
    resultado = cargar_datos()

    if curso != "Todos":
        resultado = resultado.filter(pl.col("curso") == curso)

    if asignatura != "Todas":
        resultado = resultado.filter(pl.col("asignatura") == asignatura)

    if grupo != "Todos":
        resultado = resultado.filter(pl.col("grupo") == grupo)

    return resultado.group_by("evaluacion").agg(
            pl.col("nota").mean().round(2).alias("nota_media")
        ).sort("evaluacion")