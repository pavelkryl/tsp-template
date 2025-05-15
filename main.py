from dataclasses import dataclass

@dataclass
class Cesta:
    mesta: list[str]
    cas: int


def tsp(graph) -> Cesta:
    """
    Najdi nějakou cestu skrz graf, která projde každé město právě jednou. Krom startovního města kde cesta končí.
    Vrať celkovou délku cesty a cestu jako seznam názvů měst.
    """
    # Sem studenti doplní TSP
    return Cesta([], 0)

def main():
    graph = {
        "A": [("B", 2), ("C", 5)],
        "B": [("A", 2), ("C", 1), ("D", 3)],
        "C": [("A", 5), ("B", 1), ("D", 2), ("E", 3)],
        "D": [("B", 3), ("C", 2), ("E", 1)],
        "E": [("C", 3), ("D", 1), ("F", 5)],
        "F": [("E", 5), ("A", 3) ]
    }

    cesta = tsp(graph)
    
    print(f"Cesta: {' -> '.join(cesta.mesta)}")
    print(f"Cesta je dlouhá: {cesta.cas} hodin")

if __name__ == "__main__":
    main()
