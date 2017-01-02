window.onload=function()
{
    var odiv1=document.getElementById('div1');
    var odiv2=document.getElementById('div2');
    var timer=null;
    
    div2.onmouseover=odiv1.onmouseover=function()
    {
        clearTimeout(timer);//来回移动
        odiv2.style.display='block';
        odiv1.style.background='#EAEAEA';
    }
    div2.onmouseout=div1.onmouseout=function()
    {
        timer=setTimeout(function(){
            odiv2.style.display='none';
            odiv1.style.background='#eee';
        },500)
        
    }
};