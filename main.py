import interface
import database


# Working on now:
# Allow users to select up to six mons.
# Store chosen monsters somewhere
# store monsters in db that have already been Get-ted
# Store a person's particular team? For this I will need to get a username


def main():
    print("\nStrong Pokémon, weak Pokémon, that is only the foolish perception of people. Truly skilled trainers should try to win with their favorites.\n\n")
    database.init_db()
    interface.start_interface()



if __name__ == "__main__":
    main()