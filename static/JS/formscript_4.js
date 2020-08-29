

$(document).on("click",".add-class-4",function (e){
    e.preventDefault();
    var total_forms=parseInt($("#id_step4-TOTAL_FORMS").val());
    console.log(total_forms);
    if(total_forms<=6){

            var clone_row_output = $(".form-row-4:last").clone(false).get(0);
            console.log(clone_row_output);
            $(clone_row_output).removeAttr('value');
            $(clone_row_output).removeAttr("id").hide().insertAfter(".form-row-4:last").slideDown(300);
            $(".errorlist", clone_row_output).remove();
            $(clone_row_output).children().removeClass(".error");
            $(clone_row_output).find(".form-field-output-4").each(
                function () {

                    var regular_exp1 = new RegExp('(' + 'step4' + '-\\d+-)');
                    var replacement1 = "step4-" + total_forms + "-";
                    if ($(this).attr("for")) $(this).attr("for", $(this).attr("for").replace(regular_exp1, replacement1));
                    if (this.id) this.id = this.id.replace(regular_exp1, replacement1);
                    if (this.name) this.name = this.name.replace(regular_exp1, replacement1);
                    $(this).val("")
                    $(this).removeAttr('value');
                    return true;


                }
            );


            $(".form-row-4").find(".btn-delete").click(
                function (event) {
                    event.preventDefault();
                    total_forms = $(".form-row-4").length;

                    if (total_forms > 1) {

                        $(this).parent(".form-row-4").remove();
                        $("#id_step4-TOTAL_FORMS").val($(".form-row-4").length);
                        form_name = $(".form-row-4");

                        for (i = 0; i < total_forms; i++) {
                            $(form_name.get(i)).find(".form-field-output-4").each(
                                function () {
                    var regular_exp1 = new RegExp('(' + 'step4' + '-\\d+-)');
                    var replacement1 = "step4-" + total_forms + "-";
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
            $("#id_step4-TOTAL_FORMS").val(total_forms + 1);
        }
        else{
            console.log(total_forms);
        }

    })
$(document).on("click",".btn-delete",function (event) {
    event.preventDefault();
})



