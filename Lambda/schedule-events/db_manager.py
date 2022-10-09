from db_manager_base import DBManagerBase


class DBManager(DBManagerBase):
    def select_events(self, data):
        query = """    
            SELECT
                id
            FROM
                events
            WHERE
                 %(timestamp)s::time- event_timestamp::time < '1 minute'::interval 
            AND
                 %(timestamp)s::time - event_timestamp::time >= '0 minute'::interval 
            AND 
                (
                    (
                        reminder = 'once'
                    AND
                        date_trunc('minute', event_timestamp - schedule_period)::time = date_trunc('minute', %(timestamp)s)::time
                    )
                OR 
                    (
                        reminder = 'periodical'
                    AND 
                        (
                            (
                                schedule_period = '1 week'::interval 
                            AND 
                                extract(dow from timestamp %(timestamp)s) = extract(dow from event_timestamp)
                            )
                        OR 
                            (
                                schedule_period = '1 day'::interval 
                            )
                        OR 
                            (
                                schedule_period = '1 month'::interval 
                            AND 
                                extract(day from timestamp %(timestamp)s) = extract(day from event_timestamp)
                            )
                        )
                    )
                )
        """
        return self.fetch_all(query, data)

