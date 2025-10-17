package main

import "fmt"

//func wish(){
//	fmt.Println("have a nice day")
//}
//func add(a int,b int){
//	fmt.Println(a+b)
//}
//func wish(name string){
//	var message="hello"
//	fmt.Println(message,"good morning",name)
//func math(num1 int,num2 int)(int,int,int){
//	var add=num1+num2
//	var sub=num1-num2
//	var mul=num1*num2
//	return add,sub,mul
//}
func main(){
	//const(
	//	pie=3.14
	//	status=true
	//)
	//const name ="teja"
	//var name,location string= "teja ", " hyd"
	//var age,dob int= 21, 2001
	//name:="teja"
	//age:=90
	//dob:=2001
	//web:="www.google.com"
	//var name="teja"
	//var age =23
	//var age int
	//var name string
	//age=30
	//name="ranga"
	//var rollno int = 45
	//var marks float32=68.56
	//var name string="teja"
	//var isactive bool=true
	//var name1:="teja"
	//var age=23
	//var name="teja"
	//fmt.Print(name," ",age,"\n")
	//fmt.Printf("the value of %v the type of %T",age,name)
	//fmt.Println(name,age)
	//fmt.Print("this is my first golang program")
	//fmt.Print("your rollno is :", rollno, marks, name, isactive)
	//age =70
	//fmt.Print(name , age, dob , web)
	//fmt.Print(name,age,dob,location)
	//fmt.Print(name)
	//fmt.Print(pie,status)
	//a :="hello "
	//b:="world "
	//num1:=1
	//num2:=2
	//fmt.Print(a,b)
	//fmt.Print("\n",num1,num2)
	//a:="hello"
	//b:="world"
	//fmt.Print(a)
	//fmt.Print(b)
	//fmt.Println(a)
	//fmt.Print(b)
	//a:=10
	//fmt.Printf("this is value of %v and type of %T",a,a)
	//a:=10
	//b:=20
	//fmt.Println(a+b)
	//wish()
	//add(10,20)
	//var a="teja"
	//var b="guna"
	//wish(a)
	//wish(b)
//	var a=10
//	var b=20
//	var add,sub,mul=math(a,b)
//	fmt.Println(add,sub,mul)
 //   var name string
//	var age int
//	var salary float32
//	fmt.Println("before",name,age,salary)
//	fmt.Println("enter your name : ")
//	fmt.Scanln(&name)
//	fmt.Println("enter your age :")
//	fmt.Scanln(&age)
//	fmt.Println("enter your salary :")
//	fmt.Scanln(&salary)
//	fmt.Println("after",name,age,salary)
//  var num int
//	fmt.Println("enter the day number : ")
//	fmt.Scanln(&num)
//	switch num%2 {
//	case 0:
//		fmt.Println("even number")
//	case 1:
//		fmt.Println("odd number")
//	default:
//		fmt.Println("invalid input")
//	}
//   var day int
//   fmt.Println("enter day number :")
//  fmt.Scanln(&day)
//    switch day{
//   case 1:
//	fmt.Println("monday")
//   case 2:
//	fmt.Print("tuesday")
//    case 3:
//	fmt.Print("wednesday")
//	 case 4:
//	fmt.Print("thursday")
//	 case 5:
//	fmt.Print("friday")
//	 case 6:
//	fmt.Print("saturday")
//	 case 7:
//	fmt.Print("sunday")
//	 default:
//		fmt.Print("invalid input")
//   }
    var day int
	fmt.Print("enter day number :")
	fmt.Scanln(&day)
	switch day {
	case 1,3,5:
		fmt.Print("odd weekdays")
	case 2,4:
        fmt.Println("even weekdays")
    case 6,7:
	    fmt.Print("weekends")
    default:
	   fmt.Print("invalid input")
	}
}
