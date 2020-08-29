
$(document).on('click', '.add-form-row', function (e) {
        e.preventDefault();

        var Total_Forms = parseInt($(".method_form_1").find("#id_step2-TOTAL_FORMS").val());



        if(Total_Forms<=3){
            var clone_row = $(".form-row-local:last").clone(false).get(0);
            $(clone_row).removeAttr("id").hide().insertAfter(".form-row-local:last").slideDown(300);
            $(clone_row).children().removeClass(".error");
            $(clone_row).find(".form-field-input").each(
                function () {

                    var regular_exp = new RegExp('(' + 'step2' + '-\\d+-)');
                    var replacement = "step2-" + Total_Forms + "-";
                    if ($(this).attr("for")) $(this).attr("for", $(this).attr("for").replace(regular_exp, replacement));
                    if (this.id) this.id = this.id.replace(regular_exp, replacement);
                    if (this.name) this.name = this.name.replace(regular_exp, replacement);
                     $(this).val("")
                    $(this).removeAttr('value');

                     return true


                }
            );


            $(".form-row-local").find(".delete-form-row").click(
                function (event) {
                    event.preventDefault();

                    Total_Forms = $(".form-row-local").length;
                    if (Total_Forms > 1) {

                        $(this).parent(".form-row-local").remove();
                        $(".method_form_1").find("#id_step2-TOTAL_FORMS").val($(".form-row-local").length);
                        form_name = $(".form-row-local");

                        for (i = 0; i < Total_Forms; i++) {
                            $(form_name.get(i)).find(".form-field-input").each(
                                function () {
                                    var regular_exp = new RegExp('(' + 'step2' + '-\\d+-)');
                                    var replacement = "step2-" + i + "-";
                                    if ($(this).attr("for")) $(this).attr("for", $(this).attr("for").replace(regular_exp, replacement));
                                    if (this.id) this.id = this.id.replace(regular_exp, replacement);
                                    if (this.name) this.name = this.name.replace(regular_exp, replacement);

                                    return false;
                                }
                            )
                        }


                    }


                }
            )
            $(".method_form_1").find("#id_step2-TOTAL_FORMS").val(Total_Forms+1);



        }
        else{
            console.log(Total_Forms);
        }

    })


$(document).on("click",".delete-form-row",function (event) {
    event.preventDefault();
})


