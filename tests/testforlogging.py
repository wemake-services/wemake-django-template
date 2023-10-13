from django.test import TestCase
import logging

class LoggingTest(TestCase):
    def setUp(self):
        self.original_log_level = logging.getLogger('your_logger_name').getEffectiveLevel()
        logging.getLogger('your_logger_name').setLevel(logging.INFO)  # Temporarily set the log level to INFO

    def tearDown(self):
        logging.getLogger('your_logger_name').setLevel(self.original_log_level)
    def test_info_logging(self):
        logger = logging.getLogger('your_logger_name')
        with self.assertLogs(logger, level='INFO') as cm:
            logger.info('This is an info log message')
        self.assertEqual(cm.output, ['INFO:your_logger_name:This is an info log message'])

    def test_warning_logging(self):
        logger = logging.getLogger('your_logger_name')
        with self.assertLogs(logger, level='WARNING') as cm:
            logger.warning('This is a warning log message')
        self.assertEqual(cm.output, ['WARNING:your_logger_name:This is a warning log message'])

    def test_error_logging(self):
        logger = logging.getLogger('your_logger_name')
        with self.assertLogs(logger, level='ERROR') as cm:
            logger.error('This is an error log message')
        self.assertEqual(cm.output, ['ERROR:your_logger_name:This is an error log message'])

    def test_critical_logging(self):
        logger = logging.getLogger('your_logger_name')
        with self.assertLogs(logger, level='CRITICAL') as cm:
            logger.critical('This is a critical log message')
        self.assertEqual(cm.output, ['CRITICAL:your_logger_name:This is a critical log message'])

    def test_exception_logging(self):
        logger = logging.getLogger('your_logger_name')

        def function_that_logs_exception():
            try:
                1 / 0  
            except ZeroDivisionError:
                logger.error('An error occurred', exc_info=True)

        with self.assertLogs(logger, level='ERROR') as cm:
            function_that_logs_exception()
        self.assertTrue('ERROR:your_logger_name:An error occurred' in cm.output[0])

    def test_custom_logger(self):
        custom_logger = logging.getLogger('custom_logger_name')  
        self.assertEqual(custom_logger.name, 'custom_logger_name')
        self.assertEqual(custom_logger.level, logging.DEBUG)  

    def test_logging_format(self):
        logger = logging.getLogger('your_logger_name')
        log_message = 'This is a log message with custom formatting: %d'
        with self.assertLogs(logger, level='INFO') as cm:
            logger.info(log_message, 42)  
        self.assertEqual(cm.output, ['INFO:your_logger_name:This is a log message with custom formatting: 42'])

    def test_log_handler(self):
        logger = logging.getLogger('your_logger_name')
        log_handler = logger.handlers[0]  
        self.assertIsInstance(log_handler, logging.FileHandler)  
        self.assertEqual(log_handler.level, logging.INFO)  

    def test_logging_config(self):
        logger = logging.getLogger('your_logger_name')
        self.assertEqual(logger.level, logging.INFO)  
        log_handler = logger.handlers[0]  
        self.assertIsInstance(log_handler, logging.FileHandler)  
        self.assertEqual(log_handler.level, logging.INFO)  


