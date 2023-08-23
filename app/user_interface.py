class UserInterface:
    @staticmethod
    def main_menu():
        print("\nMain Menu:")
        print("1. Create User Profile")
        print("2. Enter Biometric Data and Get Health Diagnosis")
        print("3. Predict Activity Level")
        print("4. Get Health Recommendations")
        print("5. Exit")
        
        choice = int(input("Select an option: "))
        return choice

    @staticmethod
    def create_user_profile():
        user_profile = {}
        print("\nEnter User Profile:")
        user_profile["name"] = input("Name: ")
        user_profile["age"] = int(input("Age: "))
        user_profile["gender"] = input("Gender: ")
        user_profile["health_goals"] = input("Health Goals: ")
        return user_profile

    @staticmethod
    def get_user_id():
        return int(input("\nEnter User ID: "))

    @staticmethod
    def collect_biometric_data():
        biometric_data = {}
        print("\nEnter Biometric Data:")
        biometric_data["heart_rate"] = float(input("Heart Rate: "))
        biometric_data["activity_level"] = float(input("Activity Level: "))
        biometric_data["sleep_duration"] = float(input("Sleep Duration: "))
        return biometric_data

    @staticmethod
    def display_diagnosis(diagnosis):
        print("\nHealth Diagnosis:")
        print("Diagnosis:", diagnosis)

    @staticmethod
    def display_activity_prediction(activity_level):
        print("\nActivity Prediction:")
        print("Predicted Activity Level:", activity_level)

    @staticmethod
    def display_recommendations(recommendations):
        print("\nHealth Recommendations:")
        for idx, recommendation in enumerate(recommendations, start=1):
            print(f"{idx}. {recommendation}")
