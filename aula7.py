velocidade = 60
local_carro = 10

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1


if velocidade > RADAR_1:
    print ('Você superou o limite de velocidade!!')
if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        velocidade>RADAR_1:
    print ('O carro foi multado')