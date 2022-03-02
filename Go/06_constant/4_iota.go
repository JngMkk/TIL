package main

/*
const (
	Red int = iota -> 0
	Blue int = iota -> 1
	Green int = iota -> 2
)

const (
	C1 uint = iota + 1 -> 1
	C2 		=		   -> 2
	C3 		=		   -> 3
)

비트플래그
const (
	BitFlag1 uint = 1 << iota -> 1 "0000 0001"
	Bitflag2	  =			  -> 2 "0000 0010"
	Bitflag3	  =			  -> 4 "0000 0100"
	Bitflag4	  =			  -> 8 "0000 1000"
)
*/

import "fmt"

type Room uint8

const (
	MasterRoom Room = 1 << iota
	BathRoom
	Kitchen
	LivingRoom
)

func SetLight(rooms, room Room) Room {
	return rooms | room
}

func ResetLight(rooms, room Room) Room {
	return rooms &^ room
}

func IsTurnon(rooms, room Room) bool {
	return rooms&room == room
}

func TurnonLights(rooms Room) {
	if IsTurnon(rooms, MasterRoom) {
		fmt.Println("Turn on MasterRoom Light")
	}
	if IsTurnon(rooms, BathRoom) {
		fmt.Println("Turn on BathRoom Light")
	}
	if IsTurnon(rooms, Kitchen) {
		fmt.Println("Turn on Kitchen Light")
	}
	if IsTurnon(rooms, LivingRoom) {
		fmt.Println("Turn on LivingRoom Light")
	}
}

func main() {
	var rooms Room = 0
	rooms = SetLight(rooms, MasterRoom)
	rooms = SetLight(rooms, LivingRoom)
	TurnonLights(rooms)
}
