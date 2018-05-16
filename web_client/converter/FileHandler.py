import sys
import csv
from datetime import timedelta
from web_client.converter.InputConverter import *


class FileHandler:

    @staticmethod
    def read_csv_file(file_name, headers_dictionary):

        csv_rows = []
        try:
            with open(file_name, 'rt', encoding='windows 1250') as csv_input:
                reader = csv.reader(csv_input, delimiter=';')
                for row in reader:
                    csv_rows.append(row)
                # Checking headers
            InputConverter.check_header(csv_rows[0], headers_dictionary)
            print('Working on file: {}\n'.format(file_name))

            return csv_rows

        except FileNotFoundError:
            print('File you\'re trying to read does not exist.')
            # sys.exit(0)
        except UnicodeDecodeError:
            print('It\'s not even a text file!')
            # sys.exit(0)
        except ValueError:
            print('Not all headers found')
        except Exception as e:
            print('Unexpected type of exception: "{}" occurred in read_csv_file method.'.format(e))
            sys.exit(0)

    @staticmethod
    def create_and_prepare_file(group):

        file_name = (group + '.ics')
        try:
            newfile = open(file_name, 'w')
            newfile.write('BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n\n')
            newfile.close()

            return file_name

        except FileNotFoundError:
            print('File does not exist.')
            sys.exit(0)
        except UnicodeDecodeError:
            print('It\'s not even a text file!')
            sys.exit(0)
        except Exception as e:
            print('Unexpected type of exception: "{}" occurred in create_and_prepare_file method.'.format(e))
            sys.exit(0)

    @staticmethod
    def add_to_existing_ics(converter, events, term, output):

        for event in events:
            week_num = 1
            print('\n\n', 'Week number: ', week_num, '\n\n')
            date_counter = term.term_start
            while date_counter <= term.term_end:

                if date_counter == term.holidays_start:
                    print('\n\n')
                    print(date_counter)
                    print('Holidays')
                    # week_num += 1
                    date_counter = term.holidays_end + timedelta(days=1)
                    print(date_counter)
                    print('\n\n')
                    continue

                if date_counter.weekday() == 6:
                    week_num += 1
                    print('\n\n', 'Week number: ', week_num, '\n\n')

                if date_counter.weekday() == event.week_day and week_num in event.weeks:
                    converter(event, date_counter, output)

                date_counter += timedelta(days=1)

    @staticmethod
    def finalise_file(file_name):

        output_file = open(file_name, 'a')
        output_file.write('END:VCALENDAR')
        output_file.close()

    @staticmethod
    def is_even_week(i):
        if i % 2 == 0:
            print('Week x2')
        else:
            print('Week x1')
