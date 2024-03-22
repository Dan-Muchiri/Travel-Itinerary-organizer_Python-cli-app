
from helpers import (
    exit_program,
    list_trips,
    find_trip_by_name,
    find_trip_by_id,
    create_trip,
    update_trip,
    delete_trip,
    get_duration,
    get_description,
    get_destinations,
    add_destination,
    find_destination_by_name,
    find_destination_by_id,
    delete_destination,
    update_destination,
    get_accommodations,
    list_destinations,
    find_most_expensive_accommodation,
    find_cheapest_accommodation,
    list_accommodations,
    find_accommodation_by_id,
    find_accommodation_by_name,
    add_accommodation,
    delete_accommodation,
    update_accommodation,
    get_notes,
    get_five_cheapest_accommodations,
    get_five_most_expensive_accommodations,
    list_activities,
    find_activity_by_id,
    find_activity_by_name,
    create_activity,
    update_activity,
    delete_activity,
    get_activities
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            trips_menu()
            handle_trips_menu()
        elif choice == "2":
            destinations_menu()
            handle_destinations_menu()
        elif choice == "3":
            accommodations_menu()
            handle_accommodations_menu()
        elif choice == "4":
            activities_menu()
            handle_activities_menu()
        else:
            print("Invalid choice")

def handle_trips_menu():
    while True:
        choice = input("Trips Menu > ")
        if choice == "0":
            return
        elif choice == "5":
            list_trips()
        elif choice == "6":
            find_trip_by_name()
        elif choice == "7":
            find_trip_by_id()
        elif choice == "8":
            get_description()
        elif choice == "9":
            get_duration()
        elif choice == "10":
            get_destinations()
        elif choice == "11":
            create_trip()
        elif choice == "12":
            update_trip()
        elif choice == "13":
            delete_trip()
        else:
            print("Invalid choice")

def handle_destinations_menu():
    while True:
        choice = input("Destinations Menu > ")
        if choice == "0":
            return
        elif choice == "14":
            list_destinations()
        elif choice == "15":
            add_destination()
        elif choice == "16":
            find_destination_by_name()
        elif choice == "17":
            find_destination_by_id()
        elif choice == "18":
            get_accommodations()
        elif choice == "19":
            get_activities()
        elif choice == "20":
            find_most_expensive_accommodation()
        elif choice == "21":
            find_cheapest_accommodation()
        elif choice == "22":
            update_destination()
        elif choice == "23":
            delete_destination()
        else:
            print("Invalid choice")

def handle_accommodations_menu():
    while True:
        choice = input("Accommodations Menu > ")
        if choice == "0":
            return
        elif choice == "24":
            list_accommodations()
        elif choice == "25":
            add_accommodation()
        elif choice == "26":
            find_accommodation_by_name()
        elif choice == "27":
            find_accommodation_by_id()
        elif choice == "28":
            get_notes()
        elif choice == "29":
            get_five_most_expensive_accommodations()
        elif choice == "30":
            get_five_cheapest_accommodations()
        elif choice == "31":
            update_accommodation()
        elif choice == "32":
            delete_accommodation()
        else:
            print("Invalid choice")

def handle_activities_menu():
    while True:
        choice = input("Activities Menu > ")
        if choice == "0":
            return
        elif choice == "33":
            list_activities()
        elif choice == "34":
            create_activity()
        elif choice == "35":
            find_activity_by_name()
        elif choice == "36":
            find_activity_by_id()
        elif choice == "37":
            update_activity()
        elif choice == "38":
            delete_activity()
        else:
            print("Invalid choice")



def menu():
    print("")
    print("***************Welcome to the travel itinerary organizer!***************")
    print("***********************Browse your planned trips!***********************")
    print("*****************Trips have many destinations to visit!*****************")
    print("*The destinations have many accomodations to stay and activities to do!*")
    print("")
    print("********Menu********")
    print("Please select an option:")
    print("1: Trips Menu")
    print("2: Destinations Menu")
    print("3: Accommodations Menu")
    print("4: Activities Menu")
    print("0: Exit program")
    
def trips_menu():
    print("")
    print("********Trips********")
    print("Please select an option:")
    print("5. List all available trips")
    print("6. Find a trip by it's name")
    print("7. Find a trip by it's id")
    print("8: Get a trip's description")
    print("9: Get a trip's duration")
    print("10: Get a trip's all destinations")
    print("11: Create a new trip")
    print("12: Update an existing trip")
    print("13: Delete an existing trip")
    print("0: Return to Main Menu")

def destinations_menu():
    print("")
    print("*****Destinations*****")
    print("Please select an option:")
    print("14: List all available destinations")
    print("15: Add a new destination")
    print("16. Find a destination by it's name")
    print("17. Find a destination by it's id")
    print("18: Get a destination's all activities")
    print("19: Get a destination's all accommodations")
    print("20: Find a destination's most expensive accommodation")
    print("21: Find a destination's cheapest accommodation")
    print("22: Update an existing destination")
    print("23: Delete an existing destination")
    print("0: Return to Main Menu")

def accommodations_menu():
    print("")
    print("****Accommodations****")
    print("Please select an option:")
    print("24: List all available accommodations")
    print("25: Add a new accommodation")
    print("26. Find an accommodation by it's name")
    print("27. Find an accommodation by it's id")
    print("28: Get an accommodation's notes")
    print("29: List the top 5 most expensive accommodations")
    print("30: List the top 5 cheapest accommodations")
    print("31: Update an existing accommodation")
    print("32: Delete an existing accommodation")
    print("0: Return to Main Menu")

def activities_menu():
    print("")
    print("*****Activities*****")
    print("Please select an option:")
    print("33: List all available activities")
    print("34: Add a new activity")
    print("35. Find an activity by it's name")
    print("36. Find an activity by it's id")
    print("37: Update an existing activity")
    print("38: Delete an existing activity")
    print("0: Return to Main Menu")


if __name__ == "__main__":
    main()