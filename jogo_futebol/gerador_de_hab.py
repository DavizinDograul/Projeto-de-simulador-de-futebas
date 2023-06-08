# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:00:33 2023

@author: david
"""
def porcen(val, por):
    
    return (val * por) / 100

g = 80

pesos_t = 62
p1 = 1
p2 = 2
p3 = 3
p4 = 4
p5 = 5
p6 = 6

per_p1 = 100/pesos_t *p1
per_p2 = 100/pesos_t *p2
per_p3 = 100/pesos_t *p3
per_p4 = 100/pesos_t *p4
per_p5 = 100/pesos_t *p5
per_p6 = 100/pesos_t *p6


total_geral = g * pesos_t
fsff = porcen(total_geral, per_p6)
atributo_cru = fsff / 45 * 10
atributo_real = (atributo_cru + (g * 2)) / 3

print()

