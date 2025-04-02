let x = 5
let y
var z = 4
let c

function myFunc() {
    c = 9
    var z = 7
    function func2() {
        y = 6
    }
    console.log(x)
    func2()
}

myFunc()

console.log(y)
console.log(z)
console.log(c)


const marks = (marks, nums) => marks + nums + 2

console.log(marks(12, 5))