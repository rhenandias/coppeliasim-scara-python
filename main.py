import time
from zmqRemoteApi import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

# client.setStepping(True)

sim.startSimulation()

axis_min = -160
axis_range = 320

print("Vai Filhão")

axis_A = sim.getObject("/MTB/axis")
axis_B = sim.getObject("/MTB/axis/link/axis")

sim.setJointTargetVelocity(axis_A, 10)
sim.setJointTargetPosition(axis_A, 160)


while True:
    pass

sim.stopSimulation()
