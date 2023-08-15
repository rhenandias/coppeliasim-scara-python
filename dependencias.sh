pip3 install coppeliasim-zmqremoteapi-client
pip3 install matplotlib
pip3 install opencv-python

pip uninstall opencv-python
pip install opencv-python-headless

# Caso tenha erro com a execução do Open CV:
# O build do opencv pode levar um tempo para executar
pip3 uninstall opencv-python
pip3 install --no-binary opencv-python opencv-python