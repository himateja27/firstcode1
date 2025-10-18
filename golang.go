package main

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
/*type car struct{
	model string;
	cc int;
	year int;
}*/
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
/*    var day int
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
	}*/
	/*var i int=10
	var j float32=float32(i)
	fmt.Print(j+0.56)*/
	/*var a float32=45.98
	var b int=int(a)
	fmt.Print(b)*/
	/*var n int=2001
	var str string=strconv.Itoa(n)
	fmt.Print(str)*/
	/*var str string="2001bbbb"
	var n, err=strconv.Atoi(str)
	if err==nil{
		fmt.Println("string to int : ",n)
	} else {
		fmt.Println("convert failed : ",err)	
	}*/
	/*var age =17
	if age>18{
		fmt.Print("you are eligible for vote")
	}else{
		fmt.Print("you are not eligible for work")
	}*/
	/*var age=24
	if age<18{
		fmt.Print("you are not eligible to driving licince")
	}else if age>60{
		fmt.Print("you are not eligible to driving licence")
	}else{
		fmt.Print("you are eligible for driving licence")
	}*/
	/*var age = 45
	if age<18{
		if age>60{
			fmt.Print("you are not eligible to licence")
		}else{
			fmt.Print("you are eligible for vote")
		}
	}else{
		fmt.Print("you are eligible for licence")
	}*/
	/*for i:=0; i<=10; i++{
		fmt.Println(i)
		fmt.Println("hi there")
	}*/
	/*for i:=0; i<=10; i++{
		if i==5{
			break
		}
		fmt.Println(i)
	}*/
	/*for i:=0; i<=10; i++{
		if i%2==0{
			continue
		}
		fmt.Println(i)
	}*/
	/*arr :=[...] int{10,20,60,80,25,45}
	arr[0]=100
	//for i=0; i<=len(arr); i++{
		//fmt.Print(arr[i])
		//fmt.Print(arr[5])
		//fmt.Print(len(arr))
		for i:=0; i<=len(arr); i++{
		   fmt.Println(arr[i])
		}*/
    /*variable :=[...] int{10,40,20,5,6,9}
	sort.Ints(variable[:])
	fmt.Print(variable)*/
	/*arr :=[...] string{"a","r","e","f"}
	sort.Strings(arr[:])
	fmt.Print(arr)*/
    /*var s1 =[] int{100,200,300,400,500,600}
	s1=append(s1,700,800)
	fmt.Println(s1)	
	//s1=append(s1[0:2],s1[3: ]...)
	//fmt.Println(s1)
	//for i:=0; i<=len(s1);i++{
	//	fmt.Println(s1[i])
	//}
	for index,value:=range s1{
		fmt.Println(index,value)
	}*/
	/*var s1 = make([]int,5,10)
	fmt.Print(s1,len(s1),cap(s1))
	s1=append(s1,1,2,3,4,5,6,7,8,9,11,12,13,14)
	fmt.Print(s1,len(s1),cap(s1))*/
    /*var bmw car;
	bmw.model="m5"
	bmw.cc=2000
	bmw.year=2025
	bmw.model="m5"
   fmt.Println(bmw.model)
   fmt.Println(bmw.cc)
   fmt.Println(bmw.year)
   var porche car;
   porche.model="911"
   porche.cc=2000
   porche.year=2025
   fmt.Println(porche.model)*/
   /*var myMap = map[string]string{
	"name":"teja","location":"hyd","channel":"youtube"}
	//fmt.Print(myMap["name"])
	fmt.Print(len(myMap))
	for key,value := range myMap{
        fmt.Println("key",key)
		fmt.Println("value",value)
	}*/
}
 
