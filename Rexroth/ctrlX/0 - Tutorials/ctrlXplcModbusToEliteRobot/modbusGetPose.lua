sleep(1)
--modbus slave IP Address
ip="192.168.1.201"
--modbus slave port
port=502
--get modbus tcp header
ctx=modbus_new_tcp(ip,port)

--connect to modbus header
conState=modbus_connect(ctx)
while (conState==-1) do
	sleep(0.05)
	elite_print("Connection failed")
	conState=modbus_connect(ctx)
end
elite_print("Connection OK")	

-- Function to interpret a 16-bit value as a signed integer
function toSigned16(value)
    if value > 32767 then
        return value - 65536
    else
        return value
    end
end

while true do
	-- Read the signal value from the specified Register
	-- int,int Modbus_read_register (ctx,int reg)
	ret1,value1 = modbus_read_register(ctx,531)        
	if(ret1==-1)then       
		elite_print("Read error")
	end
	
	ret2,value2 = modbus_read_register(ctx,532)        
	if(ret2==-1)then       
		elite_print("Read error")
	end
	
	ret3,value3 = modbus_read_register(ctx,533)        
	if(ret3==-1)then       
		elite_print("Read error")
	end
	
	ret4,value4 = modbus_read_register(ctx,534)        
	if(ret4==-1)then       
		elite_print("Read error")
	end
	
	ret5,value5 = modbus_read_register(ctx,535)        
	if(ret5==-1)then       
		elite_print("Read error")
	end
	
	ret6,value6 = modbus_read_register(ctx,536)        
	if(ret6==-1)then       
		elite_print("Read error")
	end
	
	--Assing Values with negative sign
	sValue1=toSigned16(value1)
	sValue2=toSigned16(value2)
	sValue3=toSigned16(value3)
	sValue4=toSigned16(value4)
	sValue5=toSigned16(value5)
	sValue6=toSigned16(value6)
	
	elite_print("x,y,z,rx,ry,rz values are:",sValue1,sValue2,sValue3,sValue4,sValue5,sValue6)
	
	--set_global_variable ("V006",sValue1,sValue2,sValue3,sValue4,sValue5,sValue6)
	set_global_variable ("V006",sValue1,sValue2,sValue3,0,0,0)

	sleep(0.1)
end

elite_print("End")
modbus_close(ctx)

