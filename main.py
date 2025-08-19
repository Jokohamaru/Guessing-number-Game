import guessing

def main():
    print("""
    Welcome to the Number guessing Game!!!
    I'm thinking of a number between 2 number from 0.""")
    
    # Choosing difficult level
    while(True):
        print("1. EASY (10 chances and choosing f3rom 1 to 100)")
        print("2. MEDIUM (5 chances and choosing from 1 to 100)")
        print("3. HARD (3 chances and choosing form 1 to 100)")
        print("4. HELL (20 chances and choosing from 1 to any number (<1000000)) (IN PROGRESS)")
        print("5. --EXIT--")

        user_selection_level = int(input("Enter your selection: "))
        match user_selection_level:
            case 1:
                guessing.playing(10,100)
            case 2:
                guessing.playing(5,100)
            case 3:
                guessing.playing(3,100)
            case 4:
                guessing.playing(20,1000000)
            case 5:
                break

    
if __name__ == "__main__":
    main()