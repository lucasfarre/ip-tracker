import math

class MathUtil:
    """
    Taken from http://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
    and adapted to Python
    """
    @staticmethod
    def deg_to_rad(deg):
        return deg * (math.pi/180)

    @staticmethod
    def get_distance_from_latlon_in_km(lat1, lon1, lat2, lon2):
        earth_radius = 6371; # Radius of the earth in km
        d_lat = MathUtil.deg_to_rad(lat2-lat1)
        d_lon = MathUtil.deg_to_rad(lon2-lon1)
        a = math.sin(d_lat/2) * math.sin(d_lat/2) + math.cos(MathUtil.deg_to_rad(lat1)) * math.cos(MathUtil.deg_to_rad(lat2)) * math.sin(d_lon/2) * math.sin(d_lon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = earth_radius * c # Distance in km
        return d
