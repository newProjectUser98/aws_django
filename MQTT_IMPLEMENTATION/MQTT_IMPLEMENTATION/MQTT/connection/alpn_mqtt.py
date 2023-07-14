from __future__ import print_function
import sys
import ssl
import time
import datetime
import logging, traceback
import paho.mqtt.client as mqtt

IoT_protocol_name = "x-amzn-mqtt-ca"
# aws_iot_endpoint = "aiko32o7f20z-ats.iot.eu-north-1.amazonaws.com" # <random>.iot.<region>.amazonaws.com
aws_iot_endpoint = "a2al4qktysi6gi-ats.iot.ap-southeast-1.amazonaws.com" # <random>.iot.<region>.amazonaws.com
url = "https://{}".format(aws_iot_endpoint)

ca = "D:\WaterPro\aws_django\aws_broker_files/testing_CA1.pem"  # Testing
cert = "D:\WaterPro\aws_django\aws_broker_files/testing_certificate.pem.crt"   # Testing 
private = "D:\WaterPro\aws_django\aws_broker_files/testing_private.pem.key"  # Testing

# ca = "D:\WaterPro\aws_django\aws_broker_files/live/Live_RootCA1.pem"  # Live
# cert = "D:\WaterPro\aws_django\aws_broker_files/live/Live_certificate.pem.crt"   # Live 
# private = "D:\WaterPro\aws_django\aws_broker_files/live/Live_private.pem.key"  # Live

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(log_format)
logger.addHandler(handler)

def ssl_alpn():
    try:
        #debug print opnessl version
        logger.info("open ssl version:{}".format(ssl.OPENSSL_VERSION))
        ssl_context = ssl.create_default_context()
        ssl_context.set_alpn_protocols([IoT_protocol_name])
        ssl_context.load_verify_locations(cafile=ca)
        ssl_context.load_cert_chain(certfile=cert, keyfile=private)

        return  ssl_context
    except Exception as e:
        print("exception ssl_alpn()")
        raise e

# if __name__ == '__main__':
#     topic = "test/date"
#     try:
#         mqttc = mqtt.Client()
#         ssl_context= ssl_alpn()
#         mqttc.tls_set_context(context=ssl_context)
#         logger.info("start connect")
#         mqttc.connect(aws_iot_endpoint, port=443)
#         logger.info("connect success")
#         mqttc.loop_start()

#         while True:
#             now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
#             logger.info("try to publish:{}".format(now))
#             mqttc.publish(topic, now)
#             time.sleep(1)
        

#     except Exception as e:
#         logger.error("exception main()")
#         logger.error("e obj:{}".format(vars(e)))
#         logger.error("message:{}".format(e.message))
#         traceback.print_exc(file=sys.stdout)
     
    