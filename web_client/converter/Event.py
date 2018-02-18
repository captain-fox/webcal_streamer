import sys
from web_client.converter.InputConverter import *
from web_client.models import *


class Event:

    @staticmethod
    def import_csv_to_db(schedule):
        InputConverter.check_header(schedule[0], InputConverter.__HEADERS__)
        # Progress bar
        process_title = 'Importing csv data to DB'
        status_bar_length = 50
        spaces = 30 - len(process_title)
        process_title = process_title + ':' + spaces * ' '
        segment = round(len(schedule[1:]) / 100, 1)
        counter = 0

        try:

            for _class in schedule[1:]:
                record = RawCSVEvent(
                    ref=InputConverter.get_ref_from(_class),
                    title=InputConverter.get_class_title_from(_class),
                    time_start=InputConverter.get_start_time_from(_class),
                    time_end=InputConverter.get_end_time_from(_class),
                    room=InputConverter.get_location_from(_class),
                    teacher=InputConverter.get_teacher_from(_class),
                    group=_class[InputConverter.group_column()],
                    weekday=InputConverter.get_week_day_from(_class),
                    semester_weeks=InputConverter.get_weeks_from(_class)
                )
                record.save()

                # Progress bar
                progress = int((counter + 1) / segment)
                bar_fill = status_bar_length / 100 * progress
                sys.stdout.write('\r')
                sys.stdout.flush()
                length_of_buffer = len('{}[{}{}] {}%'.format(process_title, round(bar_fill) * '-',
                                                             (status_bar_length - round(bar_fill)) * ' ', progress))
                sys.stdout.write('{}[{}{}] {}%'.format(process_title, round(bar_fill) * '-',
                                                       (status_bar_length - round(bar_fill)) * ' ', progress))
                sys.stdout.flush()
                counter += 1

        except IndexError:
            sys.stdout.write('\r')
            sys.stdout.write('{} Complete{}\n'.format(process_title, length_of_buffer * ' '))
        except Exception as e:
            print('Unpredicted exception while collecting raw events: {}'.format(e))
