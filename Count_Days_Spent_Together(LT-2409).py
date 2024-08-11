from datetime import datetime

class Solution:
    def countDaysTogether(self, Alice_A: str, Alice_L: str, Bob_A: str, Bob_L: str) -> int:
        date_format = "%m-%d"

        # Parse the date strings into datetime objects
        Alice_A_date = datetime.strptime(Alice_A, date_format)
        Alice_L_date = datetime.strptime(Alice_L, date_format)
        Bob_A_date = datetime.strptime(Bob_A, date_format)
        Bob_L_date = datetime.strptime(Bob_L, date_format)

        # Find the latest arrival date and the earliest departure date
        latest_arrival = max(Alice_A_date, Bob_A_date)
        earliest_departure = min(Alice_L_date, Bob_L_date)

        # Calculate the number of overlapping days
        if latest_arrival <= earliest_departure:
            overlap = (earliest_departure - latest_arrival).days + 1
            return overlap
        else:
            return 0
