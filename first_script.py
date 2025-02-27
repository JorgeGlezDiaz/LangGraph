

import os
import graphviz

# Especificar la ruta de Graphviz manualmente (si es necesario)
os.environ["PATH"] += os.pathsep + "/usr/bin/"

# Crear un objeto Digraph
dot = graphviz.Digraph()
dot.node("A", "Inicio")
dot.node("B", "Proceso")
dot.node("C", "Fin")
dot.edge("A", "B")
dot.edge("B", "C")

# Renderizar y mostrar
dot.render("graph_output", format="png", cleanup=False)
dot.view()
