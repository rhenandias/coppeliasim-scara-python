import scara
import time

# Inicia Simulação
scara.start()

scara.moveJ(90, 0, False)
scara.moveJ(0, 0, False)
scara.moveJ(-90, 0, False)

# Finaliza Simulação
scara.stop()
