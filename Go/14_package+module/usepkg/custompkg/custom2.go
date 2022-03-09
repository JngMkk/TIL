package custompkg

func Print2() {
	PrintCustom() // 같은 패키지 경로 안에 있기 때문에 바로 호출 가능(import 안해도 됨)
}
