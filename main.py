from load_csv import load_csv


def main():
    nationalites_pays = load_csv("nationalites_pays")
    championnats = load_csv("championnats")
    clubs = load_csv("clubs")
    return  # nb de joueurs par équipe : 22-25 pour EN et ES, 22-36 sinon


if __name__ == '__main__':
    main()
