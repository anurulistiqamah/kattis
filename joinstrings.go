package main

import (
	"fmt"
)

func main() {
	// var size int
	// fmt.Scanln(&size)

	// var arr = make([]string, size)
	// for i := 0; i < size; i++ {
	// 	fmt.Scanln(&arr[i])
	// }
	// fmt.Println("your array", arr)
	var a = 5
	// var p = &a // p holds variable a's memory address
	fmt.Printf("Address of var a: %p\n", &a)
	fmt.Printf("Value of var a: %v\n", *&a)

	// Let's change a value (using the initial variable or the pointer)
	// *p = 3 // using pointer
	a = 3 // using initial var

	fmt.Printf("Address of var a: %p\n", &a)
	fmt.Printf("Value of var a: %v\n", *&a)
}
