import sys
import subprocess
import time

def move_turtle(vx, vy, vtheta, tempo_em_ms):
    # Comando para mover a tartaruga
    move_cmd = f"rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '{vx}' '{vy}' 0 0 0 '{vtheta}'"

        
    
    # Início do movimento
    subprocess.run(move_cmd, shell=True)
    
    # Espera a duração especificada
    time.sleep(tempo_em_ms)
    
    # Comando para parar a tartaruga
    stop_cmd = "rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- 0 0 0 0 0 0"
    subprocess.run(stop_cmd, shell=True)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Uso: turtle_controller.py vx vy vtheta tempo_em_ms")
    else:
        try:
            vx = float(sys.argv[1])
            vy = float(sys.argv[2])
            vtheta = float(sys.argv[3])
            tempo_em_ms = float(sys.argv[4])
            move_turtle(vx, vy, vtheta, tempo_em_ms)
        except ValueError:
            print("Por favor, insira valores numéricos válidos para velocidade e duração.")
