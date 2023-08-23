from user_interface import UserInterface
from data_manager import DataManager
from models.health_diagnosis_model import HealthDiagnosisModel
from models.activity_prediction_model import ActivityPredictionModel
from models.recommendation_model import RecommendationModel

def main():
    print("Welcome to AI Health Companion!")
    
    user_interface = UserInterface()
    data_manager = DataManager()
    diagnosis_model = HealthDiagnosisModel()
    activity_model = ActivityPredictionModel()
    recommendation_model = RecommendationModel()

    while True:
        user_choice = user_interface.main_menu()

        if user_choice == 1:
            user_profile = user_interface.create_user_profile()
            data_manager.save_user_profile(user_profile)

        elif user_choice == 2:
            user_id = user_interface.get_user_id()
            biometric_data = user_interface.collect_biometric_data()
            data_manager.save_biometric_data(user_id, biometric_data)

            diagnosis = diagnosis_model.predict_health_condition(biometric_data)
            user_interface.display_diagnosis(diagnosis)

        elif user_choice == 3:
            user_id = user_interface.get_user_id()
            activity_level = activity_model.predict_activity_level()
            user_interface.display_activity_prediction(activity_level)

        elif user_choice == 4:
            user_id = user_interface.get_user_id()
            recommendations = recommendation_model.generate_recommendations(user_id)
            user_interface.display_recommendations(recommendations)

        elif user_choice == 5:
            print("Exiting AI Health Companion.")
            break

if __name__ == "__main__":
    main()
