from dj_rql.filter_cls import AutoRQLFilterClass
from parking.models import ParkingSpot, ParkingRecord


class ParkingSpotFilterClass(AutoRQLFilterClass):
    MODEL = ParkingSpot


class ParkingRecordFilterClass(AutoRQLFilterClass):
    MODEL = ParkingRecord
    FILTERS = (
        {
            'filter': 'license_plate',
            'source': 'vehicle__license_plate',
        },
    )
