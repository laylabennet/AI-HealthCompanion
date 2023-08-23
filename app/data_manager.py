import json

class DataManager:
    def __init__(self):
        self.user_profiles_file = "data/user_profiles.json"
        self.biometric_data_file = "data/biometric_data.json"
        self.health_recommendations_file = "data/health_recommendations.json"

    def load_user_profiles(self):
        try:
            with open(self.user_profiles_file, "r") as file:
                user_profiles = json.load(file)
        except FileNotFoundError:
            user_profiles = {}
        return user_profiles

    def save_user_profile(self, user_profile):
        user_profiles = self.load_user_profiles()
        user_id = len(user_profiles) + 1
        user_profiles[user_id] = user_profile
        with open(self.user_profiles_file, "w") as file:
            json.dump(user_profiles, file, indent=4)

    def load_biometric_data(self):
        try:
            with open(self.biometric_data_file, "r") as file:
                biometric_data = json.load(file)
        except FileNotFoundError:
            biometric_data = {}
        return biometric_data

    def save_biometric_data(self, user_id, biometric_data):
        biometric_data_dict = self.load_biometric_data()
        if user_id not in biometric_data_dict:
            biometric_data_dict[user_id] = []
        biometric_data_dict[user_id].append(biometric_data)
        with open(self.biometric_data_file, "w") as file:
            json.dump(biometric_data_dict, file, indent=4)

    def load_health_recommendations(self):
        try:
            with open(self.health_recommendations_file, "r") as file:
                health_recommendations = json.load(file)
        except FileNotFoundError:
            health_recommendations = {}
        return health_recommendations

    def save_health_recommendations(self, user_id, recommendations):
        health_recommendations_dict = self.load_health_recommendations()
        health_recommendations_dict[user_id] = recommendations
        with open(self.health_recommendations_file, "w") as file:
            json.dump(health_recommendations_dict, file, indent=4)
