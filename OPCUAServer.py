# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:36:52 2020

@author: black
"""

from opcua import Server

import time

server = Server()
#server.set_endpoint("opc.tcp://10.7.156.54:4048")
server.set_endpoint("opc.tcp://192.168.2.113:4048")

name = "Test_server"
addspace = server.register_namespace(name)

node = server.get_objects_node()
param = node.add_object(addspace,"pararmeters")

v1 = param.add_variable(addspace, "ConveyorSpeed1", 300)
v1.set_writable()
v2 = param.add_variable(addspace, "ConveyorSpeed2", 360)
v2.set_writable()
v3 = param.add_variable(addspace, "ConveyorSpeed3", 360)
v3.set_writable()
cycletime = param.add_variable(addspace, "Zykluszeit", 0)
cycletime.set_writable()

server.start()

while True:
    
    acycletime = 330/(v1.get_value() + v2.get_value())
    cycletime.set_value(acycletime)
    t1 = v1.get_value()
    t2 = v2.get_value()
    t3 = v3.get_value()
    t4 = cycletime.get_value()
    print("Conveyor Speed 1 ist {}".format(t1))
    print("Conveyor Speed 2 ist {}".format(t2))
    print("Conveyor Speed 3 ist {}".format(t3))
    print("Zykluszeit beträgt {} min".format(t4))
    time.sleep(1)