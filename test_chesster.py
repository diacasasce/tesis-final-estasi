
from chesster import Chesster
import serCOM as sC
import cv2
import numpy as np

##import train-data
player=Chesster(bright=70,sharp=100,contrast=100)

##inicio de juego
player.new_game()

turno=False
##sC.send_ser("0;0;0;1;1;\r\n",player.arm)
##sC.send_ser("0;200;0;1;1;\r\n",player.arm)
##sC.send_ser("0;-200;0;1;1;\r\n",player.arm)
##sC.send_ser("0;0;0;1;1;\r\n",player.arm)
def run(mstart=True):
    print('start')
##    player.view(10)
    player.mkf(player.folder)
    im=player.captura('CP0.jpg')
##    im=cv2.imread("CP0.jpg")
    player.plt_show(im)
    player.set_bright(50)
    ok=True
    while ok:
        imc=player.calibracion(im)
        chk=input('esta bien calibrado? (Y/N):  ').upper()
        if chk=='Y':
            ok=not(ok)
    player.set_bright(50)
    if mstart:
        turno=True
        
def play_alone(alone=True,turno=True):
    k=1
    d=[]
    t=[]
    while not(player.brain.is_over()):
        if alone:
            (d,t)=player.go_auto(True,na=str(k),d=d,t=t)
        else:
            if turno:
                (d,t)=player.go_auto(True,na=str(k),d=d,t=t)
            else:
                player.human(True,na=str(k),d=d,t=t)
            turno=not(turno)
        k=k+1
        
    return (d,t)
def play_data(n,m):
    d=[]
    t=[]
    b=player.board
    for k in range(n,m):
        player.a_board=b
        (p,b,c,imc,d,t)=player.recon(na=str(k),CP=True,datt=d,tr=t)
        player.cboard=c
        player.board=b
        print(k)
    return(d,t)
def get_data(m,n,d=[],t=[]):
    b=player.board
    for k in range(m,n):
        (p,b,c,imc,d,t)=player.recon(na=str(k),CP=True,datt=d,tr=t)
        input()
        print(k)
    return(d,t)

run()
input()
play_alone(alone=False)

        
