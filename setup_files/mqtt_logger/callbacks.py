import json
from mqtt_logger.log_data import add_sensors_reading_record


# Callbacks for Paho
def on_connect(client, userdata, flags, rc):
    """ "Generic on_connect function."""
    print("Connected with result code " + str(rc))
    client.subscribe("#")  # Subscribe to all topics


def on_message(client, userdata, msg):
    """Generic on_message function."""
    print(f"Topic: {msg.topic} Message: {str(msg.payload.decode())}")


def log_sensor_data(client, userdata, msg):
    """Provides callback for logging sensor_data."""
    global session
    session = session
    topic = msg.topic
    parsed_packet = json.loads(msg.payload.decode("utf-8"))
    measurements = parsed_packet["data"]
    sensor = parsed_packet["sensor"]
    print(f"Topic: {msg.topic} Message: {str(msg.payload.decode())}")
    add_sensors_reading_record(
        session=session, measurements=measurements, sensor=sensor, topic=topic
    )