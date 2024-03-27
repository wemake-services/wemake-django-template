from django.test import TestCase
import logging

class LoggingTest(TestCase):
    """
    Test case for logging functionality.
    """

    def setUp(self):
        """
        Set up the test environment, temporarily adjusting the log level to INFO.
        """
        self.original_log_level = logging.getLogger('your_logger_name').getEffectiveLevel()
        logging.getLogger('your_logger_name').setLevel(logging.INFO)

    def tearDown(self):
        """
        Clean up the test environment by restoring the original log level.
        """
        logging.getLogger('your_logger_name').setLevel(self.original_log_level)

    def test_info_logging(self):
        """
        Test INFO-level logging.
        """
        logger = logging.getLogger('your_logger_name')
        with self.assertLogs(logger, level='INFO') as cm:
            logger.info('This is an info log message')
        self.assertEqual(cm.output, ['INFO:your_logger_name:This is an info log message'])

    def test_warning_logging(self):
        """
        Test WARNING-level logging.
        """
        logger = logging.getLogger('your_logger_name')
        with self.assertLogs(logger, level='WARNING') as cm:
            logger.warning('This is a warning log message')
        self.assertEqual(cm.output, ['WARNING:your_logger_name:This is a warning log message'])

    def test_error_logging(self):
        """
        Test ERROR-level logging.
        """
        logger = logging.getLogger('your_logger_name')
        with self.assertLogs(logger, level='ERROR') as cm:
            logger.error('This is an error log message')
        self.assertEqual(cm.output, ['ERROR:your_logger_name:This is an error log message'])

    def test_critical_logging(self):
        """
        Test CRITICAL-level logging.
        """
        logger = logging.getLogger('your_logger_name')
        with self.assertLogs(logger, level='CRITICAL') as cm:
            logger.critical('This is a critical log message')
        self.assertEqual(cm.output, ['CRITICAL:your_logger_name:This is a critical log message'])

    def test_exception_logging(self):
        """
        Test logging an exception.
        """
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
        """
        Test the custom logger.
        """
        custom_logger = logging.getLogger('custom_logger_name')
        self.assertEqual(custom_logger.name, 'custom_logger_name')
        self.assertEqual(custom_logger.level, logging.DEBUG)

    def test_logging_format(self):
        """
        Test the log message format.
        """
        logger = logging.getLogger('your_logger_name')
        log_message = 'This is a log message with custom formatting: %d'
        with self.assertLogs(logger, level='INFO') as cm:
            logger.info(log_message, 42)
        self.assertEqual(cm.output, ['INFO:your_logger_name:This is a log message with custom formatting: 42'])

    def test_log_handler(self):
        """
        Test the log handler.
        """
        logger = logging.getLogger('your_logger_name')
        log_handler = logger.handlers[0]
        self.assertIsInstance(log_handler, logging.FileHandler)
        self.assertEqual(log_handler.level, logging.INFO)

    def test_logging_config(self):
        """
        Test the logging configuration.
        """
        logger = logging.getLogger('your_logger_name')
        self.assertEqual(logger.level, logging.INFO)
        log_handler = logger.handlers[0]
        self.assertIsInstance(log_handler, logging.FileHandler)
        self.assertEqual(log_handler.level, logging.INFO)
