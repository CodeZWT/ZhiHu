function ShowTopic(){
	var displayDiv = window.document.getElementById('display_topic');
	displayDiv.style.display = "block";
}
function HideTopic(){
	var displayDiv = window.document.getElementById('display_topic');
	displayDiv.style.display = "none";
}
function getValue(obj)
{
	var id = obj.id;
	var input = window.document.getElementById('inputTopic');
	input.value = document.getElementById(id).innerHTML;
}
function colorHigh(obj){
	var id = obj.id;
	var li = document.getElementById(id);
	li.style.color = "#ff3333";
}
function colorLow(obj){
	var id = obj.id;
	var li = document.getElementById(id);
	li.style.color = "#000000";
}
function ajax_inputTopic(inputText){
		//alert(inputText)
		document.getElementById("ul_topic").innerHTML = "";
		$.ajax({
			type:"POST",
			data:{'inputText':inputText},
			url:"/like/",
			cache:false,
			dataType:"html",
			success:function(data,status,xml){
				data=JSON.parse(data)
				if (data.length){
					//alert(data[0])
					for (var i=0;i<data.length;i++){
						li_id = 'li_'+i;
						str = "<li id='"+li_id+"' onmousedown='getValue(this),HideTopic()'  onmouseover='colorHigh(this)' onmouseout='colorLow(this)'>"+data[i]+"</li>"
						$("#ul_topic").append(str)
						// alert(data[i]);
					}
				}
			},
			error:function(){
				alert('输入数据不存在')
			}
		});
	}
function ask(inputText,topicName){
	$.ajax({
		type:'POST',
		data:{'inputText':inputText,'topicName':topicName},
		url:'/askQuestion/',
		cache:false,
		dataType:'html',
		success:function(){
            window.location.href = '/index' 
		
		},
		error:function(){
			alert('你还没有选择话题呢！')
		}
	});
}