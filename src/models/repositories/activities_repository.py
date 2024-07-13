from typing import Dict, Tuple, List
from sqlite3 import Connection


class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_activitiy(self, activitiy_infos: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO activities
                    (id, trip_id, title, occurs_at)
                VALUES
                    (?, ?, ?)
            ''', (
                activitiy_infos["id"],
                activitiy_infos["trip_id"],
                activitiy_infos["title"],
                activitiy_infos["occurs_at"],
            )
        )
        self.__conn.commit()

    def find_activities_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM activities WHERE trip_id = ?
            ''' , (trip_id,)
        )
        activities = cursor.fetchall()
        return activities


