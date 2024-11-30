from e_learning_environment import E_Learning_Environment
from platform_admin import PlatformAdmin

if __name__ == "__main__":
    try:
        # Initialize the PlatformAdmin and load data
        platform_admin = PlatformAdmin()
        platform_admin.load_data('data.json')  # Ensure this method exists and works correctly

        # Initialize the E-Learning Environment
        e_learning_system = E_Learning_Environment()
        e_learning_system.platform_admin = platform_admin  # Set the loaded data to the environment

        e_learning_env = E_Learning_Environment()
        e_learning_env.set_courses(platform_admin.courses)

        
        # Start the main menu
        e_learning_system.main_menu()
    
    except FileNotFoundError:
        print("Error: The data file 'data.json' was not found.")
    except ValueError as ve:
        print(f"Data error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")