require 'set'

head = [0, 0]
tail = [0, 0]
rope = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]

def update_tail(head, tail)
  difference = [head[0]-tail[0],head[1]-tail[1]]
  change_for_tail =Hash[
    '2_1' => [1, 1],
    '1_2' => [1, 1],
    '2_0'=> [1, 0],
    '2_-1'=> [1, -1],
    '1_-2'=> [1, -1],
    '0_-2'=> [0, -1],
    '-1_-2'=> [-1, -1],
    '-2_-1'=> [-1, -1],
    '-2_0'=> [-1, 0],
    '-2_1'=> [-1, 1],
    '-1_2'=>[-1, 1],
    '0_2'=>[0, 1],
    '2_2'=> [1, 1],
    '-2_-2'=> [-1, -1],
    '-2_2'=> [-1, 1],
    '2_-2'=> [1, -1]
  ]

  x = change_for_tail.dig([difference[0],'_' ,difference[1] ].join) || [0, 0]

  new_tail_pos = [tail[0] + x[0], tail[1] + x[1] ]
  return new_tail_pos
end

def update_head(head, direction)
  if direction == 'R'
      head[1] += 1
  elsif direction == 'L'
      head[1] -= 1
  elsif direction == 'U'
      head[0] += 1
  elsif direction == 'D'
      head[0] -= 1
  end
  return head
end

tail_positions = Set[]

ARGF.each do | line |
  num = line.split(" ")[1].to_i
  dir = line.split(" ")[0]

  while num > 0 do
    rope[0] = update_head(rope[0], dir)
    num -= 1
    for i in 1...rope.size do
      rope[i] = update_tail(rope[i-1], rope[i])
    end
    tail_positions.add(rope[9])
  end
end

puts tail_positions.size

