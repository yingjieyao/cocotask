import argparse
import importlib
from cocotask import ConsumerManager
import logging
import json
import sys

def class_for_name(module_name, class_name, path):
    sys.path.append(path)
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(module_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c

def load_config(path):
	with open(path, 'r') as f:
		config = json.load(f)

	return config


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('config', help = 'define config file path')
	parser.add_argument('module', help = 'define the module name')
	parser.add_argument('consumer', help = 'define the consumer class name')
	parser.add_argument('worker_number', help = 'number of consumers to work', type=int)
	parser.add_argument('--logginglevel', help = 'define logging level')
	parser.add_argument('--modulepath', default = '.', help = 'path to the module. Default to .')

	args = parser.parse_args()

	if args.logginglevel:
	    logging.basicConfig(level=args.logginglevel)

	config = load_config(args.config)

	consumer_class = class_for_name(args.module, args.consumer, args.modulepath)

	manager = ConsumerManager(config, consumer_class, args.worker_number)
	manager.start()


if __name__ == '__main__':  # pragma: no cover
    main()