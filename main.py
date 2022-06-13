from src.mqtt.mqtt import MQTTClient


def main():
    HOST = ''
    mqttc = MQTTClient(HOST)
    mqttc.sub('#')


if __name__ == '__main__':
    main()
