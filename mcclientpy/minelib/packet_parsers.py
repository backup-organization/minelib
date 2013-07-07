"""This file is used to parse the packets returned by the server."""

import data_type_parser
import packet_generators
import cStringIO

def makeio(string):
    return cStringIO.StringIO(string)

def parse_keepalive(socket):
    keepalive_id=data_type_parser.parse_int(makeio(socket.recv(4)))
    print "Got keepalive. Responding"
    socket.send(packet_generators.packet_keepalive(keepalive_id))

def parse_login_request(socket):
    result = {}
    result['EntityID'] = data_type_parser.parse_int(makeio(socket.recv(4)))
    short1=socket.recv(2)
    lenght=data_type_parser.parse_short(makeio(short1))
    result['LevelType'] = data_type_parser.parse_string8(makeio(data_type_parser.short(lenght)+socket.recv(lenght)))
    result["GameMode"]=data_type_parser.parse_byte(makeio(socket.recv(1)))
    result["Dimension"]=data_type_parser.parse_byte(makeio(socket.recv(1)))
    result["Difficulty"]=data_type_parser.parse_byte(makeio(socket.recv(1)))
    result["NotUsed"]=data_type_parser.parse_byte(makeio(socket.recv(1)))
    result["MaxPlayers"]=data_type_parser.parse_byte(makeio(socket.recv(1)))
    return result

def parse_spawn_position(socket):
    result={}
    result["X"]=data_type_parse.parse_int(makeio(socket.recv(4)))
    result["Y"]=data_type_parse.parse_int(makeio(socket.recv(4)))
    result["Z"]=data_type_parse.parse_int(makeio(socket.recv(4)))
    print result
    return result

def parse_chat_message(socket):
    short1=socket.recv(2)
    lenght=data_type_parser.parse_short(short1)
    chat_message=socket.recv(lenght)
    return chat_message

def parse_time_update(socket):
    result={}
    result["WorldAge"]=data_type_parser.parse_long(makeio(socket.recv(8)))
    result["TimeOfDay"]=data_type_parser.parse_long(makeio(socket.recv(8)))
    return result

def parse_entity_equipment(socket):
    #Not implemented yet.
    pass

def parse_health_update(socket):
    result={}
    result["Health"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    result["Food"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    result["FoodSaturation"]=data_type_parser.parse_float(makeio(socket.recv(4)))
    return result

def parse_respawn(socket):
    result={}
    result["Dimension"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    result["Difficulty"]=data_type_parser.parse_byte(makeio(socket.recv(1)))
    result["GameMode"]=data_type_parser.parse_byte(makeio(socket.recv(1)))
    result["WorldHeight"]=data_type_parser.parse_short(makeio(socket.recv(2)))
    short1=socket.recv(2)
    lenght=data_type_parser.parse_short(short1)
    result["LevelType"]=data_type_parser.parse_string8(makeio(data_type_parser.short(lenght)+socket.recv(lenght)))
    return result

def parse_player_pos_and_look(socket):
    #Not fully implemented. Just responding with an appropriate packet.
    socket.send("0x0d"+socket.recv(41))

def parse_held_item_change(socket):
    slot_id=data_type_parser.parse_short(makeio(socket.recv(2)))
    return slot_id

def parse_use_bed(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(14)

def parse_animation(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(5)

def parse_spawn_named_entity(socket):
    #Not implemented yet.
    pass

def parse_collect_item(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(8)

def parse_spawn_painting(socket):
    result={}
    result["EntitiyID"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    short1=socket.recv(2)
    lenght=data_type_parser.parse_short(makeio(short1))
    result["Title"]=data_type_parser.parse_string8(makeio(data_type_parser.short(lenght)+socket.recv(lenght)))
    result["X"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    result["Y"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    result["Z"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    result["Direction"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    return result

def parse_spawn_exp_orb(socket):
    result={}
    result["EntityID"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    result["X"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    result["Y"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    result["Z"]=data_type_parser.parse_int(makeio(socket.recv(4)))
    result["Count"]=data_type_parser.parse_short(makeio(socket.recv(2)))
    return result

def parse_entity_velocity(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(10)

def parse_destroy_entity(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    entity_count=data_type_parser.parse_byte(makeio(socket.recv(1)))
    for i in range(entity_count):
        socket.recv(4)

def parse_entity(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(4)

def parse_entity_relative_move(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(7)

def parse_entity_look(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(6)

def parse_entity_look_and_relative_move(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(9)

def parse_entity_teleport(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(18)

def parse_entity_head_look(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(5)

def parse_entity_status(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(5)

def parse_attach_entity(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(8)

def parse_entity_effect(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(8)

def parse_remove_entity_effect(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(5)

def parse_set_experience(socket):
    #Not fully implemented. Just getting the appropriate packet data.
    data=socket.recv(8)

def parse_chunk_data(socket):
    socket.recv(13)
    size=data_type_parser.parse_int(makeio(socket.recv(4)))
    socket.recv(size)
