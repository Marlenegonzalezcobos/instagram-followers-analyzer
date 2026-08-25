# 📊 Analizador de Conexiones de Instagram (Python + IA)

Este es un proyecto práctico desarrollado en Python diseñado para auditar, procesar y clasificar las relaciones de seguimiento de una cuenta de Instagram a partir de las exportaciones de datos oficiales de Meta (en formato JSON).

## 🚀 Características del Proyecto
* **Procesamiento Eficiente:** Maneja la lectura de múltiples archivos JSON de gran tamaño en simultáneo utilizando las librerías nativas `json`, `os` y `glob`.
* **Teoría de Conjuntos:** Implementa operaciones matemáticas de conjuntos (`Sets` en Python) para cruzar datos de manera exacta mediante restas e intersecciones.
* **Limpieza de Datos Automatizada:** Cuenta con una lógica de filtrado integrada que descarta automáticamente registros obsoletos o cuentas fantasmas eliminadas por la plataforma (`__deleted__`).
* **Reporte Limpio:** Exporta los resultados organizados de manera alfanumérica y numerada directamente a un archivo de texto plano (`reporte_instagram.txt`).

## 📁 Estructura del Reporte Generado
El script procesa los archivos locales y genera un output clasificado en 3 listas definitivas:
1. **Cuentas que vos seguís pero no te siguen de vuelta** (Falta de reciprocidad).
2. **Seguimiento mutuo** (Cuentas que se siguen recíprocamente).
3. **Personas que te siguen pero vos no seguís** (Seguidores pendientes de devolución).

## 💡 Metodología y Aprendizaje
Este proyecto nació como un desafío de automatización real. Como estudiante de tecnología, utilicé Inteligencia Artificial como copiloto para la optimización de la estructura del código, enfocando mi rol en:
* Configurar y gestionar el entorno de desarrollo local en **Visual Studio Code**.
* Realizar el proceso de *debugging* cuando surgieron errores de compatibilidad debido a cambios imprevistos en la estructura de claves internas de Meta (migración de lectura de campos generales a campos específicos de tipo `title`).
* Diseñar la lógica de exclusión para limpiar el reporte de datos basura.
