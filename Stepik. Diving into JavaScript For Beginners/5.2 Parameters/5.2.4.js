let p = +prompt()
let p1 = +prompt()
let p2 = +prompt()
let p3 = +prompt()
function compareAndPrintMax (n,n1,n2,n3) {
    if (n > n1 && n > n2 && n > n3) {
        console.log(n)
    } else if (n1 > n2 && n1 > n3 && n1 > n) {
        console.log(n1)
    } else if (n2 > n && n2 > n1 && n2 > n3) {
        console.log(n2)
    } else if (n3 > n1 && n3 > n2 && n3 > n) {
        console.log(n3)
    }
}
compareAndPrintMax(p,p1,p2,p3)