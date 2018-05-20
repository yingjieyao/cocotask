# coconut
A framework to help creating multiple Rabbitmq consumers based on Pika

Reasons for creating this framework:
* Minimize the efforts for team members to handcraft the code for exchange/queue handling
* Most usage for Rabbitmq is simple pub/sub on different exchanges/queues (in my case)
* Team members should focus on how to handle messages
* There lacks good mananger tool/lib to handle creating multiple rabbitmq consumers (although it's simple)
* Celery is actually the best one if it supports windows, unfortunately it's not. So we have to use pure rabbitmq and develop our own tool (somewhat similar to Celery)
<hr>

## Test

1. install rabbitmq on local machine (either docker or pure rabbitmq)
2. make sure it's running Python 3.5 above
3. pip install pika
4. pip install -e .
5. now you have coconut setup on your machine. To test, you can go to the ./test folder
   - Run: `python producer_test.py`   (this will post a string to rabbitmq. Code is very simple)
   - In another window, run: `coconut ./config.json consumerlib TestConsumer 4`, and you'll see the consumer starts and process 1 message we just posted.

6. So the key part is how we use coconut command tool. the parameters are:
   - config_path: path to config file
   - module_name: module of your customized customer class
   - class_name: the class name of your own customer class (in the example above, it's consumerlib.TestConsumer, so the module name is consumerlib, the class name is TestConsumer)
   - number of workers: the total number of customer workers

 That's it. Simple and straightforward.
