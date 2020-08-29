
var show_img=document.getElementById("avatar");
var file_input=document.getElementById("file_input");
var set_input_img=document.getElementById("set_input_img")
let cropper;
window.previewFile=function()
{
    let file=file_input.files[0]
    let reader=new FileReader()
    reader.addEventListener("load",function(event){
     	show_img.src=reader.result
    },false)
    if(file){
    	reader.readAsDataURL(file)
    }
}
show_img.addEventListener("load",function(event)
{ cropper=new Cropper(show_img,{
     preview:document.querySelector(".preview_image_upload"),
    aspectRatio:1/1
	});
})
document.getElementById("pre_de").addEventListener("click",function(event){
event.preventDefault();
document.getElementById("dec_sec_profile").value=cropper.getCroppedCanvas({

    width:250,

    }

).toDataURL( );


})
