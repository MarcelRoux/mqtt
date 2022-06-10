# MQTT Sample

This repo shows a basic MQTT demonstration through a simple client publisher and a second client subscriber.

## Installation

Best practice is to create a virtual environment, activate it and install:
```
pip install -r requirements.txt
```

## Usage

This example connects to an already running MQTT broker, which is not covered in this example.  
For reference, install Mosquitto broker.

The 2 modules provided include a subscriber and a publisher.

The subscriber subscribes to the provided topic on the broker.  
The publisher publishes to the provided topic on the broker.

The 2 modules need to be run individually.

If the topics align, the subscriber should print the topic and message as published by the publisher.
