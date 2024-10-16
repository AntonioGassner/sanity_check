import pokemon as pokemon


def main():
    pokemon1 = pokemon.Pokemon(name='Pokemon roccioso', hp=100, type='roccia', level=10, moves=['move1','move2'], next_evolve=13)

    while(pokemon1.level < 16):
        pokemon1.level_up()



if __name__ == "__main__":
    main()