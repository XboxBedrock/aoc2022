import kotlin.collections.ArrayList

val monArray: MutableList<Monkey> = ArrayList()

fun eval(a: String): Int {
    if (a.contains("*")) {
        return a.split(" * ").map { it.toInt() }.toTypedArray().fold(1){acc, i -> acc * i}
    }
    if (a.contains("+")) {
        return a.split(" + ").map { it.toInt() }.toTypedArray().fold(0){acc, i -> acc + i}
    }
    return 0
}

class Monkey(
    var items: MutableList<Int>,
    val op: String,
    val test: Int,
    val t: Int,
    val f: Int,
) {

    

    var inspected: Int = 0

    fun pr() {
        items.forEach(System.out::println)
        println(op)
        println(test)
        println(t)
        println(f)
    }

    fun getItem(item: Int) {
        items.add(item)
    }

    fun funny() {

        for (item in items) {
            val neop = op.replace("old", item.toString())
            val res = eval(neop).toString().toInt() / 3
            if (res % test == 0) {
                monArray[t].getItem(res)
            } else {
                monArray[f].getItem(res)
            }
            inspected++;
        }
        items = ArrayList();

    }

    fun insp(): Int {
        return inspected
    }


}



var inputText: String? = readLine()

while (inputText != null) {
    val monkey = inputText!!.split(" ")[1].replace(":", "").toInt()
    val list = readLine()!!.split(": ")[1].split(", ").map { it.toInt() }.toTypedArray().toMutableList()
    val op = readLine()!!.split("Operation: new = ")[1]
    val test = readLine()!!.split("Test: divisible by ")[1].toInt()
    val t = readLine()!!.split("If true: throw to monkey ")[1].toInt()
    val f = readLine()!!.split("If false: throw to monkey ")[1].toInt()

    val monkeyObj = Monkey(list, op, test, t, f)

    monArray.add(monkeyObj)

    readLine()
    inputText = readLine()
}

for (i in 1..20) {
    for (mon in monArray) {
        mon.funny();
    }
}

val monNum: MutableList<Int> = ArrayList()

for (mon in monArray) {
    monNum.add(mon.insp())
}

monNum.sortDescending()

println(monNum[0] * monNum[1])

