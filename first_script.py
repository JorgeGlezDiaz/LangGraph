

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

"""
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

"""
'''
In your terminal window, run:

bash <conda-installer-name>-latest-Linux-x86_64.sh
conda-installer-name will be one of "Miniconda3", "Anaconda", or "Miniforge3".
Using with fish shell
To use conda with fish shell, run the following in your terminal:

Add conda binary to $PATH, if not yet added:

fish_add_path <conda-install-location>/condabin
Configure fish-shell:

conda init fish

Updating conda
Open a terminal window.

Run conda update conda.

Uninstalling conda
Open a terminal window.

Remove the entire conda install directory with (this may differ depending on your installation location)

rm -rf ~/conda



Create environment from scratch

conda create -n agents python=3.11
conda activate agents
conda install -c conda-forge poetry
conda env export --from-history > environment.yml
poetry init

Create environment from file

conda env create -f environment.yml

Run agent
langgraph dev
Run fastapi server
fastapi dev app/api.py

poetry add "fastapi[standard]"
'''