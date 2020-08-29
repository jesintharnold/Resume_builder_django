
$(document).on('click', '.add-form-row-output', function (e) {
        e.preventDefault();

        var Total_Forms_output = parseInt($("#id_step6-TOTAL_FORMS").val());

        if(Total_Forms_output<=3){

            var clone_row_output = $(".form-row-output:last").clone(false).get(0);
            $(clone_row_output).removeAttr('value');
            $(clone_row_output).removeAttr("id").hide().insertAfter(".form-row-output:last").slideDown(300);
            $(".errorlist", clone_row_output).remove();
            $(clone_row_output).children().removeClass(".error");
            console.log($(clone_row_output).find(".form-field-output"));
            $(clone_row_output).find(".form-field-output").each(
                function () {

                    var regular_exp1 = new RegExp('(' + 'step6' + '-\\d+-)');
                    var replacement1 = "step6-" + Total_Forms_output + "-";
                    if ($(this).attr("for")) $(this).attr("for", $(this).attr("for").replace(regular_exp1, replacement1));
                    if (this.id) this.id = this.id.replace(regular_exp1, replacement1);
                    if (this.name) this.name = this.name.replace(regular_exp1, replacement1);
                    $(this).val("")
                    $(this).removeAttr('value');
                    return true;


                }
            );


            $(".form-row-output").find(".delete-form-row-output").click(
                function (event) {
                    event.preventDefault();

                    Total_Forms_output = $(".form-row-output").length;
                    if (Total_Forms_output > 1) {

                        $(this).parent(".form-row-output").remove();
                        $(".method_form_2").find("#id_step6-TOTAL_FORMS").val($(".form-row-output").length);
                        form_name = $(".form-row-output");

                        for (i = 0; i < Total_Forms_output; i++) {
                            $(form_name.get(i)).find(".form-field-output").each(
                                function () {
                                    var regular_exp1 = new RegExp('(' + 'step3' + '-\\d+-)');
                    var replacement1 = "step6-" + Total_Forms_output + "-";
                    if ($(this).attr("for")) $(this).attr("for", $(this).attr("for").replace(regular_exp1, replacement1));
                    if (this.id) this.id = this.id.replace(regular_exp1, replacement1);
                    if (this.name) this.name = this.name.replace(regular_exp1, replacement1);

                    return true;
                                }
                            )
                        }


                    }


                }
            )
            $(".method_form_2").find("#id_step6-TOTAL_FORMS").val(Total_Forms_output + 1);
        }
        else{
            console.log(Total_Forms_output);
        }

    })


$(document).on("click",".delete-form-row-output",function (event) {
    event.preventDefault();
})





