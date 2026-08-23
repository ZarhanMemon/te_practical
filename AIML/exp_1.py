# Experiment 1:

# Simple Reflex Agent -for Smart Home Automation

class SmartHomeAgent:

    def __init__(self):
        self.temperature = 24       
        self.motion_detected = False      # for to identify human presence by motion sensors
        self.smoke_detected = False       # for to identify smoke by smoke detectors
        self.light_level = "low"

    def sense(self, sensors):
        self.temperature = sensors.get("temperature", self.temperature)
        self.motion_detected = sensors.get("motion", False)
        self.smoke_detected = sensors.get("smoke", False)
        self.light_level = sensors.get("light", "low")

    def think(self):

        actions = []

        # Temperature control idea
        if self.temperature > 25:
            actions.append("Turn on AC")
        elif self.temperature < 22:
            actions.append("Turn on Heater")

        # Safety idea
        if self.smoke_detected:
            actions.append("Trigger Alarm")

        # Lighting automation idea
        if self.motion_detected and self.light_level == "low":
            actions.append("Turn on Lights")

        return actions

    def act(self, actions):
        for action in actions:
            print(f"Executing: {action}")


# Example run
agent = SmartHomeAgent()
sensor_data = {"temperature": 24, "motion": False, "smoke": True, "light": "high"}
agent.sense(sensor_data)
actions = agent.think()
agent.act(actions)




# Smart Home Controller Agent

# 1. PEAS Representation

# -> Performance Measure (P):
#        Maintain comfortable room temperature (22–25°C).
#        Minimize energy consumption.
#        Ensure safety (e.g., detect fire/smoke).
#        Respond quickly to user commands.


# -> Environment (E):
#        Smart home with devices: thermostat, lights, fans, security cameras, smoke detectors.
#        External factors: weather, time of day, occupancy.

# -> Actuators (A):
#        Thermostat (heat/cool).
#        Smart lights (on/off, brightness).
#        Smart plugs (on/off appliances).
#        Alarm system (trigger alerts).
#        Door locks.

# -> Sensors (S):
#        Temperature sensors.
#        Motion detectors.
#        Smoke sensors.
#        Light sensors.
#        User input via mobile app/voice assistant.