class AnalysisRegion:
    def __init__(self, region_name, south, north, east, west):
        self._region_name = region_name
        self._south = south
        self._north = north
        self._east = east
        self._west = west

    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, value):
        self._region_name = value

    @property
    def south(self):
        return self._south

    @south.setter
    def south(self, value):
        self._south = value

    @property
    def north(self):
        return self._north

    @north.setter
    def north(self, value):
        self._north = value

    @property
    def east(self):
        return self._east

    @east.setter
    def east(self, value):
        self._east = value

    @property
    def west(self):
        return self._west

    @west.setter
    def west(self, value):
        self._west = value

    @property
    def lat_lon_slices(self):
        return {
            'lat': slice(self.south, self.north),
            'lon': slice(self.west, self.east),
        }

    def __repr__(self):
        return f"{self.region_name}(south={self.south}, north={self.north}, east={self.east}, west={self.west})"

# Define specific regions as children
class EquatorialIndianOcean(AnalysisRegion):
    def __init__(self):
        """
        Initialize Equatorial Indian Ocean with predefined latitudes and longitudes:
        Latitude: -5 to 5, Longitude: 60 to 90
        """
        super().__init__(region_name='EquatorialIndianOcean', south=-5, north=5, east=90, west=60)

    def __repr__(self):
        return f"{self.region_name}(south={self.south}, north={self.north}, east={self.east}, west={self.west})"

class Congo(AnalysisRegion):
    def __init__(self):
        super().__init__(region_name='Congo', south=-5, north=5, east=45, west=15)

    def __repr__(self):
        return f"{self.region_name}(south={self.south}, north={self.north}, east={self.east}, west={self.west})"
