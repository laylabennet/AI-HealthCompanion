import matplotlib.pyplot as plt

class DataVisualization:
    @staticmethod
    def plot_biometric_data(biometric_data):
        # Placeholder logic for plotting biometric data
        heart_rate = biometric_data["heart_rate"]
        activity_level = biometric_data["activity_level"]
        sleep_duration = biometric_data["sleep_duration"]

        labels = ["Heart Rate", "Activity Level", "Sleep Duration"]
        values = [heart_rate, activity_level, sleep_duration]

        plt.bar(labels, values)
        plt.xlabel("Metrics")
        plt.ylabel("Values")
        plt.title("Biometric Data Visualization")
        plt.show()

    @staticmethod
    def plot_recommendations(recommendations):
        # Placeholder logic for plotting recommendations
        plt.figure(figsize=(8, 6))
        for idx, recommendation in enumerate(recommendations, start=1):
            plt.text(0.1, 1 - idx * 0.1, f"{idx}. {recommendation}", fontsize=12)

        plt.axis("off")
        plt.title("Health Recommendations")
        plt.show()
