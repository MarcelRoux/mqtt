from src.mqtt.mqtt import MQTTClient


def main():
    HOST = ''
    mqttc = MQTTClient(HOST)
    mqttc.sub('#')
    # mqttc.pub('proto/test', 'hello')


if __name__ == '__main__':
    main()
