import kotlin.collections.ArrayList

val monArray: MutableList<Monkey> = ArrayList()

var plsreduce = 1

fun eval(a: String): Long {
    if (a.contains("*")) {
        return a.split(" * ").map { it.toLong() }.toTypedArray().fold(1){acc, i -> acc * i}
    }
    if (a.contains("+")) {
        return a.split(" + ").map { it.toLong() }.toTypedArray().fold(0){acc, i -> acc + i}
    }
    return 0
}

class Monkey(
    var items: MutableList<Long>,
    val op: String,
    val test: Int,
    val t: Int,
    val f: Int,
) {

    

    var inspected: Long = 0

    fun pr() {
        items.forEach(System.out::println)
        println(op)
        println(test)
        println(t)
        println(f)
    }

    fun getItem(item: Long) {
        items.add(item)
    }
    fun testG(): Int {
        return test
    }

    fun funny() {

        for (item in items) {
            val neop = op.replace("old", item.toString())
            val res = eval(neop) % plsreduce
            if (res == 1501L) println(res)
            if (res % test.toLong() == 0L) {
                monArray[t].getItem(res)
            } else {
                monArray[f].getItem(res)
            }
            inspected++;
        }
        items = ArrayList();

    }

    fun insp(): Long {
        return inspected
    }


}



var inputText: String? = readLine()

while (inputText != null) {
    val monkey = inputText!!.split(" ")[1].replace(":", "").toInt()
    val list = readLine()!!.split(": ")[1].split(", ").map { it.toLong() }.toTypedArray().toMutableList()
    val op = readLine()!!.split("Operation: new = ")[1]
    val test = readLine()!!.split("Test: divisible by ")[1].toInt()
    val t = readLine()!!.split("If true: throw to monkey ")[1].toInt()
    val f = readLine()!!.split("If false: throw to monkey ")[1].toInt()

    val monkeyObj = Monkey(list, op, test, t, f)

    monArray.add(monkeyObj)

    readLine()
    inputText = readLine()
}

for (mon in monArray) {
     plsreduce *=   mon.testG();
}

for (i in 1..10000) {
    for (mon in monArray) {
        mon.funny();
    }
}

val monNum: MutableList<Long> = ArrayList()

for (mon in monArray) {
    monNum.add(mon.insp())
}

monNum.sortDescending()

println(monNum[0] * monNum[1])

