//엘리먼트들에 대한 데이터를 테이블 형식으로 화면에 표현하기

function makeTable(elem){
	var $table = $("<table border=1>");
	
	//컬럼 정의하기
	for(var i =0; i<1;i++){
		var $tr=$("<tr>");
		for(var j=0; j<elem.eq(0).children().length;j++){
			var $td=$("<td>").append(elem.eq(0).children().eq(j).prop("tagName"));
			$tr.append($td);
		}
		$table.append($tr);
	}
	//데이터 넣기
	for(var i =0; i<elem.length;i++){
		var $tr=$("<tr>");
		for(var j=0; j<elem.eq(i).children().length;j++){
			var $td=$("<td>").append(elem.eq(i).children().eq(j).text());
			$tr.append($td);
		}
		$table.append($tr);
	}
	
	//만들어진 테이블 반환
	return $table;
}