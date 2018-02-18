from web_client.converter.InputConverter import *
from web_client.models import *


class Event:

    @staticmethod
    def collect_events_for_group(schedule):
        InputConverter.check_header(schedule[0], InputConverter.__HEADERS__)
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

        except Exception as e:
            print('Unpredicted exception while collecting raw events: {}'.format(e))
