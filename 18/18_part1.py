def find_exposed_sides(coords):
    exposed_sides = 0
    for coord in coords:
        exposed_sides += 6
        x, y, z = coord
        if (x, y+1, z) in coords: exposed_sides -= 1
        if (x, y-1, z) in coords: exposed_sides -= 1
        if (x+1, y, z) in coords: exposed_sides -= 1
        if (x-1, y, z) in coords: exposed_sides -= 1
        if (x, y, z+1) in coords: exposed_sides -= 1
        if (x, y, z-1) in coords: exposed_sides -= 1

    return exposed_sides


lines = [*map(lambda x: tuple(map(int, x.split(","))), open(0).read().split("\n"))]

print(find_exposed_sides(lines))