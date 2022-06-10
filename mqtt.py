import paho.mqtt.client as mqtt


HOST = '192.168.0.179'
PORT = 1883
KEEP_ALIVE = 60


def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}')

    # client.subscribe('$SYS/#')
    client.subscribe('#')


def on_message(client, userdata, msg):
    '''
    Callback for when a PUBLISH message is received from te server.
    '''
    print(f'{msg.topic} {str(msg.payload)}')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(HOST, PORT, KEEP_ALIVE)

client.loop_forever()
