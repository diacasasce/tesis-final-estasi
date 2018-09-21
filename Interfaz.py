#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :menu.py
#description     :This program displays an interactive menu on CLI
#author          :
#date            :
#version         :0.1
#usage           :python menu.py
#notes           :
#python_version  :2.7.6  
#=======================================================================

# Import the modules needed to run the script.
from chesster import Chesster
import serCOM as sC
import cv2
import numpy as np
import sys, os
from time import sleep
from motor import Brain

class pantalla :
    def __init__(self):
        self.data = []
        self.nivel=20
        # =======================
        #    MENUS DEFINITIONS
        # =======================

        # Menu definition
        self.menu_actions = {
            'main_menu': self.main_menu,
            '1': self.menu1,
            '11': self.demo,
            '2': self.menu2,
            '21': self.normal,
            '9': self.back,
            '0': self.exit,
        }
    # =======================
    #     MENUS FUNCTIONS
    # =======================
    def header(self):
        os.system('clear')
        print()
        print() 
        print ("      ////////////////////////////////////////////////////////////////////////////////////////")
        print ("      //                                                                                    //")
        print ("      //  #######   ##   ##   #######   #######   ########   ########   #######   #######   //")
        print ("      //  ##        ##   ##   ##        ##        ##            ##      ##        ##   ##   //")
        print ("      //  ##        #######   #######   #######   ########      ##      #######   ######    //")
        print ("      //  ##        ##   ##   ##             ##         ##      ##      ##        ##   ##   //")
        print ("      //  #######   ##   ##   #######   #######   ########      ##      #######   ##    ##  //")
        print ("      //                                                                                    //")
        print ("      ////////////////////////////////////////////////////////////////////////////////////////")
        print ("      ////////////////////////////////////////////////////////////////////////////////////////")
        print ("      //                                                                                    //")
        print ("      //                                     POR                                            //")
        print ("      //                                                                                    //")
        print ("      //                         DIEGO ALEJANDRO CASAS CEVALLOS                             //")
        print ("      //                                      y                                             //")
        print ("      //                         JUAN SEBASTIAN MARTINEZ QUINTERO                           //")
        print ("      //                                                                                    //")
        print ("      ////////////////////////////////////////////////////////////////////////////////////////")
        print()
        print()
        return
    # Main menu
    def main_menu(self):
        os.system('clear')
##        self.board=Brain()
        self.header()
        print ("Bienvenido al menu de inicio de chesster \n")
        print ("Desea iniciar un juego?")
        print ("1. Version demostracion")
        print ("2. Iniciar Juego ")
        print ("\n0. Salida")
        choice = input(" >>  ")
        self.exec_menu(choice)

        return

    # Execute menu
    def exec_menu(self,choice):
        ch = choice.lower()
        if ch == '':
            self.menu_actions['main_menu']()
        else:
            try:
                self.menu_actions[ch]()
            except KeyError:
                print ("Invalid selection, please try again.\n")
                self.menu_actions['main_menu']()
        return
    
    # Menu 1
    def menu1(self):
        self.header()
        print ("¡Bienvenido al modo de demonstracion!\n ¿Listo para el juego?")
        print ("1. Iniciar")
        print ("2. Volver al menu principal")
        print ("0. Salir")
        choice ='1'+input(" >>  ")
        print(choice)
        self.exec_menu(choice)
        return
    # Alone
    def demo(self):
        self.start(demo=True)
    def start(self,demo=False):
        player=Chesster(bright=70,sharp=100,contrast=100,demo=demo)
        player.new_game()
        turno=True
        alone=False
        player.mkf(player.folder)
        im=player.captura('CP0.jpg')
        player.plt_show(im,True)
        player.set_bright(50)
        ok=True
        while ok:
            imc=player.calibracion(im)
            chk=input('esta bien calibrado? (Y/N):  ').upper()
            if chk=='Y':
                ok=not(ok)
        player.set_bright(50)
        print('TABLERO CALIBRADO')
        print('Por favor posicione las fichas en su lugar')
        input('Presiones enter para iniciar')
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
        
        sleep(2)
        player.__del__()
        self.exec_menu('main_menu')

    # Menu 2
    def menu2(self):
        self.header()
        print ("¡Bienvenido al modo de juego!\n ¿Listo para Empezar?")
        print ("Antes de iniciar por favor retira todas las piezas del tablero")
        print ("1. Iniciar")
        print ("2. Volver al menu principal")
        print ("0. Salir")
        choice ='2'+input(" >>  ")
        print(choice)
        self.exec_menu(choice)
        return
    ## not alone
    def normal(self):
        self.start()
    
    # Back to main menu
    def back(self):
        self.menu_actions['main_menu']()

    # Exit program
    def exit(self):
        sys.exit()



# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    pt=pantalla()
    pt.main_menu()