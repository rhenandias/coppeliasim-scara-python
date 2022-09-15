from zmqRemoteApi import RemoteAPIClient

# Configurações Globais de Operação do Robô
tamanho_elo_1 = 0.4670
tamanho_elo_2 = 0.4005
precisao = 3

# Configura cliente de conexão com o CoppeliaSim
client = RemoteAPIClient()
sim = client.getObject('sim')

# Adquire Handlers para as Juntas do Robô
axis_A = sim.getObject("/MTB/axis")
axis_B = sim.getObject("/MTB/axis/link/axis")


def start():
    """
    Inicia simulação no CoppeliaSim
    """
    sim.startSimulation()


def stop():
    """
    Finaliza simulação no CoppeliaSim
    """
    sim.stopSimulation()


def get_sensors():
    """
    Adquire posições de juntas do robô

    Retorno:
        t1, t2 = Posições das juntas dos Elos 1 e 2 (em graus)
    """
    t1 = sim.getJointPosition(axis_A)
    t2 = sim.getJointPosition(axis_B)

    return t1, t2


def moveJ(t1, t2, interpolation=True):
    """
    Movimenta para uma posição no espaço das juntas

    Parâmetros:
      t1, t2 = Ângulo das juntas (em graus)
    """

    sim.setJointTargetPosition(axis_A, t1)
    sim.setJointTargetPosition(axis_B, t2)

    moved = False
    threshold = 0.1

    while not moved:
        s1, s2 = get_sensors()

        moved_a = True if abs(s1, -t1)
