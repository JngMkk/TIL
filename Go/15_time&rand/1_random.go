package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	t := time.Now()         // random seed를 변화시키기 위해
	rand.Seed(t.UnixNano()) // UnixNano() -> Time structure를 int64로 변환
	for i := 0; i < 10; i++ {
		fmt.Println(rand.Intn(100)) // 0 ~ 99 랜덤값
	}
}

// 같은 값이 나온다 so, seed 조정 해줘야 함
// seed도 고정이다 -> 어떻게 랜덤하게?
// 프로그램 실행시마다 계속 변화하는 값

// time 패키지
// 시각을 나타내는 Time 객체
// 시간을 나타내는 Duration 객체
// 타임존을 나타내는 Location
