# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:32:33 2020

@author: black
"""

from opcua import Client, ua
import datetime

url = "opc.tcp://192.168.2.113:4048"
#url = "opc.tcp://192.168.20.20:4840"
client = Client(url)
client.session_timeout = 30000
client.connect()
print(f"Connected: {url}")

node = client.get_node('ns=2;i=2')
print("before: ", node.get_value())
value = node.get_value()
new_value = value + 10
node.set_value(ua.DataValue(ua.Variant(new_value, ua.VariantType.Int16)))
print("after: ", node.get_value())

node = client.get_node('ns=2;i=3')
print("before: ", node.get_value())
value = node.get_value()
new_value = value + 10
node.set_value(ua.DataValue(ua.Variant(new_value, ua.VariantType.Int16)))
print("after: ", node.get_value())

node = client.get_node('ns=2;i=4')
print("before: ", node.get_value())
value = node.get_value()
new_value = value + 10
node.set_value(ua.DataValue(ua.Variant(new_value, ua.VariantType.Int16)))
print("after: ", node.get_value())

node = client.get_node('ns=2;i=5')
print("Zykluszeit: ", node.get_value())

client.disconnect()
print("Disconnected")
 
