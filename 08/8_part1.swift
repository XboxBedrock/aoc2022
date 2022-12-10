import Glibc

var matrix: [[Int]] = [[Int]]()
var indexes: [[Int]] = [[Int]]()

var line = 0

while let thing = readLine() {
    matrix.append([])
    for char in thing {
        matrix[line].append(char.wholeNumberValue ?? 0)
    }

    line += 1
}


    //right
    var height = [Int](repeating: -1, count: matrix.count)
    for j in 0...(matrix.count-1) {
        for k in 0...(matrix.count-1) {
            if (matrix[j][k] > height[k]) {
                indexes.append([j,k])
                height[k] = matrix[j][k]
            }
        }
    }
    //left
    height = [Int](repeating: -1, count: matrix.count)
    for j in (0...(matrix.count-1)).reversed() {
        for k in 0...(matrix.count-1) {
            if (matrix[j][k] > height[k]) {
                indexes.append([j,k])
                height[k] = matrix[j][k]
            } 
        }
    }
    //top
    height = [Int](repeating: -1, count: matrix.count)
    for j in (0...((matrix.count-1))).reversed() {
        for k in (0...(matrix.count-1)) {
            if (matrix[k][j] > height[k]) {
                indexes.append([k, j])
                height[k] = matrix[k][j]
            }
        }
    }
    //down
    height = [Int](repeating: -1, count: matrix.count)
    for j in (0...(matrix.count-1)) {
        for k in (0...(matrix.count-1)) {
            if (matrix[k][j] > height[k]) {
                indexes.append([k, j])
                height[k] = matrix[k][j]
            }
        }
    }


let unique = Array(Set(indexes))

print(unique)
print(unique.count)