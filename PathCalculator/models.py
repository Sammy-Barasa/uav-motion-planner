from django.db import models


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()

    def __str__(self):
        return f"[{self.latitude}, {self.longitude}, {self.altitude}]"


class Obstacle(models.Model):
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    obstacle_data = models.JSONField()

    def __str__(self):
        return f"{self.description} - {self.obstacle_data}"
    
class HiddenObstacle(models.Model):
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    hidden_obstacle_data = models.JSONField()

    def __str__(self):
        return f"{self.description} - {self.hidden_obstacle_data}"


class DroneFlight(models.Model):
    start_location = models.ForeignKey(Location, related_name='start_flights', on_delete=models.CASCADE)
    end_location = models.ForeignKey(Location, related_name='end_flights', on_delete=models.CASCADE)
    locations = models.ManyToManyField(Location, related_name='drone_flights', blank=True)
    obstacles = models.ManyToManyField(Obstacle, related_name='drone_flights', blank=True)

    def __str__(self):
        return f"Drone Flight from {self.start_location} to {self.end_location}"

class DroneFlightPath(models.Model):
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    flight_data_path = models.JSONField()
    start = models.JSONField()
    end = models.JSONField()
    date_field = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.description}: Flight from {self.start} to {self.end}"
    
