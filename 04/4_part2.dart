import 'dart:io';

void main() {

  int total = 0;

  String line = stdin.readLineSync();

  while (line != null) {
    var p1 = line.split(",")[0].split("-").map((e) => int.parse(e)).toList();
    var p2 = line.split(",")[1].split("-").map((e) => int.parse(e)).toList();

    if ((p1[0] <= p2[0]) && (p2[0] <= p1[1]) || (p1[0] <= p2[1]) && (p2[1] <= p1[1]) || (p2[0] <= p1[0]) && (p1[0] <= p2[1]) || (p2[0] <= p1[1]) && (p1[1] <= p2[1])) total++;

    line = stdin.readLineSync();
  }


  print(total);
}