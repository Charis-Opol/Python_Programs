def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1: 
        print(f"Move disk 1 from the source {source} to the destination {destination}")
        return 
    
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from the source {source} to the destination {destination}")
    TowerOfHanoi(n-1, auxiliary, destination, source)

n = 4
TowerOfHanoi(n, 'A', 'B', 'C')