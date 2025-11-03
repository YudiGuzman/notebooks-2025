## Laboratorio: Uso de Git y GitHub con Jupyter Notebooks

Este repositorio contiene los ejercicios realizados en el **laboratorio práctico sobre control de versiones con Git y GitHub**, aplicados al trabajo con notebooks de *Machine Learning*.

### 📘 Contenido

* **`test_split.ipynb`** – Notebook que entrena un modelo *LightGBM* con división `train_test_split`, agrupando clases y aplicando *early stopping* para evaluar el rendimiento.
* **`test_kfold.ipynb`** – Variante del experimento utilizando validación cruzada (*K-Fold*) para comparar resultados.

### 🧠 Objetivos de aprendizaje

1. Comprender el flujo básico de control de versiones con Git: `init`, `add`, `commit`, `branch`, `merge` y `push`.
2. Conectar un repositorio local con GitHub y gestionar ramas de trabajo independientes.
3. Aplicar prácticas reproducibles en notebooks de experimentación.

### ⚙️ Tecnologías utilizadas

* Python 3.10
* Jupyter Notebook
* LightGBM, Scikit-learn, Pandas
* Git 2.43.0 para Windows
* GitHub (interfaz web)

### 🚀 Resultados

* Entrenamiento local con **3 clases agrupadas (0–1→0, 2–3→1, 4→2)**.
* Métricas de validación: *Accuracy ≈ 0.48*, *F1-macro ≈ 0.48*.
* Generación de archivo `submission.csv` para inferencia en conjunto *test*.

### 📂 Autoría

**Yudi Guzmán Monteza**
