import logging
import datetime

def elapsed_time(start_time, end_time):
	
	elapsed_time_seconds = "Elapsed time was %g seconds" % (end_time - start_time)
	elapsed_time_minutes = "Elapsed time was %g minutes" % int((end_time - start_time)/60)
	elapsed_time_hours = "Elapsed time was %g hours" % int((end_time - start_time)/3600)
	
	return elapsed_time_seconds, elapsed_time_minutes, elapsed_time_hours


def get_logger(logger_count):

	# if logger_count != 0:
	# 	logging.handlers[0].stream.close()
	# 	logging.removeHandler(logger.handlers[0])

	# Set up logging to file
    logging.basicConfig(level = logging.ERROR,
                        format = '%(message)s',
                        datefmt = '%m-%d %H:%M',
                        filename = "./outputs/output" + str(logger_count) +  ".log",
                        filemode = 'w')

    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console) # Add the handler to the root logger

def log_error(error):

	f = open("./errors.txt", 'a')	
	f.write(str(datetime.datetime.now()) + " - " + str(error) + "\n")
	f.close()
