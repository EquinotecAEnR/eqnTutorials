--The port connected to client
port = 5024
--The IP Address of client
ip = "192.168.1.77"
--initialize TCP server
init_tcp_server (port)
sleep (5)

local function splitStringToInts(input)
    -- Use string.gmatch to iterate over the numbers in the string
    local R, X, Y = input:match("(%d+),%s*(%d+),%s*(%d+)")
    
    -- Convert the matched strings to integers
    R = tonumber(R)
    X = tonumber(X)
    Y = tonumber(Y)
	set_global_variable ("B071", R)
	set_global_variable ("B072", X)
	set_global_variable ("B073", Y)
	
    --return R, X, Y
end

while(1)do
	--decide if client is connected to server
	ret= is_client_connected (ip)
	if (ret == 1)then
		elite_print("data")
		sleep (1)
		--server send msg to client
		server_send_data (ip ,"1")
		recv="1"
		while(recv ~= "2") do
			sleep (0.1)
			--Server receive data from client
			Ret,recv= server_recv_data (ip)
			if(Ret > 0) then
			elite_print("data length=",ret,"data=",recv)
			splitStringToInts(recv)
			end
		end
	end
end