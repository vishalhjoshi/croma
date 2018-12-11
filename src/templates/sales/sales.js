var $uid = 0;
var $item_data_set;

{% if not is_retrieve %}
$(document).unbind("keyup").keyup(function(e){
	if (e.which == 118) {
		$("#search_item_modal").modal("show");
	}
	if(e.which == 120) {
		$("#item-sale-modal-editor").modal("show");
		$("#Item-sale-form").trigger("reset");
		$("#id_batch_no").attr("readonly", false);
		$("#id_item_id").attr("readonly", false);
		$('#id_item_id').focus();
		$createMode = true;
		$editMode = false;
	}
});
$(document).ready(function(){
	AutoCompleteData("/sales/api/doctor-list/?format=json", 'doctorData', "#id_doctor_id", 15, 1);
	AutoCompleteData("/sales/api/party-list/?format=json", 'patientData', "#id_party_id", 10, 1);
	LoadAutoCompleteItemData();
})
{% endif %}

$(document).ready(function() {
	{% if is_create %}
	$("#id_party_id").focus();
	$("#cancel").attr("onclick", "location.href='{{prev.get_absolute_sale_detail_url}}'");
	$("#id_doc_dt").removeAttr("type");
	$("#id_doc_dt").datepicker();
	{% endif %}

	{% if is_retrieve %}
	$("select").attr("disabled", true);
	$("#add").attr("onclick", "location.href='/sales/create'");
	$("#edit").attr("onclick", "location.href='{{saleInvhrd_query.get_absolute_sale_edit_url}}'");
	{% if prev %}
	$("#prev").attr("onclick", "location.href='{{prev.get_absolute_sale_detail_url}}'");
	{% else %}
	$("#prev").click(function() {
		alert('No Previous Sale Record Exist!!');
	})
	{% endif %}

	{% if next %}
	$("#next").attr("onclick", "location.href='{{next.get_absolute_sale_detail_url}}'");
	{% else %}
	$("#next").click(function() {
		alert('No Next Sale Record Exist!!');
	})
	{% endif %}

	$("#search").click(function(){
		$("#sale_inv_search").modal("toggle");
		$("#search_inv_input").focus();
		$("#search_inv_input").val("");
		$("#seearch_error").css("display", "none");
	})
	$("#search_inv_input").focus(function(){
		$(document).on('keypress', "#search_inv_input", function (e) {
			if (e.which == 13) {
				e.preventDefault();
				$("#search_inv_btn").click();
			}
		})

	});
	$("#search_inv_input").attr("readonly", false);

	$("#search_inv_input").focus(function(){
		$("#seearch_error").css("display", "none");
	});
	$(document).unbind("keyup").keyup(function(e){
		if(e.which == 120) {
			alert("You cannot create/edit item in this Mode");
		}
	});
	{% endif %}
	{% if is_update %}
	$("#id_party_id").focus();
	$("#cancel").attr("onclick", "location.href='/sales/create'");
	$("#id_doc_dt").removeAttr("type");
	$("#id_doc_dt").datepicker();
	{% endif %}

	{% if is_create %}
        $item_data_set = []; //array to store the itmes
        {% else %}
        $item_data_set = JSON.parse('{{saleDtl_item_set_json | escapejs}}');
        fill_item_table($item_data_set);
        $uid = $item_data_set.length;
        {% endif %}

        var url;
        {% if is_update %}
        url = "{{item_query.get_absolute_sale_edit_url}}";
        {% else %}
        url = "/sales/create/";
        {% endif %}
        saveUpdateMethod(url);
        $("#id_party_id").attr("value", "{{saleInvhrd_query.party_id.name}}")
        $("#id_doctor_id").attr("value", "{{saleInvhrd_query.doctor_id.name}}")

}) //end of document ready function
