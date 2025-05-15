class Graph:
    
    def new_edge(self, from_city: str, to_city: str, distance: int) -> None:
        ...

    def find_shortest_path(self, from_city: str, to_city: str) -> int:
        ...
