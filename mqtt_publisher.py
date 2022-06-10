import paho.mqtt.client as mqtt
import time


HOST = '192.168.0.179'
PORT = 1883
KEEP_ALIVE = 60

TOPIC = 'proto/test'


def on_connect(client, userdata, flags, rc):
    '''
    client:     the client instance for this callback
    userdata:   the private user data as set in Client() or userdata_set()
    flags:      response flags sent by the broker
    rc:         the connection result
    '''
    print(f'Connected with result code {rc}')
    if(rc == 0):
        print(f'Successfully connected to broker (result code {rc})')

    # client.subscribe('$SYS/#')
    # client.subscribe('#')


def on_message(client, userdata, msg):
    '''
    Callback for when a PUBLISH message is received from the server.

    client:     the client instance for this callback
    userdata:   the private user data as set in Client() or userdata_set()
    message:    an instance of MQTTMessage.
                This is a class with members topic, payload, qos, retain.
    '''
    print(f'{msg.topic} {str(msg.payload)}')


def on_publish(client, userdata, mid):
    '''
    Callback for when a PUBLISH message is sent from the client.

    client:     the client instance for this callback
    userdata:   the private user data as set in Client() or userdata_set()
    mid:        matches the mid variable returned from the corresponding
                publish() call, to allow outgoing messages to be tracked.
    '''
    # print(f'{msg.topic} {str(msg.payload)}')
    print(f'{mid}')


client = mqtt.Client()
client.on_connect = on_connect
# client.on_message = on_message
# client.on_publish = on_publish

client.connect(HOST, PORT, KEEP_ALIVE)

# client.loop_forever()


def main():
    i = 0
    while True:
        msg = f'msg {i}'
        client.publish(topic=TOPIC,
                       payload=msg)
        time.sleep(1)
        i += 1


if __name__ == '__main__':
    main()
