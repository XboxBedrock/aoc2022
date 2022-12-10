import Glibc

var matrix: [[Int]] = [[Int]]()

var line = 0

var topScore = 0;

while let thing = readLine() {
    matrix.append([])
    for char in thing {
        matrix[line].append(char.wholeNumberValue ?? 0)
    }

    line += 1
}

for x in 1...(matrix.count-2) {
    for y in 1...(matrix.count-2) {
        var height = matrix[x][y]
        var left = 0;
        var right = 0;
        var up = 0;
        var down = 0;
        for j in x+1...(matrix.count-1) {
                if (matrix[j][y] >= height) {
                    left+=1
                    break
                }
                left+=1
                
        }
        

        for j in (0...x-1).reversed() {
            if (matrix[j][y] >= height) {
                right+=1
                break
                
            }
            right+=1
        }

        for j in y+1...(matrix.count-1) {
                if (matrix[x][j] >= height) {
                    up+=1
                    break
                }
                up+=1
        }
        

        for j in (0...y-1).reversed() {
            if (matrix[x][j] >= height) {
                down+=1
                break
            }
            down+=1
        }
        
        print(left*right*up*down, x, y, height)

        if (left*right*up*down > topScore) {
            topScore = left*right*up*down
        }

    }
}




print(topScore)