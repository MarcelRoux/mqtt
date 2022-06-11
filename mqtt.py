import paho.mqtt.client as mqtt


class MQTTClass(mqtt.Client):
    '''
    Reference: https://github.com/eclipse/paho.mqtt.python/blob/master/examples/client_sub-class.py
    '''

    def __init__(self, host: str, port: int = 1883, keep_alive: int = 60) -> None:
        super().__init__(self)
        self.host = host
        self.port = port
        self.keep_alive = keep_alive

    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))

    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def publish(self, topic: str, message: str):
        self.publish(topic, message)

    def subscribe(self, topic: str, qos: int = 0):
        self.connect(self.host, self.port, self.keep_alive)
        self.subscribe(topic, qos)

        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc


def main():
    HOST = ''
    mqttc = MQTTClass(HOST)
    mqttc.subscribe('#')


if __name__ == '__main__':
    main()
