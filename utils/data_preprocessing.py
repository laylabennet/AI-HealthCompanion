class DataPreprocessing:
    @staticmethod
    def normalize_biometric_data(biometric_data):
        # Placeholder logic for normalizing biometric data
        normalized_data = {}
        normalized_data["heart_rate"] = (biometric_data["heart_rate"] - 60) / 30
        normalized_data["activity_level"] = biometric_data["activity_level"]
        normalized_data["sleep_duration"] = (biometric_data["sleep_duration"] - 6) / 2
        return normalized_data

    @staticmethod
    def preprocess_user_profile(user_profile):
        # Placeholder logic for preprocessing user profile
        processed_profile = {}
        processed_profile["age"] = user_profile["age"]
        processed_profile["gender"] = user_profile["gender"]
        processed_profile["health_goals"] = user_profile["health_goals"].split(", ")
        return processed_profile
