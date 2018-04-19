#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  milho.py
#  
#  Copyright 2018 20181bsi0121 <20181bsi0121@SR6192>
#  
# 

def main():
    cont = 1;
    total = 1;
    while cont <= (8*8):

        total = 2*total;

        cont = cont + 1;

    print('Nº de grãos de milho que se pode colocar num tabuleiro de xadrez: ',total)
    return 0

if __name__ == '__main__':
	main()
